#!/bin/bash
set -e
# Loop through flames
while read -r img; do
    # Extract their parents
    p="${img%.*}"
    a="${p%x*}"
    b="${p#*x}"
    # Post them to Twitter
    id="$(python3 pyrobot.py post "$img" "$a" "$b")"
    # Rename them
    mv "$img" "flames/$id.png"
    # And their source files
    mv "${img%.*}.flam3" "flames/$id.flam3"
done
