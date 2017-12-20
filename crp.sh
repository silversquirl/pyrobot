#!/bin/bash
# Cross, render and post
a="tmp/${1##*/}"
b="tmp/${2##*/}"
cp "$1" "$a"
cp "$2" "$b"
bash cross-and-split.sh "$a" "$b" | bash render.sh | bash post.sh
