import logging
import os
import subprocess
import re
import pycdlib
import collections
import jinja2
from .constants import (
    ISOINFO_BIN,
    XORRISO,
)
from .base import (
    execute_command,
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def create_grub_cfg(iso_name: str, template:str, name: str ) -> str:
    template = jinja2.Template(template)
    return template.render(name=name, iso_name=iso_name)

def iso_volume_id(iso_location) -> str:
    print(f"executing: {ISOINFO_BIN} -d -i {iso_location}")
    command = [ISOINFO_BIN, "-d", "-i", iso_location]
    exec = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = exec.communicate()
    iso_descriptor = output.decode("UTF-8")
    iso_descriptor = iso_descriptor.splitlines()
    for i in range(len(iso_descriptor)):
        line = iso_descriptor[i]
        if re.match("Volume id", line):
            volume_id = line.split(" ")[-1]
            logger.debug(f"Volume id: {volume_id}")
            return volume_id

def create_kickstarted_iso(
    src: str,
    dst: str,
    iso_name: str,
    kickstart_cfg: str,
    grub_cfg: str,
    default_boot_cfg: str,
    default_boot_file: str,
    optional_kickstart_cfg: str = None,
) -> None:
    logger.info(f"Creating kickstarted iso image at {dst}")
    command = [
        XORRISO, "-indev", src,
        "-outdev", dst,
        "-boot_image", "any", "replay",
        "-joliet", "on",
        "-system_id", "LINUX",
        "-volid", iso_name,
        "-map", kickstart_cfg, "ks.cfg",
        "-map", grub_cfg, "EFI/BOOT/grub.cfg",
        "-map", default_boot_cfg, default_boot_file,
    ]
    if optional_kickstart_cfg:
        logger.debug(f"Adding optional kickstart configuration: {optional_kickstart_cfg}")
        base_name = os.path.basename(optional_kickstart_cfg)
        command.append("-map")
        command.append(optional_kickstart_cfg)
        command.append(base_name)
    logger.debug("Executing command: %s", ' '.join(command))
    execute_command(command)