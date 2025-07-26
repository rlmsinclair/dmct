#!/usr/bin/env python3
"""
DMCT Ghost Chat - Real Tor Message Propagation
Messages actually travel through onion routes
"""

import os
import sys
import time
import json
import socket
import threading
import readline
from datetime import datetime

# ANSI colors for beauty
class Colors:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    WHITE = '\033[97m'
    DIM = '\033[2m'
    BOLD = '\033[1m'
    END = '\033[0m'

def clear_screen():
    os.system('clear' if os.name != 'nt' else 'cls')

class GhostChat:
    def __init__(self):
        self.port = 31415
        self.peers = {}
        self.messages = []
        self.running = True
        self.server_thread = None
        
        # Generate anonymous identity
        import random
        import hashlib
        self.my_id = hashlib.sha256(str(random.random()).encode()).hexdigest()[:8]
        adjectives = ['Silent', 'Shadow', 'Mystic', 'Cosmic', 'Quantum', 'Crystal']
        nouns = ['Wave', 'Echo', 'Signal', 'Pulse', 'Ripple', 'Phantom']
        self.my_name = f"{random.choice(adjectives)}{random.choice(nouns)}"
        
        # Storage
        self.data_dir = os.path.expanduser("~/.dmct/ghost_chat")
        os.makedirs(self.data_dir, exist_ok=True)
        self.load_peers()
        
    def print_header(self):
        """Beautiful header"""
        clear_screen()
        print(f"{Colors.PURPLE}╔═══════════════════════════════════════════════════════╗")
        print(f"║{Colors.CYAN}           ▄████  ██░ ██  ▒█████    ██████ ▄▄▄█████▓  {Colors.PURPLE}║")
        print(f"║{Colors.CYAN}          ██▒ ▀█▒▓██░ ██▒▒██▒  ██▒▒██    ▒ ▓  ██▒ ▓▒ {Colors.PURPLE}║")
        print(f"║{Colors.CYAN}         ▒██░▄▄▄░▒██▀▀██░▒██░  ██▒░ ▓██▄   ▒ ▓██░ ▒░ {Colors.PURPLE}║")
        print(f"║                                                       ║")
        print(f"║{Colors.WHITE}         R E A L   T O R   M E S S A G I N G          {Colors.PURPLE}║")
        print(f"╚═══════════════════════════════════════════════════════╝{Colors.END}\n")
        
    def start_server(self):
        """Start listening for messages on local port"""
        def serve():
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server.bind(('127.0.0.1', self.port))
            server.listen(5)
            
            while self.running:
                try:
                    server.settimeout(1.0)
                    client, addr = server.accept()
                    threading.Thread(target=self.handle_message, args=(client,)).start()
                except socket.timeout:
                    continue
                except:
                    break
                    
            server.close()
            
        self.server_thread = threading.Thread(target=serve, daemon=True)
        self.server_thread.start()
        print(f"{Colors.GREEN}✓ Listening on port {self.port}{Colors.END}")
        
    def handle_message(self, client):
        """Handle incoming message through Tor"""
        try:
            data = client.recv(4096)
            if data:
                msg = json.loads(data.decode())
                
                # Add to messages
                self.messages.append(msg)
                
                # Display notification
                print(f"\n{Colors.PURPLE}◉ {msg['from']}: {msg['text']}{Colors.END}")
                print(f"{Colors.CYAN}> {Colors.WHITE}", end='', flush=True)
                
                # Send acknowledgment
                client.send(b"ACK")
                
        except Exception as e:
            pass
        finally:
            client.close()
            
    def send_message(self, peer_onion, text):
        """Send message through Tor to peer"""
        try:
            # Message packet
            msg = {
                'from': self.my_name,
                'text': text,
                'time': datetime.now().strftime("%H:%M"),
                'id': self.my_id
            }
            
            # Connect through Tor SOCKS proxy
            import socks
            
            # Create socket that goes through Tor
            s = socks.socksocket()
            s.setproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
            
            # Connect to .onion address
            print(f"{Colors.DIM}Connecting through Tor...{Colors.END}")
            s.connect((peer_onion, self.port))
            
            # Send message
            s.send(json.dumps(msg).encode())
            
            # Wait for ACK
            response = s.recv(1024)
            if response == b"ACK":
                print(f"{Colors.GREEN}✓ Message delivered through onion route{Colors.END}")
            
            s.close()
            return True
            
        except Exception as e:
            print(f"{Colors.RED}✗ Failed to send: {str(e)}{Colors.END}")
            return False
            
    def get_onion_address(self):
        """Get local .onion address"""
        onion_file = os.path.expanduser("~/.dmct/tor/hidden_service/hostname")
        if os.path.exists(onion_file):
            with open(onion_file, 'r') as f:
                return f.read().strip()
        return None
        
    def add_peer(self):
        """Add a peer's .onion address"""
        print(f"\n{Colors.CYAN}Enter peer's .onion address:{Colors.END}")
        onion = input(f"{Colors.WHITE}> {Colors.END}").strip()
        
        if '.onion' in onion:
            print(f"{Colors.CYAN}Give this peer a name:{Colors.END}")
            name = input(f"{Colors.WHITE}> {Colors.END}").strip() or f"Ghost_{onion[:6]}"
            
            self.peers[name] = onion
            self.save_peers()
            
            print(f"{Colors.GREEN}✓ Added {name} ({onion}){Colors.END}")
            
            # Test connection
            print(f"{Colors.DIM}Testing connection...{Colors.END}")
            if self.send_message(onion, f"Hello from {self.my_name}!"):
                print(f"{Colors.GREEN}✓ Connection successful!{Colors.END}")
        else:
            print(f"{Colors.RED}Invalid .onion address{Colors.END}")
            
    def chat_loop(self):
        """Main chat interface"""
        self.print_header()
        
        # Show connection info
        my_onion = self.get_onion_address()
        if my_onion:
            print(f"{Colors.PURPLE}Your address: {Colors.GREEN}{my_onion}{Colors.END}")
        print(f"{Colors.PURPLE}Your name: {Colors.CYAN}{self.my_name}{Colors.END}")
        print(f"{Colors.PURPLE}Peers: {Colors.CYAN}{len(self.peers)}{Colors.END}\n")
        
        # Start server
        self.start_server()
        
        print(f"{Colors.DIM}Commands: /peer <name> | /add | /list | /clear | /quit{Colors.END}\n")
        
        current_peer = None
        
        while self.running:
            try:
                # Input prompt
                prompt = f"{Colors.CYAN}[{current_peer or 'no peer'}]> {Colors.WHITE}"
                message = input(prompt)
                
                if message.startswith('/'):
                    # Handle commands
                    parts = message.split()
                    cmd = parts[0]
                    
                    if cmd == '/peer' and len(parts) > 1:
                        peer_name = parts[1]
                        if peer_name in self.peers:
                            current_peer = peer_name
                            print(f"{Colors.GREEN}✓ Now chatting with {peer_name}{Colors.END}")
                        else:
                            print(f"{Colors.RED}Unknown peer. Use /list to see peers.{Colors.END}")
                            
                    elif cmd == '/add':
                        self.add_peer()
                        
                    elif cmd == '/list':
                        if self.peers:
                            print(f"\n{Colors.CYAN}Peers:{Colors.END}")
                            for name, onion in self.peers.items():
                                print(f"  {Colors.PURPLE}{name}{Colors.DIM} - {onion}{Colors.END}")
                        else:
                            print(f"{Colors.DIM}No peers yet. Use /add{Colors.END}")
                            
                    elif cmd == '/clear':
                        self.print_header()
                        
                    elif cmd == '/quit':
                        break
                        
                    else:
                        print(f"{Colors.DIM}Commands: /peer <name> | /add | /list | /clear | /quit{Colors.END}")
                        
                elif message.strip() and current_peer:
                    # Send message to current peer
                    peer_onion = self.peers[current_peer]
                    self.send_message(peer_onion, message)
                    
                elif message.strip():
                    print(f"{Colors.YELLOW}Select a peer first with /peer <name>{Colors.END}")
                    
            except KeyboardInterrupt:
                break
                
        print(f"\n{Colors.PURPLE}Dissolving into the void...{Colors.END}")
        self.running = False
        
    def save_peers(self):
        """Save peers to file"""
        with open(os.path.join(self.data_dir, 'peers.json'), 'w') as f:
            json.dump(self.peers, f)
            
    def load_peers(self):
        """Load saved peers"""
        peer_file = os.path.join(self.data_dir, 'peers.json')
        if os.path.exists(peer_file):
            with open(peer_file, 'r') as f:
                self.peers = json.load(f)

