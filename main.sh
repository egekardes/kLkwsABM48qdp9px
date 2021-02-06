#!/bin/sh

chmod +x *.py
./create_model.py
./format_input.py
./fit.py
./evaluate.py
