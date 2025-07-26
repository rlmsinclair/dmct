#!/usr/bin/env python3
"""
DMCT Messaging: Trust-Based Communication
Messages propagate as waves. Privacy through physics.
"""

import dmct
import time
import json
import os
from datetime import datetime

class TrustMessenger:
    """
    Messaging without servers.
    Only those in resonance can read.
    """
    
    def __init__(self, identity=None):
        self.node = dmct.Node()
        self.identity = identity or f"user_{self.node.identity:.6f}"
        self.message_dir = os.path.expanduser("~/.dmct/messages")
        os.makedirs(self.message_dir, exist_ok=True)
        
        # Message history stored as waves
        self.wave_history = []
        self.conversations = {}
        
    def send(self, message, to=None, frequency=None):
        """
        Send message as trust wave.
        If 'to' specified, tune to their frequency.
        """
        
        # Tune to recipient's frequency if specified
        if frequency:
            # Create harmonic resonance with target
            self.node.identity = frequency
        
        # Create message wave
        wave = self.node.emit(
            amplitude=1.0,
            data={
                'type': 'message',
                'from': self.identity,
                'to': to or 'all',
                'message': message,
                'timestamp': time.time(),
                'frequency': self.node.identity
            }
        )
        
        # Store locally (in real network, this propagates)
        self._store_wave(wave)
        
        print(f"🌊 Message sent as wave {wave.id[:8]}...")
        
        if to:
            print(f"📡 Tuned to {to}'s frequency: {frequency:.6f}")
        else:
            print(f"📢 Broadcasting on frequency: {self.node.identity:.6f}")
            
        return wave
    
    def receive(self, frequency_range=0.1):
        """
        Listen for messages near your frequency.
        Only resonant messages will be clear.
        """
        
        print(f"\n👂 Listening on {self.node.identity:.6f} ± {frequency_range}")
        print("Messages in your trust field:\n")
        
        messages = self._scan_field(frequency_range)
        
        for msg in messages:
            self._display_message(msg)
            
        return messages
    
    def _scan_field(self, range_width):
        """Scan local trust field for messages"""
        
        messages = []
        
        # In real implementation, this would scan actual waves
        # For now, read from local storage
        wave_files = os.listdir(self.message_dir)
        
        for wave_file in sorted(wave_files, reverse=True)[:20]:
            with open(os.path.join(self.message_dir, wave_file), 'r') as f:
                wave_data = json.load(f)
                
            # Check if frequency is in range (resonance)
            freq_diff = abs(wave_data['data']['frequency'] - self.node.identity)
            
            if freq_diff <= range_width:
                # Calculate clarity based on frequency match
                clarity = 1.0 - (freq_diff / range_width)
                wave_data['clarity'] = clarity
                messages.append(wave_data)
                
        return messages
    
    def _display_message(self, wave_data):
        """Display message with clarity based on frequency match"""
        
        data = wave_data['data']
        clarity = wave_data.get('clarity', 1.0)
        
        # Time formatting
        timestamp = datetime.fromtimestamp(data['timestamp'])
        time_str = timestamp.strftime("%H:%M")
        
        # Clarity affects readability
        if clarity > 0.9:
            # Perfect resonance - crystal clear
            print(f"[{time_str}] {data['from']}: {data['message']}")
        elif clarity > 0.7:
            # Good resonance - mostly clear
            message = data['message']
            fuzzy = ''.join(c if i % 3 != 0 else '·' for i, c in enumerate(message))
            print(f"[{time_str}] {data['from']}: {fuzzy}")
        elif clarity > 0.5:
            # Weak resonance - partially readable
            message = data['message']
            fuzzy = ''.join(c if i % 2 == 0 else '·' for i, c in enumerate(message))
            print(f"[{time_str}] {data['from'][:3]}···: {fuzzy}")
        else:
            # Poor resonance - mostly static
            static = '·' * len(data['message'])
            print(f"[··:··] ·····: {static}")
            
    def _store_wave(self, wave):
        """Store wave locally (simulating propagation)"""
        
        wave_file = os.path.join(self.message_dir, f"{wave.id}.json")
        
        wave_data = {
            'id': wave.id,
            'amplitude': wave.amplitude,
            'frequency': wave.frequency,
            'phase': wave.phase,
            'data': wave.data,
            'origin': {
                'x': wave.origin.x,
                'y': wave.origin.y,
                'z': wave.origin.z,
                't': wave.origin.t
            }
        }
        
        with open(wave_file, 'w') as f:
            json.dump(wave_data, f)
            
    def tune_to(self, user_or_frequency):
        """Tune your frequency to match another user"""
        
        if isinstance(user_or_frequency, (int, float)):
            self.node.identity = float(user_or_frequency)
        else:
            # In real system, lookup user's frequency
            print(f"🔍 Searching trust field for {user_or_frequency}...")
            
        print(f"📻 Tuned to frequency: {self.node.identity:.6f}")
        
    def start_conversation(self, with_user=None):
        """Interactive messaging session"""
        
        print(f"""
╔═══════════════════════════════════════════╗
║          DMCT Trust Messenger             ║
║                                           ║
║  Messages travel as waves through trust   ║
║  Only resonant beings can understand      ║
╚═══════════════════════════════════════════╝

Your identity: {self.identity}
Your frequency: {self.node.identity:.6f}

Commands:
  /freq <number>  - Change frequency
  /to <user>      - Direct message
  /all           - Broadcast to all
  /scan          - Scan for messages
  /quit          - Exit

Start typing to send waves...
        """)
        
        recipient = with_user
        
        while True:
            try:
                message = input(f"\n[{self.identity}] > ").strip()
                
                if message.startswith('/quit'):
                    break
                elif message.startswith('/freq '):
                    freq = float(message.split()[1])
                    self.tune_to(freq)
                elif message.startswith('/to '):
                    recipient = message.split()[1]
                    print(f"📡 Now sending to: {recipient}")
                elif message.startswith('/all'):
                    recipient = None
                    print(f"📢 Now broadcasting to all")
                elif message.startswith('/scan'):
                    self.receive()
                elif message:
                    self.send(message, to=recipient)
                    
            except KeyboardInterrupt:
                break
                
        print("\n🌊 Dissolving back into the trust field...\n")

# Convenience functions

def chat(with_user=None):
    """Start a trust-based chat"""
    messenger = TrustMessenger()
    messenger.start_conversation(with_user)

def broadcast(message):
    """Broadcast a message to all frequencies"""
    messenger = TrustMessenger()
    messenger.send(message, to=None)
    
def listen(frequency=None):
    """Listen for messages on a frequency"""
    messenger = TrustMessenger()
    if frequency:
        messenger.tune_to(frequency)
    messenger.receive()

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "chat" and len(sys.argv) > 2:
            chat(sys.argv[2])
        elif command == "broadcast" and len(sys.argv) > 2:
            broadcast(' '.join(sys.argv[2:]))
        elif command == "listen":
            freq = float(sys.argv[2]) if len(sys.argv) > 2 else None
            listen(freq)
        else:
            print("Usage: messaging.py [chat|broadcast|listen] [args]")
    else:
        # Default: start chat
        chat()