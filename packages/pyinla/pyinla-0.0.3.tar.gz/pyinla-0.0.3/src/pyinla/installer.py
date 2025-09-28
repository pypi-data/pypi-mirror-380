import argparse
import hashlib
import os
import random
import re
import shutil
import string
import sys
import tarfile
from pathlib import Path
from urllib.parse import quote

import requests
from packaging.version import parse as parse_version
from tqdm import tqdm

try:
    import inquirer
except ImportError:
    print("Error: 'inquirer' package not found. Please run 'pip install inquirer'", file=sys.stderr)
    sys.exit(1)


# --- Configuration ---
BASE_URL = "https://inla.r-inla-download.org/Linux-builds"
FILES_URL = f"{BASE_URL}/FILES"


def get_available_builds(version_str=None):
    """
    Fetches the list of available builds. If version is None, finds the latest.
    Returns the target version and a list of available build paths for that version.
    """
    print(f"* Fetching available builds index from {FILES_URL}...")
    try:
        response = requests.get(FILES_URL)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"  [ERROR] Could not fetch build list: {e}", file=sys.stderr)
        return None, []

    lines = [line.strip() for line in response.text.strip().split('\n') if "64bit.tgz" in line]
    version_pattern = re.compile(r"Version_(\d+(\.\d+)+)")
    builds_by_version = {}

    for line in lines:
        match = version_pattern.search(line)
        if match:
            version = match.group(1)
            if version not in builds_by_version:
                builds_by_version[version] = []
            builds_by_version[version].append(line)

    if not builds_by_version:
        print("  [ERROR] No valid versions found in the build list.", file=sys.stderr)
        return None, []

    if version_str:
        if version_str not in builds_by_version:
            print(f"  [ERROR] Version '{version_str}' not found. Available versions: {', '.join(sorted(builds_by_version.keys()))}", file=sys.stderr)
            return None, []
        target_version = version_str
    else:
        target_version = max(builds_by_version.keys(), key=parse_version)
        print(f"* Found latest version: {target_version}")

    return target_version, sorted(builds_by_version[target_version])


def download_file(url, destination):
    """Downloads a file with a TQDM progress bar."""
    print(f"* Downloading {Path(destination).name}...")
    try:
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            total_size = int(r.headers.get('content-length', 0))
            with open(destination, 'wb') as f, tqdm(
                total=total_size, unit='iB', unit_scale=True, desc=Path(destination).name
            ) as bar:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
                    bar.update(len(chunk))
        return True
    except requests.RequestException as e:
        print(f"  [ERROR] Failed to download {url}: {e}", file=sys.stderr)
        return False


