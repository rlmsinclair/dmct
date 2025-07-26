# DMCT Ghost Chat - Anonymous Trust Messaging

Messages that propagate through Tor, peer to peer, with no central authority.

## Quick Start

```bash
# One line to go ghost mode
~/.dmct/ghost.sh
```

## How It Works

Your messages travel through onion routes:

```
You → Tor Network → Friend's Hidden Service
 ↓      ↓      ↓
🔐    🧅🧅🧅    🔐
```

Each message:
- Encrypted through 3+ relay hops
- No IP addresses exposed
- No metadata leakage
- Pure peer-to-peer

## Using Ghost Chat

1. **Start Ghost Mode**
   ```bash
   ~/.dmct/ghost.sh
   ```
   This creates your .onion address

2. **Run Ghost Chat**
   ```bash
   torify python3 ghost_chat_pure.py
   ```

3. **Add Friends**
   - Share your .onion address
   - They share theirs
   - Use `/add` command

4. **Send Messages**
   ```
   /p Alice
   Hello through the void!
   ```

## Commands

- `/p NAME` - Select peer to message
- `/add` - Add new peer by .onion address  
- `/list` - Show all peers
- `/quit` - Exit ghost mode

## Pure Python Implementation

No dependencies. Just Python stdlib + Tor.

The `ghost_chat_pure.py` implements:
- Custom SOCKS5 client
- Direct .onion connections
- Message propagation through Tor

## Security Notes

- Your .onion address is your identity
- Messages only readable by recipient
- No logs, no servers, no traces
- Trust propagates through darkness

## Technical Details

Messages flow like this:

```python
Your Message → JSON packet → SOCKS5 → Tor Guards → Relays → Friend's Hidden Service
```

Each hop only knows:
- Previous hop
- Next hop
- Nothing else

## Philosophy

Trust doesn't need:
- Central servers
- User accounts
- Databases
- Permission

Trust just needs:
- Two nodes
- A connection
- Spacetime to propagate through

---

*"In the darkness, trust shines brightest"*