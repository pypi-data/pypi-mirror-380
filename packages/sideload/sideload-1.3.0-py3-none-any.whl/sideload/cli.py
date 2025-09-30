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
    def __init__(
        self,
        jsonbin_token: str,
        collection_id: str,
        verify_ssl: bool = True,
        key_type: str = "master"
    ):
        self.collection_id = collection_id
        self.connector = JSONBinConnector(
            jsonbin_token,
            verify_ssl=verify_ssl,
            key_type=key_type
        )
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
        self, package_names: List[str], output_dir: Path, debug: bool = False
    ) -> List[Path]:
        """Download all packages to a temporary directory"""
        downloaded_files = []

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TaskProgressColumn(),
            console=console,
            disable=debug,  # Disable progress bar in debug mode
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
                    cmd = [
                        sys.executable,
                        "-m",
                        "pip",
                        "download",
                        "--no-deps",
                        "--dest",
                        str(output_dir),
                        package_name,
                    ]

                    if debug:
                        console.print(f"[dim]Running: {' '.join(cmd)}[/dim]")

                    subprocess.run(
                        cmd,
                        capture_output=not debug,
                        text=True,
                        check=True,
                    )

                    # Find the downloaded wheel file
                    wheel_files = list(output_dir.glob(f"{package_name}*.whl"))
                    if wheel_files:
                        downloaded_files.append(wheel_files[0])
                        if debug:
                            console.print(f"[green]✓ Downloaded: {wheel_files[0].name}[/green]")

                except subprocess.CalledProcessError as e:
                    error_msg = e.stderr if hasattr(e, 'stderr') and e.stderr else str(e)
                    console.print(
                        f"❌ Failed to download {package_name}: {error_msg}", style="red"
                    )
                    continue

            progress.update(
                download_task,
                description="✅ Download complete!",
                completed=len(package_names),
            )

        return downloaded_files

    def extract_and_reassemble(
        self, wheel_files: List[Path], package_names: List[str], original_filename: str, output_path: Path, debug: bool = False, work_dir: Path = None
    ):
        """Extract parts from wheel files and reassemble the original file"""
        # Use provided work directory or create a temporary one
        use_temp = work_dir is None
        if use_temp:
            temp_dir_obj = tempfile.TemporaryDirectory()
            temp_path = Path(temp_dir_obj.name)
        else:
            temp_dir_obj = None
            temp_path = work_dir
            temp_path.mkdir(parents=True, exist_ok=True)

        try:
            part_files = []

            if not use_temp:
                console.print(f"[yellow]⚠️  Using work directory: {temp_path}[/yellow]")
                console.print(f"[yellow]   Files will be kept after extraction for debugging[/yellow]")

            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                BarColumn(),
                TaskProgressColumn(),
                console=console,
                disable=debug,  # Disable progress bar in debug mode
            ) as progress:
                extract_task = progress.add_task(
                    "Extracting packages...", total=len(wheel_files)
                )

                # Extract each wheel file
                for i, (wheel_file, package_name) in enumerate(zip(wheel_files, package_names)):
                    progress.update(
                        extract_task,
                        description=f"📂 Extracting {wheel_file.name}...",
                        completed=i,
                    )

                    if debug:
                        console.print(f"\n[cyan]Extracting package {i + 1}/{len(wheel_files)}: {package_name}[/cyan]")

                    # Extract wheel file (it's just a zip)
                    import zipfile

                    with zipfile.ZipFile(wheel_file, "r") as zip_ref:
                        if debug:
                            console.print(f"\n[dim]Contents of {wheel_file.name}:[/dim]")
                            for name in sorted(zip_ref.namelist()):
                                console.print(f"[dim]  {name}[/dim]")
                        zip_ref.extractall(temp_path)

                    # Find the part file using the exact package name
                    # Pattern: pkgname-version.data/data/share/pkgname/pkgname
                    # Need to find the .data directory that starts with package_name
                    data_dir = None
                    for d in temp_path.iterdir():
                        if d.is_dir() and d.name.startswith(f"{package_name}-") and d.name.endswith(".data"):
                            data_dir = d
                            break

                    if data_dir:
                        part_file_path = data_dir / "data" / "share" / package_name / package_name
                        if debug:
                            console.print(f"[dim]Looking for: {part_file_path}[/dim]")
                            console.print(f"[dim]Exists: {part_file_path.exists()}, Is file: {part_file_path.is_file() if part_file_path.exists() else 'N/A'}[/dim]")
                        if part_file_path.is_file():
                            part_files.append(part_file_path)
                            if debug:
                                console.print(f"[green]✓ Found part file: {part_file_path.name} (size: {part_file_path.stat().st_size:,} bytes)[/green]")
                    else:
                        if debug:
                            console.print(f"[yellow]⚠ Could not find .data directory for {package_name}[/yellow]")

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
                    disable=debug,  # Disable progress bar in debug mode
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

                            if debug:
                                console.print(f"[dim]Reading part {i + 1}/{len(part_files)}: {part_file.name} ({part_file.stat().st_size:,} bytes)[/dim]")

                            with open(part_file, "rb") as part:
                                output_file.write(part.read())

                    progress.update(
                        reassemble_task,
                        description="✅ Reassembly complete!",
                        completed=len(part_files),
                    )
        finally:
            # Clean up temporary directory if we created one
            if use_temp and temp_dir_obj:
                temp_dir_obj.cleanup()


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
    download_parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable debug logging",
    )
    download_parser.add_argument(
        "--work-dir",
        type=Path,
        help="Working directory for extraction (for debugging, defaults to temp directory)",
    )
    download_parser.add_argument(
        "--no-verify-ssl",
        action="store_true",
        help="Disable SSL certificate verification for JSONBin API",
    )
    download_parser.add_argument(
        "--jsonbin-key-type",
        choices=["master", "access"],
        default=None,
        help="JSONBin key type to use (default: from JSONBIN_KEY_TYPE env or 'master')",
    )

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    display_header()

    if args.command == "download":
        # Get credentials
        jsonbin_token = args.token or os.environ.get("JSONBIN_TOKEN")
        collection_id = args.collection or os.environ.get("SIDELOAD_COLLECTION_ID")

        # Get SSL verification setting (CLI flag overrides env var)
        verify_ssl = not args.no_verify_ssl
        if args.no_verify_ssl:
            # If CLI flag is set, disable SSL verification
            verify_ssl = False
        else:
            # Otherwise check environment variable (default to True)
            env_verify = os.environ.get("JSONBIN_VERIFY_SSL", "true").lower()
            verify_ssl = env_verify in ("true", "1", "yes")

        # Get key type (CLI arg > env var > default)
        key_type = args.jsonbin_key_type or os.environ.get("JSONBIN_KEY_TYPE", "master").lower()

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

        # Show debug flags if enabled
        if args.debug:
            console.print("\n[bold cyan]Debug Mode Enabled[/bold cyan]")
            console.print(f"  [dim]URL:[/dim] {args.url}")
            console.print(f"  [dim]Output:[/dim] {args.output}")
            console.print(f"  [dim]Work Directory:[/dim] {args.work_dir or 'temp (auto-cleanup)'}")
            console.print(f"  [dim]Collection ID:[/dim] {collection_id}")
            console.print(f"  [dim]SSL Verification:[/dim] {verify_ssl}")
            console.print(f"  [dim]JSONBin Key Type:[/dim] {key_type}")
            console.print()

        try:
            with SideloadClient(jsonbin_token, collection_id, verify_ssl, key_type) as client:
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
                    wheel_files = client.download_packages(package_names, temp_path, args.debug)

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
                        wheel_files, package_names, original_filename, output_file, args.debug, args.work_dir
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
