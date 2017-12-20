#!/bin/bash
set -e
out="${1%.flam3}x${2##*/}"
cross0="$1" cross1="$2" repeat=1 flam3-genome > "$out"
python3 split.py "$out"
