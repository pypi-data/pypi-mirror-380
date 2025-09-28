# pyinla: The INLA Binary Installer

`pyinla` is an efficient command-line tool for downloading and installing the official pre-compiled executables for INLA (Integrated Nested Laplace Approximations).

It provides a straightforward way to set up the necessary INLA binaries on a Linux system, especially in environments where manual installation is cumbersome or R is not available.

## Features

-   **Automatic Version Detection:** Finds and defaults to the latest available INLA version.
-   **Interactive Selection:** Presents an easy-to-use menu to choose the correct binary for your Linux distribution.
-   **Script-Friendly:** Supports non-interactive installation for use in automated workflows and Dockerfiles.
-   **Safe Installation:** Backs up any existing installation during the process to prevent data loss on failure.
-   **Lightweight:** Minimal dependencies and a simple, focused purpose.

## Installation

Install directly from PyPI:

```bash
pip install pyinla
