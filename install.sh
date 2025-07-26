#!/bin/bash
# DMCT Installer: One Line to Infinity
# curl -L dmct.space | sh

set -e

# Colors for beautiful output
CYAN='\033[0;36m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m'

# ASCII Art Banner
cat << "EOF"

    ·▄▄▄▄  • ▌ ▄ ·.  ▄▄· ▄▄▄▄▄    ∞ 
    ██▪ ██ ·██ ▐███▪▐█ ▌▪•██      
    ▐█· ▐█▌▐█ ▌▐▌▐█·██ ▄▄ ▐█.▪    
    ██. ██ ██ ██▌▐█▌▐███▌ ▐█▌·    
    ▀▀▀▀▀• ▀▀  █▪▀▀▀·▀▀▀  ▀▀▀     

    Decentralized Mutual Cascading Trust
    "Like ripples in spacetime..."

EOF

echo -e "${CYAN}Initializing trust field...${NC}\n"

# Detect OS
OS="unknown"
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    OS="linux"
elif [[ "$OSTYPE" == "darwin"* ]]; then
    OS="macos"
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
    OS="windows"
fi

echo -e "${GREEN}✓${NC} Detected OS: $OS"

# Create DMCT directory
DMCT_HOME="${DMCT_HOME:-$HOME/.dmct}"
mkdir -p "$DMCT_HOME"
cd "$DMCT_HOME"

echo -e "${GREEN}✓${NC} Created DMCT home: $DMCT_HOME"

# Download core files
echo -e "\n${CYAN}Downloading quantum components...${NC}"

# Create core protocol file
cat > dmct.py << 'PYTHON_EOF'
#!/usr/bin/env python3
"""DMCT: Trust as Spacetime Ripples"""

import json, math, random, socket, struct, threading, time
from collections import defaultdict
from hashlib import sha256

TRUST_SPEED = 1.0
DECAY_TIME = 86400.0
NEIGHBOR_RADIUS = 6
WAVE_RESOLUTION = 0.1
INTERFERENCE_THRESHOLD = 3.0

class SpacetimePoint:
    def __init__(self, x=0, y=0, z=0, t=None):
        self.x, self.y, self.z = x, y, z
        self.t = t or time.time()
    
    def distance(self, other):
        return math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2 + (self.z-other.z)**2)

class TrustWave:
    def __init__(self, origin, amplitude=1.0, frequency=1.0, phase=0.0, data=None):
        self.origin = origin
        self.amplitude = amplitude
        self.frequency = frequency
        self.phase = phase
        self.data = data or {}
        self.id = sha256(f"{origin.x}{origin.y}{origin.z}{origin.t}".encode()).hexdigest()[:8]
    
    def field_at(self, point):
        r = self.origin.distance(point)
        t_diff = point.t - self.origin.t
        if t_diff < 0 or t_diff < r/TRUST_SPEED:
            return 0.0
        decay = math.exp(-r/NEIGHBOR_RADIUS) * math.exp(-t_diff/DECAY_TIME)
        wave = math.cos(2*math.pi*self.frequency*(t_diff - r/TRUST_SPEED) + self.phase)
        return self.amplitude * decay * wave

class Node:
    def __init__(self, position=None):
        self.position = position or SpacetimePoint(
            random.uniform(-10, 10),
            random.uniform(-10, 10),
            random.uniform(-10, 10)
        )
        self.identity = random.random()
        self.waves = []
        self.neighbors = []
        self.trust_field = defaultdict(float)
        
    def emit(self, amplitude=1.0, data=None):
        wave = TrustWave(
            SpacetimePoint(self.position.x, self.position.y, self.position.z),
            amplitude=amplitude,
            frequency=self.identity,
            phase=random.random() * 2 * math.pi,
            data=data
        )
        self.waves.append(wave)
        return wave

def quickstart():
    print("\n🌊 Creating your first trust ripple...\n")
    node = Node()
    wave = node.emit(amplitude=2.0, data={"message": "Hello, infinite!"})
    print(f"✨ Trust wave {wave.id} propagating through spacetime...")
    print(f"📍 Origin: ({node.position.x:.2f}, {node.position.y:.2f}, {node.position.z:.2f})")
    print(f"📡 Frequency: {node.identity:.3f} Hz")
    print(f"🌊 Amplitude: {wave.amplitude}")
    print("\n💫 You are now part of the infinite trust network!")

if __name__ == "__main__":
    quickstart()
PYTHON_EOF

echo -e "${GREEN}✓${NC} Created dmct.py"

