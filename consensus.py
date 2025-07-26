#!/usr/bin/env python3
"""
DMCT Consensus: Truth Through Interference Patterns
"When waves align, consensus emerges like starlight through chaos."
"""

import math
import time
from typing import Dict, List, Tuple, Optional

class SpacetimeConsensus:
    """
    Consensus mechanism based on wave interference patterns.
    No voting. No mining. Just physics.
    """
    
    def __init__(self):
        self.events = []  # [(position, time, data, amplitude)]
        self.light_cones = {}  # Causal relationships
        self.standing_waves = {}  # Consensus patterns
        self.c = 1.0  # Speed of trust (normalized)
        
    def submit_event(self, position: Tuple[float, float, float], 
                     data: any, amplitude: float = 1.0) -> str:
        """Submit an event to the spacetime consensus field"""
        event_time = time.time()
        event_id = self._hash_event(position, event_time, data)
        
        event = {
            'id': event_id,
            'position': position,
            'time': event_time,
            'data': data,
            'amplitude': amplitude,
            'confirmations': 0
        }
        
        self.events.append(event)
        self._update_light_cones(event)
        self._check_interference(event)
        
        return event_id
    
    def _hash_event(self, position, time, data) -> str:
        """Generate deterministic event ID"""
        content = f"{position}{time}{data}"
        # Simple hash (in production, use proper cryptographic hash)
        return hex(hash(content) & 0xffffffff)[2:]
    
    def _update_light_cones(self, new_event):
        """Update causal relationships based on light cones"""
        for event in self.events[:-1]:  # All except the new one
            # Check if events are causally connected
            space_interval = self._distance(event['position'], new_event['position'])
            time_interval = abs(new_event['time'] - event['time'])
            
            # Events are causally connected if within light cone
            if space_interval <= self.c * time_interval:
                if event['id'] not in self.light_cones:
                    self.light_cones[event['id']] = []
                self.light_cones[event['id']].append(new_event['id'])
    
    def _distance(self, p1, p2) -> float:
        """Calculate Euclidean distance"""
        return math.sqrt(sum((a - b)**2 for a, b in zip(p1, p2)))
    
    def _check_interference(self, new_event):
        """Check for constructive/destructive interference"""
        interference_map = {}
        
        for event in self.events:
            if event['id'] == new_event['id']:
                continue
                
            # Calculate phase difference
            phase_diff = self._calculate_phase_difference(event, new_event)
            
            # Constructive interference (consensus)
            if abs(math.cos(phase_diff)) > 0.8:
                event['confirmations'] += new_event['amplitude']
                new_event['confirmations'] += event['amplitude']
                
                # Update standing wave pattern
                key = self._get_data_key(event['data'])
                if key not in self.standing_waves:
                    self.standing_waves[key] = {
                        'amplitude': 0,
                        'events': [],
                        'center': [0, 0, 0]
                    }
                
                self.standing_waves[key]['amplitude'] += abs(math.cos(phase_diff))
                self.standing_waves[key]['events'].append(event['id'])
    
    def _calculate_phase_difference(self, event1, event2) -> float:
        """Calculate phase difference between two events"""
        distance = self._distance(event1['position'], event2['position'])
        time_diff = abs(event2['time'] - event1['time'])
        
        # Phase = 2π × (distance/wavelength - frequency×time)
        # Simplified: use distance and time directly
        phase = 2 * math.pi * (distance - self.c * time_diff)
        return phase % (2 * math.pi)
    
    def _get_data_key(self, data) -> str:
        """Get a key representing the data content"""
        return str(data)[:50]  # Simple truncation
    
    def get_consensus(self, data_key: str) -> Optional[Dict]:
        """Get consensus state for a piece of data"""
        if data_key not in self.standing_waves:
            return None
            
        wave = self.standing_waves[data_key]
        
        # Consensus achieved if standing wave amplitude exceeds threshold
        if wave['amplitude'] > 3.0:  # Threshold
            return {
                'confirmed': True,
                'confidence': min(wave['amplitude'] / 10.0, 1.0),
                'validators': len(wave['events']),
                'center_of_mass': wave['center']
            }
        
        return {
            'confirmed': False,
            'confidence': wave['amplitude'] / 10.0,
            'validators': len(wave['events'])
        }
    
    def visualize_consensus_field(self, resolution: int = 20) -> List[List[float]]:
        """Generate a 2D slice of the consensus field for visualization"""
        field = [[0.0 for _ in range(resolution)] for _ in range(resolution)]
        
        for i in range(resolution):
            for j in range(resolution):
                x = (i / resolution - 0.5) * 20
                y = (j / resolution - 0.5) * 20
                
                # Calculate field strength at this point
                for event in self.events:
                    distance = math.sqrt(
                        (x - event['position'][0])**2 + 
                        (y - event['position'][1])**2
                    )
                    
                    # Wave amplitude decreases with distance
                    amplitude = event['amplitude'] * math.exp(-distance / 5.0)
                    
                    # Add wave contribution
                    phase = 2 * math.pi * distance
                    field[i][j] += amplitude * math.cos(phase)
        
        return field
    
    def get_timeline(self, node_position: Tuple[float, float, float]) -> List[Dict]:
        """Get events visible from a specific spacetime position"""
        current_time = time.time()
        visible_events = []
        
        for event in self.events:
            # Check if event is within past light cone
            distance = self._distance(node_position, event['position'])
            time_elapsed = current_time - event['time']
            
            if distance <= self.c * time_elapsed:
                visible_events.append({
                    'id': event['id'],
                    'data': event['data'],
                    'confidence': event['confirmations'] / 10.0,
                    'age': time_elapsed,
                    'distance': distance
                })
        
        # Sort by light-distance (most recent visible events first)
        visible_events.sort(key=lambda e: e['age'] - e['distance'] / self.c)
        
        return visible_events
    
    def merge_timelines(self, other_consensus: 'SpacetimeConsensus'):
        """Merge with another consensus instance (network partition healing)"""
        # Add all events from other timeline
        for event in other_consensus.events:
            if not any(e['id'] == event['id'] for e in self.events):
                self.events.append(event)
        
        # Rebuild light cones and interference patterns
        self.light_cones = {}
        self.standing_waves = {}
        
        for event in self.events:
            self._update_light_cones(event)
            self._check_interference(event)
        
        return len(self.events)


