#!/bin/bash
# DMCT Ghost Mode Launcher
# Full anonymous operation through Tor

set -e

DMCT_DIR="$HOME/.dmct"
TOR_DIR="$DMCT_DIR/tor"
TOR_DATA="$TOR_DIR/data"
HIDDEN_SERVICE="$TOR_DIR/hidden_service"

# Colors
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${PURPLE}"
cat << "EOF"
   ▄████  ██░ ██  ▒█████    ██████ ▄▄▄█████▓
  ██▒ ▀█▒▓██░ ██▒▒██▒  ██▒▒██    ▒ ▓  ██▒ ▓▒
 ▒██░▄▄▄░▒██▀▀██░▒██░  ██▒░ ▓██▄   ▒ ▓██░ ▒░
 ░▓█  ██▓░▓█ ░██ ▒██   ██░  ▒   ██▒░ ▓██▓ ░ 
 ░▒▓███▀▒░▓█▒░██▓░ ████▓▒░▒██████▒▒  ▒██▒ ░ 
  ░▒   ▒  ▒ ░░▒░▒░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░  ▒ ░░   
   ░   ░  ▒ ░▒░ ░  ░ ▒ ▒░ ░ ░▒  ░ ░    ░    
   ░   ░  ░  ░░ ░░ ░ ░ ▒  ░  ░  ░    ░      
       ░  ░  ░  ░    ░ ░        ░           
                                             
   M O D E   :   A C T I V A T E D
EOF
echo -e "${NC}"

echo -e "${CYAN}Initializing anonymous trust network...${NC}\n"

# Create directories
mkdir -p "$TOR_DATA" "$HIDDEN_SERVICE"

# Check Tor installation
if ! command -v tor &> /dev/null; then
    echo -e "${RED}❌ Tor not found. Install with: brew install tor${NC}"
    exit 1
fi

# Start Tor with custom config
echo -e "${CYAN}🧅 Starting Tor hidden service...${NC}"
tor -f "$TOR_DIR/torrc" &
TOR_PID=$!

# Wait for Tor to initialize
echo -e "${CYAN}⏳ Waiting for Tor circuits...${NC}"
sleep 10

# Check if hidden service was created
if [ -f "$HIDDEN_SERVICE/hostname" ]; then
    ONION_ADDRESS=$(cat "$HIDDEN_SERVICE/hostname")
    echo -e "\n${GREEN}✅ Ghost mode active!${NC}"
    echo -e "${PURPLE}🧅 Your .onion address:${NC}"
    echo -e "${GREEN}   $ONION_ADDRESS${NC}\n"
    
    # Generate beacon
    BEACON=$(python3 -c "
import hashlib, time, random
onion = '$ONION_ADDRESS'
freq = random.random()
ts = int(time.time())
hash = hashlib.sha256(f'{onion}{ts}'.encode()).hexdigest()[:8]
print(f'DMCT:{onion}:{freq:.6f}:{ts}:{hash}')
")
    
    echo -e "${CYAN}📡 Your discovery beacon:${NC}"
    echo -e "${GREEN}   $BEACON${NC}\n"
    
    echo -e "${PURPLE}Share this beacon securely to connect with others${NC}"
    echo -e "${CYAN}Remember: No logs, no traces, just trust waves${NC}\n"
    
    # Run ghost chat through Tor
    echo -e "${CYAN}🌊 Starting Ghost Chat...${NC}\n"
    cd "$HOME/dmct"
    torify python3 ghost_chat_pure.py
    
else
    echo -e "${RED}❌ Failed to create hidden service${NC}"
    kill $TOR_PID 2>/dev/null
    exit 1
fi

# Cleanup on exit
trap "kill $TOR_PID 2>/dev/null; echo -e '\n${PURPLE}Ghost mode deactivated. No traces remain.${NC}'" EXIT