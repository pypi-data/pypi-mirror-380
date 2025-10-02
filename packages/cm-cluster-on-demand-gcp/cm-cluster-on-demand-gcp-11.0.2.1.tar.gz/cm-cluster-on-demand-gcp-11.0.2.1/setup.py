#!/usr/bin/env python
# Copyright (c) 2004-2025 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
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

from setuptools import find_packages, setup

try:
    from clusterondemandgcp._version import version as __version__
except ImportError:
    try:
        from setuptools_scm import get_version
        __version__ = get_version(
            root="..",
            relative_to="__file__",
            write_to="cluster-on-demand-gcp/clusterondemandgcp/_version.py"
        )
    except ImportError:
        __version__ = "0.0.0dev0"

with open("external_requirements.txt") as f:
    external_requirements = f.readlines()

with open("README.md") as file_in:
    readme = file_in.read()

setup(
    name="cm-cluster-on-demand-gcp",
    version=__version__,
    description="NVIDIA Base Command Manager Cluster on Demand GCP",
    author="Base Command Manager Cloud Team",
    url="https://docs.nvidia.com/base-command-manager/",
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "cm-cod-gcp = clusterondemandgcp.cli:cli_main"
        ]
    },
    tests_require=["pytest", "pycoverage"],
    include_package_data=True,
    python_requires=">=3.12",
    install_requires=[
        *external_requirements,
        "cm-cluster-on-demand==" + __version__,
        "cm-cluster-on-demand-config==" + __version__,
    ],
    setup_requires=["setuptools_scm>=4.1.2"],
)