def check_dependencies():
    """Check if required dependencies are available"""
    try:
        import socks
    except ImportError:
        print(f"{Colors.RED}Missing required dependency: PySocks{Colors.END}")
        print(f"{Colors.CYAN}Install with: pip3 install PySocks{Colors.END}")
        print(f"{Colors.DIM}Or: pip3 install requests[socks]{Colors.END}")
        return False
        
    # Check if Tor is running
    try:
        test_sock = socket.socket()
        test_sock.connect(('127.0.0.1', 9050))
        test_sock.close()
    except:
        print(f"{Colors.RED}Tor is not running on port 9050{Colors.END}")
        print(f"{Colors.CYAN}Start ghost mode first: ~/.dmct/ghost.sh{Colors.END}")
        return False
        
    return True

def main():
    # Check if we have what we need
    if not check_dependencies():
        sys.exit(1)
        
    # Check if running through Tor (optional but recommended)
    if 'TORSOCKS' not in os.environ:
        print(f"{Colors.YELLOW}⚠ Not running through torify (your IP may be visible){Colors.END}")
        print(f"{Colors.CYAN}Recommended: torify python3 ghost_chat.py{Colors.END}")
        print(f"{Colors.DIM}Press Enter to continue anyway...{Colors.END}")
        input()
        
    # Run chat
    chat = GhostChat()
    chat.chat_loop()

if __name__ == "__main__":
    main()