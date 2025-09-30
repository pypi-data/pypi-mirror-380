# 🚀 Rusthonian - Quick Start Guide

## Installation & Build

### Step 1: Clone the Repository

```bash
git clone https://github.com/YourUsername/Rusthonian.git
cd Rusthonian
```

### Step 2: Install Build Dependencies

```bash
# Install Rust (if not already installed)
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Install maturin
pip install maturin
```

### Step 3: Build the Project

```bash
# Build and install in development mode (recommended for development)
maturin develop --release 

# Or build a wheel for distribution
maturin build --release 
# Then install: pip install target/wheels/Rusthonian-*.whl
```

### Step 4: Test It!

```bash
# Quick test
python -c "from Rusthonian import uuid; print(f'UUID: {uuid.uuid4()}')"

# Run examples
python examples/basic_usage.py
python examples/uuid_example.py

# Run comprehensive tests
python UUID/test_comprehensive.py
```

## Usage

```python
from Rusthonian import uuid

# Generate UUIDs
u4 = uuid.uuid4()          # Random
u7 = uuid.uuid7()          # Timestamp-based
print(f"UUID: {u4}")

# Parse UUID
u = uuid.UUID(hex="550e8400-e29b-41d4-a716-446655440000")
print(f"Version: {u.version}, Variant: {u.variant}")

# Different formats
print(f"Simple: {u.as_simple()}")
print(f"URN: {u.as_urn()}")

# Namespace-based UUIDs
u5 = uuid.uuid5(uuid.NAMESPACE_DNS, "example.com")
print(f"Namespace UUID: {u5}")
```

## Performance

**9.6+ million UUIDs/second** on modern hardware!

```python
import time
from Rusthonian import uuid

start = time.time()
for _ in range(100000):
    uuid.uuid4()
elapsed = time.time() - start
print(f"Rate: {100000/elapsed:,.0f} UUIDs/s")
```

## Features

✅ All UUID versions (v1, v3, v4, v5, v6, v7, v8)  
✅ All formatting options  
✅ Timestamp extraction  
✅ Builder pattern  
✅ 100% uuid crate coverage  
✅ Pythonic API  
✅ Type hints ready  

## Troubleshooting

### Python 3.13+

For Python 3.13 and newer, you may need:

```bash
export PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1
maturin develop --release 
```

### Build Errors

```bash
# Clean and rebuild
cargo clean
maturin develop --release 
```

## Next Steps

- Read the full [README.md](README.md)
- Explore [examples/](examples/)
- Check the [UUID module docs](UUID/README.md)
- Review [BUILD.md](BUILD.md) for detailed build instructions
