# SPDX-License-Identifier: GPL-3.0-or-later
"""pixhawkcontroller public API."""

from .main import FlightControllerInterface, FlightControllerInfo, TonesQb
from .__version__ import __version__

__all__ = ["FlightControllerInterface", "FlightControllerInfo", "TonesQb", "__version__"]

__author__ = "Md Shahriar Forhad"
__email__ = "shahriar.forhad.eee@gmail.com"
__license__ = "GPL-3.0-or-later"