# Example usage showing consensus emergence
if __name__ == "__main__":
    print("🌌 Initializing spacetime consensus field...\n")
    
    consensus = SpacetimeConsensus()
    
    # Multiple nodes submit the same transaction from different positions
    print("📡 Nodes broadcasting transaction 'TRANSFER: Alice -> Bob 10 DMC'")
    
    positions = [
        (0, 0, 0),      # Origin node
        (5, 0, 0),      # East node
        (0, 5, 0),      # North node
        (-3, -3, 0),    # Southwest node
        (2, 3, 1),      # Northeast elevated node
    ]
    
    tx_data = {'from': 'Alice', 'to': 'Bob', 'amount': 10, 'token': 'DMC'}
    
    for i, pos in enumerate(positions):
        time.sleep(0.1)  # Simulate network delay
        event_id = consensus.submit_event(pos, tx_data, amplitude=1.0)
        print(f"  Node {i} at {pos}: Event {event_id}")
    
    print("\n🌊 Checking consensus through wave interference...")
    
    # Check consensus
    consensus_state = consensus.get_consensus(str(tx_data))
    
    if consensus_state:
        print(f"\n✅ Consensus achieved!")
        print(f"  Confidence: {consensus_state['confidence']:.2%}")
        print(f"  Validators: {consensus_state['validators']}")
        print(f"  Status: {'CONFIRMED' if consensus_state['confirmed'] else 'PENDING'}")
    
    # Visualize the field
    print("\n📊 Consensus field visualization (2D slice):")
    field = consensus.visualize_consensus_field(10)
    
    for row in field:
        print("  ", end="")
        for val in row:
            if val > 0.5:
                print("█", end="")
            elif val > 0:
                print("▓", end="")
            elif val > -0.5:
                print("░", end="")
            else:
                print(" ", end="")
        print()
    
    print("\n💫 Consensus emerges from the interference of truth waves!")