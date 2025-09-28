#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://pygpt.net                         #
# GitHub:  https://github.com/szczyglis-dev/py-gpt   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2025.09.26 03:00:00                  #
# ================================================== #

import json
from typing import Optional, List, Dict, Any

from sqlalchemy import text


class Viewer:
    def __init__(self, database):
        """
        Database viewer.

        :param database: Database instance
        """
        self.database = database
        self.tables = {}
        self.auto_backup = True

    def fetch_data(
            self,
            table: str,
            columns: List[str],
            sort_by: str,
            order: str,
            search_query: Optional[str] = None,
            search_column: Optional[str] = None,
            offset: int = 0,
            limit: int = 100,
            filters: Optional[dict] = None
    ) -> list:
        """
        Fetch data from the database with the given parameters.

        :param table: Table name
        :param columns: List of columns to fetch
        :param sort_by: Column to sort by
        :param order: Sort order (ASC or DESC)
        :param search_query: Search query
        :param search_column: Search column
        :param offset: Offset
        :param limit: Limit
        :param filters: Filters
        :return: Fetched data
        """
        tables = self.database.get_tables()

        if search_column:
            search_fields = [search_column]
        else:
            search_fields = tables[table]['search_fields']

        base_query = f"SELECT {', '.join(columns)} FROM {table}"
        where_clause = ""
        order_clause = f" ORDER BY {sort_by} {order}"
        limit_clause = f" LIMIT {limit} OFFSET {offset}"

        params = {}
        if search_query is not None:
            sq = search_query.strip()
            if sq:
                search_clauses = [f"{column} LIKE :search_query" for column in search_fields]
                where_clause = f" WHERE ({' OR '.join(search_clauses)})"
                params['search_query'] = f"%{sq}%"

        if filters:
            filter_clauses = [f"{column} = :filter_{column}" for column in filters.keys()]
            if where_clause == "":
                where_clause = f" WHERE ({' AND '.join(filter_clauses)})"
            else:
                where_clause += f" AND ({' AND '.join(filter_clauses)})"
            for column, value in filters.items():
                params[f"filter_{column}"] = value

        query = f"{base_query}{where_clause}{order_clause}{limit_clause}"
        stmt = text(query).bindparams(**params)
        with self.database.get_db().connect() as conn:
            result = conn.execute(stmt).fetchall()
            return [tuple(r) for r in result]

    def count_rows(
            self,
            table: str,
            search_query: Optional[str] = None,
            search_column: Optional[str] = None,
            filters: Optional[Dict[str, Any]] = None
    ) -> int:
        """
        Count the number of rows in the table with an optional search query.

        :param table: Table name
        :param search_query: Search query
        :param search_column: Search column
        :param filters: Filters
        :return: Number of rows
        """
        base_query = f"SELECT COUNT(*) FROM {table}"
        where_clause = ""
        params = {}
        tables = self.database.get_tables()

        if search_column:
            search_fields = [search_column]
        else:
            search_fields = tables[table]['search_fields']

        if search_query is not None:
            sq = search_query.strip()
            if sq:
                where_clause = f" WHERE {' OR '.join([f'{column} LIKE :search_query' for column in search_fields])}"
                params['search_query'] = f"%{sq}%"

        if filters:
            filter_clauses = [f"{column} = :filter_{column}" for column in filters.keys()]
            if where_clause == "":
                where_clause = f" WHERE ({' AND '.join(filter_clauses)})"
            else:
                where_clause += f" AND ({' AND '.join(filter_clauses)})"
            for column, value in filters.items():
                params[f"filter_{column}"] = value

        query = f"{base_query}{where_clause}"
        stmt = text(query).bindparams(**params)
        with self.database.get_db().connect() as conn:
            count = conn.execute(stmt).scalar()
            return int(count) if count is not None else 0

    def is_auto_backup(self) -> bool:
        """
        Get auto backup status.

        :return: Auto backup status
        """
        return self.database.window.ui.debug["db"].browser.is_auto_backup()

    def delete_row(self, data: Dict[str, Any]):
        """
        Delete row from the database.

        :param data: Dictionary with table and row_id keys
        """
        if self.is_auto_backup():
            backup_path = self.database.make_backup()
            if backup_path:
                msg = f"[DB] Created DB backup: {backup_path}"
                self.log(msg)

        tables = self.database.get_tables()
        primary_key = tables[data['table']]['primary_key']

        with self.database.get_db().begin() as conn:
            conn.execute(
                text(f"DELETE FROM {data['table']} WHERE {primary_key} = :row_id")
                .bindparams(row_id=data['row_id'])
            )
            msg = f"[DB] Deleted row ID {data['row_id']} from table {data['table']}"
            self.log(msg)
        # Force refresh to invalidate caches and handle pagination edge cases
        self.database.window.ui.debug["db"].browser.force_refresh()

    def update_row(self, data: Dict[str, Any]):
        """
        Update row in the database.

        :param data: Dictionary with table, id, field and value keys
        """
        field = data['field']
        value = data['value']
        tables = self.database.get_tables()
        json_columns = tables[data['table']]['json_columns']
        timestamp_columns = tables[data['table']]['timestamp_columns']
        primary_key = tables[data['table']]['primary_key']

        if field in json_columns or field.endswith("_json"):
            try:
                value = json.dumps(json.loads(value))
            except:
                raise ValueError(f"Invalid JSON value for column {field}")

        if field in timestamp_columns or field.endswith("_ts"):
            try:
                value = int(value)
            except:
                raise ValueError(f"Invalid timestamp value for column {field}")

        if field.endswith("_id"):
            try:
                value = int(value)
            except:
                raise ValueError(f"Invalid _id value for column {field}")

        if self.is_auto_backup():
            backup_path = self.database.make_backup()
            if backup_path:
                msg = f"[DB] Created DB backup: {backup_path}"
                self.log(msg)

        with self.database.get_db().begin() as conn:
            conn.execute(
                text(f"UPDATE {data['table']} SET {data['field']} = :value WHERE {primary_key} = :id")
                .bindparams(id=data['id'], value=value)
            )
            msg = f"[DB] Updated row ID {data['id']} in table {data['table']}"
            self.log(msg)
        # Force refresh to invalidate caches and handle pagination edge cases
        self.database.window.ui.debug["db"].browser.force_refresh()

    def truncate_table(self, data: Dict[str, Any], reset: bool = False):
        """
        Truncate table in the database.

        :param data: Dictionary with table key
        :param reset: Reset table sequence
        """
        if self.is_auto_backup():
            backup_path = self.database.make_backup()
            if backup_path:
                msg = f"[DB] Created DB backup: {backup_path}"
                self.log(msg)

        with self.database.get_db().begin() as conn:
            conn.execute(text(f"DELETE FROM {data['table']}"))
            if reset:
                conn.execute(text(f"DELETE FROM sqlite_sequence WHERE name='{data['table']}'"))
                msg = f"[DB] Truncated table {data['table']}"
            else:
                msg = f"[DB] Deleted all rows from table {data['table']}"
            self.log(msg)
        # Force refresh to invalidate caches and handle pagination edge cases
        self.database.window.ui.debug["db"].browser.force_refresh()

    def log(self, msg: str):
        """
        Log action to debug.

        :param msg: Message
        """
        self.database.window.core.debug.info(msg)
        print(msg)
        self.database.window.update_status(msg)