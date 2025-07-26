#!/usr/bin/env python3
"""
DMCT Onion Discovery - Finding Peers Without Centers
Like spores in the wind, trust finds its way
"""

import hashlib
import time
import base64

class OnionDiscovery:
    """Distributed peer discovery through creative channels"""
    
    @staticmethod
    def generate_discovery_beacon(onion_address, frequency):
        """Create a beacon that can be shared anywhere"""
        beacon = f"DMCT:{onion_address}:{frequency}:{int(time.time())}"
        checksum = hashlib.sha256(beacon.encode()).hexdigest()[:8]
        
        return f"🌊 {beacon}:{checksum}"
    
    @staticmethod
    def decode_beacon(beacon_string):
        """Decode a peer beacon"""
        try:
            # Remove emoji and whitespace
            clean = beacon_string.strip().replace("🌊", "").strip()
            parts = clean.split(':')
            
            if len(parts) != 5 or parts[0] != 'DMCT':
                return None
                
            # Verify checksum
            beacon_part = ':'.join(parts[:4])
            checksum = hashlib.sha256(beacon_part.encode()).hexdigest()[:8]
            
            if checksum == parts[4]:
                return {
                    'onion': parts[1],
                    'frequency': float(parts[2]),
                    'timestamp': int(parts[3])
                }
        except:
            pass
        return None
    
    @staticmethod
    def create_steganographic_message(onion_address):
        """Hide onion address in innocent-looking text"""
        # Split onion into words using a wordlist
        encoded = base64.b32encode(onion_address.encode()).decode()
        
        # Poetry that contains the address
        poem = f"""
        Waves ripple through spacetime's foam,
        {encoded[:8]} echoes find their home.
        Trust needs no central throne,
        {encoded[8:16]} travels alone.
        In darkness, photons gleam,
        {encoded[16:24]} builds the dream.
        Physics guards what's true,
        {encoded[24:]} waits for you.
        """
        
        return poem
    
    @staticmethod 
    def extract_from_stego(poem):
        """Extract onion from steganographic message"""
        import re
        
        # Find all base32-looking strings
        matches = re.findall(r'[A-Z2-7]{8}', poem)
        if len(matches) >= 4:
            try:
                combined = ''.join(matches[:4])
                decoded = base64.b32decode(combined + '====')  # Padding
                return decoded.decode()
            except:
                pass
        return None

def discovery_methods():
    """Ways to share your .onion without centralization"""
    
    print("""
╔═══════════════════════════════════════════════════╗
║         DMCT DISTRIBUTED DISCOVERY                ║
║                                                   ║
║   "Like mycelium, we connect underground"        ║
╚═══════════════════════════════════════════════════╝

🌐 Discovery Methods (No Central Authority):

1. BEACON SHARING
   Post your beacon in:
   - Encrypted messaging apps
   - Steganographic images  
   - Comment sections using ROT13
   - Git commit messages
   - DNS TXT records
   
2. DEAD DROP LOCATIONS  
   - Tor-only pastebins
   - Hidden wiki pages
   - Encrypted IPFS objects
   - Blockchain OP_RETURN data
   
3. TEMPORAL COORDINATION
   - Emit beacons at specific times
   - Monitor known frequencies
   - Use astronomical events as sync
   
4. SOCIAL GRAPHS
   - Web of trust introduction
   - PGP signed peer lists
   - Cryptographic commitments
   
5. SIDE CHANNELS
   - Embed in legitimate traffic
   - Use existing P2P networks
   - Steganographic carriers

Remember: The harder it is to find peers, 
the harder it is to stop the network.
    """)

def generate_onion_beacon():
    """Interactive beacon generator"""
    discovery = OnionDiscovery()
    
    print("\n🧅 Generate Your Discovery Beacon\n")
    
    onion = input("Your .onion address: ").strip()
    if not onion.endswith('.onion'):
        print("❌ Must be a .onion address")
        return
        
    import dmct
    node = dmct.Node()
    frequency = node.identity
    
    # Generate beacon
    beacon = discovery.generate_discovery_beacon(onion, frequency)
    
    print(f"\n📡 Your beacon:\n{beacon}")
    print("\n🔐 Steganographic version:")
    print(discovery.create_steganographic_message(onion))
    
    print("\n📋 Share this beacon through secure channels")
    print("Others can decode it to find you")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == '--generate':
        generate_onion_beacon()
    else:
        discovery_methods()