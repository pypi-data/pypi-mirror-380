import os
from dataclasses import dataclass

from graphgen.bases.base_storage import BaseKVStorage, BaseListStorage
from graphgen.utils import load_json, logger, write_json


@dataclass
class JsonKVStorage(BaseKVStorage):
    _data: dict[str, str] = None

    def __post_init__(self):
        self._file_name = os.path.join(self.working_dir, f"{self.namespace}.json")
        self._data = load_json(self._file_name) or {}
        logger.info("Load KV %s with %d data", self.namespace, len(self._data))

    @property
    def data(self):
        return self._data

    async def all_keys(self) -> list[str]:
        return list(self._data.keys())

    async def index_done_callback(self):
        write_json(self._data, self._file_name)

    async def get_by_id(self, id):
        return self._data.get(id, None)

    async def get_by_ids(self, ids, fields=None) -> list:
        if fields is None:
            return [self._data.get(id, None) for id in ids]
        return [
            (
                {k: v for k, v in self._data[id].items() if k in fields}
                if self._data.get(id, None)
                else None
            )
            for id in ids
        ]

    async def filter_keys(self, data: list[str]) -> set[str]:
        return {s for s in data if s not in self._data}

    async def upsert(self, data: dict):
        left_data = {k: v for k, v in data.items() if k not in self._data}
        self._data.update(left_data)
        return left_data

    async def drop(self):
        self._data = {}


@dataclass
class JsonListStorage(BaseListStorage):
    _data: list = None

    def __post_init__(self):
        self._file_name = os.path.join(self.working_dir, f"{self.namespace}.json")
        self._data = load_json(self._file_name) or []
        logger.info("Load List %s with %d data", self.namespace, len(self._data))

    @property
    def data(self):
        return self._data

    async def all_items(self) -> list:
        return self._data

    async def index_done_callback(self):
        write_json(self._data, self._file_name)

    async def get_by_index(self, index: int):
        if index < 0 or index >= len(self._data):
            return None
        return self._data[index]

    async def append(self, data):
        self._data.append(data)

    async def upsert(self, data: list):
        left_data = [d for d in data if d not in self._data]
        self._data.extend(left_data)
        return left_data

    async def drop(self):
        self._data = []
