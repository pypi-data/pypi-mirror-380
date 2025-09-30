#!/usr/bin/env python3
"""
Sideload CLI Client
A beautiful command-line interface for downloading files via the Sideload service.
"""

import os
import sys
import time
import subprocess
import tempfile
import argparse
from pathlib import Path
from typing import List, Dict

from rich.console import Console
from rich.progress import (
    Progress,
    SpinnerColumn,
    TextColumn,
    BarColumn,
    TaskProgressColumn,
)
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.align import Align
from rich.rule import Rule

from sideload.jsonbin_old import JSONBinConnector, SideloadBinManager

console = Console()


class SideloadClient:
    def __init__(self, jsonbin_token: str, collection_id: str):
        self.collection_id = collection_id
        self.connector = JSONBinConnector(jsonbin_token)
        self.manager = SideloadBinManager(self.connector)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connector.close()

    def create_request(self, url: str) -> str:
        """Create a new sideload request and return the bin ID"""
        with console.status("[bold green]Creating sideload request..."):
            bin_id = self.manager.create_sideload_request(url, self.collection_id)

        console.print(f"✅ Created sideload request: [bold cyan]{bin_id}[/bold cyan]")
        return bin_id

    def monitor_request(self, bin_id: str) -> Dict:
        """Monitor the sideload request progress"""

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TaskProgressColumn(),
            console=console,
            transient=True,
        ) as progress:
            download_task = progress.add_task("Monitoring request...", total=100)

            while True:
                try:
                    data = self.manager.get_sideload_data(bin_id)

                    status = data.get("status", "UNKNOWN")
                    current_progress = data.get("progress", 0)

                    if status == "DOWNLOADING":
                        progress.update(
                            download_task,
                            description=f"📥 Downloading... ({current_progress}%)",
                            completed=current_progress,
                        )
                    elif status == "BUILDING":
                        progress.update(
                            download_task,
                            description="🔨 Building packages...",
                            completed=90,
                        )
                    elif status == "UPLOADING":
                        current_part = data.get("current_part", 1)
                        total_parts = data.get("total_parts", 1)
                        progress.update(
                            download_task,
                            description=f"📤 Uploading part {current_part}/{total_parts}...",
                            completed=95,
                        )
                    elif status == "UPLOADED":
                        progress.update(
                            download_task,
                            description="✅ Upload complete!",
                            completed=100,
                        )
                        break
                    elif status in ["FAILED", "REJECTED"]:
                        reason = data.get("reason", "Unknown error")
                        console.print(f"❌ Request failed: {reason}", style="bold red")
                        return data

                    time.sleep(2)

                except KeyboardInterrupt:
                    console.print("\n⚠️  Monitoring interrupted by user", style="yellow")
                    break
                except Exception as e:
                    console.print(f"❌ Error monitoring request: {e}", style="red")
                    break

        # Get final data
        return self.manager.get_sideload_data(bin_id)

    def download_packages(
        self, package_names: List[str], output_dir: Path
    ) -> List[Path]:
        """Download all packages to a temporary directory"""
        downloaded_files = []

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TaskProgressColumn(),
            console=console,
        ) as progress:
            download_task = progress.add_task(
                "Downloading packages...", total=len(package_names)
            )

            for i, package_name in enumerate(package_names):
                progress.update(
                    download_task,
                    description=f"📦 Downloading {package_name}...",
                    completed=i,
                )

                # Download using pip to temporary directory
                try:
                    subprocess.run(
                        [
                            sys.executable,
                            "-m",
                            "pip",
                            "download",
                            "--no-deps",
                            "--dest",
                            str(output_dir),
                            package_name,
                        ],
                        capture_output=True,
                        text=True,
                        check=True,
                    )

                    # Find the downloaded wheel file
                    wheel_files = list(output_dir.glob(f"{package_name}*.whl"))
                    if wheel_files:
                        downloaded_files.append(wheel_files[0])

                except subprocess.CalledProcessError as e:
                    console.print(
                        f"❌ Failed to download {package_name}: {e.stderr}", style="red"
                    )
                    continue

            progress.update(
                download_task,
                description="✅ Download complete!",
                completed=len(package_names),
            )

        return downloaded_files

    def extract_and_reassemble(
        self, wheel_files: List[Path], original_filename: str, output_path: Path
    ):
        """Extract parts from wheel files and reassemble the original file"""
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            part_files = []

            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                BarColumn(),
                TaskProgressColumn(),
                console=console,
            ) as progress:
                extract_task = progress.add_task(
                    "Extracting packages...", total=len(wheel_files)
                )

                # Extract each wheel file
                for i, wheel_file in enumerate(wheel_files):
                    progress.update(
                        extract_task,
                        description=f"📂 Extracting {wheel_file.name}...",
                        completed=i,
                    )

                    # Extract wheel file (it's just a zip)
                    import zipfile

                    with zipfile.ZipFile(wheel_file, "r") as zip_ref:
                        zip_ref.extractall(temp_path)

                    # Find the part file in the wheel's data directory structure
                    # Pattern: pkgname.data/data/share/pkgname/pkgname
                    data_dirs = list(temp_path.glob("*.data/data/share/*/*"))
                    for part_file in data_dirs:
                        if part_file.is_file():
                            part_files.append(part_file)

                progress.update(
                    extract_task,
                    description="✅ Extraction complete!",
                    completed=len(wheel_files),
                )

            # Sort part files to ensure correct order
            part_files.sort(key=lambda x: x.name)

            if len(part_files) == 1 and part_files[0].name == original_filename:
                # Single file, just copy it
                console.print("📄 Single file detected, copying...")
                import shutil

                shutil.copy2(part_files[0], output_path)
            else:
                # Multiple parts, concatenate them
                console.print(f"🔗 Reassembling {len(part_files)} parts...")

                with Progress(
                    SpinnerColumn(),
                    TextColumn("[progress.description]{task.description}"),
                    BarColumn(),
                    TaskProgressColumn(),
                    console=console,
                ) as progress:
                    reassemble_task = progress.add_task(
                        "Reassembling file...", total=len(part_files)
                    )

                    with open(output_path, "wb") as output_file:
                        for i, part_file in enumerate(part_files):
                            progress.update(
                                reassemble_task,
                                description=f"🔗 Assembling part {i + 1}/{len(part_files)}...",
                                completed=i,
                            )

                            with open(part_file, "rb") as part:
                                output_file.write(part.read())

                    progress.update(
                        reassemble_task,
                        description="✅ Reassembly complete!",
                        completed=len(part_files),
                    )


