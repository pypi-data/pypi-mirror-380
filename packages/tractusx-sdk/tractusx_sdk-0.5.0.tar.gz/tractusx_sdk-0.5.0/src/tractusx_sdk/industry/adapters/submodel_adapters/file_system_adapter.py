#################################################################################
# Eclipse Tractus-X - Software Development KIT
#
# Copyright (c) 2025 Contributors to the Eclipse Foundation
#
# See the NOTICE file(s) distributed with this work for additional
# information regarding copyright ownership.
#
# This program and the accompanying materials are made available under the
# terms of the Apache License, Version 2.0 which is available at
# https://www.apache.org/licenses/LICENSE-2.0.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the
# License for the specific language govern in permissions and limitations
# under the License.
#
# SPDX-License-Identifier: Apache-2.0
#################################################################################

from .. import SubmodelAdapter
from tractusx_sdk.dataspace.tools import op
from typing import List

class FileSystemAdapter(SubmodelAdapter):

    def __init__(self, root_path: str):
        self.root_path = root_path
        print("FileSystem initilized")

    @classmethod
    def builder(cls):
        return cls._Builder(cls)

    class _Builder:
        def __init__(self, cls):
            self.cls = cls
            self._data = {}

        def root_path(self, path:str):
            self._data["root_path"] = path
            return self
        
        def build(self):
            if "root_path" not in self._data:
                raise ValueError("Missing required buider parameter: root_path")
            return self.cls(**self._data)
    

    def read(self, path: str):
        """
        Return the entire content of a file
        """
        total_path = op.join_paths(self.root_path, path)
        return op.read_json_file(total_path)
         

    def write(self, path: str, content) -> None:
        """
        Write a new file
        """
        total_path = op.join_paths(self.root_path, path)
        op.to_json_file(content, json_file_path=total_path)

    def delete(self, path: str) -> None:
        """
        Delete a specific file
        """
        total_path = op.join_paths(self.root_path, path)
        op.delete_file(total_path)

    def exists(self, path: str) -> bool:
        """
        Check if a file exists
        """
        total_path = op.join_paths(self.root_path, path)
        return op.path_exists(total_path)

    def list_contents(self, directory_path: str) -> List[dict]:
        """
        Return a list of files based in a directory
        """
        results = []
        total_path = op.join_paths(self.root_path, directory_path)
        for entry_name in op.list_directories(total_path):
            entry_abs_path = op.join_paths(total_path, entry_name)
            if op.is_file(entry_abs_path):
                try:
                    results.append(entry_abs_path)
                except FileNotFoundError:
                    continue
                except PermissionError:
                    continue
        return results


    def create_directory(self, path: str) -> None:
        """
        Create a directory
        """
        total_path = op.join_paths(self.root_path, path)
        op.make_dir(total_path)

    def delete_directory(self, path: str) -> None:
        """
        Remove a directory
        """
        total_path = op.join_paths(self.root_path, path)
        op.delete_dir(total_path)   
