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


from __future__ import annotations

from setuptools import find_packages, setup

try:
    from clusterondemand._version import version as __version__
except ImportError:
    try:
        from setuptools_scm import get_version
        __version__ = get_version(
            root="..",
            relative_to="__file__",
            write_to="cluster-on-demand/clusterondemand/_version.py"
        )
    except ImportError:
        __version__ = "0.0.0dev0"

with open("README.md") as file_in:
    readme = file_in.read()

with open("external_requirements.txt") as f:
    external_requirements = f.readlines()

setup(
    name="cm-cluster-on-demand",
    version=__version__,
    description="Cluster on Demand Utility",
    author="Base Command Manager Cloud Team",
    author_email="sw-bright-cloud-team@nvidia.onmicrosoft.com",
    url="https://docs.nvidia.com/base-command-manager/index.html",
    long_description=readme,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.12",
        "Topic :: System :: Clustering",
        "Topic :: System :: Installation/Setup",
        "Topic :: System :: Monitoring",
        "Topic :: System :: Systems Administration"
    ],
    packages=find_packages(),
    package_data={
        "clusterondemand": [
            "py.typed",
            "eula.txt",
            "version-info.yaml",
        ],
        "cmbrightimagerepo": [
            "py.typed",
        ],
    },
    tests_require=["pytest", "pycoverage"],
    entry_points={
        "console_scripts": [
            "cm-cod = clusterondemand.cli:cli_main",
        ]
    },
    python_requires=">=3.12",
    install_requires=[
        *external_requirements,
        "cm-cluster-on-demand-config==" + __version__
    ],
    setup_requires=["setuptools_scm>=4.1.2"]
)
