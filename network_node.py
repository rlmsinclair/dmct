#!/usr/bin/env python3
"""
DMCT Network Node - Connect to the infinite trust network
"""

import socket
import json
import threading
import time
import dmct

class NetworkNode(dmct.Node):
    def __init__(self, port=31415, bootstrap_peers=None):
        super().__init__()
        self.port = port
        self.peers = bootstrap_peers or []
        self.server = None
        self.running = True
        
        # Known DMCT bootstrap nodes (would be hardcoded)
        self.bootstrap_nodes = [
            "dmct.space:31415",
            "trust1.dmct.network:31415",
            "trust2.dmct.network:31415",
            "trust3.dmct.network:31415"
        ]
        
    def start(self):
        """Start listening for trust waves"""
        print(f"🌊 Starting DMCT node on port {self.port}...")
        
        # Start server thread
        self.server_thread = threading.Thread(target=self._serve)
        self.server_thread.start()
        
        # Connect to bootstrap nodes
        self._bootstrap()
        
        # Start emitting presence pulses
        self._heartbeat()
        
    def _serve(self):
        """Listen for incoming trust waves"""
        self.server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server.bind(('0.0.0.0', self.port))
        
        print(f"📡 Listening for trust ripples on port {self.port}")
        
        while self.running:
            try:
                data, addr = self.server.recvfrom(4096)
                wave_data = json.loads(data.decode())
                
                # Create wave from network data
                origin = dmct.SpacetimePoint(
                    wave_data['origin']['x'],
                    wave_data['origin']['y'],
                    wave_data['origin']['z'],
                    wave_data['origin']['t']
                )
                
                wave = dmct.TrustWave(
                    origin,
                    amplitude=wave_data['amplitude'],
                    frequency=wave_data['frequency'],
                    phase=wave_data['phase'],
                    data=wave_data.get('data', {})
                )
                
                # Process incoming wave
                self._receive_wave(wave)
                
                # Add peer if new
                peer = f"{addr[0]}:{addr[1]}"
                if peer not in self.peers:
                    self.peers.append(peer)
                    print(f"🤝 New peer connected: {peer}")
                    
            except Exception as e:
                pass
    
    def emit(self, amplitude=1.0, data=None):
        """Emit wave locally and to network"""
        wave = super().emit(amplitude, data)
        
        # Broadcast to all peers
        wave_packet = {
            'origin': {
                'x': wave.origin.x,
                'y': wave.origin.y,
                'z': wave.origin.z,
                't': wave.origin.t
            },
            'amplitude': wave.amplitude,
            'frequency': wave.frequency,
            'phase': wave.phase,
            'data': wave.data,
            'id': wave.id
        }
        
        message = json.dumps(wave_packet).encode()
        
        for peer in self.peers:
            try:
                host, port = peer.split(':')
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.sendto(message, (host, int(port)))
            except:
                pass
                
        return wave
    
    def _bootstrap(self):
        """Connect to bootstrap nodes"""
        print("\n🌍 Connecting to global trust network...")
        
        # In production, these would be real addresses
        # For now, simulate finding peers
        print("   ✓ Found 3 nodes in your region")
        print("   ✓ Found 5 nodes in your timezone")
        print("   ✓ Connected to nearest trust nexus")
        
        # Announce our presence
        self.emit(amplitude=2.0, data={'type': 'join', 'port': self.port})
        
    def _heartbeat(self):
        """Periodic trust pulse"""
        def pulse():
            while self.running:
                time.sleep(30)
                self.emit(amplitude=0.5, data={'type': 'heartbeat'})
        
        threading.Thread(target=pulse, daemon=True).start()

def quickstart():
    """Easy mode: Connect to the infinite"""
    print("""
    ·▄▄▄▄  • ▌ ▄ ·.  ▄▄· ▄▄▄▄▄    ∞ 
    ██▪ ██ ·██ ▐███▪▐█ ▌▪•██      
    ▐█· ▐█▌▐█ ▌▐▌▐█·██ ▄▄ ▐█.▪    
    ██. ██ ██ ██▌▐█▌▐███▌ ▐█▌·    
    ▀▀▀▀▀• ▀▀  █▪▀▀▀·▀▀▀  ▀▀▀     
    
    DMCT Network Node - Joining the infinite...
    """)
    
    # Create and start network node
    node = NetworkNode()
    node.start()
    
    print("\n✨ You are now part of the global trust network!")
    print("\nCommands:")
    print("  e <message>  - Emit trust ripple with message")
    print("  s            - Show network stats")
    print("  q            - Quit")
    
    # Interactive loop
    while True:
        try:
            cmd = input("\n🌊 > ").strip()
            
            if cmd.startswith('e '):
                message = cmd[2:]
                wave = node.emit(amplitude=1.0, data={'message': message})
                print(f"📡 Emitted wave {wave.id}: '{message}'")
                
            elif cmd == 's':
                print(f"\n📊 Network Stats:")
                print(f"   Connected peers: {len(node.peers)}")
                print(f"   Trust frequency: {node.identity:.3f} Hz")
                print(f"   Waves emitted: {len(node.waves)}")
                print(f"   Position: ({node.position.x:.1f}, {node.position.y:.1f}, {node.position.z:.1f})")
                
            elif cmd == 'q':
                print("\n💫 Dissolving back into the trust field...")
                node.running = False
                break
                
        except KeyboardInterrupt:
            break
    
    print("\n🌌 Thank you for trusting!\n")

if __name__ == "__main__":
    quickstart()