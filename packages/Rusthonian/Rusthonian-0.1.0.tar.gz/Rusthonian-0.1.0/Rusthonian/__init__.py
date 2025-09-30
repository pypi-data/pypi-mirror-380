"""
Rusthonian - High-performance Python bindings for Rust crates

Build the module first:
    pip install maturin
    maturin develop --release --features uuid

Or install from wheel:
    maturin build --release --features uuid
    pip install target/wheels/Rusthonian-*.whl
"""

__version__ = "0.1.0"
__author__ = "Rusthonian Team"

# This will be populated by maturin when building
# The Rust module will be compiled as Rusthonian.rusthonian
try:
    from .rusthonian import *
    
    # Export uuid if available
    if hasattr(rusthonian, 'uuid'):
        uuid = rusthonian.uuid
        __all__ = ['uuid']
    else:
        __all__ = []
        
except ImportError as e:
    import sys
    print(f"""
╔══════════════════════════════════════════════════════════════╗
║                   Rusthonian Not Built                       ║
╚══════════════════════════════════════════════════════════════╝

The Rusthonian Rust extension module is not installed.

To build and install:
    
    1. Install maturin:
       pip install maturin
    
    2. Build and install in development mode:
       maturin develop --release --features uuid
    
    Or build a wheel:
       maturin build --release --features uuid
       pip install target/wheels/Rusthonian-*.whl

Error: {e}
""", file=sys.stderr)
    raise
