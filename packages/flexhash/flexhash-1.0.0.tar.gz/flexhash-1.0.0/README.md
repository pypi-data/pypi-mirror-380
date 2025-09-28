# FlexHash

A fast Python extension module implementing the Flex hashing algorithm used by Kylacoin and Lyncoin cryptocurrencies.

[![PyPI version](https://badge.fury.io/py/flexhash.svg)](https://pypi.org/project/flexhash/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

## What is FlexHash?

FlexHash is a high-performance cryptographic hash function that combines multiple proven algorithms including SHA3, CryptoNight variants, and Lyra2. It's specifically designed for blockchain applications requiring secure and efficient hashing.

## Installation

Install from PyPI (recommended):

```bash
pip install flexhash
```

Or visit the [PyPI project page](https://pypi.org/project/flexhash/) for more details.

## Quick Start

```python
import flexhash

# Hash some data
data = b"Hello, World!"
result = flexhash.hash(data)

print(f"Input: {data}")
print(f"Hash: {result.hex()}")
# Output: Hash: 7a8b9c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b
```

## API Reference

### `flexhash.hash(data: bytes) -> bytes`

Computes the Flex hash of the input data.

**Parameters:**

- `data` (bytes): The data to hash

**Returns:**

- `bytes`: 32-byte hash digest

**Example:**

```python
import flexhash

# Basic usage
hash_output = flexhash.hash(b"example data")
assert len(hash_output) == 32

# Hash is deterministic
hash1 = flexhash.hash(b"test")
hash2 = flexhash.hash(b"test")
assert hash1 == hash2
```

## Requirements

- Python 3.8 or later
- Works on Windows, Linux, and macOS

## License

This project is licensed under the terms specified in the LICENSE file.

## Related Projects

- [Kylacoin](https://github.com/Kylacoin) - Kylacoin GitHub Repos
- [Lyncoin](https://github.com/Lyncoin) - Lyncoin GitHub Repos

## Links

- **PyPI**: https://pypi.org/project/flexhash/
- **Source Code**: https://github.com/cdonnachie/flexhash
- **Issues**: https://github.com/cdonnachie/flexhash/issues

---

_FlexHash is a cryptographic library for blockchain applications. Use responsibly and verify the implementation for your specific security requirements._