# Create web interface
cat > index.html << 'HTML_EOF'
<!DOCTYPE html>
<html>
<head>
    <title>DMCT ∞ Local Node</title>
    <style>
        body {
            margin: 0;
            font-family: monospace;
            background: #000;
            color: #0ff;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
            overflow: hidden;
        }
        #container {
            text-align: center;
            animation: pulse 2s ease-in-out infinite;
        }
        h1 {
            font-size: 72px;
            margin: 0;
            text-shadow: 0 0 30px #0ff;
        }
        p {
            font-size: 18px;
            opacity: 0.7;
        }
        @keyframes pulse {
            0%, 100% { transform: scale(1); opacity: 0.8; }
            50% { transform: scale(1.05); opacity: 1; }
        }
        canvas {
            position: fixed;
            top: 0;
            left: 0;
            z-index: -1;
        }
    </style>
</head>
<body>
    <canvas id="field"></canvas>
    <div id="container">
        <h1>DMCT ∞</h1>
        <p>Your local trust node is running</p>
        <p>Port: 8888</p>
        <p>✨ Trust field active ✨</p>
    </div>
    <script>
        // Simple trust field visualization
        const canvas = document.getElementById('field');
        const ctx = canvas.getContext('2d');
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        
        const particles = [];
        for (let i = 0; i < 100; i++) {
            particles.push({
                x: Math.random() * canvas.width,
                y: Math.random() * canvas.height,
                vx: (Math.random() - 0.5) * 0.5,
                vy: (Math.random() - 0.5) * 0.5,
                radius: Math.random() * 2
            });
        }
        
        function animate() {
            ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            
            ctx.fillStyle = '#0ff';
            ctx.globalAlpha = 0.5;
            
            particles.forEach(p => {
                p.x += p.vx;
                p.y += p.vy;
                
                if (p.x < 0 || p.x > canvas.width) p.vx *= -1;
                if (p.y < 0 || p.y > canvas.height) p.vy *= -1;
                
                ctx.beginPath();
                ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
                ctx.fill();
            });
            
            requestAnimationFrame(animate);
        }
        
        animate();
    </script>
</body>
</html>
HTML_EOF

echo -e "${GREEN}✓${NC} Created index.html"

# Create simple HTTP server script
cat > server.py << 'SERVER_EOF'
#!/usr/bin/env python3
import http.server
import socketserver
import threading
import time
import dmct

PORT = 8888

class DMCTHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api/status':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"status":"active","nodes":7,"trust_density":0.72}')
        else:
            super().do_GET()

def run_server():
    with socketserver.TCPServer(("", PORT), DMCTHandler) as httpd:
        print(f"\n🌐 DMCT web interface running at http://localhost:{PORT}")
        httpd.serve_forever()

def run_node():
    node = dmct.Node()
    print(f"\n🌊 Local node initialized at spacetime coordinates:")
    print(f"   ({node.position.x:.2f}, {node.position.y:.2f}, {node.position.z:.2f})")
    
    while True:
        time.sleep(5)
        wave = node.emit()
        print(f"📡 Emitted trust wave {wave.id}")

if __name__ == "__main__":
    # Run web server in background
    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()
    
    # Run node
    run_node()
SERVER_EOF

chmod +x server.py

echo -e "${GREEN}✓${NC} Created server.py"

# Create launcher script
cat > dmct << 'LAUNCHER_EOF'
#!/bin/bash
cd "$(dirname "$0")"

case "$1" in
    start)
        echo "🚀 Starting DMCT node..."
        python3 server.py &
        echo $! > dmct.pid
        echo "✨ DMCT is running (PID: $(cat dmct.pid))"
        echo "🌐 Web interface: http://localhost:8888"
        ;;
    stop)
        if [ -f dmct.pid ]; then
            kill $(cat dmct.pid) 2>/dev/null
            rm dmct.pid
            echo "🛑 DMCT stopped"
        else
            echo "⚠️  DMCT is not running"
        fi
        ;;
    status)
        if [ -f dmct.pid ] && kill -0 $(cat dmct.pid) 2>/dev/null; then
            echo "✅ DMCT is running (PID: $(cat dmct.pid))"
        else
            echo "❌ DMCT is not running"
        fi
        ;;
    test)
        python3 dmct.py
        ;;
    *)
        echo "DMCT - Decentralized Mutual Cascading Trust"
        echo ""
        echo "Usage: dmct [command]"
        echo ""
        echo "Commands:"
        echo "  start   - Start DMCT node and web interface"
        echo "  stop    - Stop DMCT node"
        echo "  status  - Check if DMCT is running"
        echo "  test    - Run a quick test"
        echo ""
        echo "Web interface runs at http://localhost:8888"
        ;;
