#!/bin/bash
# DMCT Ghost Mode - One Line to Anonymity
# Works on any system, installs everything needed

curl -sL https://raw.githubusercontent.com/rlmsinclair/dmct/main/install.sh | sh && \
(command -v tor >/dev/null 2>&1 || ([ "$(uname)" = "Darwin" ] && brew install tor || sudo apt-get install -y tor)) && \
(command -v torsocks >/dev/null 2>&1 || ([ "$(uname)" = "Darwin" ] && brew install torsocks || sudo apt-get install -y torsocks)) && \
~/.dmct/ghost.sh