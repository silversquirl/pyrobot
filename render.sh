#!/bin/bash
while read -r flame; do
    out="${flame%.flam3}.png"
    in="$flame" out="$out" qs=50 flam3-render
    echo "$out"
done
