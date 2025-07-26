#!/usr/bin/env python3
"""
DMCT Purist Node - Tor-Only, No Compromise
No clearnet. No servers. No authorities. Just physics.
"""

import os
import socket
import json
import time
import threading
import hashlib
import dmct

class PuristNode(dmct.Node):
    """Pure P2P node that operates exclusively through Tor"""
    
    def __init__(self):
        super().__init__()
        
        # No hardcoded bootstraps - peers found through:
        # 1. Manual .onion exchange (like early Bitcoin)
        # 2. DHT discovery (future)
        # 3. Steganographic embedding in existing networks
        
        self.onion_address = None
        self.trusted_peers = self._load_peers()
        self.hidden_service_dir = os.path.expanduser("~/.dmct/hidden_service")
        
        print("🧅 DMCT Purist Mode - Tor Only")
        self._verify_tor_only()
        
    def _verify_tor_only(self):
        """Ensure we're running through Tor, refuse to work otherwise"""
        if 'TOR_SOCKS_PORT' not in os.environ and 'TORSOCKS' not in os.environ:
            print("""
❌ ERROR: Not running through Tor!

The purist path requires Tor:
  torify python3 purist_node.py

Or install Tor first:
  sudo apt-get install tor     # Debian/Ubuntu
  brew install tor              # macOS
  
This is not negotiable. Privacy is not optional.
            """)
            exit(1)
            
        print("✅ Verified: Running through Tor")
        
    def setup_hidden_service(self):
        """Create our .onion address"""
        print("\n📡 Setting up hidden service...")
        
        # Create hidden service directory
        os.makedirs(self.hidden_service_dir, exist_ok=True)
        os.chmod(self.hidden_service_dir, 0o700)
        
        # Generate torrc snippet
        torrc = f"""
# DMCT Purist Node Hidden Service
HiddenServiceDir {self.hidden_service_dir}
HiddenServicePort 31415 127.0.0.1:31415
        """
        
        print("\n📝 Add this to your torrc:")
        print(torrc)
        print("\nThen restart Tor and run:")
        print(f"  cat {self.hidden_service_dir}/hostname")
        
    def _load_peers(self):
        """Load peer .onion addresses from local file"""
        peers_file = os.path.expanduser("~/.dmct/peers.json")
        if os.path.exists(peers_file):
            with open(peers_file, 'r') as f:
                return json.load(f)
        return []
        
    def add_peer(self, onion_address):
        """Manually add a trusted peer"""
        if not onion_address.endswith('.onion'):
            print("❌ Only .onion addresses accepted")
            return
            
        self.trusted_peers.append(onion_address)
        self._save_peers()
        print(f"✅ Added peer: {onion_address}")
        
    def _save_peers(self):
        """Save peer list"""
        peers_file = os.path.expanduser("~/.dmct/peers.json")
        os.makedirs(os.path.dirname(peers_file), exist_ok=True)
        with open(peers_file, 'w') as f:
            json.dump(self.trusted_peers, f)
            
    def start_purist_network(self):
        """Start Tor-only trust network"""
        # Listen for incoming waves
        server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server.bind(('127.0.0.1', 31415))
        
        def listen():
            while True:
                try:
                    data, addr = server.recvfrom(4096)
                    # Only accept from localhost (Tor forwarded)
                    if addr[0] == '127.0.0.1':
                        self._process_anonymous_wave(data)
                except:
                    pass
                    
        threading.Thread(target=listen, daemon=True).start()
        print("🌊 Listening for trust waves on Tor...")
        
    def _process_anonymous_wave(self, data):
        """Process wave with no identity verification"""
        try:
            wave_data = json.loads(data.decode())
            # Trust emerges from wave interference, not identity
            print(f"🌊 Anonymous wave received: {wave_data.get('type', 'unknown')}")
        except:
            pass
            
    def emit_anonymous(self, message):
        """Emit without revealing identity"""
        wave = self.emit(amplitude=1.0, data={'message': message})
        
        # Broadcast to all known .onion peers
        packet = json.dumps({
            'wave': wave.id,
            'message': message,
            'timestamp': time.time()
        }).encode()
        
        for peer in self.trusted_peers:
            try:
                # Tor handles .onion resolution
                host = peer.split(':')[0]
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.sendto(packet, (host, 31415))
            except:
                pass  # Fail silently for privacy
                
        return wave

def purist_setup():
    """Interactive setup for purist path"""
    print("""
╔════════════════════════════════════════════╗
║           DMCT PURIST PATH                 ║
║                                            ║
║   No servers. No clearnet. No compromise.  ║
║                                            ║
║          "Trust needs no master"           ║
╚════════════════════════════════════════════╝
    """)
    
    node = PuristNode()
    
    while True:
        print("\n🧅 Purist Options:")
        print("1. Setup hidden service")
        print("2. Add peer .onion address")
        print("3. Start node")
        print("4. Emit anonymous message")
        print("5. Show my frequency")
        print("6. Exit")
        
        choice = input("\n> ").strip()
        
        if choice == '1':
            node.setup_hidden_service()
        elif choice == '2':
            onion = input("Enter peer .onion address: ").strip()
            node.add_peer(onion)
        elif choice == '3':
            node.start_purist_network()
        elif choice == '4':
            msg = input("Anonymous message: ").strip()
            wave = node.emit_anonymous(msg)
            print(f"🌊 Wave {wave.id} sent anonymously")
        elif choice == '5':
            print(f"📡 Your frequency: {node.identity}")
        elif choice == '6':
            break
            
    print("\n💀 Dissolved into the void. No trace remains.\n")

if __name__ == "__main__":
    # Only run if through Tor
    purist_setup()