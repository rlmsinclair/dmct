# Genesis Guide: Starting the Trust Network

As the first node, you're not waiting for others - you're creating the conditions for trust to emerge.

## Your Role as Genesis Node

### 1. **Keep Your Node Running**
```bash
# Start persistent node
nohup python3 network_node.py > dmct.log 2>&1 &

# Or with systemd service (Linux)
sudo tee /etc/systemd/system/dmct.service << EOF
[Unit]
Description=DMCT Trust Node
After=network.target

[Service]
Type=simple
User=$USER
WorkingDirectory=$HOME/dmct
ExecStart=/usr/bin/python3 $HOME/dmct/network_node.py
Restart=always

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl enable dmct
sudo systemctl start dmct
```

### 2. **Emit Regular Trust Pulses**
Even alone, your waves create the field:
```python
# genesis_beacon.py
import dmct
import time

node = dmct.Node()
while True:
    node.emit(amplitude=1.0, data={
        'type': 'genesis_beacon',
        'message': 'Trust field active',
        'timestamp': time.time()
    })
    time.sleep(300)  # Every 5 minutes
```

### 3. **Document Your Frequency**
Your node's frequency becomes historically significant:
```bash
python3 -c "import dmct; n = dmct.Node(); print(f'Genesis frequency: {n.identity}')"
```
Add this to bootstrap.json

### 4. **Spread the Ripples** (Without Spam)

**Technical Communities:**
- Hacker News: Share the physics, not the project
- Reddit r/crypto, r/darknet: Focus on Tor integration
- IRC/Matrix: ##dmct channel
- Mastodon/Nostr: Decentralized platforms understand

**The Pitch:**
"What if trust worked like gravity - a fundamental force rather than a computation? DMCT implements consensus through wave interference. No mining, no voting, just physics."

### 5. **Create Seed Content**
```bash
# Generate interesting trust patterns
python3 << EOF
import dmct
import json

# Create philosophical trust waves
truths = [
    "Trust is discovered, not computed",
    "Consensus emerges from interference",
    "Every node strengthens the field",
    "Physics protects truth"
]

node = dmct.Node()
for truth in truths:
    wave = node.emit(amplitude=1.0, data={'philosophy': truth})
    print(f"Wave {wave.id}: {truth}")
EOF
```

### 6. **Bridge to Existing Networks**

Create bridges to where people already are:
- Nostr relay that converts notes to trust waves
- Mastodon bot that visualizes the trust field
- Discord/IRC bot that shows network status

### 7. **The First Week**

Day 1-2: You alone, creating the field
Day 3-4: First curious nodes join
Day 5-6: Small clusters form
Day 7: First natural consensus emerges

## Remember

You're not recruiting users - you're creating a field that naturally attracts those who resonate with it. Like Bitcoin's genesis block, your early waves will be studied by future historians of decentralized trust.

The network doesn't need marketing. It needs existence. By running continuously and emitting regular pulses, you create the standing waves that others will discover and join.

**Your Historical Genesis Command:**
```bash
echo "$(date): First trust wave in the infinite network" >> genesis.log
python3 dmct.py
```

Welcome to Day Zero. The trust field begins with you.

✨ 🌊 ∞