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

import os


class SharedConfig:
    """Config and Settings Configuration."""

    DEBUG: bool = bool(os.getenv("DEBUG", None))
    TESTING: bool = bool(os.getenv("TESTING", None))

    USE_NIO_STORAGE: bool = bool(os.getenv("USE_NIO_STORAGE", None))
    NIO_STORAGE_ROOT: str = os.getenv("NIO_STORAGE_ROOT", None)

    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "WARNING")
    TEMPORAL_NAMESPACE: str = os.getenv("TEMPORAL_NAMESPACE", "default")
    TEMPORAL_URI: str = os.getenv(
        "TEMPORAL_URI", "localhost:7233"
    )  # Deploy should set to CS cluster location.
    CACHE_DIR: str = os.getenv("CACHE_DIR", "cache")

    TEST_BUCKET_NAME: str = os.getenv("TEST_BUCKET_NAME", None)

    DOWNLOAD_TIMEOUT: int = int(os.getenv("DOWNLOAD_TIMEOUT", "1200"))
    DOWNLOAD_ATTEMPTS: int = int(os.getenv("DOWNLOAD_ATTEMPTS", "4"))

    UPLOAD_TIMEOUT: int = int(os.getenv("UPLOAD_TIMEOUT", "1200"))
    UPLOAD_ATTEMPTS: int = int(os.getenv("UPLOAD_ATTEMPTS", "4"))
    
    CLEAN_TIMEOUT: int = int(os.getenv("CLEAN_TIMEOUT", "300"))
    CLEAN_ATTEMPTS: int = int(os.getenv("CLEAN_ATTEMPTS", "4"))

    # IO operations which come from other workers.
    IO_STORE_QUEUE = os.getenv("STORE_QUEUE", "STORE_TASK_QUEUE")
    IO_DOWNLOAD_OBJECT = os.getenv("IO_DOWNLOAD_OBJECT", "io-temporal-download-object")
    IO_UPLOAD = os.getenv("IO_UPLOAD", "io-temporal-upload")
    IO_CLEAN = os.getenv("IO_CLEAN", "io-temporal-clean")


shared_config = SharedConfig()
