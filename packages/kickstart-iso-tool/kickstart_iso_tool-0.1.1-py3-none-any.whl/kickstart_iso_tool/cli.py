import argparse
import configparser
from logging import getLogger
import os
import uuid
import signal
import shutil
import sys
from functools import partial
from .base import (
    download_file,
)
from .iso import (
    create_grub_cfg,
    iso_volume_id,
    create_kickstarted_iso,
)
from .constants import (
    grub_cfg_template,
    isolinux_cfg_template
)

logger = getLogger(__name__)
logger.setLevel("DEBUG")


def cli_arguments():
    parser = argparse.ArgumentParser(prog="kiso", description="Add kickstart files to rhel based iso images")
    parser.add_argument(
            "--work-dir",
            default="/tmp",
            type=str,
            help="Working directory where to store temp files"
        )
    parser.add_argument(
            "-c",
            "--config",
            type=str,
            default="/etc/kiso/config.ini",
            help="Config file path"
        )
    parser.add_argument(
            "-b",
            "--build",
            help="Image to build"
        )
    parser.add_argument(
            "--remove-source",
            action='store_true',
            help="Remove source iso file"
        )
    return parser.parse_args()


def config_parser(conf_file):
    logger.debug(f"Parsing config file: {conf_file}")
    config = configparser.ConfigParser()
    with open(conf_file, "r") as file:
        config.read_string(file.read())
    return config


def handler(working_path, signum, frame):
    print()
    logger.error("CTR+C was pressed, cleaning up")
    sys.exit(1)


def cleanup(working_path, source_iso=None):
    logger.debug(f"Removing: {working_path}")
    shutil.rmtree(working_path)
    if source_iso:
        logger.debug(f"Removing: {source_iso}")
        os.remove(source_iso)


def process_parent(config, arguments):
    parent_ks_section = config.get(arguments.build, "parent")
    logger.debug(f"Parent: {parent_ks_section}")
    parent_url = config.get(parent_ks_section, "url")
    logger.debug(f"Parent download url: {parent_url}")
    parent_ks = config.get(parent_ks_section, "kcfg")
    logger.debug(f"Parent kcfg: {parent_ks}")
    child_ks = config.get(arguments.build, "kcfg")
    logger.debug(f"Child kcfg: {child_ks}")
    return parent_url, parent_ks, child_ks


def main():
    arguments = cli_arguments()
    try:
        work_subdir = uuid.uuid4().hex
        child_ks = None
        working_path = os.path.join(arguments.work_dir, work_subdir)
        signal.signal(signal.SIGINT, partial(handler, working_path))
        logger.debug(f"Argument selection: {arguments}")
        logger.debug(f"Working path: {working_path}")
        if os.path.exists(arguments.config):
            kiso_name = f"{arguments.build}-kickstarted.iso"
            config = config_parser(arguments.config)
            iso_save_path = os.path.join(config.get("DEFAULT", "storage"))
            updated_iso_path = os.path.join(iso_save_path, kiso_name)
            if not os.path.isdir(iso_save_path):
                logger.warning(f"Iso save path doesn't exists, creating {iso_save_path}")
                os.makedirs(iso_save_path)
        if arguments.build in config.sections():
            print(f"Building: {arguments.build}")
            if config.has_option(arguments.build, "parent"):
                iso_url, k_cfg, child_ks = process_parent(config, arguments)
                iso_file_name = f"{config.get(arguments.build, 'parent')}.iso"
                logger.debug("Child ks: %s", child_ks)
            else:
                iso_url = config.get(arguments.build, "url")
                k_cfg = config.get(arguments.build, "kcfg")
                iso_file_name = f"{arguments.build}.iso"
            logger.debug("Downloading iso from: %s", iso_url)
            iso_download_location = os.path.join(arguments.work_dir, iso_file_name)
        iso_location = download_file(iso_url, iso_download_location)
        os.makedirs(working_path)
        print(f"working path: {working_path}")
        iso_file = os.path.join(arguments.work_dir, iso_file_name)
        iso_volume_name = iso_volume_id(iso_file)
        logger.debug("Iso volume name: %s", iso_volume_name)
        efi_boot_cfg = create_grub_cfg(iso_volume_name, grub_cfg_template, arguments.build)
        grub_menu = os.path.join(working_path, "grub.cfg")
        print(f"Creating grub.cfg for {arguments.build} at {grub_menu}")
        with open(grub_menu, "w") as grub_file:
            print(f"writing grub.cfg to {os.path.join(working_path, '/grub.cfg')}")
            grub_file.write(efi_boot_cfg)
        iso_default_boot_file = "boot/grub2/grub.cfg"
        if arguments.build == "rocky-10":
            print("Detected rocky-10 build, using efi boot config")
            default_boot_menu = grub_menu
        else:
            print("Using isolinux boot config")
            grub_cfg = create_grub_cfg(iso_volume_name, isolinux_cfg_template, arguments.build)
            iso_default_boot_file = "isolinux/isolinux.cfg"
            default_boot_menu = os.path.join(working_path, "isolinux.cfg")
            with open(default_boot_menu, "w") as isolinux_file:
                print(f"writing isolinux.cfg to {os.path.join(working_path, '/isolinux.cfg')}")
                isolinux_file.write(grub_cfg)
        logger.info("Using kickstart file: %s", k_cfg)
        dst_iso=os.path.join(working_path, "kickstarted.iso")
        logger.debug("Destination iso: %s", dst_iso)
        if config.has_option(arguments.build, "parent"):
            modified_kcfg = os.path.join(working_path, "ks.cfg")
            shutil.copy(k_cfg, modified_kcfg)
            logger.debug("Appending child kickstart file: %s", child_ks)
            with open(modified_kcfg, "a") as append:
                append.write(f"\n%ksappend /run/install/repo/{os.path.basename(child_ks)}\n")
            logger.info("Creating kickstarted iso image")
            create_kickstarted_iso(
                src=iso_file,
                dst=dst_iso,
                iso_name=iso_volume_name,
                kickstart_cfg=modified_kcfg,
                grub_cfg=grub_menu,
                default_boot_cfg=default_boot_menu,
                default_boot_file=iso_default_boot_file,
                optional_kickstart_cfg=child_ks
            )
        else:
            create_kickstarted_iso(
                src=iso_file,
                dst=dst_iso,
                iso_name=iso_volume_name,
                kickstart_cfg=k_cfg,
                grub_cfg=grub_menu,
                default_boot_cfg=default_boot_menu,
                default_boot_file=iso_default_boot_file
            )
        logger.info("Moving %s iso to %s", dst_iso, updated_iso_path)
        os.rename(dst_iso, updated_iso_path)
    finally:
        logger.info("=" * 50)
        logger.info("Cleaninig up.")
        if os.path.isdir(working_path):
            if arguments.remove_source:
                logger.debug("Removing working dir and source iso")
                cleanup(working_path, iso_download_location)
            else:
                logger.debug("Removing working dir")
                cleanup(working_path)
