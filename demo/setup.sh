#!/usr/bin/env bash
# One-time setup. Run the night before: it downloads PyTorch and the MACE-MP-0 weights.
set -e
cd "$(dirname "$0")"
uv venv .venv --python 3.11
uv pip install --python .venv/bin/python mace-torch ase matplotlib
# Warm the model cache (~/.cache/mace) so nothing downloads during class
.venv/bin/python mace_tool.py score CCCCCCCCAAAAAAAACCCCCCCCAAAAAAAA
.venv/bin/python 01_hello_forces.py
echo "Ready."
