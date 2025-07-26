#!/usr/bin/env python3
"""
DMCT: Decentralized Mutual Cascading Trust
"Like ripples in spacetime, trust propagates through consciousness itself."
"""

import json
import math
import random
import socket
import struct
import threading
import time
from collections import defaultdict
from hashlib import sha256

# Universal Constants
TRUST_SPEED = 1.0
DECAY_TIME = 86400.0
NEIGHBOR_RADIUS = 6
WAVE_RESOLUTION = 0.1
INTERFERENCE_THRESHOLD = 3.0
LIGHT_SPEED = 299792458.0

class SpacetimePoint:
    def __init__(self, x=0, y=0, z=0, t=None):
        self.x, self.y, self.z = x, y, z
        self.t = t or time.time()
    
    def distance(self, other):
        return math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2 + (self.z-other.z)**2)
    
    def interval(self, other):
        space = self.distance(other)
        time_diff = abs(self.t - other.t)
        return math.sqrt(time_diff**2 - (space/LIGHT_SPEED)**2) if time_diff > space/LIGHT_SPEED else 0

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
    def __init__(self, position=None, identity=None):
        self.position = position or SpacetimePoint(
            random.uniform(-10, 10),
            random.uniform(-10, 10),
            random.uniform(-10, 10)
        )
        self.identity = identity or random.random()
        self.waves = []
        self.neighbors = []
        self.trust_field = defaultdict(float)
        self.running = True
        
    def emit(self, amplitude=1.0, data=None):
        wave = TrustWave(
            SpacetimePoint(self.position.x, self.position.y, self.position.z),
            amplitude=amplitude,
            frequency=self.identity,
            phase=random.random() * 2 * math.pi,
            data=data
        )
        self.waves.append(wave)
        self._propagate(wave)
        return wave
    
    def observe(self, radius=NEIGHBOR_RADIUS):
        field = {}
        current_time = time.time()
        
        for neighbor in self.neighbors:
            if self.position.distance(neighbor.position) <= radius:
                field[neighbor.identity] = self._calculate_field(neighbor, current_time)
        
        return field
    
    def _calculate_field(self, source, t):
        total = 0.0
        point = SpacetimePoint(self.position.x, self.position.y, self.position.z, t)
        
        for wave in source.waves:
            total += wave.field_at(point)
        
        return total
    
    def _propagate(self, wave):
        for neighbor in self.neighbors:
            if neighbor != self:
                threading.Thread(target=neighbor._receive_wave, args=(wave,)).start()
    
    def _receive_wave(self, wave):
        self.waves.append(wave)
        
        current_field = self._calculate_field(self, time.time())
        if abs(current_field) > INTERFERENCE_THRESHOLD * self._local_average():
            self._cascade(wave)
    
    def _cascade(self, original_wave):
        new_wave = self.emit(
            amplitude=original_wave.amplitude * 0.8,
            data={**original_wave.data, 'cascaded_from': original_wave.id}
        )
    
    def _local_average(self):
        if not self.trust_field:
            return 1.0
        return sum(abs(v) for v in self.trust_field.values()) / len(self.trust_field)
    
    def connect(self, other):
        if other not in self.neighbors:
            self.neighbors.append(other)
            other.neighbors.append(self)

class Network:
    def __init__(self):
        self.nodes = []
        self.epoch = time.time()
        
    def add_node(self, node):
        self.nodes.append(node)
        
        # Connect to nearby nodes
        for other in self.nodes:
            if other != node and node.position.distance(other.position) < NEIGHBOR_RADIUS * 2:
                node.connect(other)
        
        # Announcement ripple
        node.emit(amplitude=2.0, data={'type': 'join', 'epoch': self.epoch})
        
    def visualize(self):
        state = {
            'nodes': [],
            'waves': [],
            'time': time.time() - self.epoch
        }
        
        for node in self.nodes:
            state['nodes'].append({
                'id': node.identity,
                'position': [node.position.x, node.position.y, node.position.z],
                'field': sum(node.trust_field.values()),
                'neighbors': len(node.neighbors)
            })
            
            for wave in node.waves[-10:]:  # Last 10 waves
                state['waves'].append({
                    'origin': [wave.origin.x, wave.origin.y, wave.origin.z],
                    'amplitude': wave.amplitude,
                    'age': time.time() - wave.origin.t
                })
        
        return state

def genesis():
    """Birth of a trust universe"""
    network = Network()
    
    # Create founding nodes in a beautiful pattern
    for i in range(7):  # Seven, a perfect number
        angle = i * 2 * math.pi / 7
        node = Node(SpacetimePoint(
            5 * math.cos(angle),
            5 * math.sin(angle),
            0
        ))
        network.add_node(node)
    
    # The first trust ripple
    network.nodes[0].emit(amplitude=3.0, data={
        'type': 'genesis',
        'message': 'Let there be trust'
    })
    
    return network

def simulate(network, duration=60):
    """Watch trust evolve"""
    start = time.time()
    
    while time.time() - start < duration:
        # Random trust emissions
        if random.random() < 0.1:
            node = random.choice(network.nodes)
            node.emit(amplitude=random.uniform(0.5, 2.0))
        
        # Occasional new nodes
        if random.random() < 0.02:
            network.add_node(Node())
        
        time.sleep(WAVE_RESOLUTION)
        
        # Print network state
        state = network.visualize()
        total_trust = sum(n['field'] for n in state['nodes'])
        print(f"\rTime: {state['time']:.1f}s | Nodes: {len(state['nodes'])} | Trust: {total_trust:.2f}", end="")

if __name__ == "__main__":
    print("DMCT: Initializing trust field...")
    print("✨ Creating genesis nodes...")
    
    network = genesis()
    
    print("\n🌊 Trust ripples beginning...\n")
    
    try:
        simulate(network)
    except KeyboardInterrupt:
        print("\n\n💫 Trust field stabilized. Network persists in quantum foam.")