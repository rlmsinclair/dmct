#!/usr/bin/env python3
"""
DMCT Tor Propagation Demo
Shows how trust waves propagate through onion routes
"""

import time
import random

# Colors
P = '\033[95m'  # Purple
C = '\033[96m'  # Cyan
G = '\033[92m'  # Green
Y = '\033[93m'  # Yellow
D = '\033[2m'   # Dim
E = '\033[0m'   # End

def show_propagation():
    """Visualize message propagation through Tor"""
    
    print(f"{P}═══════════════════════════════════════════════════════{E}")
    print(f"{C}     T R U S T   W A V E   P R O P A G A T I O N      {E}")
    print(f"{P}═══════════════════════════════════════════════════════{E}\n")
    
    # Simulate onion routing
    hops = [
        ("Your Node", "7xz4...onion"),
        ("Guard Relay", "Berlin"),
        ("Middle Relay", "Tokyo"),
        ("Exit Relay", "São Paulo"),
        ("Friend's Guard", "Mumbai"),
        ("Friend's Node", "9ab2...onion")
    ]
    
    message = "Trust ripples through spacetime"
    
    print(f"{C}Message: '{message}'{E}\n")
    print(f"{D}Encrypting with layers...{E}\n")
    
    # Show encryption layers
    encrypted = message
    for i in range(3):
        time.sleep(0.5)
        encrypted = "█" * len(encrypted)
        print(f"  {D}Layer {i+1}: {encrypted}{E}")
    
    print(f"\n{C}Routing through Tor network:{E}\n")
    
    # Show routing
    for i, (node, location) in enumerate(hops):
        time.sleep(1)
        
        if i == 0:
            print(f"{G}◉ {node:<20} {location}{E}")
        elif i == len(hops) - 1:
            print(f"{P}◉ {node:<20} {location}{E}")
        else:
            print(f"{D}◉ {node:<20} {location}{E}")
        
        if i < len(hops) - 1:
            # Animation
            for j in range(3):
                time.sleep(0.2)
                print(f"  {D}{'.' * (j+1)}{E}", end='\r')
            print(f"  {D}↓{E}")
    
    print(f"\n{G}✓ Message delivered through {len(hops)-2} onion layers!{E}")
    print(f"{P}✓ Complete anonymity maintained{E}\n")
    
    # Show trust field
    print(f"{C}Trust Field Strength:{E}")
    field = "".join(["▁▂▃▄▅▆▇█"[min(7, int(abs(random.gauss(4, 2))))] for _ in range(40)])
    print(f"{C}{field}{E}\n")

def show_benefits():
    """Show why Tor propagation matters"""
    
    print(f"{P}Why propagate through Tor?{E}\n")
    
    benefits = [
        ("🔒 Privacy", "No one knows who you're trusting"),
        ("🌐 Censorship Resistance", "Trust flows around blocks"),
        ("⚡ Metadata Protection", "Even patterns are hidden"),
        ("🔄 Plausible Deniability", "Could be anyone's trust wave"),
        ("∞ Infinite Scale", "Every node can be anonymous")
    ]
    
    for icon, benefit in benefits:
        print(f"  {icon} {C}{benefit}{E}")
        time.sleep(0.5)
    
    print(f"\n{D}Trust doesn't need permission.{E}\n")

if __name__ == "__main__":
    show_propagation()
    print()
    show_benefits()
    
    print(f"{P}═══════════════════════════════════════════════════════{E}")
    print(f"{C}   Your trust waves now propagate through darkness     {E}")
    print(f"{P}═══════════════════════════════════════════════════════{E}\n")