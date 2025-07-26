#!/bin/bash
# DMCT One-Line Deploy: Become Genesis
curl -sL https://raw.githubusercontent.com/rlmsinclair/dmct/main/install.sh | sh && ~/.dmct/dmct start && python3 ~/.dmct/genesis_beacon.py