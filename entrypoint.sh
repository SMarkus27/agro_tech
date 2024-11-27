#!/bin/sh
set -e

# Start app
python3 -u create_table.py
python3 -u main.py