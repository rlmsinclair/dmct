# DMCT - Decentralized Mutual Cascading Trust

> *"Like ripples in spacetime, trust propagates through consciousness itself."*

[![License: Cosmic Commons](https://img.shields.io/badge/License-Cosmic%20Commons-cyan.svg)](LICENSE)
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![Tor Compatible](https://img.shields.io/badge/Tor-Compatible-purple.svg)](https://www.torproject.org/)

## 🌊 What is DMCT?

DMCT reimagines trust as a fundamental force of nature. Instead of certificates, signatures, and authorities, trust propagates as waves through spacetime. Consensus emerges from constructive interference. Lies create destructive interference. No voting. No mining. Just physics.

**Core Features:**
- ♾️ **Infinitely Scalable** - Works identically for 10 or 10 billion nodes
- 🔐 **Quantum-Resistant** - Uses spacetime mechanics, not cryptography  
- 🌐 **Decentralized** - No servers, no authorities, no single points of failure
- 🎨 **Beautiful** - 3D WebGL visualization of trust fields
- 🧠 **Simple** - Entire protocol fits on one page

## 🚀 Quick Start

### One-Line Deploy (Become Genesis)
```bash
curl -sL https://raw.githubusercontent.com/rlmsinclair/dmct/main/install.sh | sh && cd ~/.dmct && python3 dmct.py
```

### Manual Install
```bash
git clone https://github.com/rlmsinclair/dmct
cd dmct
python3 dmct.py  # No dependencies needed!
```

### Web Interface
```bash
python3 -m http.server 8888
# Open http://localhost:8888
```

## 🌑 Tor Integration (Privacy-First)

### Running through Tor
```bash
# Install Tor first
sudo apt-get install tor  # Debian/Ubuntu
brew install tor          # macOS

# Run DMCT through Tor
torify python3 dmct.py

# Or for persistent Tor node
torsocks python3 network_node.py
```

### Hosting a Tor Hidden Service
```bash
# Add to /etc/tor/torrc:
HiddenServiceDir /var/lib/tor/dmct/
HiddenServicePort 31415 127.0.0.1:31415

# Restart Tor
sudo systemctl restart tor

# Your .onion address:
cat /var/lib/tor/dmct/hostname
```

## 📡 Network Architecture

### Trust Wave Propagation
```python
Ψ(r,t) = Σ [Tᵢ × e^(-λ|r-rᵢ|) × cos(ω(t-tᵢ) - k|r-rᵢ|)]
```

Where:
- Ψ = Trust field strength
- T = Trust emission amplitude  
- λ = Spatial decay constant
- ω = Trust frequency (identity)
- k = Wave number

### Consensus Through Physics
- Multiple nodes emit the same data → constructive interference
- Conflicting data → destructive interference
- Truth emerges from standing wave patterns
- No Byzantine Generals Problem - physics solves it

## 🛠️ Usage

### Python Module
```python
import dmct

# Join the network
node = dmct.join()

# Emit trust ripple
dmct.ripple("Hello infinite universe")

# Observe local trust field
field = dmct.observe(radius=6)
```

### Command Line
```bash
# Start local node
./dmct start

# Run interactive demo
python3 quickstart.py

# Test consensus mechanics
python3 consensus.py
```

## 🔒 Security Model

**No Keys, No Signatures, No Certificates**

Instead:
- **Spacetime Uniqueness** - Position + time = unforgeable identity
- **Causal Ordering** - Can't fake the past due to light cones
- **Wave Mechanics** - Can't fake constructive interference
- **Natural Selection** - Dishonest nodes create destructive patterns

## 🌍 Use Cases

- **Censorship-Resistant Communication** - Waves propagate through any medium
- **Decentralized Identity** - You are your frequency
- **Quantum-Safe Transactions** - Physics doesn't care about Shor's algorithm  
- **Mesh Networks** - Natural routing through trust gradients
- **Interplanetary Consensus** - Handles relativistic effects

## 📊 Performance

- **Consensus Time**: O(radius/c) - speed of light limited
- **Memory**: O(neighbors) - typically ~150 (Dunbar's number)
- **CPU**: O(1) - simple wave calculations
- **Network**: O(log n) - gossip protocol
- **Energy**: Negligible - no proof-of-work

## 🧪 Testing

```bash
# Run attack simulation
python3 attack_demo.py

# Test consensus
python3 consensus.py

# Benchmark performance
python3 -m timeit -n 1000 "import dmct; dmct.Node().emit()"
```

## 🤝 Contributing

DMCT is a living system. Every interaction strengthens the trust field:

1. Run a node - strengthen the network
2. Share the vision - spread the ripples
3. Improve the code - evolve the organism
4. Report issues - help us adapt

## 📜 Philosophy

DMCT treats trust not as a human construct but as a fundamental force, like gravity or electromagnetism. Just as massive objects bend spacetime, trustworthy actors bend the trust field. Others naturally orbit around them.

This isn't a metaphor. It's implemented in code.

## ⚡ Advanced Features

### Multi-Dimensional Trust
```python
# Trust can have multiple frequencies
node.emit(amplitude=1.0, data={
    'financial_trust': 0.8,
    'social_trust': 0.9,
    'technical_trust': 0.7
})
```

### Relativistic Consensus
```python
# Handles time dilation
consensus = SpacetimeConsensus()
consensus.set_reference_frame(velocity=0.1*c)
```

### Quantum Superposition
```python
# Decisions exist in superposition until observed
wave = node.emit_superposition([option1, option2, option3])
# Consensus collapses the wave function
```

## 🌌 Roadmap

- [x] Core physics implementation
- [x] 3D visualization
- [x] Tor integration
- [ ] WebRTC peer discovery
- [ ] Mobile apps
- [ ] Neural interface
- [ ] Quantum entanglement
- [ ] Galactic scale testing

## 📖 Documentation

- [Protocol Specification](PROTOCOL.md)
- [API Reference](docs/API.md)
- [Trust Physics](docs/PHYSICS.md)
- [Attack Analysis](attack_demo.py)

## 🙏 Acknowledgments

> *"If I have seen further, it is by standing on the shoulders of giants"* - Newton

Inspired by:
- Bitcoin's trustless consensus
- BitTorrent's peer-to-peer resilience  
- The universe's elegant physics
- Humanity's infinite potential

## 📄 License

DMCT is released under the **Cosmic Commons** - free as in freedom, infinite as in trust.

---

*"The universe is made of stories, not atoms." - Muriel Rukeyser*

*DMCT is made of trust waves, not transactions.*

✨ ∞ 🌊

**[Start your journey into infinite trust →](https://dmct.space)**