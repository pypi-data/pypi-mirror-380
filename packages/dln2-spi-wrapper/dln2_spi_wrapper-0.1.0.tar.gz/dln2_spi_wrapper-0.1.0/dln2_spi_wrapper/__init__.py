"""
DLN2 SPI Wrapper - A Python library for interfacing with DLN2 SPI adapters.

This package provides a spidev-compatible API for working with DLN2 USB-to-SPI
adapters, allowing existing spidev-based code to work with DLN2 devices with
minimal modifications.

Main components:
- dln2_spi_client: Low-level DLN2 USB communication
- dln2_spidev: High-level spidev-compatible API
- SpiDev: Main class for SPI communication
"""

__version__ = "0.1.0"
__author__ = "IPM Group"
__email__ = "ipm.grp@googlemail.com"
__license__ = "Apache 2.0"

from .dln2_spi_client import Dln2Usb, find_device
from .dln2_spidev import SpiDev

__all__ = [
    "SpiDev",
    "Dln2Usb", 
    "find_device",
    "__version__",
]
