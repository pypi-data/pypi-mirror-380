# SPDX-License-Identifier: GPL-3.0-or-later
from pathlib import Path
from setuptools import setup, find_packages

HERE = Path(__file__).parent
README_PATH = HERE / "README.md"
long_description = README_PATH.read_text(encoding="utf-8") if README_PATH.exists() else (
    "Lightweight Pixhawk/ArduPilot controller utilities using pymavlink."
)

# Load version without importing the package (works for sdists & linting)
about = {}
exec((HERE / "pixhawkcontroller" / "__version__.py").read_text(), about)
package_version = about["__version__"]

setup(
    name="pixhawkcontroller",
    version=package_version,  # <— from __version__.py
    description="Lightweight Pixhawk/ArduPilot controller utilities using pymavlink",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Md Shahriar Forhad",
    author_email="shahriar.forhad.eee@gmail.com",
    url="https://github.com/Shahriar88/pixhawkcontroller",
    license="GPL-3.0-or-later",
    license_files=["LICENSE"],
    packages=find_packages(exclude=("tests", "docs", "examples")),
    include_package_data=True,
    install_requires=[
        "pymavlink>=2.4.41",
        "pyserial>=3.5",
        "build==1.3.0",
        "setuptools==80.9.0",
        "wheel==0.45.1",
        "twine==6.2.0",
        "packaging==25.0",
    ],
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering",
        "Topic :: System :: Hardware",
        "Topic :: Software Development :: Libraries",
    ],
    keywords=["pixhawk", "ardupilot", "mavlink", "pymavlink", "drone", "uav"],
    project_urls={
        "Source": "https://github.com/Shahriar88/pixhawkcontroller",
        "Issues": "https://github.com/Shahriar88/pixhawkcontroller/issues",
    },
)
