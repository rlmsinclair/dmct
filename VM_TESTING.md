# Testing DMCT Ghost Mode in a VM

## Quick VM Setup Options

### 1. Ubuntu VM (Easiest)
```bash
# In a fresh Ubuntu VM, run:
curl -sL https://raw.githubusercontent.com/rlmsinclair/dmct/main/ghost-anywhere.sh | bash
```

### 2. macOS VM (if you have one)
```bash
# Install Homebrew first:
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Then run:
curl -sL https://raw.githubusercontent.com/rlmsinclair/dmct/main/ghost-anywhere.sh | bash
```

## Step-by-Step Testing

### 1. Create VM
- **VirtualBox/VMware**: Ubuntu 22.04+ or Debian 12
- **UTM (Mac)**: Ubuntu ARM64
- **Multipass**: `multipass launch --name dmct-test`

### 2. Test Fresh Install
```bash
# SSH into VM, then:
wget -qO- https://raw.githubusercontent.com/rlmsinclair/dmct/main/ghost-anywhere.sh | bash
```

### 3. Verify Components
```bash
# Check Tor
ps aux | grep tor

# Check hidden service
cat ~/.dmct/tor/hidden_service/hostname

# Check ports
netstat -tlnp | grep -E "9050|31415"
```

### 4. Test Between VMs
Create two VMs and:
1. Run ghost mode on both
2. Exchange .onion addresses
3. Test messaging between them

## Docker Alternative
```dockerfile
FROM ubuntu:22.04
RUN apt-get update && apt-get install -y curl python3 tor torsocks
RUN curl -sL https://raw.githubusercontent.com/rlmsinclair/dmct/main/install.sh | sh
CMD ["~/.dmct/ghost.sh"]
```

## Quick Multipass Test
```bash
# Create VM
multipass launch --name ghost1

# Run ghost mode
multipass exec ghost1 -- bash -c "curl -sL https://raw.githubusercontent.com/rlmsinclair/dmct/main/ghost-anywhere.sh | bash"

# Create second VM
multipass launch --name ghost2

# Run on second
multipass exec ghost2 -- bash -c "curl -sL https://raw.githubusercontent.com/rlmsinclair/dmct/main/ghost-anywhere.sh | bash"
```

## Testing Checklist
- [ ] Fresh system install works
- [ ] Tor starts automatically
- [ ] Hidden service generates
- [ ] Port 31415 is listening
- [ ] Can connect between VMs
- [ ] Messages propagate through Tor

## Minimal Test Script
```bash
#!/bin/bash
# Save as test-ghost.sh
echo "Testing DMCT Ghost Mode..."

# Install and run
curl -sL https://raw.githubusercontent.com/rlmsinclair/dmct/main/ghost-anywhere.sh | bash &
GHOST_PID=$!

# Wait for initialization
sleep 20

# Check if running
if ps -p $GHOST_PID > /dev/null; then
    echo "✓ Ghost mode running"
    cat ~/.dmct/tor/hidden_service/hostname
else
    echo "✗ Ghost mode failed"
fi
```

---

*Test in isolation, trust in darkness*