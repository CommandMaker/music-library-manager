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


from typing import override
from database.models.model import Model
from database.query import SelectQuery


class Artist(Model):
    def __init__(
        self,
        id: int,
        name: str,
        folder_name: str
    ) -> None:
        self.id: int = id
        self.name: str = name
        self.folder_name: str = folder_name


    @staticmethod
    def fetch_artists() -> list[Artist]:
        artists = SelectQuery('artists')\
            .fetch_all(Artist)
        return artists


    @classmethod
    @override
    def build_from_dict(cls, dikt: dict[str, str]) -> Artist:
        return cls(int(dikt.get('id', 0)), dikt.get('name', ''), dikt.get('folder_name', ''))
