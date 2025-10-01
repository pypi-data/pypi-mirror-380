import requests
from urllib.parse import urlparse
from logging import getLogger
import sys
import time
import os
import shutil
import subprocess
from kickstart_iso_tool.constants import (
    SPEED_UNITS,
    CHUNK_SIZE,
    HUMAN_UNITS
)

logger = getLogger(__name__)


def convert_size_to_human(size: float, speed=None):
    if speed:
        for unit in SPEED_UNITS:
            if unit == SPEED_UNITS[-1]:
                logger.warning(f"Breaking from loop as reached {SPEED_UNITS[-1]}")
                break
            if float(size) < 1024.0:
                break
            size = float(size) / 1024.0
        size *= 8
    else:
        for unit in HUMAN_UNITS:
            if unit == HUMAN_UNITS[-1]:
                logger.warning(f"Breaking from loop as reached {HUMAN_UNITS[-1]}")
                break
            if float(size) < 1024.0:
                break
            size = float(size) / 1024.0
    return f"{size:.2f} {unit}"


def progress_bar(terminal_size: int, current_length: int, total_length: int, speed: float, file_name: str) -> None:
    done_percent = round(current_length * 100 / total_length, 2)
    bar_prefix = f"Downloading {file_name}:"
    bar_suffix = f"{done_percent:0>6.2f}% | Speed: {speed}"
    bar_length = (len(bar_prefix) + len(bar_suffix)) + 1
    bar_size = terminal_size - bar_length - 3
    done = int(bar_size * current_length / total_length)
    done_length = "=" * (done)
    in_progress_length = "." * (bar_size - done - 1)
    if bar_size <= done:
        current_progress = ""
    else:
        current_progress = ">"
    if bar_length > terminal_size:
        sys.stdout.write(f"\rDL: {done_percent:0>6.2f}%")
    else:
        sys.stdout.write(f"\r{bar_prefix} [{done_length}{current_progress}{in_progress_length}] {bar_suffix}")


def download_file(url: str, save_path: str):
    logger.debug(f"URL: {url}")
    logger.debug(f"Download save path: {save_path}")
    file_name = urlparse(url)
    file_name = os.path.basename(file_name.path)
    start_time = time.perf_counter()
    download = requests.get(url, stream=True)
    total_length = download.headers.get("content-length")
    if os.path.exists(save_path):
        logger.warning(f"File: {save_path} already exists")
        old_file_size = os.stat(save_path)
        logger.debug(f"Old file size: {convert_size_to_human(old_file_size.st_size)}")
        if int(total_length) > int(old_file_size.st_size):
            logger.warning("Remote file size different, re-downloading")
        else:
            logger.warning("Old file size matches remote, re-using!")
            return save_path
    with open(save_path, "wb") as file:
        check_free_space(int(total_length) * 2, save_path)
        totoal_length_human = convert_size_to_human(total_length)
        logger.debug(f"Download size: {totoal_length_human}")
        current_length = 0
        if total_length is None:
            file.write(download.content)
        else:
            total_length = int(total_length)
            dl_speed = 0
            update_time = 1
            for data in download.iter_content(chunk_size=CHUNK_SIZE):
                TERMINAL_SIZE = os.get_terminal_size().columns
                file.write(data)
                current_length += len(data)
                current_time = time.perf_counter()
                time_diff = (current_time - start_time)
                if int(time_diff) + 1 == update_time:
                    dl_speed = convert_size_to_human(current_length / time_diff, speed=True)
                    update_time += 1
                    progress_bar(TERMINAL_SIZE, current_length, total_length, dl_speed, file_name=file_name)
            progress_bar(TERMINAL_SIZE, current_length, total_length, dl_speed, file_name=file_name)
    return save_path


def check_free_space(size: int, save_path: str) -> None:
    current_usage = shutil.disk_usage(save_path)
    free = current_usage.free
    size = round(size * 1.1)
    logger.debug(f"Available disk space: {convert_size_to_human(free)} for path: {save_path}")
    logger.debug(f"Estimated needs: {convert_size_to_human(size)}")
    if size >= free:
        logger.critical(f"Low disk space for {save_path}")
        logger.critical(f"Available space: {convert_size_to_human(free)}")
        logger.critical(f"Expected usage: {convert_size_to_human(size)}")
        sys.exit(1)


def execute_command(shell_cli):
    logger.debug(f"Executing: {' '.join(shell_cli)}")
    print(f"Executing: {' '.join(shell_cli)}")
    exec = subprocess.Popen(shell_cli, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = exec.communicate()
    print(output.decode("UTF-8"))
    print(err.decode("UTF-8"))