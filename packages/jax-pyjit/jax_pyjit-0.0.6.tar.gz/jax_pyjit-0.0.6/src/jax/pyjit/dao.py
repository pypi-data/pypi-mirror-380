# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.    
#
# Copyright [2025] The Jackson Laboratory


from dataclasses import dataclass, field
from typing import List, Optional, Any
from pathlib import Path
from enum import Enum

import os


class State:
    SUBMITTED: str = "SUBMITTED"
    RUNNING: str = "RUNNING"
    COMPLETE: str = "COMPLETE"
    ERROR: str = "ERROR"
    NONE: str = "NONE"
    CANCELLED: str = "CANCELLED"


@dataclass
class UntypedStatus:
    """
    Based on cimg-api/org.jax.cimg.api.evt.UntypedStatus
    which we use in Image Tools.
    These fields are shared across multiple tools.
    Do not change them.
    """

    message: Optional[str] = None
    state: str = State.NONE
    complete: float = 0
    errorStack: Optional[str] = None
    workflowId: Optional[str] = None
    results: List[str] = field(default_factory=lambda: [""])
    submissionInput: Optional[str] = None
    userName: Optional[str] = None


class Protocol(str, Enum):
    GS = "GS"
    S3 = "S3"
    NIO = "NIO"


@dataclass
class StorageKey:

    bucket: str
    object: str
    protocol: Optional[str] = Protocol.GS
    endpoint: Optional[str] = None
    test: Optional[bool] = False

    def to_uri(self, create=False) -> str:
        if self._is_local():
            file_path: str = None
            if self.endpoint is None:
                file_path: str = "{}/{}".format(self.bucket, self.object)
            else:
                file_path: str = "{}/{}/{}".format(
                    self.endpoint, self.bucket, self.object
                )

            NIO_STORAGE_ROOT: str = os.getenv("NIO_STORAGE_ROOT", None)
            if NIO_STORAGE_ROOT:
                file_path = "{}/{}".format(NIO_STORAGE_ROOT, file_path)

            # Remove double slashes
            file_path = file_path.replace("//", "/")

            if create:
                path: Path = Path(file_path)
                os.makedirs(path.parent, exist_ok=True)
                path.touch(exist_ok=True)
            return file_path
        else:
            return f"{self.protocol.lower()}://{self.bucket}/{self.object}"

    def _is_local(self) -> bool:
        if self.protocol == Protocol.NIO:
            return True
        if self.test:
            return True

        USE_NIO_STORAGE: bool = bool(os.getenv("USE_NIO_STORAGE", None))
        if USE_NIO_STORAGE:
            return True
        return False


# @see org.jax.cimg.api.workflow.AbstactRequest
# Your request should inherit from this base class please.
class AbstractRequest:
    info: Optional[Any] = None

@dataclass
class Input:
    image: StorageKey
    request: AbstractRequest
    result: Optional[Any] = None

def blank_key() -> StorageKey:
    return StorageKey("", "", test=True)
