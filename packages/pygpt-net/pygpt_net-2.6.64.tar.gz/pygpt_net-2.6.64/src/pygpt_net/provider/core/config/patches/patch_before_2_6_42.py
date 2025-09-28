#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://pygpt.net                         #
# GitHub:  https://github.com/szczyglis-dev/py-gpt   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2025.09.12 00:00:00                  #
# ================================================== #

import copy
import os
from typing import Tuple

from packaging.version import parse as parse_version, Version


class Patch:
    def __init__(self, window=None):
        self.window = window

    def execute(self, version: Version) -> Tuple[dict, bool, bool]:
        """
        Migrate config to current app version

        :param version: current app version
        :return: Updated data, and True if updated, and True if old version
        """
        data = self.window.core.config.all()
        cfg_get_base = self.window.core.config.get_base
        remove_plugin_config = self.window.core.config.remove_plugin_config
        patch_css = self.window.core.updater.patch_css
        current = "0.0.0"
        updated = False
        is_old = False

        # get version of config file
        if '__meta__' in data and 'version' in data['__meta__']:
            current = data['__meta__']['version']
        old = parse_version(current)

        # check if config file is older than current app version
        if old < version:

            # mark as older version
            is_old = True

            # < 0.9.1
            if old < parse_version("0.9.1"):
                print("Migrating config from < 0.9.1...")
                keys_to_remove = ['user_id', 'custom']  # not needed anymore
                for key in keys_to_remove:
                    if key in data:
                        del data[key]
                keys_to_add = ['organization_key']
                for key in keys_to_add:
                    if key not in data:
                        data[key] = ""
                updated = True

            # < 0.9.2
            if old < parse_version("0.9.2"):
                print("Migrating config from < 0.9.2...")
                keys_to_remove = ['ui.ctx.min_width',
                                  'ui.ctx.max_width',
                                  'ui.toolbox.min_width',
                                  'ui.toolbox.max_width',
                                  'ui.dialog.settings.width',
                                  'ui.dialog.settings.height',
                                  'ui.chatbox.font.color']
                for key in keys_to_remove:
                    if key in data:
                        del data[key]
                if 'theme' not in data:
                    data['theme'] = "dark_teal"
                updated = True

            # < 0.9.4
            if old < parse_version("0.9.4"):
                print("Migrating config from < 0.9.4...")
                if 'plugins' not in data:
                    data['plugins'] = {}
                if 'plugins_enabled' not in data:
                    data['plugins_enabled'] = {}
                updated = True

            # < 0.9.6
            if old < parse_version("0.9.6"):
                print("Migrating config from < 0.9.6...")
                data['debug'] = True  # enable debug by default
                updated = True

            # < 2.0.0
            if old < parse_version("2.0.0"):
                print("Migrating config from < 2.0.0...")
                data['theme'] = 'dark_teal'  # force, because removed light themes!
                if 'cmd' not in data:
                    data['cmd'] = True
                if 'stream' not in data:
                    data['stream'] = True
                if 'attachments_send_clear' not in data:
                    data['attachments_send_clear'] = True
                if 'assistant' not in data:
                    data['assistant'] = None
                if 'assistant_thread' not in data:
                    data['assistant_thread'] = None
                updated = True

            # < 2.0.1
            if old < parse_version("2.0.1"):
                print("Migrating config from < 2.0.1...")
                if 'send_mode' not in data:
                    data['send_mode'] = 1
                if 'send_shift_enter' in data:
                    del data['send_shift_enter']
                if 'font_size.input' not in data:
                    data['font_size.input'] = 11
                if 'font_size.ctx' not in data:
                    data['font_size.ctx'] = 9
                if 'ctx.auto_summary' not in data:
                    data['ctx.auto_summary'] = True
                if 'ctx.auto_summary.system' not in data:
                    data['ctx.auto_summary.system'] = "You are an expert in conversation summarization"
                if 'ctx.auto_summary.prompt' not in data:
                    data['ctx.auto_summary.prompt'] = "Summarize topic of this conversation in one sentence. Use best " \
                                                      "keywords to describe it. Summary must be in the same language " \
                                                      "as the conversation and it will be used for conversation title " \
                                                      "so it must be EXTREMELY SHORT and concise - use maximum 5 " \
                                                      "words: \n\nUser: {input}\nAI Assistant: {output}"
                updated = True

            # < 2.0.6
            if old < parse_version("2.0.6"):
                print("Migrating config from < 2.0.6...")
                if 'layout.density' not in data:
                    data['layout.density'] = -2
                updated = True

            # < 2.0.8
            if old < parse_version("2.0.8"):
                print("Migrating config from < 2.0.8...")
                if 'plugins' not in data:
                    data['plugins'] = {}
                if 'cmd_web_google' not in data['plugins']:
                    data['plugins']['cmd_web_google'] = {}
                data['plugins']['cmd_web_google'][
                    'prompt_summarize'] = "Summarize the English text in a maximum of 3 " \
                                          "paragraphs, trying to find the most " \
                                          "important content that can help answer the " \
                                          "following question: "
                data['plugins']['cmd_web_google']['chunk_size'] = 100000
                data['plugins']['cmd_web_google']['max_page_content_length'] = 0
                updated = True

            # < 2.0.13
            if old < parse_version("2.0.13"):
                print("Migrating config from < 2.0.13...")
                if 'layout.density' not in data:
                    data['layout.density'] = 0
                else:
                    if data['layout.density'] == -2:
                        data['layout.density'] = 0
                updated = True

            # < 2.0.14
            if old < parse_version("2.0.14"):
                print("Migrating config from < 2.0.14...")
                if 'vision.capture.enabled' not in data:
                    data['vision.capture.enabled'] = True
                if 'vision.capture.auto' not in data:
                    data['vision.capture.auto'] = True
                if 'vision.capture.width' not in data:
                    data['vision.capture.width'] = 800
                if 'vision.capture.height' not in data:
                    data['vision.capture.height'] = 600
                updated = True

            # < 2.0.16
            if old < parse_version("2.0.16"):
                print("Migrating config from < 2.0.16...")
                if 'vision.capture.idx' not in data:
                    data['vision.capture.idx'] = 0
                if 'img_raw' not in data:
                    data['img_raw'] = True
                if 'img_prompt_model' not in data:
                    data['img_prompt_model'] = "gpt-4-1106-preview"
                updated = True

            # < 2.0.19
            if old < parse_version("2.0.19"):
                print("Migrating config from < 2.0.19...")
                if 'img_raw' not in data:
                    data['img_raw'] = True
                if not data['img_raw']:
                    data['img_raw'] = True
                updated = True

            # < 2.0.25
            if old < parse_version("2.0.25"):
                print("Migrating config from < 2.0.25...")
                if 'cmd.prompt' not in data:
                    data['cmd.prompt'] = cfg_get_base('cmd.prompt')
                if 'img_prompt' not in data:
                    data['img_prompt'] = cfg_get_base('img_prompt')
                if 'vision.capture.quality' not in data:
                    data['vision.capture.quality'] = 85
                if 'attachments_capture_clear' not in data:
                    data['attachments_capture_clear'] = True
                if 'plugins' not in data:
                    data['plugins'] = {}
                if 'cmd_web_google' not in data['plugins']:
                    data['plugins']['cmd_web_google'] = {}
                data['plugins']['cmd_web_google']['prompt_summarize'] = "Summarize the English text in a maximum of 3 " \
                                                                        "paragraphs, trying to find the most " \
                                                                        "important content that can help answer the " \
                                                                        "following question: "
                updated = True

            # < 2.0.26
            if old < parse_version("2.0.26"):
                print("Migrating config from < 2.0.26...")
                if 'ctx.auto_summary.model' not in data:
                    data['ctx.auto_summary.model'] = 'gpt-3.5-turbo-1106'
                updated = True

            # < 2.0.27
            if old < parse_version("2.0.27"):
                print("Migrating config from < 2.0.27...")
                if 'plugins' not in data:
                    data['plugins'] = {}
                if 'cmd_web_google' not in data['plugins']:
                    data['plugins']['cmd_web_google'] = {}
                data['plugins']['cmd_web_google'][
                    'prompt_summarize'] = "Summarize text in English in a maximum of 3 " \
                                          "paragraphs, trying to find the most " \
                                          "important content that can help answer the " \
                                          "following question: {query}"
                data['cmd.prompt'] = cfg_get_base('cmd.prompt')  # fix
                updated = True

            # < 2.0.30
            if old < parse_version("2.0.30"):
                print("Migrating config from < 2.0.30...")
                if 'plugins' not in data:
                    data['plugins'] = {}
                if 'audio_openai_whisper' not in data['plugins']:
                    data['plugins']['audio_openai_whisper'] = {}
                data['plugins']['audio_openai_whisper']['timeout'] = 1
                data['plugins']['audio_openai_whisper']['phrase_length'] = 5
                data['plugins']['audio_openai_whisper']['min_energy'] = 2000
                updated = True

            # < 2.0.31
            if old < parse_version("2.0.31"):
                print("Migrating config from < 2.0.31...")
                if 'plugins' not in data:
                    data['plugins'] = {}
                if 'audio_openai_whisper' not in data['plugins']:
                    data['plugins']['audio_openai_whisper'] = {}
                data['plugins']['audio_openai_whisper']['continuous_listen'] = False
                data['plugins']['audio_openai_whisper']['timeout'] = 2
                data['plugins']['audio_openai_whisper']['phrase_length'] = 4
                data['plugins']['audio_openai_whisper']['magic_word_timeout'] = 1
                data['plugins']['audio_openai_whisper']['magic_word_phrase_length'] = 2
                data['plugins']['audio_openai_whisper']['min_energy'] = 1.3
                updated = True

            # < 2.0.34
            if old < parse_version("2.0.34"):
                print("Migrating config from < 2.0.34...")
                if 'lock_modes' not in data:
                    data['lock_modes'] = True
                updated = True

            # < 2.0.37
            if old < parse_version("2.0.37"):
                print("Migrating config from < 2.0.37...")
                if 'font_size.toolbox' not in data:
                    data['font_size.toolbox'] = 12
                updated = True

            # < 2.0.46
            if old < parse_version("2.0.46"):
                print("Migrating config from < 2.0.46...")
                data['cmd'] = False  # disable on default
                updated = True

            # < 2.0.47
            if old < parse_version("2.0.47"):
                print("Migrating config from < 2.0.47...")
                if 'notepad.num' not in data:
                    data['notepad.num'] = 5
                updated = True

            # < 2.0.52
            if old < parse_version("2.0.52"):
                print("Migrating config from < 2.0.52...")
                if 'layout.dpi.scaling' not in data:
                    data['layout.dpi.scaling'] = True
                if 'layout.dpi.factor' not in data:
                    data['layout.dpi.factor'] = 1.0
                updated = True

            # < 2.0.62
            if old < parse_version("2.0.62"):
                print("Migrating config from < 2.0.62...")
                if 'ctx.records.limit' not in data:
                    data['ctx.records.limit'] = 0
                updated = True

            # < 2.0.65
            if old < parse_version("2.0.65"):
                print("Migrating config from < 2.0.65...")
                if 'ctx.search.string' not in data:
                    data['ctx.search.string'] = ""
                updated = True

            # < 2.0.69
            if old < parse_version("2.0.69"):
                print("Migrating config from < 2.0.69...")
                data['img_prompt'] = "Whenever I provide a basic idea or concept for an image, such as 'a picture " \
                                     "of mountains', I want you to ALWAYS translate it into English and expand " \
                                     "and elaborate on this idea. Use your knowledge and creativity to add " \
                                     "details that would make the image more vivid and interesting. This could " \
                                     "include specifying the time of day, weather conditions, surrounding " \
                                     "environment, and any additional elements that could enhance the scene. Your " \
                                     "goal is to create a detailed and descriptive prompt that provides DALL-E " \
                                     "with enough information to generate a rich and visually appealing image. " \
                                     "Remember to maintain the original intent of my request while enriching the " \
                                     "description with your imaginative details."
                data['img_raw'] = False
                data['img_prompt_model'] = "gpt-4-1106-preview"
                updated = True

            # < 2.0.71
            if old < parse_version("2.0.71"):
                print("Migrating config from < 2.0.71...")
                prompt = 'IMAGE GENERATION: Whenever I provide a basic idea or concept for an image, such as \'a picture of ' \
                         'mountains\', I want you to ALWAYS translate it into English and expand and elaborate on this idea. ' \
                         'Use your  knowledge and creativity to add details that would make the image more vivid and ' \
                         'interesting. This could include specifying the time of day, weather conditions, surrounding ' \
                         'environment, and any additional elements that could enhance the scene. Your goal is to create a ' \
                         'detailed and descriptive prompt that provides DALL-E  with enough information to generate a rich ' \
                         'and visually appealing image. Remember to maintain the original  intent of my request while ' \
                         'enriching the description with your imaginative details. HOW TO START IMAGE GENERATION: to start ' \
                         'image generation return to me prepared prompt in JSON format, all in one line,  using following ' \
                         'syntax: ~###~{"cmd": "image", "params": {"query": "your query here"}}~###~. Use ONLY this syntax ' \
                         'and remember to surround JSON string with ~###~.  DO NOT use any other syntax. Use English in the ' \
                         'generated JSON command, but conduct all the remaining parts of the discussion with me in the ' \
                         'language in which I am speaking to you. The image will be generated on my machine  immediately ' \
                         'after the command is issued, allowing us to discuss the photo once it has been created.  Please ' \
                         'engage with me about the photo itself, not only by giving the generate command. '
                if 'openai_dalle' not in data['plugins']:
                    data['plugins']['openai_dalle'] = {}
                    data['plugins']['openai_dalle']['prompt'] = prompt  # fixed prompt

                data['plugins_enabled']['openai_dalle'] = True
                data['plugins_enabled']['openai_vision'] = True

                # deprecate vision and img modes
                if data['mode'] == 'vision' or data['mode'] == 'img':
                    data['mode'] = 'chat'

                updated = True

            # < 2.0.72
            if old < parse_version("2.0.72"):
                print("Migrating config from < 2.0.72...")
                prompt = 'IMAGE GENERATION: Whenever I provide a basic idea or concept for an image, such as \'a picture of ' \
                         'mountains\', I want you to ALWAYS translate it into English and expand and elaborate on this idea. ' \
                         'Use your  knowledge and creativity to add details that would make the image more vivid and ' \
                         'interesting. This could include specifying the time of day, weather conditions, surrounding ' \
                         'environment, and any additional elements that could enhance the scene. Your goal is to create a ' \
                         'detailed and descriptive prompt that provides DALL-E  with enough information to generate a rich ' \
                         'and visually appealing image. Remember to maintain the original  intent of my request while ' \
                         'enriching the description with your imaginative details. HOW TO START IMAGE GENERATION: to start ' \
                         'image generation return to me prepared prompt in JSON format, all in one line,  using following ' \
                         'syntax: ~###~{"cmd": "image", "params": {"query": "your query here"}}~###~. Use ONLY this syntax ' \
                         'and remember to surround JSON string with ~###~.  DO NOT use any other syntax. Use English in the ' \
                         'generated JSON command, but conduct all the remaining parts of the discussion with me in the ' \
                         'language in which I am speaking to you. The image will be generated on my machine  immediately ' \
                         'after the command is issued, allowing us to discuss the photo once it has been created.  Please ' \
                         'engage with me about the photo itself, not only by giving the generate command. '
                if 'openai_dalle' not in data['plugins']:
                    data['plugins']['openai_dalle'] = {}
                data['plugins']['openai_dalle']['prompt'] = prompt  # fixed prompt
                updated = True

            # < 2.0.75
            if old < parse_version("2.0.75"):
                print("Migrating config from < 2.0.75...")
                if 'updater.check.launch' not in data:
                    data['updater.check.launch'] = True
                if 'updater.check.bg' not in data:
                    data['updater.check.bg'] = False
                updated = True

            # < 2.0.78
            if old < parse_version("2.0.78"):
                print("Migrating config from < 2.0.78...")
                if 'render.plain' not in data:
                    data['render.plain'] = False
                updated = True

            # < 2.0.81
            if old < parse_version("2.0.81"):
                print("Migrating config from < 2.0.81...")
                patch_css('markdown.light.css', True)  # force replace file
                updated = True

            # < 2.0.85
            if old < parse_version("2.0.85"):
                print("Migrating config from < 2.0.85...")
                prompt = "AUTONOMOUS MODE:\n1. You will now enter self-dialogue mode, where you will be conversing with " \
                         "yourself, not with a human.\n2. When you enter self-dialogue mode, remember that you are engaging " \
                         "in a conversation with yourself. Any user input will be considered a reply featuring your previous response.\n" \
                         "3. The objective of this self-conversation is well-defined—focus on achieving it.\n" \
                         "4. Your new message should be a continuation of the last response you generated, essentially replying" \
                         " to yourself and extending it.\n5. After each response, critically evaluate its effectiveness " \
                         "and alignment with the goal. If necessary, refine your approach.\n6. Incorporate self-critique " \
                         "after every response to capitalize on your strengths and address areas needing improvement.\n7. To " \
                         "advance towards the goal, utilize all the strategic thinking and resources at your disposal.\n" \
                         "8. Ensure that the dialogue remains coherent and logical, with each response serving as a stepping " \
                         "stone towards the ultimate objective.\n9. Treat the entire dialogue as a monologue aimed at devising" \
                         " the best possible solution to the problem.\n10. Conclude the self-dialogue upon realizing the " \
                         "goal or reaching a pivotal conclusion that meets the initial criteria.\n11. You are allowed to use " \
                         "any commands and tools without asking for it.\n12. While using commands, always use the correct " \
                         "syntax and never interrupt the command before generating the full instruction.\n13. ALWAYS break " \
                         "down the main task into manageable logical subtasks, systematically addressing and analyzing each" \
                         " one in sequence.\n14. With each subsequent response, make an effort to enhance your previous " \
                         "reply by enriching it with new ideas and do it automatically without asking for it.\n14. Any input " \
                         "that begins with 'user: ' will come from me, and I will be able to provide you with ANY additional " \
                         "commands or goal updates in this manner. The other inputs, not prefixed with 'user: ' will represent" \
                         " your previous responses.\n15. Start by breaking down the task into as many smaller sub-tasks as " \
                         "possible, then proceed to complete each one in sequence.  Next, break down each sub-task into even " \
                         "smaller tasks, carefully and step by step go through all of them until the required goal is fully " \
                         "and correctly achieved.\n"
                if 'self_loop' not in data['plugins']:
                    data['plugins']['self_loop'] = {}
                data['plugins']['self_loop']['prompt'] = prompt  # fixed prompt

                # before fix (from 2.0.72)
                prompt = 'IMAGE GENERATION: Whenever I provide a basic idea or concept for an image, such as \'a picture of ' \
                         'mountains\', I want you to ALWAYS translate it into English and expand and elaborate on this idea. ' \
                         'Use your  knowledge and creativity to add details that would make the image more vivid and ' \
                         'interesting. This could include specifying the time of day, weather conditions, surrounding ' \
                         'environment, and any additional elements that could enhance the scene. Your goal is to create a ' \
                         'detailed and descriptive prompt that provides DALL-E  with enough information to generate a rich ' \
                         'and visually appealing image. Remember to maintain the original  intent of my request while ' \
                         'enriching the description with your imaginative details. HOW TO START IMAGE GENERATION: to start ' \
                         'image generation return to me prepared prompt in JSON format, all in one line,  using following ' \
                         'syntax: ~###~{"cmd": "image", "params": {"query": "your query here"}}~###~. Use ONLY this syntax ' \
                         'and remember to surround JSON string with ~###~.  DO NOT use any other syntax. Use English in the ' \
                         'generated JSON command, but conduct all the remaining parts of the discussion with me in the ' \
                         'language in which I am speaking to you. The image will be generated on my machine  immediately ' \
                         'after the command is issued, allowing us to discuss the photo once it has been created.  Please ' \
                         'engage with me about the photo itself, not only by giving the generate command. '
                if 'openai_dalle' not in data['plugins']:
                    data['plugins']['openai_dalle'] = {}
                data['plugins']['openai_dalle']['prompt'] = prompt  # fixed prompt

                updated = True

            # < 2.0.88
            if old < parse_version("2.0.88"):
                print("Migrating config from < 2.0.88...")
                prompt = "AUTONOMOUS MODE:\n1. You will now enter self-dialogue mode, where you will be conversing with " \
                         "yourself, not with a human.\n2. When you enter self-dialogue mode, remember that you are engaging " \
                         "in a conversation with yourself. Any user input will be considered a reply featuring your previous response.\n" \
                         "3. The objective of this self-conversation is well-defined—focus on achieving it.\n" \
                         "4. Your new message should be a continuation of the last response you generated, essentially replying" \
                         " to yourself and extending it.\n5. After each response, critically evaluate its effectiveness " \
                         "and alignment with the goal. If necessary, refine your approach.\n6. Incorporate self-critique " \
                         "after every response to capitalize on your strengths and address areas needing improvement.\n7. To " \
                         "advance towards the goal, utilize all the strategic thinking and resources at your disposal.\n" \
                         "8. Ensure that the dialogue remains coherent and logical, with each response serving as a stepping " \
                         "stone towards the ultimate objective.\n9. Treat the entire dialogue as a monologue aimed at devising" \
                         " the best possible solution to the problem.\n10. Conclude the self-dialogue upon realizing the " \
                         "goal or reaching a pivotal conclusion that meets the initial criteria.\n11. You are allowed to use " \
                         "any commands and tools without asking for it.\n12. While using commands, always use the correct " \
                         "syntax and never interrupt the command before generating the full instruction.\n13. ALWAYS break " \
                         "down the main task into manageable logical subtasks, systematically addressing and analyzing each" \
                         " one in sequence.\n14. With each subsequent response, make an effort to enhance your previous " \
                         "reply by enriching it with new ideas and do it automatically without asking for it.\n15. Any input " \
                         "that begins with 'user: ' will come from me, and I will be able to provide you with ANY additional " \
                         "commands or goal updates in this manner. The other inputs, not prefixed with 'user: ' will represent" \
                         " your previous responses.\n16. Start by breaking down the task into as many smaller sub-tasks as " \
                         "possible, then proceed to complete each one in sequence.  Next, break down each sub-task into even " \
                         "smaller tasks, carefully and step by step go through all of them until the required goal is fully " \
                         "and correctly achieved.\n"
                if 'self_loop' not in data['plugins']:
                    data['plugins']['self_loop'] = {}
                data['plugins']['self_loop']['prompt'] = prompt  # fixed prompt
                updated = True

            # < 2.0.91
            if old < parse_version("2.0.91"):
                print("Migrating config from < 2.0.91...")
                patch_css('style.dark.css', True)  # force replace file
                updated = True

            # < 2.0.96
            if old < parse_version("2.0.96"):
                print("Migrating config from < 2.0.96...")
                if 'img_quality' not in data:
                    data['img_quality'] = "standard"
                updated = True

            # < 2.0.98
            if old < parse_version("2.0.98"):
                print("Migrating config from < 2.0.98...")
                data['img_resolution'] = "1792x1024"  # char fix
                patch_css('style.css', True)  # force replace file
                patch_css('style.light.css', True)  # force replace file
                patch_css('style.dark.css', True)  # force replace file
                updated = True

            # < 2.0.99
            if old < parse_version("2.0.99"):
                print("Migrating config from < 2.0.99...")
                if 'layout.splitters' in data:
                    if 'calendar' in data['layout.splitters']:
                        # restore if was hidden at < 2.0.99
                        if len(data['layout.splitters']['calendar']) == 2 \
                                and data['layout.splitters']['calendar'][1] == 0:
                            data['layout.splitters']['calendar'] = [100, 100]
                if data['layout.density'] == 0:
                    data['layout.density'] = -1
                updated = True

            # < 2.0.100
            if old < parse_version("2.0.100"):
                print("Migrating config from < 2.0.100...")
                # rename output dir to data dir
                src = os.path.join(self.window.core.config.path, 'output')
                dst = os.path.join(self.window.core.config.path, 'data')

                # migrate data dir name
                if os.path.exists(src):
                    # backup old data dir
                    if os.path.exists(dst):
                        backup = os.path.join(self.window.core.config.path, 'data.backup')
                        os.rename(dst, backup)
                    # rename "output" to "data"
                    if os.path.exists(src):
                        os.rename(src, dst)

                # add llama-index config keys:
                if "llama.idx.auto" not in data:
                    data["llama.idx.auto"] = False
                if "llama.idx.auto.index" not in data:
                    data["llama.idx.auto.index"] = "base"
                if "llama.idx.current" not in data:
                    data["llama.idx.current"] = "base"
                if "llama.idx.db.index" not in data:
                    data["llama.idx.db.index"] = ""
                if "llama.idx.db.last" not in data:
                    data["llama.idx.db.last"] = 0
                if "llama.idx.list" not in data:
                    data["llama.idx.list"] = [
                        {
                            "id": "base",
                            "name": "Base",
                        }
                    ]
                if "llama.idx.status" not in data:
                    data["llama.idx.status"] = {}

                if "llama.log" not in data:
                    data["llama.log"] = False

                updated = True

            # < 2.0.101
            if old < parse_version("2.0.101"):
                print("Migrating config from < 2.0.101...")
                if 'layout.tooltips' not in data:
                    data['layout.tooltips'] = True
                updated = True

            # < 2.0.102
            if old < parse_version("2.0.102"):
                print("Migrating config from < 2.0.102...")
                if 'llama.hub.loaders' not in data:
                    data['llama.hub.loaders'] = [
                        {
                            "ext": "pptx",
                            "loader": "PptxReader"
                        },
                        {
                            "ext": "png,jpg,jpeg",
                            "loader": "ImageReader"
                        }
                    ]
                updated = True

            # < 2.0.112
            if old < parse_version("2.0.112"):
                print("Migrating config from < 2.0.112...")
                if 'img_dialog_open' not in data:
                    data['img_dialog_open'] = True
                updated = True

            # < 2.0.114
            if old < parse_version("2.0.114"):
                print("Migrating config from < 2.0.114...")
                if 'llama.idx.storage' not in data:
                    data['llama.idx.storage'] = "SimpleVectorStore"
                if 'llama.idx.storage.args' not in data:
                    data['llama.idx.storage.args'] = []
                if 'llama.idx.raw' not in data:
                    data['llama.idx.raw'] = False
                updated = True

            # < 2.0.116
            if old < parse_version("2.0.116"):
                print("Migrating config from < 2.0.116...")
                data['debug'] = False
                updated = True

            # < 2.0.118
            if old < parse_version("2.0.118"):
                print("Migrating config from < 2.0.118...")
                if 'layout.tray' not in data:
                    data['layout.tray'] = True
                updated = True

            """
            # < 2.0.119
            if old < parse_version("2.0.119"):
                print("Migrating config from < 2.0.119...")
                if 'layout.minimized' not in data:
                    data['layout.minimized'] = False
                updated = True
            """

            # < 2.0.121
            if old < parse_version("2.0.121"):
                print("Migrating config from < 2.0.121...")
                if 'openai_vision' not in data['plugins']:
                    data['plugins']['openai_vision'] = {}
                data['plugins']['openai_vision']['model'] = "gpt-4-vision-preview"
                updated = True

            # < 2.0.123
            if old < parse_version("2.0.123"):
                print("Migrating config from < 2.0.123...")
                if 'llama.idx.recursive' not in data:
                    data['llama.idx.recursive'] = False
                updated = True

            # < 2.0.127
            if old < parse_version("2.0.127"):
                print("Migrating config from < 2.0.127...")
                if 'upload.store' not in data:
                    data['upload.store'] = True
                if 'upload.data_dir' not in data:
                    data['upload.data_dir'] = False
                updated = True

            # < 2.0.131
            if old < parse_version("2.0.131"):
                print("Migrating config from < 2.0.131...")
                if 'self_loop' in data['plugins'] \
                        and 'prompts' not in data['plugins']['self_loop'] \
                        and 'prompt' in data['plugins']['self_loop'] \
                        and 'extended_prompt' in data['plugins']['self_loop']:

                    # copy old prompts to new list of prompts
                    data['plugins']['self_loop']['prompts'] = [
                        {
                            "enabled": True,
                            "name": "Default",
                            "prompt": data['plugins']['self_loop']['prompt'],
                        },
                        {
                            "enabled": False,
                            "name": "Extended",
                            "prompt": data['plugins']['self_loop']['extended_prompt'],
                        },
                    ]
                    updated = True

            # < 2.0.132
            if old < parse_version("2.0.132"):
                print("Migrating config from < 2.0.132...")
                if 'agent.auto_stop' not in data:
                    data['agent.auto_stop'] = True
                if 'agent.iterations' not in data:
                    data['agent.iterations'] = 3
                updated = True

            # < 2.0.135
            if old < parse_version("2.0.135"):
                print("Migrating config from < 2.0.135...")
                if 'agent.mode' not in data:
                    data['agent.mode'] = "chat"
                if 'agent.idx' not in data:
                    data['agent.idx'] = "base"
                updated = True

            # < 2.0.138
            if old < parse_version("2.0.138"):
                print("Migrating config from < 2.0.138...")
                if 'layout.tray.minimize' not in data:
                    data['layout.tray.minimize'] = False
                updated = True

            # < 2.0.139
            if old < parse_version("2.0.139"):
                print("Migrating config from < 2.0.139...")
                data['updater.check.bg'] = True
                if 'license.accepted' not in data:
                    data['license.accepted'] = False
                if 'updater.check.bg.last_time' not in data:
                    data['updater.check.bg.last_time'] = None
                if 'updater.check.bg.last_version' not in data:
                    data['updater.check.bg.last_version'] = None
                updated = True

            # < 2.0.142
            if old < parse_version("2.0.142"):
                print("Migrating config from < 2.0.142...")
                if 'agent.goal.notify' not in data:
                    data['agent.goal.notify'] = True
                updated = True

            # < 2.0.143
            if old < parse_version("2.0.143"):
                print("Migrating config from < 2.0.143...")
                if 'ctx.records.filter' not in data:
                    data['ctx.records.filter'] = "all"
                updated = True

            # < 2.0.144
            if old < parse_version("2.0.144"):
                print("Migrating config from < 2.0.144...")
                if 'cmd_history' in data['plugins'] \
                        and 'syntax_get_ctx_list_in_date_range' in data['plugins']['cmd_history']:
                    # remove
                    del data['plugins']['cmd_history']['syntax_get_ctx_list_in_date_range']
                if 'cmd_history' in data['plugins'] \
                        and 'syntax_get_ctx_content_by_id' in data['plugins']['cmd_history']:
                    # remove
                    del data['plugins']['cmd_history']['syntax_get_ctx_content_by_id']
                updated = True

            # < 2.0.149
            if old < parse_version("2.0.149"):
                print("Migrating config from < 2.0.149...")
                # logger
                if 'log.dalle' not in data:
                    data['log.dalle'] = False
                if 'log.level' not in data:
                    data['log.level'] = "error"
                if 'log.plugins' not in data:
                    data['log.plugins'] = False
                if 'log.assistants' not in data:
                    data['log.assistants'] = False
                if 'log.llama' not in data:
                    if 'llama.log' in data:
                        data['log.llama'] = data['llama.log']
                        del data['llama.log']
                    else:
                        data['log.llama'] = False

                # painter
                if 'painter.brush.color' not in data:
                    data['painter.brush.color'] = 'Black'
                if 'painter.brush.mode' not in data:
                    data['painter.brush.mode'] = 'brush'
                if 'painter.brush.size' not in data:
                    data['painter.brush.size'] = 3
                updated = True

            # < 2.0.152
            if old < parse_version("2.0.152"):
                print("Migrating config from < 2.0.152...")
                data['cmd.prompt'] = cfg_get_base('cmd.prompt')  # bg run fix
                updated = True

            # < 2.0.153
            if old < parse_version("2.0.153"):
                print("Migrating config from < 2.0.153...")
                if 'layout.dialog.geometry.store' not in data:
                    data['layout.dialog.geometry.store'] = True
                updated = True

            # < 2.0.157
            if old < parse_version("2.0.157"):
                # decrease chunk size
                print("Migrating config from < 2.0.157...")
                if 'cmd_web_google' in data['plugins'] \
                        and 'chunk_size' in data['plugins']['cmd_web_google']:
                    if data['plugins']['cmd_web_google']['chunk_size'] > 20000:
                        data['plugins']['cmd_web_google']['chunk_size'] = 20000
                updated = True

            # < 2.0.161
            if old < parse_version("2.0.161"):
                print("Migrating config from < 2.0.161...")
                if 'ctx.search_content' not in data:
                    data['ctx.search_content'] = False
                if 'download.dir' not in data:
                    data['download.dir'] = "download"
                updated = True

            # < 2.0.162 - migrate indexes into db
            if old < parse_version("2.0.162"):
                print("Migrating indexes from < 2.0.162...")
                if 'llama.idx.replace_old' not in data:
                    data['llama.idx.replace_old'] = True
                self.window.core.idx.patch(old)
                updated = True

            # < 2.0.164 - migrate indexes into db
            if old < parse_version("2.0.164"):
                print("Migrating config from < 2.0.164...")

                # Migrate plugins to provider-based versions

                # rename cmd_web_google to cmd_web
                if 'cmd_web_google' in data["plugins"]:
                    data["plugins"]["cmd_web"] = data["plugins"]["cmd_web_google"]
                    del data["plugins"]["cmd_web_google"]
                if 'cmd_web_google' in data["plugins_enabled"]:
                    data["plugins_enabled"]["cmd_web"] = data["plugins_enabled"]["cmd_web_google"]
                    del data["plugins_enabled"]["cmd_web_google"]

                # rename audio_openai_whisper to audio_input
                if 'audio_openai_whisper' in data["plugins"]:
                    data["plugins"]["audio_input"] = data["plugins"]["audio_openai_whisper"]
                    del data["plugins"]["audio_openai_whisper"]
                if 'audio_openai_whisper' in data["plugins_enabled"]:
                    data["plugins_enabled"]["audio_input"] = data["plugins_enabled"]["audio_openai_whisper"]
                    del data["plugins_enabled"]["audio_openai_whisper"]

                # migrate model to whisper_model
                if 'audio_input' in data["plugins"] and "model" in data["plugins"]["audio_input"]:
                    data["plugins"]["audio_input"]["whisper_model"] = data["plugins"]["audio_input"]["model"]
                    del data["plugins"]["audio_input"]["model"]

                # rename audio_openai_tts to audio_output
                if 'audio_openai_tts' in data["plugins"]:
                    data["plugins"]["audio_output"] = data["plugins"]["audio_openai_tts"]
                    del data["plugins"]["audio_openai_tts"]
                if 'audio_openai_tts' in data["plugins_enabled"]:
                    data["plugins_enabled"]["audio_output"] = data["plugins_enabled"]["audio_openai_tts"]
                    del data["plugins_enabled"]["audio_openai_tts"]

                # migrate model and voice to openai_model and openai_voice
                if 'audio_output' in data["plugins"] and "model" in data["plugins"]["audio_output"]:
                    data["plugins"]["audio_output"]["openai_model"] = data["plugins"]["audio_output"]["model"]
                    del data["plugins"]["audio_output"]["model"]
                if 'audio_output' in data["plugins"] and "voice" in data["plugins"]["audio_output"]:
                    data["plugins"]["audio_output"]["openai_voice"] = data["plugins"]["audio_output"]["voice"]
                    del data["plugins"]["audio_output"]["voice"]

                # migrate azure settings
                if 'audio_azure' in data["plugins"] and "azure_api_key" in data["plugins"]["audio_azure"]:
                    data["plugins"]["audio_output"]["azure_api_key"] = data["plugins"]["audio_azure"]["azure_api_key"]
                if 'audio_azure' in data["plugins"] and "azure_region" in data["plugins"]["audio_azure"]:
                    data["plugins"]["audio_output"]["azure_region"] = data["plugins"]["audio_azure"]["azure_region"]
                if 'audio_azure' in data["plugins"] and "voice_en" in data["plugins"]["audio_azure"]:
                    data["plugins"]["audio_output"]["azure_voice_en"] = data["plugins"]["audio_azure"]["voice_en"]
                if 'audio_azure' in data["plugins"] and "voice_pl" in data["plugins"]["audio_azure"]:
                    data["plugins"]["audio_output"]["azure_voice_pl"] = data["plugins"]["audio_azure"]["voice_pl"]

                # remove audio voice
                if 'audio_output' in data["plugins"] and "voice_en" in data["plugins"]["audio_output"]:
                    del data["plugins"]["audio_output"]["voice_en"]
                if 'audio_output' in data["plugins"] and "voice_pl" in data["plugins"]["audio_output"]:
                    del data["plugins"]["audio_output"]["voice_pl"]

                # remove audio_azure
                if 'audio_azure' in data["plugins"]:
                    del data["plugins"]["audio_azure"]
                if 'audio_azure' in data["plugins_enabled"]:
                    del data["plugins_enabled"]["audio_azure"]

                updated = True

            # < 2.0.165
            if old < parse_version("2.0.165"):
                print("Migrating config from < 2.0.165...")
                if 'llama.idx.excluded_ext' not in data:
                    data['llama.idx.excluded_ext'] = "3g2,3gp,7z,a,aac,aiff,alac,apk,apk,apng,app,ar,avi,avif," \
                                                     "bin,bmp,bz2,cab,class,deb,deb,dll,dmg,dmg,drv,dsd,dylib," \
                                                     "dylib,ear,egg,elf,esd,exe,flac,flv,gif,gz,heic,heif,ico," \
                                                     "img,iso,jar,jpeg,jpg,ko,lib,lz,lz4,m2v,m4a,m4v,mkv,mov,mp3," \
                                                     "mp4,mpc,msi,nrg,o,ogg,ogv,pcm,pkg,pkg,png,psd,pyc,rar,rpm,rpm," \
                                                     "so,so,svg,swm,sys,tar,tiff,vdi,vhd,vhdx,vmdk,vob,war,wav," \
                                                     "webm,webp,whl,wim,wma,wmv,xz,zip,zst"
                if 'cmd_custom' in data["plugins"]:
                    if 'cmds' in data["plugins"]["cmd_custom"]:
                        for i, cmd in enumerate(data["plugins"]["cmd_custom"]["cmds"]):
                            if "enabled" not in cmd:
                                data["plugins"]["cmd_custom"]["cmds"][i]["enabled"] = True
                updated = True

            # < 2.0.166 - migrate self_loop plugin to agent
            if old < parse_version("2.0.166"):
                print("Migrating config from < 2.0.166...")
                if 'self_loop' in data["plugins"]:
                    data["plugins"]["agent"] = data["plugins"]["self_loop"]
                    del data["plugins"]["self_loop"]
                if 'self_loop' in data["plugins_enabled"]:
                    data["plugins_enabled"]["agent"] = data["plugins_enabled"]["self_loop"]
                    del data["plugins_enabled"]["self_loop"]
                updated = True

            # < 2.0.170 - add audio input language
            if old < parse_version("2.0.170"):
                print("Migrating config from < 2.0.170...")
                if 'audio_input' in data["plugins"]:
                    # add language to google_args if not present
                    is_lang = False
                    if "google_args" in data["plugins"]["audio_input"] \
                            and isinstance(data["plugins"]["audio_input"]["google_args"], list):
                        for option in data["plugins"]["audio_input"]["google_args"]:
                            if option["name"] == "language":
                                is_lang = True
                                break
                    if not is_lang:
                        if "google_args" not in data["plugins"]["audio_input"] or \
                                not isinstance(data["plugins"]["audio_input"]["google_args"], list):
                            data["plugins"]["audio_input"]["google_args"] = []
                        data["plugins"]["audio_input"]["google_args"].append({
                            "name": "language",
                            "value": "en-US",
                            "type": "str",
                        })

                    # add language to google_cloud_args if not present
                    is_lang = False
                    if "google_cloud_args" in data["plugins"]["audio_input"] \
                            and isinstance(data["plugins"]["audio_input"]["google_cloud_args"], list):
                        for option in data["plugins"]["audio_input"]["google_cloud_args"]:
                            if option["name"] == "language":
                                is_lang = True
                                break
                    if not is_lang:
                        if "google_cloud_args" not in data["plugins"]["audio_input"] or \
                                not isinstance(data["plugins"]["audio_input"]["google_cloud_args"], list):
                            data["plugins"]["audio_input"]["google_cloud_args"] = []
                        data["plugins"]["audio_input"]["google_cloud_args"].append({
                            "name": "language",
                            "value": "en-US",
                            "type": "str",
                        })

                    # add language to bing_args if not present
                    is_lang = False
                    if "bing_args" in data["plugins"]["audio_input"] \
                            and isinstance(data["plugins"]["audio_input"]["bing_args"], list):
                        for option in data["plugins"]["audio_input"]["bing_args"]:
                            if option["name"] == "language":
                                is_lang = True
                                break
                    if not is_lang:
                        if "bing_args" not in data["plugins"]["audio_input"] or \
                                not isinstance(data["plugins"]["audio_input"]["bing_args"], list):
                            data["plugins"]["audio_input"]["bing_args"] = []
                        data["plugins"]["audio_input"]["bing_args"].append({
                            "name": "language",
                            "value": "en-US",
                            "type": "str",
                        })
                updated = True

            # < 2.0.172 - fix cmd syntax
            if old < parse_version("2.0.172"):
                print("Migrating config from < 2.0.172...")
                if 'cmd_files' in data["plugins"] and 'syntax_file_index' in data["plugins"]["cmd_files"]:
                    syntax = '"file_index": use it to index (embed in Vector Store) a file or directory for ' \
                             'future use, params: "path"'
                    data["plugins"]["cmd_files"]["syntax_file_index"] = syntax
                if 'cmd_web' in data["plugins"] and 'syntax_web_url_open' in data["plugins"]["cmd_web"]:
                    syntax = '"web_url_open": use it to get contents from a specific Web page. ' \
                             'Use a custom summary prompt if necessary, otherwise a default summary will be used, ' \
                             'params: "url", "summarize_prompt"'
                    data["plugins"]["cmd_web"]["syntax_web_url_open"] = syntax
                if 'cmd_web' in data["plugins"] and 'syntax_web_url_raw' in data["plugins"]["cmd_web"]:
                    syntax = '"web_url_raw": use it to get RAW text/html content (not summarized) from ' \
                             'a specific Web page, params: "url"'
                    data["plugins"]["cmd_web"]["syntax_web_url_raw"] = syntax
                if 'cmd_web' in data["plugins"] and 'syntax_web_urls' in data["plugins"]["cmd_web"]:
                    syntax = '"web_urls": use it to search the Web for URLs to use, prepare a search query itself, ' \
                             'a list of found links to websites will be returned, 10 links per page max. ' \
                             'You can change the page or the number of links per page using the provided parameters, ' \
                             'params: "query", "page", "num_links"'
                    data["plugins"]["cmd_web"]["syntax_web_urls"] = syntax
                updated = True

            # < 2.1.1
            if old < parse_version("2.1.1"):
                print("Migrating config from < 2.1.1...")
                if 'llama.hub.loaders.args' not in data:
                    data['llama.hub.loaders.args'] = []
                updated = True

            # < 2.1.2
            if old < parse_version("2.1.2"):
                print("Migrating config from < 2.1.2...")
                if 'llama.hub.loaders.use_local' not in data:
                    data['llama.hub.loaders.use_local'] = False
                updated = True

            # < 2.1.5 - syntax
            if old < parse_version("2.1.5"):
                print("Migrating config from < 2.1.5...")
                if 'cmd_files' in data["plugins"] and 'syntax_file_index' in data["plugins"]["cmd_files"]:
                    syntax = '"file_index": use it to index (embed in Vector Store) a file or directory, params: "path"'
                    data["plugins"]["cmd_files"]["syntax_file_index"] = syntax
                    updated = True

            # < 2.1.8 - syntax
            if old < parse_version("2.1.8"):
                print("Migrating config from < 2.1.8...")
                if 'idx_llama_index' in data["plugins"] and 'syntax_prepare_question' in data["plugins"]["idx_llama_index"]:
                    syntax = 'Simplify the question into a short query for retrieving information from a vector store.'
                    data["plugins"]["idx_llama_index"]["syntax_prepare_question"] = syntax
                    updated = True

            # < 2.1.9 - syntax
            if old < parse_version("2.1.9"):
                print("Migrating config from < 2.1.9...")
                if 'cmd_files' in data["plugins"] and 'syntax_read_file' in data["plugins"]["cmd_files"]:
                    syntax = '"read_file": read data from file, if multiple files then pass list of files, params: "filename"'
                    data["plugins"]["cmd_files"]["syntax_read_file"] = syntax
                if 'log.events' not in data:
                    data["log.events"] = False
                    updated = True

            # < 2.1.10
            if old < parse_version("2.1.10"):
                print("Migrating config from < 2.1.10...")

                # fix missing updated before >>>
                if 'cmd_files' in data["plugins"] and 'syntax_file_index' in data["plugins"]["cmd_files"]:
                    syntax = '"file_index": use it to index (embed in Vector Store) a file or directory, params: "path"'
                    data["plugins"]["cmd_files"]["syntax_file_index"] = syntax
                if 'idx_llama_index' in data["plugins"] and 'syntax_prepare_question' in data["plugins"]["idx_llama_index"]:
                    syntax = 'Simplify the question into a short query for retrieving information from a vector store.'
                    data["plugins"]["idx_llama_index"]["syntax_prepare_question"] = syntax
                if 'cmd_files' in data["plugins"] and 'syntax_read_file' in data["plugins"]["cmd_files"]:
                    syntax = '"read_file": read data from file, if multiple files then pass list of files, params: "filename"'
                    data["plugins"]["cmd_files"]["syntax_read_file"] = syntax
                if 'log.events' not in data:
                    data["log.events"] = False
                # <<< fix missing updated before

                # current
                if 'ctx.records.filter.labels' not in data:
                    data["ctx.records.filter.labels"] = [0, 1, 2, 3, 4, 5, 6, 7]

                if 'preset.plugins' not in data:
                    data["preset.plugins"] = ""

                if 'ctx.records.filter' in data and str(data["ctx.records.filter"]).startswith("label"):
                    data["ctx.records.filter"] = "all"
                updated = True

            if old < parse_version("2.1.12"):
                print("Migrating config from < 2.1.12...")
                if 'max_requests_limit' not in data:
                    data["max_requests_limit"] = 60
                if 'ctx.allow_item_delete' not in data:
                    data["ctx.allow_item_delete"] = True
                if 'ctx.counters.all' not in data:
                    data["ctx.counters.all"] = False
                if 'agent.prompt.continue' not in data:
                    data["agent.prompt.continue"] = "continue..."
                if 'api_endpoint' not in data:
                    data["api_endpoint"] = "https://api.openai.com/v1"
                updated = True

            if old < parse_version("2.1.15"):
                print("Migrating config from < 2.1.15...")
                if 'ctx.edit_icons' not in data:
                    data["ctx.edit_icons"] = False
                if 'llama.idx.auto.modes' not in data:
                    data["llama.idx.auto.modes"] = "chat,completion,vision,assistant,langchain,llama_index,agent"
                if 'ctx.allow_item_delete' in data:
                    del data["ctx.allow_item_delete"]
                updated = True

            if old < parse_version("2.1.16"):
                print("Migrating config from < 2.1.16...")
                if 'ctx.sources' not in data:
                    data["ctx.sources"] = True
                updated = True

            if old < parse_version("2.1.18"):
                print("Migrating config from < 2.1.18...")
                if 'ctx.audio' not in data:
                    data["ctx.audio"] = True
                updated = True

            if old < parse_version("2.1.19"):
                print("Migrating config from < 2.1.19...")
                if 'llama.idx.excluded_ext' in data:
                    data["llama.idx.excluded.ext"] = copy.deepcopy(data["llama.idx.excluded_ext"])
                    del data["llama.idx.excluded_ext"]
                if 'llama.idx.excluded.force' not in data:
                    data["llama.idx.excluded.force"] = False
                if 'llama.idx.custom_meta' not in data:
                    data["llama.idx.custom_meta"] = [
                          {
                              "extensions": "*",
                              "key": "file_name",
                              "value": "{relative_path}"
                          }
                    ]
                updated = True

            # < 2.1.20
            if old < parse_version("2.1.20"):
                print("Migrating config from < 2.1.20...")
                data['cmd.prompt'] = cfg_get_base('cmd.prompt')  # moved to json schema
                updated = True

            # < 2.1.22
            if old < parse_version("2.1.22"):
                print("Migrating config from < 2.1.22...")
                if 'llama.idx.custom_meta.web' not in data:
                    data["llama.idx.custom_meta.web"] = []
                updated = True

            # < 2.1.23
            if old < parse_version("2.1.23"):
                print("Migrating config from < 2.1.23...")
                if 'llama.idx.embeddings.provider' not in data:
                    data["llama.idx.embeddings.provider"] = "openai"
                if 'llama.idx.embeddings.args' not in data:
                    data["llama.idx.embeddings.args"] = [
                        {
                            "name": "model",
                            "value": "text-embedding-3-small",
                            "type": "str"
                        }
                    ]
                if 'llama.idx.embeddings.env' not in data:
                    data["llama.idx.embeddings.env"] = [
                        {
                            "name": "OPENAI_API_KEY",
                            "value": "{api_key}",
                        },
                        {
                            "name": "OPENAI_API_BASE",
                            "value": "{api_endpoint}",
                        }
                    ]
                self.window.core.plugins.reset_options("cmd_web", [
                    "cmd.web_url_open",
                    "cmd.web_url_raw",
                ])
                updated = True

            # < 2.1.26
            if old < parse_version("2.1.26"):
                print("Migrating config from < 2.1.26...")
                if 'agent.prompt.continue' in data and data['agent.prompt.continue'] == 'continue...':
                    data["agent.prompt.continue"] = "continue if needed..."
                self.window.core.plugins.reset_options("idx_llama_index", [
                    "prompt",
                ])
                updated = True

            # < 2.1.28
            if old < parse_version("2.1.28"):
                print("Migrating config from < 2.1.28...")
                if 'log.ctx' not in data:
                    data["log.ctx"] = True
                if 'llama.idx.embeddings.limit.rpm' not in data:
                    data["llama.idx.embeddings.limit.rpm"] = 100
                updated = True

            # < 2.1.29
            if old < parse_version("2.1.29"):
                print("Migrating config from < 2.1.29...")
                self.window.core.plugins.reset_options("cmd_code_interpreter", [
                    "cmd.code_execute",
                ])
                updated = True

            # < 2.1.31
            if old < parse_version("2.1.31"):
                print("Migrating config from < 2.1.31...")
                self.window.core.plugins.reset_options("cmd_code_interpreter", [
                    "cmd.code_execute",
                ])
                files_to_move = [
                    {"_interpreter.current.py": ".interpreter.current.py"},
                    {"_interpreter.py": ".interpreter.output.py"},
                    {"_interpreter.input.py": ".interpreter.input.py"},
                ]
                files_to_remove = [
                    "_interpreter.tmp.py",
                ]
                dir = self.window.core.config.get_user_dir("data")
                try:
                    for file in files_to_move:
                        for src, dst in file.items():
                            src = os.path.join(dir, src)
                            dst = os.path.join(dir, dst)
                            if os.path.exists(src):
                                os.rename(src, dst)
                    for file in files_to_remove:
                        file = os.path.join(dir, file)
                        if os.path.exists(file):
                            os.remove(file)
                except Exception as e:
                    print("Error while migrating interpreter files:", e)

                updated = True

            # < 2.1.32
            if old < parse_version("2.1.32"):
                print("Migrating config from < 2.1.32...")
                if 'ctx.use_extra' not in data:
                    data["ctx.use_extra"] = True

                self.window.core.plugins.reset_options("real_time", [
                    "tpl",
                ])

                # old keys first
                data['cmd.prompt'] = cfg_get_base('prompt.cmd')  # new format
                data['cmd.prompt.extra'] = cfg_get_base('prompt.cmd.extra')  # new format
                data['cmd.prompt.extra.assistants'] = cfg_get_base('prompt.cmd.extra.assistants')  # new format

                # new keys
                data['prompt.agent.goal'] = cfg_get_base('prompt.agent.goal')  # new format

                # replace to new keys
                self.window.core.config.replace_key(data, "img_prompt", "prompt.img")
                self.window.core.config.replace_key(data, "ctx.auto_summary.prompt", "prompt.ctx.auto_summary.user")
                self.window.core.config.replace_key(data, "ctx.auto_summary.system", "prompt.ctx.auto_summary.system")
                self.window.core.config.replace_key(data, "cmd.prompt", "prompt.cmd")
                self.window.core.config.replace_key(data, "cmd.prompt.extra", "prompt.cmd.extra")
                self.window.core.config.replace_key(data, "cmd.prompt.extra.assistants", "prompt.cmd.extra.assistants")
                self.window.core.config.replace_key(data, "agent.prompt.continue", "prompt.agent.continue")
                self.window.core.config.replace_key(data, "default_prompt", "prompt.default")
                updated = True

            # < 2.1.35
            if old < parse_version("2.1.35"):
                print("Migrating config from < 2.1.35...")
                if 'interpreter.auto_clear' not in data:
                    data["interpreter.auto_clear"] = True
                if 'interpreter.execute_all' not in data:
                    data["interpreter.execute_all"] = True
                if 'interpreter.edit' not in data:
                    data["interpreter.edit"] = False
                if 'interpreter.input' not in data:
                    data["interpreter.input"] = ""
                if 'video.player.path' not in data:
                    data["video.player.path"] = ""
                if 'video.player.volume' not in data:
                    data["video.player.volume"] = 100
                if 'video.player.volume.mute' not in data:
                    data["video.player.volume.mute"] = False
                updated = True

            # < 2.1.37
            if old < parse_version("2.1.37"):
                print("Migrating config from < 2.1.37...")
                if 'audio.transcribe.convert_video' not in data:
                    data["audio.transcribe.convert_video"] = True
                updated = True

            # < 2.1.38
            if old < parse_version("2.1.38"):
                print("Migrating config from < 2.1.38...")
                if 'lang' in data and data['lang'] == 'ua':
                    data["lang"] = "uk"
                updated = True

            # < 2.1.45
            if old < parse_version("2.1.45"):
                print("Migrating config from < 2.1.45...")
                if 'ctx.copy_code' not in data:
                    data["ctx.copy_code"] = True
                updated = True

            # < 2.1.52
            if old < parse_version("2.1.52"):
                print("Migrating config from < 2.1.52...")
                if 'ctx.code_interpreter' not in data:
                    data["ctx.code_interpreter"] = True
                updated = True

            # < 2.1.59
            if old < parse_version("2.1.59"):
                print("Migrating config from < 2.1.59...")
                if 'render.code_syntax' not in data:
                    data["render.code_syntax"] = "github-dark"
                if 'zoom' not in data:
                    data["zoom"] = 1.0
                if 'render.engine' not in data:
                    data["render.engine"] = "web"
                if 'render.open_gl' not in data:
                    data["render.open_gl"] = False

                # in snap, leave legacy render engine by default
                # if self.window.core.platforms.is_snap():
                    # data["render.engine"] = "legacy"

                # css upgrade
                patch_css('web.css', True)  # NEW
                patch_css('web.light.css', True)  # NEW
                patch_css('web.dark.css', True)  #  NEW
                updated = True

            # < 2.1.60
            if old < parse_version("2.1.60"):
                print("Migrating config from < 2.1.60...")
                # css upgrade
                patch_css('web.css', True)  # force update
                updated = True

            # < 2.1.61
            if old < parse_version("2.1.61"):
                print("Migrating config from < 2.1.61...")
                # css upgrade
                patch_css('web.css', True)  # force update
                updated = True

            # < 2.1.63
            if old < parse_version("2.1.63"):
                print("Migrating config from < 2.1.63...")
                # css upgrade
                patch_css('web.css', True)  # force update
                patch_css('web.light.css', True)  # force update
                patch_css('web.dark.css', True)  # force update
                updated = True

            # < 2.1.70
            if old < parse_version("2.1.70"):
                print("Migrating config from < 2.1.70...")
                # css upgrade
                patch_css('web.css', True)  # force update
                updated = True

            # < 2.1.72
            if old < parse_version("2.1.72"):
                print("Migrating config from < 2.1.72...")
                # css upgrade
                patch_css('web.css', True)  # force update
                patch_css('web.light.css', True)  # force update
                patch_css('web.dark.css', True)  # force update
                updated = True

            # < 2.1.73
            if old < parse_version("2.1.73"):
                print("Migrating config from < 2.1.73...")
                # fix: issue #50
                if "llama.idx.embeddings.args" in data:
                    for arg in data["llama.idx.embeddings.args"]:
                        if "type" not in arg:
                            arg["type"] = "str"
                updated = True

            # < 2.1.74
            if old < parse_version("2.1.74"):
                print("Migrating config from < 2.1.74...")
                # css upgrade
                patch_css('web.css', True)  # force update
                patch_css('web.light.css', True)  # force update
                patch_css('web.dark.css', True)  # force update
                updated = True

            # < 2.1.75
            if old < parse_version("2.1.75"):
                print("Migrating config from < 2.1.75...")
                # css upgrade
                patch_css('web.css', True)  # force update
                patch_css('web.light.css', True)  # force update
                patch_css('web.dark.css', True)  # force update
                updated = True

            # < 2.1.76
            if old < parse_version("2.1.76"):
                print("Migrating config from < 2.1.76...")
                if 'render.blocks' not in data:
                    data["render.blocks"] = True
                # css upgrade
                patch_css('web.css', True)  # force update
                patch_css('web.light.css', True)  # force update
                patch_css('web.dark.css', True)  # force update
                updated = True

            # < 2.1.78
            if old < parse_version("2.1.78"):
                print("Migrating config from < 2.1.78...")
                # css upgrade, scroll bg
                patch_css('web.css', True)  # force update
                patch_css('web.light.css', True)  # force update
                patch_css('web.dark.css', True)  # force update
                updated = True

            # < 2.1.79
            if old < parse_version("2.1.79"):
                print("Migrating config from < 2.1.79...")
                if 'assistant.store.hide_threads' not in data:
                    data["assistant.store.hide_threads"] = True
                updated = True

            # < 2.2.2
            if old < parse_version("2.2.2"):
                print("Migrating config from < 2.2.2...")
                if 'app.env' not in data:
                    data["app.env"] = []
                updated = True

            # < 2.2.7
            if old < parse_version("2.2.7"):
                print("Migrating config from < 2.2.7...")
                if 'prompt.agent.instruction' not in data:
                    data["prompt.agent.instruction"] = ""
                if 'prompt.expert' not in data:
                    data["prompt.expert"] = ""
                if 'experts.mode' not in data:
                    data["experts.mode"] = "chat"
                # from base
                data["prompt.agent.instruction"] = cfg_get_base('prompt.agent.instruction')
                data["prompt.agent.continue"] = cfg_get_base('prompt.agent.continue')
                data["prompt.agent.goal"] = cfg_get_base('prompt.agent.goal')
                data["prompt.expert"] = cfg_get_base('prompt.expert')
                data["prompt.img"] = cfg_get_base('prompt.img')
                updated = True

            # < 2.2.8
            if old < parse_version("2.2.8"):
                print("Migrating config from < 2.2.8...")
                if 'access.audio.event.speech' not in data:
                    data["access.audio.event.speech"] = False
                if 'access.audio.notify.execute' not in data:
                    data["access.audio.notify.execute"] = True
                if 'access.microphone.notify' not in data:
                    data["access.microphone.notify"] = True
                if 'access.shortcuts' not in data:
                    data["access.shortcuts"] = [
                        {
                            "action": "voice_cmd.toggle",
                            "key": "Space",
                            "key_modifier": "Control"
                        },
                        {
                            "action": "tab.chat",
                            "key": "1",
                            "key_modifier": "Control"
                        },
                        {
                            "action": "tab.files",
                            "key": "2",
                            "key_modifier": "Control"
                        },
                        {
                            "action": "tab.calendar",
                            "key": "3",
                            "key_modifier": "Control"
                        },
                        {
                            "action": "tab.draw",
                            "key": "4",
                            "key_modifier": "Control"
                        },
                        {
                            "action": "tab.notepad",
                            "key": "5",
                            "key_modifier": "Control"
                        }
                    ]
                if 'access.voice_control' not in data:
                    data["access.voice_control"] = False
                if 'access.voice_control.model' not in data:
                    data["access.voice_control.model"] = "gpt-3.5-turbo"
                updated = True

            # < 2.2.11
            if old < parse_version("2.2.11"):
                print("Migrating config from < 2.2.11...")
                if 'access.audio.event.speech.disabled' not in data:
                    data["access.audio.event.speech.disabled"] = []
                updated = True

            # < 2.2.14
            if old < parse_version("2.2.14"):
                print("Migrating config from < 2.2.14...")
                if 'access.voice_control.blacklist' not in data:
                    data["access.voice_control.blacklist"] = []
                updated = True

            # < 2.2.16
            if old < parse_version("2.2.16"):
                print("Migrating config from < 2.2.16...")
                if 'access.audio.use_cache' not in data:
                    data["access.audio.use_cache"] = True
                updated = True

            # < 2.2.20
            if old < parse_version("2.2.20"):
                print("Migrating config from < 2.2.20...")
                if 'func_call.native' not in data:
                    data["func_call.native"] = True
                patch_css('web.css', True)  # force update
                updated = True

            # < 2.2.22
            if old < parse_version("2.2.22"):
                print("Migrating config from < 2.2.22...")
                if 'llama.idx.stop.error' not in data:
                    data["llama.idx.stop.error"] = True
                updated = True

            # < 2.2.25
            if old < parse_version("2.2.25"):
                print("Migrating config from < 2.2.25...")
                data["prompt.expert"] = cfg_get_base('prompt.expert')
                updated = True

            # < 2.2.26
            if old < parse_version("2.2.26"):
                print("Migrating config from < 2.2.26...")
                if 'ctx.records.folders.top' not in data:
                    data["ctx.records.folders.top"] = False
                if 'ctx.records.separators' not in data:
                    data["ctx.records.separators"] = True
                if 'ctx.records.groups.separators' not in data:
                    data["ctx.records.groups.separators"] = True
                updated = True

            # < 2.2.27
            if old < parse_version("2.2.27"):
                print("Migrating config from < 2.2.27...")
                if 'ctx.records.pinned.separators' not in data:
                    data["ctx.records.pinned.separators"] = False
                updated = True

            # < 2.2.28
            if old < parse_version("2.2.28"):
                print("Migrating config from < 2.2.28...")
                if 'llama.idx.chat.mode' not in data:
                    data["llama.idx.chat.mode"] = "context"
                if 'llama.idx.mode' not in data:
                    data["llama.idx.mode"] = "chat"
                updated = True

            # < 2.2.31
            if old < parse_version("2.2.31"):
                print("Migrating config from < 2.2.31...")
                if 'agent.continue.always' not in data:
                    data["agent.continue.always"] = False
                if 'prompt.agent.continue.always' not in data:
                    data["prompt.agent.continue.always"] = "Continue reasoning..."
                updated = True

            # < 2.4.0
            if old < parse_version("2.4.0"):
                print("Migrating config from < 2.4.0...")
                if 'tabs.data' not in data:
                    data["tabs.data"] = self.window.core.tabs.from_defaults()
                updated = True

            # < 2.4.7
            if old < parse_version("2.4.7"):
                print("Migrating config from < 2.4.7...")
                self.window.core.plugins.reset_options("cmd_mouse_control", [
                    "prompt",
                ])
                updated = True

            # < 2.4.10
            if old < parse_version("2.4.10"):
                print("Migrating config from < 2.4.10...")
                if 'prompt.agent.continue.llama' not in data:
                    data["prompt.agent.continue.llama"] = cfg_get_base('prompt.agent.continue.llama')
                if 'agent.llama.idx' not in data:
                    data["agent.llama.idx"] = cfg_get_base('agent.llama.idx')
                if 'agent.llama.steps' not in data:
                    data["agent.llama.steps"] = cfg_get_base('agent.llama.steps')
                if 'agent.llama.provider' not in data:
                    data["agent.llama.provider"] = cfg_get_base('agent.llama.provider')
                if 'agent.llama.verbose' not in data:
                    data["agent.llama.verbose"] = cfg_get_base('agent.llama.verbose')
                data["agent.goal.notify"] = False  # disable by default
                updated = True

            # < 2.4.11
            if old < parse_version("2.4.11"):
                print("Migrating config from < 2.4.11...")
                if 'api_proxy' not in data:
                    data["api_proxy"] =""
                updated = True

            # < 2.4.13
            if old < parse_version("2.4.13"):
                print("Migrating config from < 2.4.13...")
                data["interpreter.auto_clear"] = False
                if 'cmd_code_interpreter' in data['plugins'] \
                        and 'cmd.code_execute' in data['plugins']['cmd_code_interpreter']:
                    # remove
                    del data['plugins']['cmd_code_interpreter']['cmd.code_execute']
                if 'cmd_code_interpreter' in data['plugins'] \
                        and 'cmd.code_execute_all' in data['plugins']['cmd_code_interpreter']:
                    # remove
                    del data['plugins']['cmd_code_interpreter']['cmd.code_execute_all']
                if 'cmd_code_interpreter' in data['plugins'] \
                        and 'cmd.code_execute_file' in data['plugins']['cmd_code_interpreter']:
                    # remove
                    del data['plugins']['cmd_code_interpreter']['cmd.code_execute_file']
                updated = True

            # < 2.4.14
            if old < parse_version("2.4.14"):
                print("Migrating config from < 2.4.14...")
                if 'prompt.agent.llama.max_eval' not in data:
                    data["prompt.agent.llama.max_eval"] = cfg_get_base('prompt.agent.llama.max_eval')
                if 'prompt.agent.llama.append_eval' not in data:
                    data["prompt.agent.llama.append_eval"] = cfg_get_base('prompt.agent.llama.append_eval')
                if 'agent.llama.loop.enabled' not in data:
                    data["agent.llama.loop.enabled"] = cfg_get_base('agent.llama.loop.enabled')
                if 'agent.llama.loop.score' not in data:
                    data["agent.llama.loop.score"] = cfg_get_base('agent.llama.loop.score')
                updated = True

            # < 2.4.15
            if old < parse_version("2.4.15"):
                print("Migrating config from < 2.4.15...")
                data["interpreter.auto_clear"] = False
                if 'cmd_code_interpreter' in data['plugins'] \
                        and 'cmd.ipython_execute_new' in data['plugins']['cmd_code_interpreter']:
                    # remove
                    del data['plugins']['cmd_code_interpreter']['cmd.ipython_execute_new']
                if 'cmd_code_interpreter' in data['plugins'] \
                        and 'cmd.ipython_execute' in data['plugins']['cmd_code_interpreter']:
                    # remove
                    del data['plugins']['cmd_code_interpreter']['cmd.ipython_execute']
                if 'cmd_code_interpreter' in data['plugins'] \
                        and 'cmd.sys_exec' in data['plugins']['cmd_code_interpreter']:
                    # remove
                    del data['plugins']['cmd_code_interpreter']['cmd.sys_exec']
                if 'cmd_mouse_control' in data['plugins']:
                    del data['plugins']['cmd_mouse_control']
                updated = True

            # < 2.4.16
            if old < parse_version("2.4.16"):
                print("Migrating config from < 2.4.16...")
                data["interpreter.auto_clear"] = False
                if 'cmd_code_interpreter' in data['plugins'] \
                        and 'cmd.ipython_execute_new' in data['plugins']['cmd_code_interpreter']:
                    # remove
                    del data['plugins']['cmd_code_interpreter']['cmd.ipython_execute_new']
                if 'cmd_code_interpreter' in data['plugins'] \
                        and 'cmd.ipython_execute' in data['plugins']['cmd_code_interpreter']:
                    # remove
                    del data['plugins']['cmd_code_interpreter']['cmd.ipython_execute']
                updated = True

            # < 2.4.19
            if old < parse_version("2.4.19"):
                print("Migrating config from < 2.4.19...")
                if 'cmd_code_interpreter' in data['plugins'] \
                        and 'cmd.ipython_execute' in data['plugins']['cmd_code_interpreter']:
                    # remove
                    del data['plugins']['cmd_code_interpreter']['cmd.ipython_execute']
                updated = True

            # < 2.4.21
            if old < parse_version("2.4.21"):
                print("Migrating config from < 2.4.21...")
                if 'ctx.attachment.mode' not in data:
                    data["ctx.attachment.mode"] = cfg_get_base('ctx.attachment.mode')
                if 'ctx.attachment.summary.model' not in data:
                    data["ctx.attachment.summary.model"] = cfg_get_base('ctx.attachment.summary.model')
                if 'ctx.attachment.verbose' not in data:
                    data["ctx.attachment.verbose"] = cfg_get_base('ctx.attachment.verbose')
                updated = True

            # < 2.4.22
            if old < parse_version("2.4.22"):
                print("Migrating config from < 2.4.22...")
                data["ctx.attachment.mode"] = cfg_get_base('ctx.attachment.mode')
                if 'ctx.attachment.img' not in data:
                    data["ctx.attachment.img"] = cfg_get_base(
                        'ctx.attachment.img')
                updated = True

            # < 2.4.29
            if old < parse_version("2.4.29"):
                print("Migrating config from < 2.4.29...")
                if 'cmd_code_interpreter' in data['plugins'] \
                        and 'ipython_dockerfile' in data['plugins']['cmd_code_interpreter']:
                    # remove
                    del data['plugins']['cmd_code_interpreter']['ipython_dockerfile']
                updated = True

            # < 2.4.31
            if old < parse_version("2.4.31"):
                print("Migrating config from < 2.4.31...")
                if 'attachments_auto_index' not in data:
                    data["attachments_auto_index"] = cfg_get_base(
                        'attachments_auto_index')
                updated = True

            # < 2.4.34
            if old < parse_version("2.4.34"):
                print("Migrating config from < 2.4.34...")
                if 'ctx.attachment.query.model' not in data:
                    data["ctx.attachment.query.model"] = cfg_get_base(
                        'ctx.attachment.query.model')
                updated = True

            # < 2.4.35
            if old < parse_version("2.4.35"):
                print("Migrating config from < 2.4.35...")
                data["ctx.edit_icons"] = True
                updated = True

            # < 2.4.37
            if old < parse_version("2.4.37"):
                print("Migrating config from < 2.4.37...")
                if 'ctx.attachment.rag.history' not in data:
                    data["ctx.attachment.rag.history"] = cfg_get_base(
                        'ctx.attachment.rag.history')
                if 'ctx.attachment.rag.history.max_items' not in data:
                    data["ctx.attachment.rag.history.max_items"] = cfg_get_base(
                        'ctx.attachment.rag.history.max_items')
                updated = True

            # < 2.4.38
            if old < parse_version("2.4.38"):
                print("Migrating config from < 2.4.38...")
                if 'theme.style' not in data:
                    data["theme.style"] = "blocks"
                if 'audio.input.device' not in data:
                    data["audio.input.device"] = "0"
                if 'audio.input.channels' not in data:
                    data["audio.input.channels"] = 1
                if 'audio.input.rate' not in data:
                    data["audio.input.rate"] = 44100
                patch_css('style.light.css', True)  # force update
                updated = True

            # < 2.4.39
            if old < parse_version("2.4.39"):
                print("Migrating config from < 2.4.39...")
                if 'layout.split' not in data:
                    data["layout.split"] = False
                updated = True

            # < 2.4.40
            if old < parse_version("2.4.40"):
                print("Migrating config from < 2.4.40...")
                if 'cmd_web' in data['plugins'] \
                        and 'max_result_length' in data['plugins']['cmd_web']:
                    del data['plugins']['cmd_web']['max_result_length']
                if 'cmd_web' in data['plugins'] \
                        and 'cmd.web_search' in data['plugins']['cmd_web']:
                    del data['plugins']['cmd_web']['cmd.web_search']
                if 'cmd_web' in data['plugins'] \
                        and 'cmd.web_url_open' in data['plugins']['cmd_web']:
                    del data['plugins']['cmd_web']['cmd.web_url_open']
                if 'cmd_web' in data['plugins'] \
                        and 'cmd.web_url_raw' in data['plugins']['cmd_web']:
                    del data['plugins']['cmd_web']['cmd.web_url_raw']
                patch_css('web-blocks.css', True)  # force update
                patch_css('web-blocks.light.css', True)  # force update
                patch_css('web-chatgpt.css', True)  # force update
                patch_css('web-chatgpt_wide.css', True)  # force update
                updated = True

            # < 2.4.44
            if old < parse_version("2.4.44"):
                print("Migrating config from < 2.4.44...")
                data["ctx.records.folders.top"] = True
                updated = True

            # < 2.4.45
            if old < parse_version("2.4.45"):
                print("Migrating config from < 2.4.45...")
                patch_css('style.css', True)  # force update
                updated = True

            # < 2.4.46
            if old < parse_version("2.4.46"):
                print("Migrating config from < 2.4.46...")
                if 'api_azure_version' not in data:
                    data["api_azure_version"] = "2023-07-01-preview"
                if 'api_azure_endpoint' not in data:
                    data["api_azure_endpoint"] = "https://<your-resource-name>.openai.azure.com/"
                if 'api_key_google' not in data:
                    data["api_key_google"] = ""
                if 'api_key_anthropic' not in data:
                    data["api_key_anthropic"] = ""
                if 'api_key_hugging_face' not in data:
                    data["api_key_hugging_face"] = ""
                updated = True

            # < 2.4.51
            if old < parse_version("2.4.51"):
                print("Migrating config from < 2.4.51...")
                if 'audio.input.stop_interval' not in data:
                    data["audio.input.stop_interval"] = 10
                if 'audio.input.continuous' not in data:
                    data["audio.input.continuous"] = False

            # < 2.4.55
            if old < parse_version("2.4.55"):
                print("Migrating config from < 2.4.55...")
                if 'audio.input.timeout' not in data:
                    data["audio.input.timeout"] = 120
                if 'audio.input.timeout.continuous' not in data:
                    data["audio.input.timeout.continuous"] = False

            # < 2.4.56
            if old < parse_version("2.4.56"):
                print("Migrating config from < 2.4.56...")
                remove_modifiers = ["Meta", "Keypad", "GroupSwitch"]
                if 'access.shortcuts' in data:
                    for item in data['access.shortcuts']:
                        if 'key_modifier' in item and item['key_modifier'] == 'Control':
                            item['key_modifier'] = 'Ctrl'
                        elif 'key_modifier' in item and item['key_modifier'] in remove_modifiers:
                            item['key_modifier'] = ''
                updated = True

            # < 2.5.0
            if old < parse_version("2.5.0"):
                print("Migrating config from < 2.5.0...")
                if 'api_key_deepseek' not in data:
                    data["api_key_deepseek"] = ""
                updated = True

            # < 2.5.7
            if old < parse_version("2.5.7"):
                print("Migrating config from < 2.5.7...")
                patch_css('web-blocks.css', True)  # force update
                patch_css('web-chatgpt.css', True)  # force update
                patch_css('web-chatgpt_wide.css', True)  # force update
                updated = True

            # < 2.5.8
            if old < parse_version("2.5.8"):
                print("Migrating config from < 2.5.8...")
                if 'api_key_perplexity' not in data:
                    data["api_key_perplexity"] = ""
                if 'api_endpoint_perplexity' not in data:
                    data["api_endpoint_perplexity"] = "https://api.perplexity.ai"
                updated = True

            # < 2.5.17
            if old < parse_version("2.5.17"):
                print("Migrating config from < 2.5.17...")
                if 'remote_tools.web_search' not in data:
                    data["remote_tools.web_search"] = True
                updated = True

            # < 2.5.18
            if old < parse_version("2.5.18"):
                print("Migrating config from < 2.5.18...")
                if 'remote_tools.image' not in data:
                    data["remote_tools.image"] = False
                updated = True

            # < 2.5.19
            if old < parse_version("2.5.19"):
                print("Migrating config from < 2.5.19...")
                if 'api_use_responses' not in data:
                    data["api_use_responses"] = True
                if 'api_key_xai' not in data:
                    data["api_key_xai"] = ""
                if 'api_endpoint_xai' not in data:
                    data["api_endpoint_xai"] = "https://api.x.ai/v1"
                updated = True

            # < 2.5.20
            if old < parse_version("2.5.20"):
                print("Migrating config from < 2.5.20...")
                if 'api_endpoint_deepseek' not in data:
                    data["api_endpoint_deepseek"] = "https://api.deepseek.com/v1"
                if 'api_endpoint_google' not in data:
                    data["api_endpoint_google"] = "https://generativelanguage.googleapis.com/v1beta/openai"
                if "mode" in data and "mode" == "langchain":  # deprecated mode
                    data["mode"] = "chat"
                updated = True

            # < 2.5.21
            if old < parse_version("2.5.21"):
                print("Migrating config from < 2.5.21...")
                patch_css('web-chatgpt.css', True)  # force replace file
                updated = True

            # < 2.5.24
            if old < parse_version("2.5.24"):
                print("Migrating config from < 2.5.24...")
                patch_css('web-chatgpt.css', True)  # force replace file
                updated = True

            # < 2.5.25
            if old < parse_version("2.5.25"):
                print("Migrating config from < 2.5.25...")
                if 'api_use_responses_llama' not in data:
                    data["api_use_responses_llama"] = False
                updated = True

            # < 2.5.27
            if old < parse_version("2.5.27"):
                print("Migrating config from < 2.5.27...")
                if 'remote_tools.code_interpreter' not in data:
                    data["remote_tools.code_interpreter"] = False
                if 'llama.idx.react' not in data:
                    data["llama.idx.react"] = True
                updated = True

            # < 2.5.29
            if old < parse_version("2.5.29"):
                print("Migrating config from < 2.5.29...")
                if 'api_endpoint_anthropic' not in data:
                    data["api_endpoint_anthropic"] = "https://api.anthropic.com/v1"
                updated = True

            # < 2.5.31
            if old < parse_version("2.5.31"):
                print("Migrating config from < 2.5.31...")
                if 'llama.idx.chat.auto_retrieve' not in data:
                    data["llama.idx.chat.auto_retrieve"] = True
                if 'api_key_mistral' not in data:
                    data["api_key_mistral"] = ""
                if 'api_endpoint_mistral' not in data:
                    data["api_endpoint_mistral"] = "https://api.mistral.ai/v1"
                updated = True

            # < 2.5.35
            if old < parse_version("2.5.35"):
                print("Migrating config from < 2.5.35...")
                data["img_dialog_open"] = False
                updated = True

            # < 2.5.36
            if old < parse_version("2.5.36"):
                print("Migrating config from < 2.5.36...")
                patch_css('style.css', True)  # force replace file
                patch_css('style.dark.css', True)  # force replace file
                patch_css('style.light.css', True)  # force replace file
                patch_css('web-chatgpt.css', True)  # force replace file
                patch_css('web-chatgpt.light.css', True)  # force replace file
                patch_css('web-chatgpt.dark.css', True)  # force replace file
                patch_css('web-chatgpt_wide.css', True)  # force replace file
                patch_css('web-chatgpt_wide.light.css', True)  # force replace file
                patch_css('web-chatgpt_wide.dark.css', True)  # force replace file
                updated = True

            # < 2.5.37
            if old < parse_version("2.5.37"):
                print("Migrating config from < 2.5.37...")
                patch_css('style.css', True)  # force replace file
                patch_css('style.dark.css', True)  # force replace file
                patch_css('style.light.css', True)  # force replace file
                patch_css('web-chatgpt.css', True)  # force replace file
                patch_css('web-chatgpt.light.css', True)  # force replace file
                patch_css('web-chatgpt.dark.css', True)  # force replace file
                patch_css('web-chatgpt_wide.css', True)  # force replace file
                patch_css('web-chatgpt_wide.light.css', True)  # force replace file
                patch_css('web-chatgpt_wide.dark.css', True)  # force replace file
                updated = True

            # < 2.5.40 - update tool prompts
            if old < parse_version("2.5.40"):
                print("Migrating config from < 2.5.40...")

                # config
                data['prompt.agent.goal'] = cfg_get_base('prompt.agent.goal')
                data['prompt.agent.instruction'] = cfg_get_base('prompt.agent.instruction')
                data['prompt.ctx.auto_summary.user'] = cfg_get_base('prompt.ctx.auto_summary.user')
                data['prompt.cmd'] = cfg_get_base('prompt.cmd')
                data['prompt.cmd.extra'] = cfg_get_base('prompt.cmd.extra')
                data['prompt.cmd.extra.assistants'] = cfg_get_base('prompt.cmd.extra.assistants')
                data['prompt.expert'] = cfg_get_base('prompt.expert')

                # plugins
                if 'openai_dalle' in data['plugins'] \
                        and 'prompt' in data['plugins']['openai_dalle']:
                    del data['plugins']['openai_dalle']['prompt']
                if 'idx_llama_index' in data['plugins'] \
                        and 'prompt' in data['plugins']['idx_llama_index']:
                    del data['plugins']['idx_llama_index']['prompt']

            # < 2.5.41
            if old < parse_version("2.5.41"):
                print("Migrating config from < 2.5.41...")
                if "max_output_tokens" in data and "max_output_tokens" == 1024:
                    data["max_output_tokens"] = 0  # update default value
                updated = True

            # < 2.5.42 - action img padding
            if old < parse_version("2.5.42"):
                print("Migrating config from < 2.5.42...")
                patch_css('web-chatgpt.css', True)  # force replace file
                patch_css('web-chatgpt_wide.css', True)  # force replace file
                updated = True

            # < 2.5.43 - remove cmd_code_interpreter fresh_kernel option
            if old < parse_version("2.5.43"):
                print("Migrating config from < 2.5.43...")
                # plugins
                if 'cmd_code_interpreter' in data['plugins'] \
                        and 'fresh_kernel' in data['plugins']['cmd_code_interpreter']:
                    del data['plugins']['cmd_code_interpreter']['fresh_kernel']

            # < 2.5.51
            if old < parse_version("2.5.51"):
                print("Migrating config from < 2.5.51...")
                patch_css('style.css', True)  # force replace file
                patch_css('style.dark.css', True)  # force replace file
                patch_css('style.light.css', True)  # force replace file
                updated = True

            # < 2.5.54
            if old < parse_version("2.5.54"):
                print("Migrating config from < 2.5.54...")
                patch_css('web-chatgpt.css', True)  # force replace file
                updated = True

            # < 2.5.55
            if old < parse_version("2.5.55"):
                print("Migrating config from < 2.5.55...")
                patch_css('web-chatgpt.css', True)  # force replace file
                updated = True

            # < 2.5.60
            if old < parse_version("2.5.60"):
                print("Migrating config from < 2.5.60...")
                patch_css('style.css', True)  # force replace file
                patch_css('style.dark.css', True)  # force replace file
                patch_css('style.light.css', True)  # force replace file
                patch_css('web-chatgpt.css', True)  # force replace file
                patch_css('web-chatgpt.light.css', True)  # force replace file
                patch_css('web-chatgpt.dark.css', True)  # force replace file
                patch_css('web-chatgpt_wide.css', True)  # force replace file
                patch_css('web-chatgpt_wide.light.css', True)  # force replace file
                patch_css('web-chatgpt_wide.dark.css', True)  # force replace file
                updated = True

            # < 2.5.61
            if old < parse_version("2.5.61"):
                print("Migrating config from < 2.5.61..")
                if "agent.output.render.all" not in data:
                    data["agent.output.render.all"] = False
                data["prompt.expert"] = cfg_get_base(
                    'prompt.expert')
                if "experts.use_agent" not in data:
                    data["experts.use_agent"] = True
                updated = True

            # < 2.5.63 - disable cmd.get_time in real_time plugin by default
            if old < parse_version("2.5.63"):
                print("Migrating config from < 2.5.63...")
                if 'real_time' in data['plugins'] \
                        and 'cmd.get_time' in data['plugins']['real_time']:
                    del data['plugins']['real_time']['cmd.get_time']
                updated = True

            # < 2.5.64
            if old < parse_version("2.5.64"):
                print("Migrating config from < 2.5.64..")
                data["prompt.cmd"] = cfg_get_base(
                    'prompt.cmd')
                data["prompt.cmd.extra"] = cfg_get_base(
                    'prompt.cmd.extra')
                data["prompt.expert"] = cfg_get_base(
                    'prompt.expert')
                data["experts.use_agent"] = False
                updated = True

            # < 2.5.65
            if old < parse_version("2.5.65"):
                print("Migrating config from < 2.5.65..")
                data["prompt.expert"] = cfg_get_base(
                    'prompt.expert')
                updated = True

            # < 2.5.68
            if old < parse_version("2.5.68"):
                print("Migrating config from < 2.5.68..")
                if "agent.func_call.native" not in data:
                    data["agent.func_call.native"] = False
                if "experts.func_call.native" not in data:
                    data["experts.func_call.native"] = False
                updated = True

            # < 2.5.69
            if old < parse_version("2.5.69"):
                print("Migrating config from < 2.5.69.")
                data["prompt.agent.continue"] = cfg_get_base(
                    'prompt.agent.continue')
                data["prompt.agent.goal"] = cfg_get_base(
                    'prompt.agent.goal')
                data["prompt.expert"] = cfg_get_base(
                    'prompt.expert')
                if "agent.api_use_responses" not in data:
                    data["agent.api_use_responses"] = False
                if "experts.api_use_responses" not in data:
                    data["experts.api_use_responses"] = False
                if "experts.internal.api_use_responses" not in data:
                    data["experts.internal.api_use_responses"] = False
                if 'cmd_web' in data['plugins'] \
                        and 'cmd.web_search' in data['plugins']['cmd_web']:
                    del data['plugins']['cmd_web']['cmd.web_search']
                updated = True

            # < 2.5.71
            if old < parse_version("2.5.71"):
                print("Migrating config from < 2.5.71.")
                if "remote_tools.computer_use.env" not in data:
                    data["remote_tools.computer_use.env"] = ""
                if "remote_tools.mcp" not in data:
                    data["remote_tools.mcp"] = False
                if "remote_tools.mcp.args" not in data:
                    data["remote_tools.mcp.args"] = cfg_get_base(
                    'remote_tools.mcp.args')
                if "remote_tools.file_search" not in data:
                    data["remote_tools.file_search"] = False
                if "remote_tools.file_search.args" not in data:
                    data["remote_tools.file_search.args"] = ""
                if 'cmd_mouse_control' in data['plugins'] \
                        and 'cmd.mouse_move' in data['plugins']['cmd_mouse_control']:
                    del data['plugins']['cmd_mouse_control']['cmd.mouse_move']
                if 'cmd_mouse_control' in data['plugins'] \
                        and 'cmd.mouse_scroll' in data['plugins']['cmd_mouse_control']:
                    del data['plugins']['cmd_mouse_control']['cmd.mouse_scroll']
                if 'cmd_mouse_control' in data['plugins'] \
                        and 'cmd.keyboard_type' in data['plugins']['cmd_mouse_control']:
                    del data['plugins']['cmd_mouse_control']['cmd.keyboard_type']
                updated = True

            # < 2.5.73
            if old < parse_version("2.5.73"):
                print("Migrating config from < 2.5.73...")
                patch_css('web-chatgpt.css', True)  # force replace file
                patch_css('web-chatgpt.light.css', True)  # force replace file
                patch_css('web-chatgpt_wide.css', True)  # force replace file
                patch_css('web-chatgpt_wide.light.css', True)  # force replace file
                patch_css('web-chatgpt_wide.dark.css', True)  # force replace file
                updated = True

            # < 2.5.76
            if old < parse_version("2.5.76"):
                print("Migrating config from < 2.5.76.")
                if "agent.llama.loop.mode" not in data:
                    data["agent.llama.loop.mode"] = cfg_get_base(
                        'agent.llama.loop.mode')
                if "prompt.agent.llama.eval.complete" not in data:
                    data["prompt.agent.llama.eval.complete"] = cfg_get_base(
                        'prompt.agent.llama.eval.complete')
                data["prompt.agent.llama.eval"] = cfg_get_base(
                    'prompt.agent.llama.eval')

            # < 2.5.89
            if old < parse_version("2.5.89"):
                print("Migrating config from < 2.5.89.")
                if "audio.input.backend" not in data:
                    data["audio.input.backend"] = "native"
                if "audio.output.backend" not in data:
                    data["audio.output.backend"] = "native"
                if "audio.input.device" not in data:
                    data["audio.input.device"] = "0"
                if "audio.output.device" not in data:
                    data["audio.output.device"] = "0"

            # < 2.5.90
            if old < parse_version("2.5.90"):
                print("Migrating config from < 2.5.90...")
                patch_css('style.dark.css', True)  # force replace file
                patch_css('style.light.css', True)  # force replace file
                patch_css('web-blocks.css', True)  # force replace file
                patch_css('web-blocks.dark.css', True)  # force replace file
                patch_css('web-blocks.light.css', True)  # force replace file
                updated = True

            # < 2.5.91
            if old < parse_version("2.5.91"):
                print("Migrating config from < 2.5.91...")
                if "audio.cache.enabled" not in data:
                    data["audio.cache.enabled"] = True
                updated = True

            # < 2.5.92
            if old < parse_version("2.5.92"):
                print("Migrating config from < 2.5.92...")
                if "audio.cache.max_files" not in data:
                    data["audio.cache.max_files"] = 1000
                updated = True

            # < 2.5.94
            if old < parse_version("2.5.94"):
                print("Migrating config from < 2.5.94...")
                if "api_endpoint_hugging_face" not in data:
                    data["api_endpoint_hugging_face"] = "https://router.huggingface.co/v1"

                # tips
                patch_css('web-chatgpt.css', True)  # force replace file
                patch_css('web-chatgpt.light.css', True)  # force replace file
                patch_css('web-chatgpt.dark.css', True)  # force replace file
                patch_css('web-chatgpt_wide.css', True)  # force replace file
                patch_css('web-chatgpt_wide.light.css', True)  # force replace file
                patch_css('web-chatgpt_wide.dark.css', True)  # force replace file
                patch_css('web-blocks.css', True)  # force replace file
                patch_css('web-blocks.light.css', True)  # force replace file
                patch_css('web-blocks.dark.css', True)  # force replace file
                updated = True

            # < 2.5.95
            if old < parse_version("2.5.95"):
                print("Migrating config from < 2.5.95...")
                if "personalize.about" not in data:
                    data["personalize.about"] = ""
                if "personalize.modes" not in data:
                    data["personalize.modes"] = "chat"

                # avatars css
                patch_css('web-chatgpt.css', True)  # force replace file
                patch_css('web-chatgpt.light.css', True)  # force replace file
                patch_css('web-chatgpt.dark.css', True)  # force replace file
                patch_css('web-chatgpt_wide.css', True)  # force replace file
                patch_css('web-chatgpt_wide.light.css', True)  # force replace file
                patch_css('web-chatgpt_wide.dark.css', True)  # force replace file
                patch_css('web-blocks.css', True)  # force replace file
                patch_css('web-blocks.light.css', True)  # force replace file
                patch_css('web-blocks.dark.css', True)  # force replace file
                updated = True

            # < 2.5.98
            if old < parse_version("2.5.98"):
                print("Migrating config from < 2.5.98...")
                if "agent.openai.response.split" not in data:
                    data["agent.openai.response.split"] = True
                updated = True

            # < 2.6.0
            if old < parse_version("2.6.0"):
                print("Migrating config from < 2.6.0...")
                patch_css('style.light.css', True)  # scrollbar, calendar fix
                patch_css('style.dark.css', True)  # calendar fix
                updated = True

            # < 2.6.8
            if old < parse_version("2.6.8"):
                print("Migrating config from < 2.6.8...")
                patch_css('web-chatgpt.light.css', True)  # p color
                patch_css('web-chatgpt.dark.css', True)  # p color
                patch_css('web-chatgpt_wide.light.css', True)  # p color
                patch_css('web-chatgpt_wide.dark.css', True)  # p color
                patch_css('style.light.css', True)  # tree
                patch_css('style.dark.css', True)  # tree
                updated = True

            # < 2.6.10
            if old < parse_version("2.6.10"):
                print("Migrating config from < 2.6.10...")
                if "agent.idx.auto_retrieve" not in data:
                    data["agent.idx.auto_retrieve"] = True
                if 'google' in data['plugins'] \
                        and 'oauth_scopes' in data['plugins']['google']:
                    # add documents scope
                    if "https://www.googleapis.com/auth/documents" not in data['plugins']['google']['oauth_scopes']:
                        data['plugins']['google']['oauth_scopes'] += " https://www.googleapis.com/auth/documents"
                updated = True

            # < 2.6.21
            if old < parse_version("2.6.21"):
                print("Migrating config from < 2.6.21...")
                if "agent.output.render.all" not in data:
                    data["agent.output.render.all"] = True
                updated = True

            # < 2.6.23  -- fix: restore <p> color
            if old < parse_version("2.6.23"):
                print("Migrating config from < 2.6.23...")
                patch_css('web-chatgpt.dark.css', True)
                patch_css('web-chatgpt_wide.dark.css', True)
                patch_css('web-chatgpt.light.css', True)
                patch_css('web-chatgpt_wide.light.css', True)
                patch_css('web-blocks.dark.css', True)
                patch_css('web-blocks.light.css', True)
                updated = True

            # < 2.6.24
            if old < parse_version("2.6.24"):
                print("Migrating config from < 2.6.24...")
                if "llama.idx.embeddings.default" not in data:
                    data["llama.idx.embeddings.default"] = cfg_get_base(
                        'llama.idx.embeddings.default')
                updated = True

            # < 2.6.25
            if old < parse_version("2.6.25"):
                print("Migrating config from < 2.6.25...")
                if "api_key_voyage" not in data:
                    data["api_key_voyage"] = ""
                if "agent.llama.eval_model" not in data:
                    data["agent.llama.eval_model"] = "_"
                if "llama.idx.embeddings.default" in data:
                    providers = []
                    for item in data["llama.idx.embeddings.default"]:
                        p = item.get('provider', '')
                        if p and p not in providers:
                            providers.append(p)

                    if "anthropic" not in providers:
                        data["llama.idx.embeddings.default"].append({
                            "provider": "anthropic",
                            "model": "voyage-3.5",
                        })
                    if "deepseek_api" not in providers:
                        data["llama.idx.embeddings.default"].append({
                            "provider": "deepseek_api",
                            "model": "voyage-3.5",
                        })
                    if "mistral_ai" not in providers:
                        data["llama.idx.embeddings.default"].append({
                            "provider": "mistral_ai",
                            "model": "mistral-embed",
                        })
                    if "x_ai" not in providers:
                        data["llama.idx.embeddings.default"].append({
                            "provider": "x_ai",
                            "model": "",
                        })
                updated = True

            # < 2.6.26
            if old < parse_version("2.6.26"):
                print("Migrating config from < 2.6.26...")
                if "api_key_open_router" not in data:
                    data["api_key_open_router"] = ""
                if "api_endpoint_open_router" not in data:
                    data["api_endpoint_open_router"] = "https://openrouter.ai/api/v1"
                updated = True

            # < 2.6.28  -- fix: cmd color
            if old < parse_version("2.6.28"):
                print("Migrating config from < 2.6.28...")
                patch_css('web-chatgpt.css', True)
                patch_css('web-chatgpt_wide.css', True)
                patch_css('web-chatgpt.dark.css', True)
                patch_css('web-chatgpt_wide.dark.css', True)
                patch_css('web-chatgpt.light.css', True)
                patch_css('web-chatgpt_wide.light.css', True)
                updated = True

            # < 2.6.30
            if old < parse_version("2.6.30"):
                print("Migrating config from < 2.6.30...")
                if "api_native_google" not in data:
                    data["api_native_google"] = True
                if "remote_tools.google.web_search" not in data:
                    data["remote_tools.google.web_search"] = True
                if "remote_tools.google.code_interpreter" not in data:
                    data["remote_tools.google.code_interpreter"] = False
                updated = True

            # < 2.6.31
            if old < parse_version("2.6.31"):
                print("Migrating config from < 2.6.31...")
                if "log.realtime" not in data:
                    data["log.realtime"] = False
                if "remote_tools.google.url_ctx" not in data:
                    data["remote_tools.google.url_ctx"] = False
                if "audio.input.auto_turn" not in data:
                    data["audio.input.auto_turn"] = False
                if "audio.input.vad.prefix" not in data:
                    data["audio.input.vad.prefix"] = 300
                if "audio.input.vad.silence" not in data:
                    data["audio.input.vad.silence"] = 2000
                updated = True

            # < 2.6.32
            if old < parse_version("2.6.32"):
                print("Migrating config from < 2.6.32...")

                data["prompt.img"] = cfg_get_base(
                    'prompt.img')

                if "prompt.video" not in data:
                    data["prompt.video"] = cfg_get_base('prompt.video')
                if "video.prompt_model" not in data:
                    data["video.prompt_model"] = cfg_get_base( 'video.prompt_model')
                if "video.aspect_ratio" not in data:
                    data["video.aspect_ratio"] = cfg_get_base( 'video.aspect_ratio')
                if "video.duration" not in data:
                    data["video.duration"] = cfg_get_base('video.duration')
                if "video.fps" not in data:
                    data["video.fps"] = cfg_get_base('video.fps')
                if "video.seed" not in data:
                    data["video.seed"] = cfg_get_base('video.seed')
                if "video.negative_prompt" not in data:
                    data["video.negative_prompt"] = cfg_get_base('video.negative_prompt')
                if "video.generate_audio" not in data:
                    data["video.generate_audio"] = cfg_get_base('video.generate_audio')
                if "video.resolution" not in data:
                    data["video.resolution"] = cfg_get_base('video.resolution')

                # google vertex
                if "api_native_google.use_vertex" not in data:
                    data["api_native_google.use_vertex"] = cfg_get_base('api_native_google.use_vertex')
                if "api_native_google.cloud_project" not in data:
                    data["api_native_google.cloud_project"] = cfg_get_base('api_native_google.cloud_project')
                if "api_native_google.cloud_location" not in data:
                    data["api_native_google.cloud_location"] = cfg_get_base('api_native_google.cloud_location')
                if "api_native_google.app_credentials" not in data:
                    data["api_native_google.app_credentials"] = cfg_get_base('api_native_google.app_credentials')

                # audio loop
                if "audio.input.loop" not in data:
                    data["audio.input.loop"] = False

                # add video player CSS
                patch_css('web-chatgpt.css', True)
                patch_css('web-chatgpt_wide.css', True)
                patch_css('web-blocks.css', True)
                updated = True

            # < 2.6.35
            if old < parse_version("2.6.35"):
                print("Migrating config from < 2.6.35...")
                # remove will-change
                patch_css('web-chatgpt.css', True)
                patch_css('web-chatgpt_wide.css', True)
                patch_css('web-blocks.css', True)
                updated = True

            # < 2.6.36
            if old < parse_version("2.6.36"):
                print("Migrating config from < 2.6.36...")
                # perf css
                patch_css('web-chatgpt.css', True)
                patch_css('web-chatgpt_wide.css', True)
                patch_css('web-blocks.css', True)
                updated = True

            # < 2.6.37
            if old < parse_version("2.6.37"):
                print("Migrating config from < 2.6.37...")

                # add: label-desc CSS
                patch_css('style.dark.css', True)
                patch_css('style.light.css', True)

                # add: Anthropic SDK
                if "api_native_anthropic" not in data:
                    data["api_native_anthropic"] = True
                if "remote_tools.anthropic.web_search" not in data:
                    data["remote_tools.anthropic.web_search"] = True

                # add: xAI SDK
                if "api_native_xai" not in data:
                    data["api_native_xai"] = True
                if "remote_tools.xai.mode" not in data:
                    data["remote_tools.xai.mode"] = "auto"
                if "remote_tools.xai.sources.web" not in data:
                    data["remote_tools.xai.sources.web"] = True
                if "remote_tools.xai.sources.x" not in data:
                    data["remote_tools.xai.sources.x"] = True
                if "remote_tools.xai.sources.news" not in data:
                    data["remote_tools.xai.sources.news"] = False

                updated = True

            # < 2.6.40
            if old < parse_version("2.6.40"):
                print("Migrating config from < 2.6.40...")
                # perf css
                patch_css('web-chatgpt.css', True)
                patch_css('web-chatgpt_wide.css', True)
                patch_css('web-blocks.css', True)
                updated = True

            # < 2.6.41
            if old < parse_version("2.6.41"):
                print("Migrating config from < 2.6.41...")
                if "render.memory.limit" not in data:
                    data["render.memory.limit"] = "2.5GB"
                # ul p
                patch_css('web-chatgpt.css', True)
                patch_css('web-chatgpt_wide.css', True)
                patch_css('web-blocks.css', True)
                updated = True

            # < 2.6.42
            if old < parse_version("2.6.42"):
                print("Migrating config from < 2.6.42...")
                if "render.code_syntax.stream_max_lines" not in data:
                    data["render.code_syntax.stream_max_lines"] = 1000
                if "render.code_syntax.final_max_lines" not in data:
                    data["render.code_syntax.final_max_lines"] = 1500
                if "render.code_syntax.final_max_chars" not in data:
                    data["render.code_syntax.final_max_chars"] = 350000
                updated = True

        return data, updated, is_old
