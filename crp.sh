#!/bin/bash
# Cross, render and post
bash cross-and-split.sh "$1" "$2" | bash render.sh | bash post.sh
