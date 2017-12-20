#!/bin/bash
# Loop through flames
while read -r img; do
    # Post them to Twitter
    id="$(python3 pyrobot.py post "$img")"
    # Rename them
    mv "$img" "flames/$id.png"
    # And their source files
    mv "${img%.*}.flam3" "flames/$id.flam3"
done
