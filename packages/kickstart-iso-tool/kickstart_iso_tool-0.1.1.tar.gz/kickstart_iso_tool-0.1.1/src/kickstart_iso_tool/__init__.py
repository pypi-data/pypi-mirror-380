from logging import basicConfig, config, WARNING
from os import path
from sys import exit
from kickstart_iso_tool.constants import (
    ISOINFO_BIN,
    XORRISO,
)


if not path.exists(ISOINFO_BIN):
    print(f"{ISOINFO_BIN} doesn't exists, try to install -> genisoimage")
    exit(1)
if not path.exists(XORRISO):
    print(f"{XORRISO} doesn't exists, try to install -> xorriso")
    exit(1)

try:
    config.fileConfig("/etc/kiso/logging.ini")
except KeyError:
    basicConfig(level=WARNING)
except FileNotFoundError:
    basicConfig(level=WARNING)