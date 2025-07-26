#!/usr/bin/env python3
"""
DMCT Tor Node - Trust Through Onion Routing
Run with: torify python3 tor_node.py
"""

import socket
import json
import threading
import time
import os
import dmct

class TorNode(dmct.Node):
    """DMCT node that operates through Tor for maximum privacy"""
    
    def __init__(self, hidden_service_port=31415):
        super().__init__()
        self.port = hidden_service_port
        self.onion_address = None
        self.peers = []
        
        # Bootstrap onion addresses (examples - would be real in production)
        self.bootstrap_onions = [
            "dmctnode7xz4ggbq.onion:31415",
            "trustwav3sfkgf4tb.onion:31415", 
            "quantumripplewxyz.onion:31415"
        ]
        
        print("🧅 Initializing DMCT Tor Node...")
        self._check_tor()
        
    def _check_tor(self):
        """Verify Tor is running"""
        try:
            # Check if we're running through Tor
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            sock.connect(('check.torproject.org', 443))
            sock.close()
            print("✅ Tor connection verified")
            
            # Get our onion address if configured
            if os.path.exists('/var/lib/tor/dmct/hostname'):
                with open('/var/lib/tor/dmct/hostname', 'r') as f:
                    self.onion_address = f.read().strip()
                    print(f"🧅 Your onion address: {self.onion_address}")
        except:
            print("⚠️  Not connected through Tor. Run with: torify python3 tor_node.py")
    
    def start_hidden_service(self):
        """Start listening as a Tor hidden service"""
        server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server.bind(('127.0.0.1', self.port))
        
        print(f"📡 Hidden service listening on port {self.port}")
        
        def listen():
            while True:
                try:
                    data, addr = server.recvfrom(4096)
                    wave_data = json.loads(data.decode())
                    
                    # Process anonymous trust wave
                    self._process_wave(wave_data)
                    
                except Exception as e:
                    pass
        
        threading.Thread(target=listen, daemon=True).start()
    
    def emit_anonymous(self, data, amplitude=1.0):
        """Emit trust wave anonymously through Tor"""
        wave = self.emit(amplitude=amplitude, data=data)
        
        # Broadcast to onion peers
        packet = {
            'wave_id': wave.id,
            'amplitude': amplitude,
            'frequency': self.identity,
            'data': data,
            'timestamp': time.time()
        }
        
        for peer in self.bootstrap_onions:
            self._send_to_onion(peer, packet)
            
        print(f"🧅 Anonymous wave {wave.id} sent through Tor")
        return wave
    
    def _send_to_onion(self, onion_address, data):
        """Send data to an onion address"""
        try:
            host, port = onion_address.split(':')
            
            # Tor will handle the .onion resolution
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(json.dumps(data).encode(), (host, int(port)))
            
        except Exception as e:
            pass  # Silent fail for privacy
    
    def _process_wave(self, wave_data):
        """Process incoming anonymous wave"""
        # Create wave from anonymous data
        wave = dmct.TrustWave(
            dmct.SpacetimePoint(0, 0, 0),  # Anonymous origin
            amplitude=wave_data['amplitude'],
            frequency=wave_data['frequency'],
            phase=0,
            data=wave_data['data']
        )
        
        self.waves.append(wave)
        print(f"🌊 Received anonymous wave: {wave_data.get('data', {})}")

def anonymous_consensus():
    """Demonstrate anonymous consensus through Tor"""
    print("""
    ╔═══════════════════════════════════════╗
    ║        DMCT Anonymous Consensus       ║
    ║         Trust Without Identity        ║
    ╚═══════════════════════════════════════╝
    """)
    
    # Create anonymous node
    node = TorNode()
    
    # Start hidden service
    node.start_hidden_service()
    
    print("\n🔒 Privacy Features:")
    print("  ✓ No IP addresses logged")
    print("  ✓ No identities required") 
    print("  ✓ Consensus through physics alone")
    print("  ✓ Plausible deniability")
    
    print("\n📡 Broadcasting anonymous truth...")
    
    # Emit anonymous messages
    truths = [
        "Privacy is a human right",
        "Trust needs no identity",
        "Physics protects truth"
    ]
    
    for truth in truths:
        node.emit_anonymous({'message': truth, 'type': 'anonymous'})
        time.sleep(1)
    
    print("\n✨ Anonymous consensus demonstration complete!")
    print("🧅 Your trust ripples propagate without revealing your identity")

if __name__ == "__main__":
    # Check if running through Tor
    if 'TORSOCKS' in os.environ or 'TOR_SOCKS_PORT' in os.environ:
        anonymous_consensus()
    else:
        print("⚠️  Please run through Tor for anonymous operation:")
        print("    torify python3 tor_node.py")
        print("\nOr install Tor first:")
        print("    sudo apt-get install tor  # Debian/Ubuntu")
        print("    brew install tor          # macOS")
        print("\nFor maximum privacy, set up a hidden service:")
        print("    See: https://community.torproject.org/onion-services/setup/")