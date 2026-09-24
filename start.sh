#!/bin/bash
echo "Installing/verifying dependencies..."
python3 -m pip install -r requirements.txt
echo "Starting Rose Bot..."
python3 main.py
