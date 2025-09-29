#!/usr/bin/env python3

__author__ = "xi"
__all__ = [
    "JSONDirReader",
    "JSONDirWriter",
]

import json
import os
from typing import Optional, Union

from libdata.common import DocReader, DocWriter
from libdata.url import URL


class JSONDirReader(DocReader):

    @classmethod
    def from_url(cls, url: Union[str, URL]):
        url = URL.ensure_url(url)

        if not url.scheme in {"jsondir"}:
            raise ValueError(f"Unsupported scheme \"{url.scheme}\".")

        return JSONDirReader(dir_path=url.path, **url.parameters)

    def __init__(
            self,
            dir_path: str,
            encoding: str = "UTF-8",
            key_field: Optional[str] = None,
            recursive: bool = True
    ) -> None:
        if not os.path.isdir(dir_path):
            raise ValueError(f"\"{dir_path}\" should be a directory.")
        self.dir_path = dir_path
        self.encoding = encoding
        self.key_field = key_field
        self.recursive = recursive

        self.file_list = []
        self._get_file_list(self.dir_path)
        self.index = None

    def _get_file_list(self, dir_path: str):
        for filename in os.listdir(dir_path):
            path = os.path.join(dir_path, filename)
            if os.path.isdir(path):
                if self.recursive:
                    self._get_file_list(path)
            else:
                self.file_list.append(path)

    def __len__(self):
        return len(self.file_list)

    def __getitem__(self, idx: int):
        path = self.file_list[idx]
        with open(path, "rt", encoding=self.encoding) as f:
            return json.load(f)

    def read(self, key):
        if self.key_field is None:
            path = os.path.join(self.dir_path, key)
            if not path.endswith(".json"):
                path += ".json"
        else:
            if self.index is None:
                self.index = {}
                for path in self.file_list:
                    with open(path, "rt", encoding=self.encoding) as f:
                        doc = json.load(f)
                        self.index[doc[self.key_field]] = path
            path = self.index[key]

        with open(path, "rt", encoding=self.encoding) as f:
            return json.load(f)


class JSONDirWriter(DocWriter):

    @classmethod
    def from_url(cls, url: Union[str, URL]):
        url = URL.ensure_url(url)

        if not url.scheme in {"jsondir"}:
            raise ValueError(f"Unsupported scheme \"{url.scheme}\".")

        return JSONDirWriter(dir_path=url.path, **url.parameters)

    def __init__(
            self,
            dir_path: str,
            key_field: str = "id",
            encoding: str = "UTF-8",
            indent: int = 2
    ) -> None:
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        if not os.path.isdir(dir_path):
            raise ValueError(f"\"{dir_path}\" should be a directory.")
        self.dir_path = dir_path
        self.key_field = key_field
        self.encoding = encoding
        self.indent = indent

    def write(self, doc):
        _id = doc.get(self.key_field)
        if _id is None:
            raise ValueError(f"The input document doesn't contain an id field (\"{self.key_field}\").")
        file_path = os.path.join(self.dir_path, _id + ".json")
        with open(file_path, "wt", encoding=self.encoding) as f:
            f.write(json.dumps(doc, indent=self.indent))

    def close(self):
        pass
