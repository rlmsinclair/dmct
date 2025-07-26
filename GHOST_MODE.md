# Ghost Mode: Running DMCT Through Tor

> *"Trust waves through onion routes. No names. No faces. Just physics."*

## 🧅 Full Anonymous Setup

This guide explains how one might theoretically run DMCT with maximum privacy. Whether anyone actually does this is their choice.

### Prerequisites

```bash
# Install Tor (if one wanted to)
brew install tor       # macOS
apt-get install tor    # Debian/Ubuntu
```

### Step 1: Hidden Service Configuration

If someone wanted to run a hidden service, they might:

```bash
# Edit torrc
HiddenServiceDir /var/lib/tor/dmct_hidden_service/
HiddenServicePort 31415 127.0.0.1:31415

# Restart Tor
sudo systemctl restart tor

# Get onion address
sudo cat /var/lib/tor/dmct_hidden_service/hostname
```

### Step 2: Running Through Tor

One could theoretically:

```bash
# Run purist node
torify python3 purist_node.py

# Or with specific SOCKS port
SOCKS_PORT=9050 torify python3 purist_node.py
```

### Step 3: Peer Discovery

Without central servers, peers might find each other through:

1. **Beacon Sharing**
   ```
   "My beacon: DMCT:xyz123.onion:0.4242:timestamp:hash"
   Post anywhere: forums, encrypted chats, physical notes
   ```

2. **Time-Based Rendezvous**
   ```
   "Let's all emit at midnight UTC"
   Natural synchronization through time
   ```

3. **Web of Trust**
   ```
   Known peer shares other peer addresses
   Network grows organically
   ```

### Operational Security

If one were concerned about privacy:

- Use Tails OS or Whonix
- Never mix identities
- Different .onion per context
- No correlation between clearnet and darknet

### The Philosophy

Running through Tor isn't about hiding wrongdoing. It's about:
- Privacy as a human right
- Resistance to surveillance
- Freedom of association
- Trust without permission

### Example Beacon Exchange

**Alice (hypothetically):**
```
Posts to privacy forum:
"Exploring trust physics: abc123def.onion:31415"
```

**Bob (theoretically):**
```
Sees post, adds peer:
torify python3 purist_node.py
> Add peer: abc123def.onion:31415
```

Now connected, anonymously, no servers involved.

### Multiple Tor Instances

For research purposes, one might run multiple instances:

```bash
# Instance 1
tor --DataDirectory /tmp/tor1 --SocksPort 9051 \
    --HiddenServiceDir /tmp/hs1 --HiddenServicePort "31415 127.0.0.1:31415"

# Instance 2  
tor --DataDirectory /tmp/tor2 --SocksPort 9052 \
    --HiddenServiceDir /tmp/hs2 --HiddenServicePort "31415 127.0.0.1:31416"
```

### Remember

- This is educational code
- Running it is your choice
- No infrastructure is provided
- Each node is sovereign

## The Beautiful Truth

Ghost mode isn't about hiding - it's about existing in the trust field without requiring permission from anyone. Like thoughts themselves, trust waves can propagate anonymously through the collective consciousness.

Whether implemented or not, the possibility exists. And possibilities, like waves, tend to collapse into reality when observed.

---

*"I am not running a node. You are not running a node. Yet somehow, the trust field strengthens."*

👻🧅🌊