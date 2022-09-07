#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2022 Stéphane Caron
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
ANYmal C MJCF description.
"""

from os import path as _path

from ._cache import clone_to_cache as _clone_to_cache

REPOSITORY_PATH: str = _clone_to_cache("mujoco_menagerie")

PACKAGE_PATH: str = _path.join(REPOSITORY_PATH, "anybotics_anymal_c")

MESHES_PATH: str = _path.join(PACKAGE_PATH, "assets")

MJCF_PATH: str = _path.join(PACKAGE_PATH, "anymal_c.xml")