def display_header():
    """Display the application header"""
    header = Text("🚀 SIDELOAD", style="bold magenta")
    subtitle = Text("Download large files via PyPI packages", style="dim")

    panel = Panel(
        Align.center(f"{header}\n{subtitle}"), border_style="magenta", padding=(1, 2)
    )
    console.print(panel)


def display_summary(data: Dict):
    """Display a summary of the completed request"""
    table = Table(title="📊 Download Summary", style="cyan")
    table.add_column("Property", style="bold")
    table.add_column("Value")

    table.add_row("Original Filename", data.get("filename", "Unknown"))
    table.add_row("File Size", f"{data.get('file_size', 0):,} bytes")
    table.add_row("Total Packages", str(data.get("total_packages", 0)))
    table.add_row("Status", f"✅ {data.get('status', 'Unknown')}")

    console.print(table)


def main():
    parser = argparse.ArgumentParser(
        description="Sideload CLI - Download large files via PyPI packages",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  sideload download https://example.com/largefile.zip
  sideload download https://example.com/file.zip --output ./downloads/
        """,
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Download command
    download_parser = subparsers.add_parser(
        "download", help="Download a file via sideload"
    )
    download_parser.add_argument("url", help="URL of the file to download")
    download_parser.add_argument(
        "--output",
        "-o",
        type=Path,
        default=Path.cwd(),
        help="Output directory (default: current directory)",
    )
    download_parser.add_argument("--collection", help="JSONBin collection ID")
    download_parser.add_argument("--token", help="JSONBin API token")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    display_header()

    if args.command == "download":
        # Get credentials
        jsonbin_token = args.token or os.environ.get("JSONBIN_TOKEN")
        collection_id = args.collection or os.environ.get("SIDELOAD_COLLECTION_ID")

        if not jsonbin_token:
            console.print(
                "❌ JSONBin token required. Set JSONBIN_TOKEN environment variable or use --token",
                style="red",
            )
            return

        if not collection_id:
            console.print(
                "❌ Collection ID required. Set SIDELOAD_COLLECTION_ID environment variable or use --collection",
                style="red",
            )
            return

        # Ensure output directory exists
        args.output.mkdir(parents=True, exist_ok=True)

        try:
            with SideloadClient(jsonbin_token, collection_id) as client:
                # Create the request
                console.print(
                    f"🌐 Requesting download for: [bold blue]{args.url}[/bold blue]"
                )
                bin_id = client.create_request(args.url)

                # Monitor the request
                console.print(Rule("📡 Monitoring Progress"))
                data = client.monitor_request(bin_id)

                if data.get("status") != "UPLOADED":
                    console.print(
                        "❌ Request did not complete successfully", style="red"
                    )
                    return

                # Display summary
                display_summary(data)

                # Download packages
                package_names = data.get("packages_names", [])
                if not package_names:
                    console.print("❌ No packages found in the response", style="red")
                    return

                console.print(Rule("📦 Downloading Packages"))

                with tempfile.TemporaryDirectory() as temp_dir:
                    temp_path = Path(temp_dir)
                    wheel_files = client.download_packages(package_names, temp_path)

                    if not wheel_files:
                        console.print(
                            "❌ No packages were downloaded successfully", style="red"
                        )
                        return

                    # Extract and reassemble
                    console.print(Rule("🔧 Reassembling File"))
                    original_filename = data.get("filename", "downloaded_file")
                    output_file = args.output / original_filename

                    client.extract_and_reassemble(
                        wheel_files, original_filename, output_file
                    )

                    # Success!
                    console.print(Rule("✨ Complete"))
                    console.print(
                        f"🎉 File successfully downloaded to: [bold green]{output_file}[/bold green]"
                    )
                    console.print(
                        f"📊 File size: [cyan]{output_file.stat().st_size:,} bytes[/cyan]"
                    )

        except KeyboardInterrupt:
            console.print("\n⚠️  Download interrupted by user", style="yellow")
        except Exception as e:
            console.print(f"❌ Error: {e}", style="bold red")
            raise


if __name__ == "__main__":
    main()
