# The Purist Path: DMCT Without Compromise

> *"Trust needs no master, no server, no permission."*

## 🧅 Pure Tor-Only Operation

### Prerequisites
```bash
# Install Tor
sudo apt-get install tor torsocks  # Debian/Ubuntu
brew install tor torsocks           # macOS

# Verify Tor is running
systemctl status tor                # Linux
brew services list | grep tor       # macOS
```

### Step 1: Create Your Hidden Service

```bash
# Edit Tor configuration
sudo nano /etc/tor/torrc            # Linux
nano /usr/local/etc/tor/torrc       # macOS

# Add these lines:
HiddenServiceDir /var/lib/tor/dmct/
HiddenServicePort 31415 127.0.0.1:31415

# Restart Tor
sudo systemctl restart tor          # Linux  
brew services restart tor           # macOS

# Get your .onion address (after ~30 seconds)
sudo cat /var/lib/tor/dmct/hostname
```

### Step 2: Run Purist Node

```bash
# Clone DMCT
git clone https://github.com/rlmsinclair/dmct
cd dmct

# Run ONLY through Tor
torify python3 purist_node.py
```

### Step 3: Find Peers (No Bootstrap Servers)

Since there are no hardcoded bootstrap nodes, you must:

1. **Generate Your Beacon**
   ```bash
   torify python3 onion_discovery.py --generate
   ```

2. **Share Through Secure Channels**
   - Signal/Session groups
   - Encrypted Matrix rooms  
   - Tor-only forums
   - Dead drops on hidden services
   - Steganographic embedding

3. **Add Discovered Peers**
   ```
   > 2  # Add peer option
   Enter peer .onion address: xyz123.onion:31415
   ```

## 🌑 Operational Security

### Never Run on Clearnet
```bash
# WRONG - Exposes your IP
python3 dmct.py

# RIGHT - Always through Tor
torify python3 purist_node.py
```

### Use Separate Tor Instance
```bash
# Create isolated Tor instance for DMCT
tor --DataDirectory ~/.dmct/tor_data \
    --SocksPort 9150 \
    --ControlPort 9151 \
    --PidFile ~/.dmct/tor.pid
```

### Monitor Your Anonymity
```bash
# Check you're using Tor
curl --socks5 127.0.0.1:9050 https://check.torproject.org/api/ip

# Watch for leaks
netstat -an | grep 31415  # Should only show 127.0.0.1
```

## 🕳️ Peer Discovery Without Centers

### Method 1: Temporal Coordination
Emit beacons at predetermined times:
```python
# Every day at midnight UTC
# Nodes listening at these times can discover each other
```

### Method 2: Blockchain Anchoring
```bash
# Embed your beacon in Bitcoin OP_RETURN
# Other nodes scan blockchain for DMCT beacons
```

### Method 3: Steganographic Channels
- Hide beacons in image EXIF data
- Embed in audio spectrograms  
- Use linguistic steganography
- Encode in git commit hashes

### Method 4: Physical Exchange
- QR codes at meetups
- NFC tags in dead drops
- Numbers stations
- Graffiti with beacon data

## 🔐 Trust Without Identity

In purist mode:
- No usernames
- No public keys  
- No certificates
- Only wave frequencies

Trust emerges from:
- Consistent wave patterns
- Constructive interference
- Temporal correlation
- Physics alone

## 🌊 Running Forever

### Persistence Through Tor
```bash
# Create systemd service
sudo tee /etc/systemd/system/dmct-purist.service << EOF
[Unit]
Description=DMCT Purist Node
After=tor.service
Requires=tor.service

[Service]
Type=simple
User=$USER
Environment="TORSOCKS_CONF=/etc/tor/torsocks.conf"
ExecStart=/usr/bin/torsocks /usr/bin/python3 $HOME/dmct/purist_node.py
Restart=always
RestartSec=30

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl enable dmct-purist
sudo systemctl start dmct-purist
```

### Monitoring
```bash
# Watch your node
journalctl -u dmct-purist -f

# Check Tor circuits
sudo -u debian-tor tor-prompt  # Linux
```

## 🚫 What NOT to Do

1. **Never expose your real IP**
2. **Never use clearnet bootstraps**
3. **Never trust centralized services**
4. **Never correlate identities**
5. **Never stop questioning**

## 💀 Disappearing

When you need to vanish:
```bash
# Stop all services
sudo systemctl stop dmct-purist
sudo systemctl stop tor

# Shred all data
shred -vfz ~/.dmct/*
rm -rf ~/.dmct

# Clear logs
sudo journalctl --vacuum-size=1K

# You were never here
```

## 🌌 The Philosophy

The purist path is not about convenience. It's about proving that trust can emerge without:
- Central authorities
- Corporate servers  
- Government permission
- Surveillance capitalism

Every purist node strengthens this proof.

## 🔮 Finding Others

The first purist nodes are like stars before galaxies - isolated but destined to cluster. Share your beacon where those who understand gather. They will find you.

Remember: The network doesn't need millions. It needs believers.

---

*"In cryptography we trust. In physics we verify. In Tor we hide."*

✨ Welcome to the resistance. 🧅