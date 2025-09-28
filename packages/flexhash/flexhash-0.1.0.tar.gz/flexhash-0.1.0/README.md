# FlexHash

A Python extension module implementing the Kylacoin Flex hashing algorithm. This is a high-performance C implementation that provides Python bindings for cryptographic hashing operations.

## Overview

FlexHash is a multi-algorithm hash function that combines various cryptographic hashing algorithms including:

- **SHA3 family**: Blake, BMW, Groestl, Keccak, Skein, Luffa, CubeHash, Shavite, SIMD, Echo, Hamsi, Fugue, Shabal, Whirlpool, SHA2, Haval, Tiger
- **Lyra2**: Memory-hard key derivation function
- **GOST Streebog**: Russian cryptographic standard
- **CryptoNight variants**: CryptoNight, CryptoNight Lite, CryptoNight Fast, CryptoNight Dark, CryptoNight Soft Shell, CryptoNight Turtle

## Features

- ⚡ **High Performance**: C implementation with Python bindings
- 🔒 **Cryptographically Secure**: Multiple proven hash algorithms
- 🐍 **Python 3.8+**: Modern Python support
- 🏗️ **Cross Platform**: Works on Windows, Linux, and macOS
- 📦 **Easy Installation**: Standard Python packaging

## Installation

### Prerequisites

**Linux/Ubuntu:**

```bash
sudo apt-get install python3-dev build-essential
```

**Windows:**

- Visual Studio Build Tools or Visual Studio with C++ support
- Python 3.8 or later

**macOS:**

```bash
xcode-select --install
```

### Install from Source

1. Clone this repository:

```bash
git clone https://github.com/cdonnachie/flexhash.git
cd flexhash
```

2. Install the package:

```bash
# Using pip (recommended)
pip install .

# Or in development mode
pip install -e .

# Or using setuptools directly
python setup.py install
```

## Usage

### Basic Usage

```python
import flexhash

# Hash some data
data = b"Hello, World!"
hash_result = flexhash.hash(data)

print(f"Input: {data}")
print(f"Hash: {hash_result.hex()}")
```

### Mining/Blockchain Usage

```python
import flexhash
import struct

def mine_block(previous_hash, merkle_root, timestamp, bits, nonce):
    """Example mining function using FlexHash"""
    # Construct block header (simplified)
    header = struct.pack(
        '<32s32sIII',
        previous_hash,
        merkle_root,
        timestamp,
        bits,
        nonce
    )

    # Compute hash
    return flexhash.hash(header)

# Example usage
prev_hash = b'\x00' * 32
merkle = b'\xFF' * 32
timestamp = 1640995200  # Unix timestamp
bits = 0x1d00ffff      # Difficulty target
nonce = 12345

block_hash = mine_block(prev_hash, merkle, timestamp, bits, nonce)
print(f"Block hash: {block_hash.hex()}")
```

### Performance Testing

```python
import flexhash
import time

def benchmark_hash(iterations=10000):
    """Benchmark the hash function performance"""
    data = b"benchmark_data_" * 10  # 150 bytes

    start_time = time.time()
    for i in range(iterations):
        result = flexhash.hash(data + str(i).encode())
    end_time = time.time()

    duration = end_time - start_time
    hashes_per_sec = iterations / duration

    print(f"Iterations: {iterations}")
    print(f"Time: {duration:.3f} seconds")
    print(f"Performance: {hashes_per_sec:.0f} hashes/second")

benchmark_hash()
```

## API Reference

### `flexhash.hash(data: bytes) -> bytes`

Computes the Kylacoin Flex hash of the input data.

**Parameters:**

- `data` (bytes): Input data to hash

**Returns:**

- `bytes`: 32-byte hash digest

**Example:**

```python
result = flexhash.hash(b"example data")
assert len(result) == 32
```

## Development

### Building from Source

```bash
# Clone the repository
git clone https://github.com/cdonnachie/flexhash.git
cd flexhash

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e .
```

### Testing

```python
# Basic functionality test
import flexhash

def test_basic_functionality():
    # Test with known input
    test_data = b"test_input_data"
    result = flexhash.hash(test_data)

    # Verify output properties
    assert isinstance(result, bytes)
    assert len(result) == 32

    # Test consistency
    result2 = flexhash.hash(test_data)
    assert result == result2

    print("✓ All tests passed!")

test_basic_functionality()
```

### Project Structure

```
flexhash/
├── __init__.py          # Python package initialization
├── _flexmodule.c        # Python C extension interface
├── flex.c               # Main Flex algorithm implementation
├── flex.h               # Header file for Flex algorithm
├── crypto/              # Cryptographic primitives
├── cryptonote/          # CryptoNight algorithm variants
├── sha3/                # SHA3 and related algorithms
└── utils/               # Utility functions
```

## Requirements

- Python 3.8 or later
- C compiler (GCC, Clang, or MSVC)
- Standard C library

## License

This project is licensed under the terms specified in the LICENSE file.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Security

This library implements cryptographic functions. While the algorithms used are well-established, please:

- Use this library at your own risk
- Verify the implementation for your specific use case
- Report security issues responsibly

## Related Projects

- [Kylacoin](https://github.com/AvianNetwork) - The cryptocurrency that uses this hash function
- [AvianNetwork](https://github.com/AvianNetwork) - Related blockchain projects

---

**Note**: This is a cryptographic library intended for blockchain and cryptocurrency applications. Ensure you understand the security implications before using in production systems.