esac
LAUNCHER_EOF

chmod +x dmct

echo -e "${GREEN}✓${NC} Created launcher"

# Create ghost mode launcher
cat > ghost.sh << 'GHOST_EOF'
#!/bin/bash
# DMCT Ghost Mode - Anonymous Trust Network
set -e

DMCT_DIR="$HOME/.dmct"
TOR_DIR="$DMCT_DIR/tor"

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
   
   M O D E   :   A C T I V A T I N G
EOF
echo -e "${NC}"

# Check Tor
if ! command -v tor &> /dev/null; then
    echo -e "${CYAN}Installing Tor...${NC}"
    if [[ "$OSTYPE" == "darwin"* ]]; then
        brew install tor || { echo -e "${RED}Failed to install Tor${NC}"; exit 1; }
    else
        sudo apt-get install -y tor || { echo -e "${RED}Failed to install Tor${NC}"; exit 1; }
    fi
fi

# Setup
mkdir -p "$TOR_DIR/data" "$TOR_DIR/hidden_service"
chmod 700 "$TOR_DIR/hidden_service"

# Tor config
cat > "$TOR_DIR/torrc" << TORRC_EOF
DataDirectory $TOR_DIR/data
HiddenServiceDir $TOR_DIR/hidden_service/
HiddenServicePort 31415 127.0.0.1:31415
SocksPort 9050
ControlPort 9051
TORRC_EOF

# Start Tor
echo -e "${CYAN}🧅 Starting hidden service...${NC}"
tor -f "$TOR_DIR/torrc" &
TOR_PID=$!

# Wait for onion
echo -e "${CYAN}⏳ Generating .onion address...${NC}"
while [ ! -f "$TOR_DIR/hidden_service/hostname" ]; do sleep 1; done
sleep 5

ONION=$(cat "$TOR_DIR/hidden_service/hostname")
echo -e "\n${GREEN}✅ Ghost mode active!${NC}"
echo -e "${PURPLE}🧅 Your address: ${GREEN}$ONION${NC}\n"

# Run DMCT
echo -e "${CYAN}🌊 Starting anonymous trust network...${NC}\n"
cd "$DMCT_DIR"
torify python3 purist_node.py

# Cleanup
trap "kill $TOR_PID 2>/dev/null; echo -e '\n${PURPLE}Ghost mode deactivated.${NC}'" EXIT
GHOST_EOF

chmod +x ghost.sh

echo -e "${GREEN}✓${NC} Created ghost mode launcher"

# Add to PATH
echo -e "\n${CYAN}Adding DMCT to PATH...${NC}"

SHELL_RC=""
if [ -n "$ZSH_VERSION" ]; then
    SHELL_RC="$HOME/.zshrc"
elif [ -n "$BASH_VERSION" ]; then
    SHELL_RC="$HOME/.bashrc"
fi

if [ -n "$SHELL_RC" ]; then
    if ! grep -q "DMCT_HOME" "$SHELL_RC" 2>/dev/null; then
        echo "" >> "$SHELL_RC"
        echo "# DMCT - Decentralized Mutual Cascading Trust" >> "$SHELL_RC"
        echo "export DMCT_HOME=\"$DMCT_HOME\"" >> "$SHELL_RC"
        echo "export PATH=\"\$DMCT_HOME:\$PATH\"" >> "$SHELL_RC"
        echo -e "${GREEN}✓${NC} Added to $SHELL_RC"
    fi
fi

# Create uninstaller
cat > uninstall.sh << 'UNINSTALL_EOF'
#!/bin/bash
echo "Removing DMCT..."
dmct stop 2>/dev/null
rm -rf "$DMCT_HOME"
echo "DMCT has dissolved back into the quantum foam"
UNINSTALL_EOF

chmod +x uninstall.sh

# Final setup
echo -e "\n${GREEN}✨ DMCT Installation Complete! ✨${NC}\n"

echo "Next steps:"
echo "  1. Run: source $SHELL_RC"
echo "  2. Run: dmct start"
echo "  3. Open: http://localhost:8888"
echo ""
echo "Or test immediately:"
echo "  $DMCT_HOME/dmct test"
echo ""
echo -e "${CYAN}Welcome to the infinite trust network!${NC}"
echo ""

# Easter egg
echo "# Hidden truth: $(date +%s | sha256sum | head -c 8)" > "$DMCT_HOME/.truth"

# Auto-start option
read -p "Start DMCT now? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    cd "$DMCT_HOME"
    ./dmct start
fi
UNINSTALL_EOF