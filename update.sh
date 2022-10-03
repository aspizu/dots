#!/bin/bash
set -e
python update.py
git add .
git commit -m "dots"
git push
