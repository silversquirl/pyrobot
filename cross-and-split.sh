#!/bin/bash
set -e
out="${1%.flam3}x${2##*/}"
flam3-genome < "$1" > "mutated-$1"
flam3-genome < "$2" > "mutated-$2"
cross0="mutated-$1" cross1="mutated-$2" repeat=1 flam3-genome > "$out"
python3 split.py "$out"
