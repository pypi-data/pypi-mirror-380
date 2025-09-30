import os
from pathlib import Path
import subprocess
import tempfile
import threading
import time

import requests

from sideload.jsonbin_connector import JSONBinConnector

JSONBIN_TOKEN = os.environ["JSONBIN_TOKEN"]
PYPI_TOKEN = os.environ["PYPI_TOKEN"]
MAX_PACKAGE_SIZE = 95 * 1024 * 1024  # 95 MB

LAST_BINS: dict[str, str | None] = {}

PYPROJECT_TEMPLATE = """
[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"

[project]
name = "{package_name}"
version = "1.0.0"
description = "Sideloaded package"
requires-python = ">=3.8"
authors = [
  {{name = "Null Void" }}
]

[tool.setuptools.data-files]
"share/{package_name}" = ["{package_name}"]
"""

jsonbin_connector = JSONBinConnector()


def package_build(directory: Path) -> bool:
    result = subprocess.run(
        ["python3", "-m", "build", "--wheel"], cwd=str(directory), check=True
    )
    return result.returncode == 0


def twine_upload(directory: Path):
    result = subprocess.run(
        [
            "twine",
            "upload",
            "dist/*",
            "-u",
            "__token__",
            "-p",
            PYPI_TOKEN,
        ],
        cwd=str(directory),
        check=True,
    )
    return result.returncode == 0


def download_file(bin_id: str, url: str):
    try:
        # Send a HTTP request to the server.
        response = requests.get(url, stream=True)
    except Exception as e:
        jsonbin_connector.update_bin(
            bin_id,
            {
                "status": "REJECTED",
                "details": f"Failed to download file: [{e.__class__.__name__}]: {e}",
            },
        )
        return
    if not response.ok:
        jsonbin_connector.update_bin(
            bin_id,
            {
                "status": "REJECTED",
                "details": f"URL returned code {response.status_code}: {response.reason}",
            },
        )
        return
    # Total size in bytes.
    total_size = int(response.headers.get("content-length", 1))
    try:
        filename = response.headers["Content-Disposition"].split("; filename=")[1]
    except Exception:
        filename = response.url.removesuffix("/").split("/")[-1]

    # Initialize variables to track progress.
    downloaded = 0
    chunk_size = 1024 * 1000  # Size of each chunk in bytes.
    last_progress = 0
    filename_root = filename.split(".")[0]
    package_name = f"sideload_{filename_root}_bin_{bin_id}"
    # replace all non-alphanumeric characters with an underscore
    package_name = "".join(c if c.isalnum() else "_" for c in package_name)
    parts: list[Path] = []

    def make_part_name():
        return f"{package_name}_p{len(parts)}"

    def make_new_part():
        part_name = make_part_name()
        part_directory = Path(temp_dir) / package_name / part_name
        part_directory.mkdir(parents=True, exist_ok=False)
        part_path = part_directory / part_name
        parts.append(part_path)
        return open(part_path, "wb")

    # Open a local file for writing in binary mode.
    with tempfile.TemporaryDirectory() as temp_dir:
        # temp_dir = "./dumptmp3"  # only for debugging
        os.mkdir(os.path.join(temp_dir, package_name))
        jsonbin_connector.update_bin(
            bin_id,
            {"status": "DOWNLOADING", "progress": 0},
        )
        current_part_fp = make_new_part()
        try:
            current_chunk_size = 0
            for data in response.iter_content(chunk_size=chunk_size):
                current_part_fp.write(data)
                downloaded += len(data)
                current_chunk_size += len(data)
                if current_chunk_size >= MAX_PACKAGE_SIZE:
                    current_part_fp.close()
                    current_part_fp = make_new_part()
                    current_chunk_size = 0
                if total_size < downloaded:
                    total_size = downloaded
                    progress = 99
                else:
                    progress = int((downloaded / total_size) * 100)
                if progress != last_progress:
                    jsonbin_connector.update_bin(bin_id, {"progress": progress})
                    last_progress = progress
        finally:
            current_part_fp.close()
        jsonbin_connector.update_bin(bin_id, {"progress": 100, "status": "DOWNLOADED"})
        for part_idx, path_part in enumerate(parts):
            with open(
                path_part.parent / "pyproject.toml",
                "w",
                encoding="utf-8",
            ) as pyproject_file:
                pyproject_file.write(
                    PYPROJECT_TEMPLATE.format(package_name=path_part.name)
                )

            jsonbin_connector.update_bin(
                bin_id,
                {
                    "status": "BUILDING",
                    "details": f"Building package part {part_idx}/{len(parts)}.",
                },
            )
            if not package_build(path_part.parent):
                jsonbin_connector.update_bin(
                    bin_id,
                    {
                        "status": "BULDING",
                        "details": f"Failed to build package part {part_idx}/{len(parts)}.",
                    },
                )
                return
            jsonbin_connector.update_bin(
                bin_id,
                {
                    "status": "UPLOADING",
                    "details": f"Uploading package part {part_idx}/{len(parts)}.",
                },
            )
            if not twine_upload(path_part.parent):
                jsonbin_connector.update_bin(
                    bin_id,
                    {
                        "status": "FAILED",
                        "details": f"Failed to upload package part {part_idx}/{len(parts)}.",
                    },
                )
                return
        jsonbin_connector.update_bin(
            bin_id,
            {
                "status": "UPLOADED",
                "packages_names": [path_part.name for path_part in parts],
                "filename": filename,
                "file_size": total_size,
                "total_packages": len(parts),
            },
        )


def process_bin(bin_id: str):
    url = f"https://api.jsonbin.io/v3/b/{bin_id}"
    bin_data = requests.get(url, headers={"X-Master-Key": JSONBIN_TOKEN}).json()
    bin_record = bin_data["record"]
    if bin_record["status"] == "CREATED":
        print("Processing bin:", bin_id)
        download_file(bin_id, bin_record["url"])
    elif bin_record["status"] != "UPLOADED":
        jsonbin_connector.update_bin(
            bin_id, {"status": "FAILED", "details": "Server interruption"}
        )
    else:
        print("Bin already processed:", bin_id)


def watch_collection(collection_id: str):
    print("Watching collection:", collection_id)
    while True:
        collection_data = jsonbin_connector.get_collection_bins(
            collection_id, LAST_BINS.get(collection_id)
        )
        last_bin: str | None = None
        for bin_data in collection_data:
            bin_id = bin_data["record"]
            process_bin(bin_id)
            last_bin = bin_id
        if last_bin is not None:
            LAST_BINS[collection_id] = last_bin
        time.sleep(3)


def main():
    collections = jsonbin_connector.get_collections()
    for collection in collections:
        if collection["collectionMeta"]["name"].startswith("sideload_"):
            threading.Thread(
                target=watch_collection, args=(collection["record"],)
            ).start()


main()
