# DMCT Ghost Mode - Instant Anonymous Messaging

## The Ultimate One-Liners

### 🐳 Docker (Works on ANY OS - Windows, Mac, Linux)

**IMPORTANT: Copy and paste as ONE LINE**

```bash
docker run -it --rm ubuntu:22.04 bash -c "apt-get update -qq && apt-get install -y -qq curl python3 tor torsocks >/dev/null 2>&1 && curl -sL https://raw.githubusercontent.com/rlmsinclair/dmct/main/install.sh | sh && ~/.dmct/ghost.sh"
```

### 🖥️ Native Install (Mac/Linux)
```bash
curl -sL https://raw.githubusercontent.com/rlmsinclair/dmct/main/install.sh | sh && (command -v tor >/dev/null || ([ "$(uname)" = "Darwin" ] && brew install tor || sudo apt-get install -y tor)) && (command -v torsocks >/dev/null || ([ "$(uname)" = "Darwin" ] && brew install torsocks || sudo apt-get install -y torsocks)) && ~/.dmct/ghost.sh
```

## What It Does

1. **Downloads and installs DMCT** if not present
2. **Installs Tor** if not present (macOS/Linux)
3. **Installs torsocks** if not present 
4. **Starts ghost mode** with hidden service
5. **Launches anonymous chat** interface

## Even Shorter (if DMCT is installed)

```bash
~/.dmct/ghost.sh
```

## Kill and Restart

```bash
pkill -f "tor.*dmct|ghost" 2>/dev/null; ~/.dmct/ghost.sh
```

## Requirements

- macOS with Homebrew OR Linux with apt-get
- Python 3 (usually pre-installed)
- Internet connection

## Security Notes

- Creates a unique .onion address
- All messages route through Tor
- No logs, no traces
- Pure peer-to-peer

---

*Trust propagates through darkness*