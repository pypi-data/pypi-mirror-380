try:
    from ._flexhash import hash
except ImportError as e:
    raise ImportError(f"Failed to import flexhash C extension: {e}")

__all__ = ["hash"]
