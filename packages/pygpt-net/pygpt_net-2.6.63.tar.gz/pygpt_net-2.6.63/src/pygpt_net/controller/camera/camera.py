#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://pygpt.net                         #
# GitHub:  https://github.com/szczyglis-dev/py-gpt   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2025.08.23 15:00:00                  #
# ================================================== #

import datetime
import os
import time
from typing import Any

from PySide6.QtCore import Slot, QObject
from PySide6.QtGui import QImage, QPixmap, Qt

from pygpt_net.core.events import AppEvent, KernelEvent
from pygpt_net.core.camera.worker import CaptureWorker
from pygpt_net.core.types import MODE_ASSISTANT
from pygpt_net.utils import trans


class Camera(QObject):
    def __init__(self, window=None):
        """
        Camera controller

        :param window: Window instance
        """
        super(Camera, self).__init__()
        self.window = window
        self.frame = None
        self.thread_started = False
        self.is_capture = False
        self.stop = False
        self.auto = False

    def setup(self):
        """Setup camera"""
        if self.is_capture and not self.thread_started:
            self.start()

    def setup_ui(self):
        """Update layout checkboxes"""
        if self.window.core.config.get('vision.capture.enabled'):
            self.is_capture = True
            self.window.ui.menu['video.capture'].setChecked(True)
            self.window.ui.nodes['icon.video.capture'].set_icon(":/icons/webcam.svg")
            # self.window.ui.nodes['vision.capture.enable'].setChecked(True)
        else:
            self.is_capture = False
            self.window.ui.menu['video.capture'].setChecked(False)
            self.window.ui.nodes['icon.video.capture'].set_icon(":/icons/webcam_off.svg")
            # self.window.ui.nodes['vision.capture.enable'].setChecked(False)

        if self.window.core.config.get('vision.capture.auto'):
            self.auto = True
            self.window.ui.menu['video.capture.auto'].setChecked(True)
            # self.window.ui.nodes['vision.capture.auto'].setChecked(True)
        else:
            self.auto = False
            self.window.ui.menu['video.capture.auto'].setChecked(False)
            # self.window.ui.nodes['vision.capture.auto'].setChecked(False)

        # update label
        if not self.window.core.config.get('vision.capture.auto'):
            self.window.ui.nodes['video.preview'].label.setText(trans("vision.capture.label"))
        else:
            self.window.ui.nodes['video.preview'].label.setText(trans("vision.capture.auto.label"))

    def update(self):
        """Update camera frame"""
        if not self.thread_started \
                or self.frame is None \
                or not self.is_capture:
            return

        # scale and update frame
        width = self.window.ui.nodes['video.preview'].video.width()
        image = QImage(
            self.frame,
            self.frame.shape[1],
            self.frame.shape[0],
            self.frame.strides[0],
            QImage.Format_RGB888
        )
        pixmap = QPixmap.fromImage(image)
        scaled_pixmap = pixmap.scaled(
            width,
            pixmap.height(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        self.window.ui.nodes['video.preview'].video.setPixmap(scaled_pixmap)

    def manual_capture(self, force: bool = False):
        """
        Capture frame via click on video output

        :param force: force capture even if auto is enabled
        """
        if not self.is_auto() or force:
            if not self.capture_frame(True):
                event = KernelEvent(KernelEvent.STATE_ERROR, {
                    'msg': trans("vision.capture.manual.captured.error"),
                })
                self.window.dispatch(event)
        else:
            event = KernelEvent(KernelEvent.STATUS, {
                'status': trans('vision.capture.auto.click'),
            })
            self.window.dispatch(event)
        self.window.dispatch(AppEvent(AppEvent.CAMERA_CAPTURED))  # app event

    def internal_capture(self) -> bool:
        """
        Capture frame internally

        :return: True if success
        """
        before_enabled = self.is_enabled()
        if not self.thread_started:
            self.is_capture = True
            self.window.ui.menu['video.capture'].setChecked(True)
            self.window.ui.nodes['icon.video.capture'].set_icon(":/icons/webcam.svg")
            print("Starting camera thread...")
            self.start()
            time.sleep(3)

        if not self.capture_frame(False):
            event = KernelEvent(KernelEvent.STATE_ERROR, {
                    'msg': trans("vision.capture.manual.captured.error"),
                })
            self.window.dispatch(event)
            result = False
        else:
            self.window.dispatch(AppEvent(AppEvent.CAMERA_CAPTURED))  # app event
            result = True

        # stop capture if not enabled before
        if not before_enabled:
            self.disable_capture_internal()

        return result

    def handle_auto_capture(self, mode: str):
        """
        Handle auto capture

        :param mode: current mode
        """
        if mode == MODE_ASSISTANT:
            return  # abort in Assistants mode
        if self.window.controller.ui.vision.has_vision():
            if self.is_enabled():
                if self.is_auto():
                    self.capture_frame(switch=False)
                    self.window.controller.chat.log("Captured frame from camera.")  # log

    def get_current_frame(self, flip_colors: bool = True):
        """
        Get current frame

        :param flip_colors: True if flip colors
        """
        import cv2
        if self.frame is None:
            return None
        if flip_colors:
            return cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        else:
            return self.frame

    def capture_frame(self, switch: bool = True) -> bool:
        """
        Capture frame and save it as attachment

        :param switch: true if switch to attachments tab (tmp: disabled)
        :return: True if success
        """
        import cv2
        # clear attachments before capture if needed
        if self.window.controller.attachment.is_capture_clear():
            self.window.controller.attachment.clear(True, auto=True)

        # capture frame
        try:
            # prepare filename
            now = datetime.datetime.now()
            dt = now.strftime("%Y-%m-%d_%H-%M-%S")
            name = 'cap-' + dt
            path = os.path.join(
                self.window.core.config.get_user_dir('capture'),
                name + '.jpg'
            )

            # capture frame
            compression_params = [
                cv2.IMWRITE_JPEG_QUALITY,
                int(self.window.core.config.get('vision.capture.quality'))
            ]
            frame = self.get_current_frame()
            self.window.controller.painter.capture.camera()  # capture to draw

            cv2.imwrite(path, frame, compression_params)
            mode = self.window.core.config.get('mode')

            # make attachment
            dt_info = now.strftime("%Y-%m-%d %H:%M:%S")
            title = trans('vision.capture.name.prefix') + ' ' + name
            title = title.replace('cap-', '').replace('_', ' ')
            self.window.core.attachments.new(mode, title, path, False)
            self.window.core.attachments.save()
            self.window.controller.attachment.update()

            # show last capture time in status
            event = KernelEvent(KernelEvent.STATUS, {
                'status': trans("vision.capture.manual.captured.success") + ' ' + dt_info,
            })
            self.window.dispatch(event)

            return True

        except Exception as e:
            print("Frame capture exception", e)
            self.window.core.debug.log(e)
            event = KernelEvent(KernelEvent.STATUS, {
                'status': trans('vision.capture.error'),
            })
            self.window.dispatch(event)
        return False

    def capture_frame_save(self) -> str:
        """
        Capture frame and save

        :return: Path to saved frame
        """
        import cv2
        # capture frame
        before_enabled = self.is_enabled()
        if not self.thread_started:
            self.is_capture = True
            self.window.ui.menu['video.capture'].setChecked(True)
            self.window.ui.nodes['icon.video.capture'].set_icon(":/icons/webcam.svg")
            print("Starting camera thread...")
            self.start()
            time.sleep(3)

        path = ""
        try:
            # prepare filename
            now = datetime.datetime.now()
            dt = now.strftime("%Y-%m-%d_%H-%M-%S")
            name = 'cap-' + dt
            path = os.path.join(
                self.window.core.config.get_user_dir('capture'),
                name + '.jpg'
            )
            # capture frame
            compression_params = [
                cv2.IMWRITE_JPEG_QUALITY,
                int(self.window.core.config.get('vision.capture.quality'))
            ]
            frame = self.get_current_frame()
            cv2.imwrite(path, frame, compression_params)

            # stop capture if not enabled before
            if not before_enabled:
                self.disable_capture_internal()

            return path

        except Exception as e:
            print("Frame capture exception", e)
            self.window.core.debug.log(e)

        # stop capture if not enabled before
        if not before_enabled:
            self.disable_capture_internal()
        return path

    def disable_capture_internal(self):
        """Disable camera capture"""
        self.window.ui.menu['video.capture'].setChecked(False)
        self.window.ui.nodes['icon.video.capture'].set_icon(":/icons/webcam_off.svg")
        self.disable_capture(force=True)

    def show_camera(self):
        """Show camera"""
        if self.is_capture:
            self.window.ui.nodes['video.preview'].setVisible(True)

    def hide_camera(self, stop: bool = True):
        """
        Hide camera

        :param stop: True if stop capture thread
        """
        self.window.ui.nodes['video.preview'].setVisible(False)

        if stop:
            self.stop_capture()

    def enable_capture(self):
        """Enable capture"""
        if not self.capture_allowed():
            return

        self.is_capture = True
        self.window.core.config.set('vision.capture.enabled', True)
        """
        self.window.controller.config.checkbox.apply(
            'config',
            'vision.capture.enabled',
            {'value': True}
        )
        """
        self.window.ui.nodes['video.preview'].setVisible(True)
        if not self.thread_started:
            self.start()

    def disable_capture(self, force: bool = False):
        """
        Disable capture

        :param force: force disable
        """
        if not self.capture_allowed() and not force:
            return

        self.is_capture = False
        self.window.core.config.set('vision.capture.enabled', False)
        """
        self.window.controller.config.checkbox.apply(
            'config',
            'vision.capture.enabled',
            {'value': False}
        )
        """
        # self.window.ui.nodes['vision.capture.enable'].setChecked(False)
        self.window.ui.nodes['video.preview'].setVisible(False)
        self.stop_capture()
        self.blank_screen()

    def toggle(self, state: bool):
        """
        Toggle camera

        :param state: state
        """
        if state:
            self.enable_capture()
        else:
            self.disable_capture()
        self.setup_ui()

    def toggle_capture(self):
        """Toggle camera"""
        if not self.is_capture:
            self.enable_capture()
        else:
            self.disable_capture()
        self.setup_ui()

    def enable_auto(self):
        """Enable capture"""
        if not self.capture_allowed():
            return

        self.auto = True
        self.window.core.config.set('vision.capture.auto', True)
        self.window.ui.menu['video.capture.auto'].setChecked(True)
        """
        self.window.controller.config.checkbox.apply(
            'config',
            'vision.capture.auto',
            {'value': True}
        )
        """
        self.window.ui.nodes['video.preview'].label.setText(trans("vision.capture.auto.label"))

        if not self.window.core.config.get('vision.capture.enabled'):
            self.enable_capture()
            self.window.ui.menu['video.capture'].setChecked(True)
            # self.window.ui.nodes['vision.capture.enable'].setChecked(True)

    def disable_auto(self):
        """Disable capture"""
        if not self.capture_allowed():
            return

        self.auto = False
        self.window.core.config.set('vision.capture.auto', False)
        self.window.ui.menu['video.capture.auto'].setChecked(False)
        """
        self.window.controller.config.checkbox.apply(
            'config',
            'vision.capture.auto',
            {'value': False}
        )
        """
        self.window.ui.nodes['video.preview'].label.setText(trans("vision.capture.label"))

    def toggle_auto(self, state: bool):
        """
        Toggle camera

        :param state: state (True/False)
        """
        if state:
            self.enable_auto()
        else:
            self.disable_auto()

        self.window.update_status('')

    def is_enabled(self) -> bool:
        """
        Check if camera is enabled

        :return: True if enabled, false otherwise
        """
        return self.is_capture

    def is_auto(self) -> bool:
        """
        Check if camera is enabled

        :return: True if enabled, false otherwise
        """
        return self.auto

    def blank_screen(self):
        """Make and set blank screen"""
        self.window.ui.nodes['video.preview'].video.setPixmap(QPixmap.fromImage(QImage()))

    def start(self):
        """Start camera thread"""
        if self.thread_started:
            return

        # prepare thread
        self.stop = False

        # worker
        worker = CaptureWorker()
        worker.window = self.window

        # signals
        worker.signals.capture.connect(self.handle_capture)
        worker.signals.finished.connect(self.handle_stop)
        worker.signals.unfinished.connect(self.handle_unfinished)
        worker.signals.stopped.connect(self.handle_stop)
        worker.signals.error.connect(self.handle_error)

        # start
        self.window.threadpool.start(worker)
        self.thread_started = True
        self.window.dispatch(AppEvent(AppEvent.CAMERA_ENABLED))  # app event

    def stop_capture(self):
        """Stop camera capture thread"""
        if not self.thread_started:
            return

        self.stop = True
        self.window.dispatch(AppEvent(AppEvent.CAMERA_DISABLED))  # app event

    @Slot(object)
    def handle_error(self, err: Any):
        """
        Handle thread error signal

        :param err: error message
        """
        self.window.core.debug.log(err)
        self.window.ui.dialogs.alert(err)

    @Slot(object)
    def handle_capture(self, frame):
        """
        Handle capture frame signal

        :param frame: frame
        """
        self.frame = frame
        self.update()

    @Slot()
    def handle_stop(self):
        """On capture stopped signal"""
        self.thread_started = False
        self.hide_camera(False)

    @Slot()
    def handle_unfinished(self):
        """On capture unfinished (never started) signal"""
        if self.window.core.platforms.is_snap():
            self.window.ui.dialogs.open(
                'snap_camera',
                width=400,
                height=200
            )
        self.thread_started = False
        self.disable_capture()

    def capture_allowed(self) -> bool:
        """
        Check if capture is allowed

        :return: True if capture is allowed
        """
        if self.window.controller.painter.is_active():
            return True
        if self.window.controller.ui.vision.has_vision():
            return True
        return False

