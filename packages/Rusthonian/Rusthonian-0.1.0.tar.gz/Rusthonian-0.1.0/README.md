# 🦀 Rusthonian

**High-performance Python bindings for Rust crates**

[![CI](https://github.com/Rusthonian/Rusthonian/workflows/CI/badge.svg)](https://github.com/Rusthonian/Rusthonian/actions)
[![License](https://img.shields.io/badge/license-MIT%2FApache--2.0-blue.svg)](https://github.com/Rusthonian/Rusthonian)

Rusthonian is an umbrella project that provides Python bindings for high-quality Rust crates through PyO3.

## 🚀 Quick Start

```bash
# 1. Clone
git clone https://github.com/YourUsername/Rusthonian.git
cd Rusthonian

# 2. Build
pip install maturin
maturin develop --release

# 3. Use
python -c "from Rusthonian import uuid; print(uuid.uuid4())"
```

## 📦 Included Modules

### UUID
Complete Python bindings for Rust's [`uuid` crate](https://docs.rs/uuid/).

- All UUID versions (v1-v8)
- **9.6+ million UUIDs/second** performance
- See [`uuid/README.md`](uuid/README.md) for full documentation

**Example:**
```python
from Rusthonian import uuid

u = uuid.uuid4()  # Random UUID
print(u)
```

## 🛠️ Building

### Requirements
- Python 3.9+
- Rust (latest stable)
- Maturin (`pip install maturin`)

### Build Commands

```bash
# Development build (editable install)
maturin develop --release

# Production build (wheel)
maturin build --release

# Quick test
python -c "from Rusthonian import uuid; print(uuid.uuid4())"
```

### Python 3.13+

```bash
export PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1
maturin develop --release
```

## 📖 Documentation

- **Quick Start**: See [`QUICKSTART.md`](QUICKSTART.md)
- **UUID Module**: See [`uuid/README.md`](uuid/README.md)
- **Examples**: Check [`examples/`](examples/)

## 🧪 Testing

```bash
# Run all tests
./test_all.sh

# Or manually
python examples/basic_usage.py
python uuid/test_comprehensive.py
```

## 🏗️ Project Structure

```
Rusthonian/
├── src/              # Main umbrella project
│   └── lib.rs
├── uuid/             # UUID module
│   ├── src/
│   └── README.md
├── Rusthonian/       # Python package wrapper
│   └── __init__.py
├── examples/         # Usage examples
├── Cargo.toml        # Rust config
└── pyproject.toml    # Python packaging
```

## 📄 License

Dual-licensed under MIT OR Apache-2.0

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repo
2. Create a feature branch
3. Make your changes
4. Run tests: `./test_all.sh`
5. Submit a PR

## 📮 Links

- [GitHub](https://github.com/Rusthonian/Rusthonian)
- [Issues](https://github.com/Rusthonian/Rusthonian/issues)

---

Built with [PyO3](https://pyo3.rs/) ❤️