# SPDX-FileCopyrightText: Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
import random
import time
from collections.abc import Callable
from typing import Any

from .types import RetryableError


def retry(func: Callable) -> Callable:
    """
    Decorator to retry a function call if a retryable error is raised.
    """

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        storage_client_instance = args[0]
        retry_config = getattr(storage_client_instance, "_retry_config", None)
        # If retry_config is None, just run the function without retrying
        if retry_config is None:
            return func(*args, **kwargs)

        delay = retry_config.delay
        for attempt in range(retry_config.attempts):
            try:
                return func(*args, **kwargs)
            except RetryableError as e:
                logging.warning("Attempt %d failed for %s: %s", attempt + 1, func.__name__, e)
                # Exponential backoff
                delay *= 2**attempt
                # Add random jitter
                delay += random.uniform(0, 1)
                if attempt < retry_config.attempts - 1:
                    time.sleep(retry_config.delay)
                else:
                    logging.error("All retry attempts failed for %s", func.__name__)
                    raise
            except Exception as e:
                logging.error("Non-retryable error occurred for %s: %s", func.__name__, e)
                raise

    return wrapper
