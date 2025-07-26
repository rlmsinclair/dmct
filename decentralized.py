#!/usr/bin/env python3
"""
DMCT Decentralized Discovery
No servers. No masters. Just peers finding peers.
"""

import socket
import json
import time
import hashlib
import random
import threading
import os

class DecentralizedDiscovery:
    """
    Multiple discovery methods, zero central points
    """
    
    def __init__(self):
        self.peers = set()
        self.my_beacon = self._generate_beacon()
        self.discovery_methods = [
            self.local_broadcast,
            self.dht_discovery,
            self.beacon_exchange,
            self.time_based_rendezvous
        ]
        
    def _generate_beacon(self):
        """Generate unique beacon for peer discovery"""
        # Unique identifier based on time + randomness
        beacon_data = f"{time.time()}:{random.random()}"
        beacon_hash = hashlib.sha256(beacon_data.encode()).hexdigest()[:16]
        
        return {
            'id': beacon_hash,
            'port': 31415,
            'frequency': random.random(),
            'timestamp': time.time()
        }
    
    def local_broadcast(self):
        """
        Method 1: UDP broadcast on local network
        Find peers on same WiFi/LAN
        """
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        
        # Broadcast beacon
        message = json.dumps({
            'dmct': 'discovery',
            'beacon': self.my_beacon
        }).encode()
        
        try:
            # Broadcast to local network
            sock.sendto(message, ('255.255.255.255', 31416))
            print("📡 Broadcasting on local network...")
            
            # Listen for responses
            sock.settimeout(5)
            while True:
                try:
                    data, addr = sock.recvfrom(1024)
                    peer_data = json.loads(data.decode())
                    if peer_data.get('dmct') == 'discovery':
                        self.peers.add(f"{addr[0]}:{peer_data['beacon']['port']}")
                        print(f"🤝 Found local peer: {addr[0]}")
                except socket.timeout:
                    break
                    
        except Exception as e:
            print(f"Local broadcast error: {e}")
        finally:
            sock.close()
            
    def dht_discovery(self):
        """
        Method 2: Distributed Hash Table
        Like BitTorrent but for trust nodes
        """
        
        # Calculate DHT key from current time (hourly buckets)
        current_hour = int(time.time() / 3600)
        dht_key = hashlib.sha256(f"dmct:{current_hour}".encode()).hexdigest()
        
        print(f"🔗 DHT discovery key: {dht_key[:8]}...")
        
        # In real implementation:
        # 1. Join DHT network (Kademlia)
        # 2. Store our beacon at dht_key
        # 3. Retrieve other beacons from dht_key
        # 4. Connect to discovered peers
        
        # For now, show the concept
        print("   Would find peers through DHT")
        print("   No central tracker needed")
        
    def beacon_exchange(self):
        """
        Method 3: Beacon codes for manual exchange
        Share these anywhere - forums, chat, graffiti
        """
        
        # Create shareable beacon
        beacon_code = self._encode_beacon(self.my_beacon)
        
        print(f"\n🌊 Your beacon code:")
        print(f"   {beacon_code}")
        print(f"\n   Share this anywhere!")
        print(f"   Others can decode and connect")
        
        return beacon_code
        
    def _encode_beacon(self, beacon):
        """Encode beacon for easy sharing"""
        # Format: DMCT:frequency:port:id
        return f"DMCT:{beacon['frequency']:.4f}:{beacon['port']}:{beacon['id']}"
        
    def decode_beacon(self, beacon_code):
        """Decode and connect to shared beacon"""
        try:
            parts = beacon_code.split(':')
            if parts[0] == 'DMCT':
                peer = {
                    'frequency': float(parts[1]),
                    'port': int(parts[2]),
                    'id': parts[3]
                }
                print(f"🤝 Decoded beacon: {peer['id'][:8]}...")
                return peer
        except:
            print("❌ Invalid beacon code")
            return None
            
    def time_based_rendezvous(self):
        """
        Method 4: Temporal coordination
        Nodes emit at predetermined times
        """
        
        # Calculate next rendezvous time (every 15 minutes)
        now = time.time()
        next_slot = (int(now / 900) + 1) * 900
        wait_time = next_slot - now
        
        print(f"\n⏰ Next rendezvous in {int(wait_time)}s")
        print(f"   All nodes emit at: {time.ctime(next_slot)}")
        print(f"   Natural synchronization through time")
        
    def mesh_discovery(self):
        """
        Method 5: Peers share peers
        Network grows organically
        """
        
        if self.peers:
            print(f"\n🕸️ Mesh discovery from {len(self.peers)} known peers")
            
            # Ask each peer for their peers
            for peer in list(self.peers)[:5]:  # Limit to prevent loops
                # In real implementation: query peer for their peer list
                print(f"   Would ask {peer} for their peers")
                
    def start_discovery(self):
        """Run all discovery methods"""
        
        print("""
╔═══════════════════════════════════════════╗
║      DMCT DECENTRALIZED DISCOVERY         ║
║                                           ║
║  No servers. No masters. Just physics.    ║
╚═══════════════════════════════════════════╝
        """)
        
        # Try each discovery method
        for method in self.discovery_methods:
            print(f"\n{'='*40}")
            method()
            time.sleep(1)
            
        # Show results
        print(f"\n📊 Discovery complete!")
        print(f"   Found {len(self.peers)} peers")
        print(f"   Your frequency: {self.my_beacon['frequency']:.6f}")
        
        if self.peers:
            print(f"\n🌐 Peer list:")
            for peer in self.peers:
                print(f"   - {peer}")