def install_binary(build_path, install_prefix, md5_check=True):
    """
    Performs the full installation of a single binary, including backup and restore.
    """
    # Define paths
    install_prefix = Path(install_prefix).resolve()
    install_prefix.mkdir(parents=True, exist_ok=True)
    
    target_dir = install_prefix / "64bit"
    rand_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    backup_dir = install_prefix / f"64bit-backup-{rand_suffix}"
    temp_tgz_path = install_prefix / f"64bit-download-{rand_suffix}.tgz"
    temp_md5_path = install_prefix / f"64bit-download-md5sum-{rand_suffix}.txt"

    # Construct URLs
    tgz_url = f"{BASE_URL}/{quote(build_path)}"
    md5_url = tgz_url.replace("/64bit.tgz", "/md5sum.txt")
    print(f"* Preparing to install from: {tgz_url}")

    # 1. Download MD5 and binary
    if not download_file(tgz_url, temp_tgz_path):
        return False
    
    if md5_check:
        if not download_file(md5_url, temp_md5_path):
            print("  [WARNING] Could not download MD5 checksum. Skipping check.", file=sys.stderr)
        else:
            try:
                expected_md5 = Path(temp_md5_path).read_text().strip().split()[0]
                print(f"* Verifying MD5 checksum ({expected_md5})...")
                hasher = hashlib.md5()
                with open(temp_tgz_path, 'rb') as f:
                    for chunk in iter(lambda: f.read(8192), b""):
                        hasher.update(chunk)
                calculated_md5 = hasher.hexdigest()

                if calculated_md5 == expected_md5:
                    print("* MD5 checksum OK.")
                else:
                    print(f"  [ERROR] MD5 Checksum FAILED! Expected {expected_md5}, got {calculated_md5}", file=sys.stderr)
                    temp_tgz_path.unlink()
                    temp_md5_path.unlink()
                    return False
            except (IOError, IndexError) as e:
                print(f"  [WARNING] Could not read MD5 file: {e}. Skipping check.", file=sys.stderr)
    
    # 2. The critical installation transaction (backup, unpack, cleanup)
    restored = False
    try:
        # Backup existing installation
        if target_dir.exists():
            print(f"* Backing up existing '{target_dir.name}' directory to '{backup_dir.name}'...")
            target_dir.rename(backup_dir)

        # Unpack new version
        print(f"* Unpacking archive to '{install_prefix}'...")
        with tarfile.open(temp_tgz_path, "r:gz") as tar:
            tar.extractall(path=install_prefix)
        
        if not target_dir.exists():
             raise IOError(f"Archive did not contain the expected '{target_dir.name}' directory.")
        print("* Unpacking successful.")

        # Cleanup backup
        if backup_dir.exists():
            print(f"* Removing backup directory '{backup_dir.name}'...")
            shutil.rmtree(backup_dir)

    except Exception as e:
        print(f"\n  [ERROR] An error occurred during installation: {e}", file=sys.stderr)
        print("* Attempting to restore previous state...")
        if backup_dir.exists():
            if target_dir.exists():
                shutil.rmtree(target_dir)
            backup_dir.rename(target_dir)
            print("* Restore successful.")
            restored = True
        else:
            print("* No backup found to restore.", file=sys.stderr)
        return False
    finally:
        # Always cleanup downloaded files
        if temp_tgz_path.exists():
            temp_tgz_path.unlink()
        if temp_md5_path.exists():
            temp_md5_path.unlink()
    
    if not restored:
        print("\n--- Installation successful! ---")
        print(f"INLA binaries are now in: {target_dir}")
        print("Example executable path:")
        print(f"{target_dir}/inla")
        return True
    return False


def main():
    parser = argparse.ArgumentParser(
        description="Install a specific pre-compiled INLA binary for Linux. Mimics the R function `inla.binary.install`.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "--path",
        type=str,
        required=True,
        help="The directory where the '64bit' folder containing INLA binaries will be installed."
    )
    parser.add_argument(
        "--os",
        type=str,
        help="A search string to non-interactively select the OS build (e.g., 'Ubuntu-22.04').\nMust match exactly one available build."
    )
    parser.add_argument(
        "--version",
        type=str,
        help="Specify an INLA version to install (e.g., '24.05.02').\nIf omitted, the latest version is used."
    )
    parser.add_argument(
        "--no-md5-check",
        action="store_true",
        help="Disable MD5 checksum verification."
    )
    
    args = parser.parse_args()
    
    target_version, builds = get_available_builds(args.version)
    if not builds:
        sys.exit(1)
        
    selected_build = None
    if args.os:
        # Non-interactive mode
        print(f"* Searching for OS string: '{args.os}'...")
        matches = [b for b in builds if args.os in b]
        if len(matches) == 1:
            selected_build = matches[0]
            print(f"* Found unique match: {selected_build}")
        elif len(matches) > 1:
            print(f"  [ERROR] Ambiguous OS string '{args.os}'. Found {len(matches)} matches:", file=sys.stderr)
            for m in matches:
                print(f"    - {m}")
            sys.exit(1)
        else:
            print(f"  [ERROR] No builds found for version {target_version} matching OS string '{args.os}'.", file=sys.stderr)
            sys.exit(1)
    else:
        # Interactive mode
        # The choice text should be cleaner than the full path
        def clean_name(path):
            parts = path.split('/')
            try:
                # Find the part that is not the version or the end file
                os_part = [p for p in parts if "Version_" not in p and "64bit.tgz" not in p and p not in ['.', 'testing']]
                return " / ".join(os_part) if os_part else path
            except Exception:
                return path

        choices = [(clean_name(b), b) for b in builds]
        
        questions = [
            inquirer.List('build',
                          message=f"Choose an INLA binary to install for version {target_version}",
                          choices=choices,
                          ),
        ]
        try:
            answers = inquirer.prompt(questions)
            if answers:
                selected_build = answers['build']
        except KeyboardInterrupt:
            print("\nInstallation cancelled by user.")
            sys.exit(0)

    if selected_build:
        install_binary(selected_build, args.path, md5_check=not args.no_md5_check)
    else:
        print("No build selected. Exiting.")


if __name__ == "__main__":
    main()