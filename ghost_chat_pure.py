#!/usr/bin/env python3
"""
DMCT Ghost Chat - Pure Python Tor Implementation
No external dependencies - messages propagate through Tor
"""

import os
import sys
import time
import json
import socket
import struct
import threading
import subprocess
from datetime import datetime

# ANSI colors
class C:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    WHITE = '\033[97m'
    DIM = '\033[2m'
    END = '\033[0m'

def clear():
    os.system('clear' if os.name != 'nt' else 'cls')

class TorSocket:
    """Pure Python SOCKS5 implementation for Tor"""
    
    def __init__(self, proxy_host='127.0.0.1', proxy_port=9050):
        self.proxy = (proxy_host, proxy_port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def connect(self, dest_host, dest_port):
        """Connect through Tor to destination"""
        # Connect to Tor proxy
        self.sock.connect(self.proxy)
        
        # SOCKS5 handshake
        # Send: Version(5) + NumMethods(1) + Method(0=No Auth)
        self.sock.send(b'\x05\x01\x00')
        
        # Receive: Version(5) + Method(0)
        resp = self.sock.recv(2)
        if resp != b'\x05\x00':
            raise Exception("SOCKS5 handshake failed")
            
        # Connection request
        # Version(5) + Command(1=Connect) + Reserved(0) + AddrType(3=Domain)
        addr_bytes = dest_host.encode()
        addr_len = len(addr_bytes)
        
        req = b'\x05\x01\x00\x03' + struct.pack('B', addr_len) + addr_bytes + struct.pack('>H', dest_port)
        self.sock.send(req)
        
        # Response
        resp = self.sock.recv(10)
        if resp[1] != 0:
            error_codes = {
                1: "General failure",
                2: "Connection not allowed",
                3: "Network unreachable",
                4: "Host unreachable",
                5: "Connection refused"
            }
            raise Exception(f"SOCKS5 error: {error_codes.get(resp[1], 'Unknown')}")
            
        # Connected!
        return True
        
    def send(self, data):
        return self.sock.send(data)
        
    def recv(self, size):
        return self.sock.recv(size)
        
    def close(self):
        self.sock.close()

class GhostChat:
    def __init__(self):
        self.port = 31415
        self.peers = {}
        self.running = True
        
        # Generate identity
        import random
        import hashlib
        self.id = hashlib.sha256(str(time.time()).encode()).hexdigest()[:8]
        adj = ['Silent', 'Shadow', 'Quantum', 'Crystal', 'Mystic', 'Cosmic']
        noun = ['Wave', 'Echo', 'Signal', 'Pulse', 'Ghost', 'Phantom']
        self.name = f"{random.choice(adj)}{random.choice(noun)}"
        
        # Storage
        self.data_dir = os.path.expanduser("~/.dmct/ghost_chat")
        os.makedirs(self.data_dir, exist_ok=True)
        
        # Load peers
        self.load_peers()
        
    def header(self):
        """Print beautiful header"""
        clear()
        print(f"{C.PURPLE}╔═══════════════════════════════════════════════╗")
        print(f"║  {C.CYAN}G H O S T   C H A T   :   T O R   M O D E{C.PURPLE}  ║")
        print(f"╚═══════════════════════════════════════════════╝{C.END}\n")
        
    def get_onion(self):
        """Get our .onion address"""
        hostname_file = os.path.expanduser("~/.dmct/tor/hidden_service/hostname")
        if os.path.exists(hostname_file):
            with open(hostname_file, 'r') as f:
                return f.read().strip()
        return None
        
    def start_server(self):
        """Listen for incoming messages"""
        def serve():
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server.bind(('127.0.0.1', self.port))
            server.listen(5)
            
            while self.running:
                try:
                    server.settimeout(1.0)
                    client, _ = server.accept()
                    threading.Thread(target=self.handle_msg, args=(client,)).start()
                except socket.timeout:
                    continue
                except:
                    break
                    
        threading.Thread(target=serve, daemon=True).start()
        
    def handle_msg(self, client):
        """Handle incoming message"""
        try:
            data = client.recv(4096)
            if data:
                msg = json.loads(data.decode())
                print(f"\n{C.PURPLE}◉ {msg['from']}: {msg['text']}{C.END}")
                print(f"{C.CYAN}> {C.WHITE}", end='', flush=True)
                client.send(b"OK")
        except:
            pass
        finally:
            client.close()
            
    def send_msg(self, onion, text):
        """Send message through Tor"""
        try:
            msg = {
                'from': self.name,
                'text': text,
                'time': datetime.now().strftime("%H:%M")
            }
            
            # Connect through Tor
            tor_sock = TorSocket()
            print(f"{C.DIM}Routing through Tor...{C.END}")
            
            tor_sock.connect(onion, self.port)
            tor_sock.send(json.dumps(msg).encode())
            
            # Wait for acknowledgment
            if tor_sock.recv(1024) == b"OK":
                print(f"{C.GREEN}✓ Delivered via onion route{C.END}")
            
            tor_sock.close()
            return True
            
        except Exception as e:
            print(f"{C.RED}✗ Failed: {str(e)}{C.END}")
            return False
            
    def add_peer(self):
        """Add new peer"""
        print(f"\n{C.CYAN}Peer's .onion address:{C.END}")
        onion = input(f"{C.WHITE}> {C.END}").strip()
        
        if '.onion' in onion:
            print(f"{C.CYAN}Name for this peer:{C.END}")
            name = input(f"{C.WHITE}> {C.END}").strip() or f"Ghost_{onion[:6]}"
            
            self.peers[name] = onion
            self.save_peers()
            
            print(f"{C.GREEN}✓ Added {name}{C.END}")
            
            # Test connection
            print(f"{C.DIM}Testing connection...{C.END}")
            if self.send_msg(onion, f"Hello from {self.name}!"):
                print(f"{C.GREEN}✓ Connected successfully!{C.END}")
                
    def chat(self):
        """Main chat loop"""
        self.header()
        
        # Show info
        my_onion = self.get_onion()
        if my_onion:
            print(f"{C.PURPLE}Your .onion: {C.GREEN}{my_onion}{C.END}")
        print(f"{C.PURPLE}Your name: {C.CYAN}{self.name}{C.END}")
        print(f"{C.PURPLE}Peers: {C.CYAN}{len(self.peers)}{C.END}\n")
        
        # Start server
        self.start_server()
        print(f"{C.GREEN}✓ Listening on port {self.port}{C.END}")
        
        print(f"\n{C.DIM}Commands: /p NAME | /add | /list | /quit{C.END}\n")
        
        current = None
        
        while self.running:
            try:
                # Prompt
                prompt = f"{C.CYAN}[{current or 'select peer'}]> {C.WHITE}"
                msg = input(prompt)
                
                if msg.startswith('/'):
                    parts = msg.split()
                    cmd = parts[0]
                    
                    if cmd == '/p' and len(parts) > 1:
                        name = parts[1]
                        if name in self.peers:
                            current = name
                            print(f"{C.GREEN}✓ Chatting with {name}{C.END}")
                        else:
                            print(f"{C.RED}Unknown peer{C.END}")
                            
                    elif cmd == '/add':
                        self.add_peer()
                        
                    elif cmd == '/list':
                        if self.peers:
                            print(f"\n{C.CYAN}Peers:{C.END}")
                            for name, onion in self.peers.items():
                                print(f"  {C.PURPLE}{name} {C.DIM}- {onion}{C.END}")
                        else:
                            print(f"{C.DIM}No peers yet{C.END}")
                            
                    elif cmd == '/quit':
                        break
                        
                elif msg.strip() and current:
                    # Send to current peer
                    self.send_msg(self.peers[current], msg)
                    
                elif msg.strip():
                    print(f"{C.YELLOW}Select peer first: /p NAME{C.END}")
                    
            except KeyboardInterrupt:
                break
                
        print(f"\n{C.PURPLE}Fading into darkness...{C.END}\n")
        self.running = False
        
    def save_peers(self):
        with open(os.path.join(self.data_dir, 'peers.json'), 'w') as f:
            json.dump(self.peers, f)
            
    def load_peers(self):
        peer_file = os.path.join(self.data_dir, 'peers.json')
        if os.path.exists(peer_file):
            with open(peer_file, 'r') as f:
                self.peers = json.load(f)

def check_tor():
    """Verify Tor is running"""
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect(('127.0.0.1', 9050))
        s.close()
        return True
    except:
        return False

def main():
    # Check Tor
    if not check_tor():
        print(f"{C.RED}Tor is not running!{C.END}")
        print(f"{C.CYAN}Start ghost mode first:{C.END}")
        print(f"{C.WHITE}~/.dmct/ghost.sh{C.END}")
        sys.exit(1)
        
    # Check if torified
    if 'TORSOCKS' not in os.environ:
        print(f"{C.YELLOW}⚠ Not running through torify{C.END}")
        print(f"{C.DIM}Your connection to Tor may be visible{C.END}")
        print(f"\n{C.CYAN}Recommended:{C.END}")
        print(f"{C.WHITE}torify python3 ghost_chat_pure.py{C.END}")
        print(f"\n{C.DIM}Press Enter to continue...{C.END}")
        input()
        
    # Run
    chat = GhostChat()
    chat.chat()

if __name__ == "__main__":
    main()