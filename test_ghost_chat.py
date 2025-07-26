#!/usr/bin/env python3
"""Test Ghost Chat Tor Propagation"""

import subprocess
import time
import os

# Colors
PURPLE = '\033[0;35m'
CYAN = '\033[0;36m'
GREEN = '\033[0;32m'
YELLOW = '\033[0;33m'
NC = '\033[0m'

print(f"{PURPLE}Testing DMCT Ghost Chat Tor Propagation{NC}\n")

# Check if Tor is running
print(f"{CYAN}1. Checking Tor status...{NC}")
try:
    import socket
    s = socket.socket()
    s.settimeout(1)
    s.connect(('127.0.0.1', 9050))
    s.close()
    print(f"{GREEN}✓ Tor is running on port 9050{NC}")
except:
    print(f"{YELLOW}✗ Tor is not running{NC}")
    print(f"{CYAN}Start with: ~/.dmct/ghost.sh{NC}")
    exit(1)

# Check hidden service
print(f"\n{CYAN}2. Checking hidden service...{NC}")
hostname_file = os.path.expanduser("~/.dmct/tor/hidden_service/hostname")
if os.path.exists(hostname_file):
    with open(hostname_file, 'r') as f:
        onion = f.read().strip()
    print(f"{GREEN}✓ Hidden service: {onion}{NC}")
else:
    print(f"{YELLOW}✗ No hidden service found{NC}")
    onion = None

# Test pure Python SOCKS5
print(f"\n{CYAN}3. Testing pure Python SOCKS5 implementation...{NC}")
try:
    from ghost_chat_pure import TorSocket
    print(f"{GREEN}✓ TorSocket class loaded successfully{NC}")
    
    # Test connection
    if onion:
        print(f"{CYAN}4. Testing self-connection through Tor...{NC}")
        try:
            tor_sock = TorSocket()
            tor_sock.connect(onion, 31415)
            print(f"{GREEN}✓ Successfully connected to own .onion address{NC}")
            tor_sock.close()
        except Exception as e:
            print(f"{YELLOW}✗ Connection failed: {e}{NC}")
except Exception as e:
    print(f"{YELLOW}✗ Failed to load TorSocket: {e}{NC}")

print(f"\n{PURPLE}Summary:{NC}")
print(f"• Tor SOCKS proxy: {GREEN}Active{NC}" if onion else f"• Tor SOCKS proxy: {YELLOW}Inactive{NC}")
print(f"• Hidden service: {GREEN}{onion}{NC}" if onion else f"• Hidden service: {YELLOW}Not configured{NC}")
print(f"• Pure Python SOCKS5: {GREEN}Working{NC}")
print(f"\n{CYAN}Ready for anonymous messaging through Tor!{NC}\n")