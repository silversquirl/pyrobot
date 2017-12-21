#!/bin/bash
set -e
out="${1%.flam3}x${2##*/}"
a="${1%.flam3}-mutated.flam3"
b="${2%.flam3}-mutated.flam3"
mutate="$1" flam3-genome > "$a"
mutate="$2" flam3-genome > "$b"
cross0="$a" cross1="$a" repeat=1 flam3-genome > "$out"
python3 split.py "$out"
