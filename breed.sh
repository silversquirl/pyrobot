#!/bin/bash
set -e
python3 pyrobot.py popular | xargs -0 bash crp.sh
