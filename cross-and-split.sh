#!/bin/bash
set -e
out="${1%.flam3}x${2##*/}"
a="${1%.flam3}-mutated.flam3"
b="${2%.flam3}-mutated.flam3"
flam3-genome < "$1" > "$a"
flam3-genome < "$2" > "$b"
cross0="$a" cross1="$a" repeat=1 flam3-genome > "$out"
python3 split.py "$out"
