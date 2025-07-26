#!/usr/bin/env python3
"""
DMCT Quickstart: Your First Trust Ripples
Run this to see the magic happen
"""

import dmct
import consensus
import time
import random

def main():
    print("""
    ·▄▄▄▄  • ▌ ▄ ·.  ▄▄· ▄▄▄▄▄    ∞ 
    ██▪ ██ ·██ ▐███▪▐█ ▌▪•██      
    ▐█· ▐█▌▐█ ▌▐▌▐█·██ ▄▄ ▐█.▪    
    ██. ██ ██ ██▌▐█▌▐███▌ ▐█▌·    
    ▀▀▀▀▀• ▀▀  █▪▀▀▀·▀▀▀  ▀▀▀     
    
    Welcome to DMCT - Let's create some trust ripples!
    """)
    
    # Create a small network
    print("🌌 Creating a trust universe with 7 founding nodes...\n")
    
    network = dmct.Network()
    nodes = []
    
    # Genesis nodes in sacred geometry
    for i in range(7):
        angle = i * 2 * 3.14159 / 7
        node = dmct.Node(
            dmct.SpacetimePoint(
                5 * math.cos(angle),
                5 * math.sin(angle),
                0
            )
        )
        network.add_node(node)
        nodes.append(node)
        print(f"✨ Node {i+1} spawned at coordinates ({node.position.x:.2f}, {node.position.y:.2f}, {node.position.z:.2f})")
    
    print("\n🌊 Initiating trust cascade...\n")
    
    # Simulate trust interactions
    for round in range(5):
        print(f"\n--- Round {round+1} ---")
        
        # Random trust emissions
        emitter = random.choice(nodes)
        wave = emitter.emit(
            amplitude=random.uniform(0.5, 2.0),
            data={
                'round': round,
                'message': random.choice([
                    'Peace', 'Unity', 'Harmony', 'Truth', 'Love'
                ])
            }
        )
        
        print(f"📡 Node emitted trust wave {wave.id}")
        print(f"   Message: {wave.data['message']}")
        print(f"   Amplitude: {wave.amplitude:.2f}")
        
        time.sleep(0.5)
    
    # Check consensus
    print("\n🔮 Checking consensus field...\n")
    
    consensus_system = consensus.SpacetimeConsensus()
    
    # Multiple nodes agree on something
    truth = "The universe is made of trust"
    positions = [(n.position.x, n.position.y, n.position.z) for n in nodes[:5]]
    
    for i, pos in enumerate(positions):
        consensus_system.submit_event(pos, truth, amplitude=1.5)
        print(f"✓ Node {i+1} declares: '{truth}'")
    
    # Check if consensus emerged
    result = consensus_system.get_consensus(truth)
    
    if result and result['confirmed']:
        print(f"\n🎉 CONSENSUS ACHIEVED!")
        print(f"   Confidence: {result['confidence']:.1%}")
        print(f"   Validators: {result['validators']}")
    elif result:
        print(f"\n🌊 Consensus emerging... ({result['confidence']:.1%})")
    else:
        print(f"\n🌊 Consensus field initializing...")
    
    # Visualize the field
    print("\n📊 Trust Field Visualization:")
    print("   (Higher density = more trust)")
    print("   " + "─" * 40)
    
    field = consensus_system.visualize_consensus_field(20)
    for row in field[::2]:  # Sample every other row
        print("   ", end="")
        for val in row[::2]:  # Sample every other column
            if val > 0.5:
                print("█", end="")
            elif val > 0:
                print("▓", end="")
            elif val > -0.5:
                print("░", end="")
            else:
                print(" ", end="")
        print()
    
    print("\n✨ Beautiful! Trust ripples create consensus naturally.")
    print("💫 No voting. No mining. Just physics.\n")
    
    # Interactive section
    print("Try it yourself:")
    print("  python3 -c \"import dmct; dmct.join()\"")
    print("  python3 -c \"import dmct; dmct.ripple('Hello Universe')\"")
    print("\nOr start the web interface:")
    print("  ./dmct start")
    print("  Open http://localhost:8888")
    print("\n🌌 Welcome to the infinite trust network!\n")

if __name__ == "__main__":
    import math  # For genesis geometry
    main()