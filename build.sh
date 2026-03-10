#!/usr/bin/env bash
set -e

BASEPATH="${1:-/BootDev_Python_Static_Site_Generator/}"
python3 src/main.py "$BASEPATH"
