#
# Copyright (C) 2026  CommandMaker
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sqlite3
from typing import TypeVar

from database.connection import DatabaseConnection
from database.models.model import Model


T = TypeVar('T', bound='Model')

class DatabaseQuery:
    '''
    Build an SQL query and fetch results from the database connection
    '''
    def __init__(self, table: str, columns: list[str] | None = None) -> None:
        self.query: list[str] = [f'SELECT {", ".join(columns if columns != None else ["*"])} FROM {table}']
        self.arguments: tuple[str|int|bool, ...] = ()


    def get_query(self) -> str:
        '''
        Return the current SQL query as a valid SQL

        @returns {str} The built query from the current query class
        '''
        return ' '.join(self.query)


    def fetch_all(self, klass: type[T]) -> list[T]:
        '''
        Fetch all rows matching the query built

        @params {type[T]} klass The model class to convert the results to. Must be a class herited from Model
        @returns {list[T]} Returns the list of rows converted to the given model
        '''
        db = DatabaseConnection.get_instance()
        results: list[sqlite3.Row] = db.get_cursor().execute(self.get_query(), self.arguments).fetchall()

        return [klass.build_from_dict(dict(row)) for row in results]
