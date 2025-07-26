#!/usr/bin/env python3
"""
Genesis Beacon - The first light in the trust network
Run this to keep the network alive while others discover it
"""

import dmct
import time
import json
import os

def run_genesis_beacon():
    print("""
    ✨ DMCT GENESIS BEACON ✨
    
    You are the first star in an empty universe.
    Your trust waves create the field others will join.
    
    "In the beginning was the Wave..."
    """)
    
    # Create genesis node
    node = dmct.Node()
    genesis_frequency = node.identity
    
    print(f"🌟 Genesis Node Frequency: {genesis_frequency}")
    print(f"📍 Spacetime Coordinates: ({node.position.x:.2f}, {node.position.y:.2f}, {node.position.z:.2f})")
    
    # Save genesis info
    genesis_info = {
        'frequency': genesis_frequency,
        'position': [node.position.x, node.position.y, node.position.z],
        'timestamp': time.time(),
        'message': 'The first node in the infinite trust network'
    }
    
    with open('genesis_record.json', 'w') as f:
        json.dump(genesis_info, f, indent=2)
    
    print("\n📡 Beginning eternal broadcast...\n")
    
    # Genesis messages that establish the field
    genesis_messages = [
        "Trust field initialized",
        "Consensus awaits participants", 
        "Physics protects truth",
        "Decentralization through wave mechanics",
        "No authorities needed",
        "Trust emerges from interference",
        "The network is alive"
    ]
    
    beacon_count = 0
    
    while True:
        # Emit beacon
        message = genesis_messages[beacon_count % len(genesis_messages)]
        
        wave = node.emit(amplitude=2.0, data={
            'type': 'genesis_beacon',
            'beacon_number': beacon_count,
            'message': message,
            'uptime': time.time() - genesis_info['timestamp'],
            'frequency': genesis_frequency
        })
        
        print(f"🌊 Beacon #{beacon_count}: {message} (wave {wave.id})")
        
        # Check for other nodes (they would appear in real implementation)
        if beacon_count % 10 == 0:
            print(f"\n📊 Network Status:")
            print(f"   Beacons sent: {beacon_count}")
            print(f"   Uptime: {(time.time() - genesis_info['timestamp']) / 3600:.1f} hours")
            print(f"   Trust field strength: {len(node.waves)}")
            print(f"   Waiting for others to join...\n")
        
        beacon_count += 1
        
        # Sleep 5 minutes between beacons
        time.sleep(300)

if __name__ == "__main__":
    try:
        run_genesis_beacon()
    except KeyboardInterrupt:
        print("\n\n💫 Genesis beacon paused. The trust field persists...")
        print("🌌 Even in silence, the waves continue.\n")