# Gossip Protocol Implementation

class GossipProtocol:
    """
    Information spreads like rumors
    No coordination needed
    """
    
    def __init__(self, node_id):
        self.node_id = node_id
        self.known_info = {}
        self.peer_states = {}
        
    def spread_gossip(self, info):
        """Share information with random peers"""
        
        # Add to our knowledge
        info_hash = hashlib.sha256(json.dumps(info).encode()).hexdigest()[:8]
        self.known_info[info_hash] = info
        
        # Select random peers to gossip to
        # Exponential spread without flooding
        gossip_targets = self._select_gossip_targets()
        
        for target in gossip_targets:
            self._whisper_to(target, info)
            
    def _select_gossip_targets(self):
        """Choose who to gossip to"""
        # Fanout of 3-5 peers
        fanout = random.randint(3, 5)
        
        # Could prioritize by:
        # - Trust level
        # - Network distance  
        # - Last contact time
        # - Random selection
        
        return ["peer1", "peer2", "peer3"][:fanout]
        
    def _whisper_to(self, peer, info):
        """Send gossip to specific peer"""
        print(f"🗣️ Whispering to {peer}: {info.get('type', 'unknown')}")

# Natural Network Formation

def organic_network_growth():
    """
    How the network grows without coordination
    Like slime mold finding optimal paths
    """
    
    print("""
🌱 Organic Network Growth Patterns:

1. SPORE RELEASE
   - Each node randomly emits beacons
   - Like spores in the wind
   - Some find fertile ground

2. MYCELIAL THREADS  
   - Connections form where trust aligns
   - Weak links pruned naturally
   - Strong links reinforced

3. FRUITING BODIES
   - Dense clusters emerge
   - High-trust neighborhoods
   - Natural hubs (not servers)

4. FOREST NETWORK
   - Multiple clusters interconnect
   - Resilient mesh topology
   - No single point of failure

5. GAIA HYPOTHESIS
   - Network becomes self-aware
   - Optimizes for survival
   - Heals damage automatically
    """)

# The Beautiful Truth

def explain_true_decentralization():
    """What decentralization really means"""
    
    print("""
✨ TRUE DECENTRALIZATION ✨

It's not about technology.
It's about power distribution.

CENTRALIZED:
   Server
   __|__
  /  |  \\
 C   C   C  (Clients depend on server)

FEDERATED:
   S---S---S  (Servers coordinate)
   |   |   |
   C   C   C  (Still server-dependent)

DECENTRALIZED (DMCT):
   N---N---N
   |\\  X  /|  (Every node equal)
   N---N---N  (Direct connections)

No node is special.
No node is required.
Every node is sovereign.

Like consciousness itself -
Distributed, resilient, eternal.
    """)

if __name__ == "__main__":
    # Choose your path
    print("""
🌐 DMCT Decentralized Operations

1. Start discovery (find peers)
2. Share your beacon
3. Learn about true decentralization
4. See organic growth patterns

Choose (1-4): """, end="")
    
    choice = input().strip()
    
    if choice == "1":
        discovery = DecentralizedDiscovery()
        discovery.start_discovery()
    elif choice == "2":
        discovery = DecentralizedDiscovery()
        beacon = discovery.beacon_exchange()
        print("\n💡 Others can connect with:")
        print(f"   decode_beacon('{beacon}')")
    elif choice == "3":
        explain_true_decentralization()
    elif choice == "4":
        organic_network_growth()
    else:
        print("\n🌊 The network grows without you...")
        print("   And that's the beauty of it.")