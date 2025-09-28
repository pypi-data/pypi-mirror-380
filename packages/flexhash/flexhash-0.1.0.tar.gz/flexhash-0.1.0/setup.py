from setuptools import setup, Extension
import sys
from pathlib import Path

base = Path(__file__).parent / "flexhash"

# Manually specify source files to avoid template/helper files
def get_source_files():
    sources = [
        str(base / "_flexmodule.c"),
        str(base / "flex.c"),
    ]
    
    # Add crypto files (main directory, excluding template files)
    crypto_dir = base / "crypto"
    for c_file in crypto_dir.glob("*.c"):
        sources.append(str(c_file))
    
    # Add cryptonote files
    cryptonote_dir = base / "crypto/cryptonote"
    if cryptonote_dir.exists():
        for c_file in cryptonote_dir.glob("*.c"):
            sources.append(str(c_file))
    
    
    # Add sha3 files, excluding template/helper files and non-sph duplicates
    sha3_dir = base / "crypto/sha3"
    exclude_files = {'md_helper.c', 'aes_helper.c', 'hamsi_helper.c', 'haval_helper.c','gost_streebog.c'}
    if sha3_dir.exists():
        for c_file in sha3_dir.glob("*.c"):
            if c_file.name not in exclude_files:
                sources.append(str(c_file))
    
    # Verify all source files exist
    missing_files = [src for src in sources if not Path(src).exists()]
    if missing_files:
        raise FileNotFoundError(f"Missing source files: {missing_files}")
    
    print(f"Found {len(sources)} source files for compilation")
    return sources

if sys.platform == "win32":
    extra_compile_args = ["/O2", "/DWIN32"]
    extra_link_args = []
else:
    extra_compile_args = ["-O3"]
    extra_link_args = []

ext = Extension(
    "flexhash._flexhash",
    sources=get_source_files(),
    include_dirs=[str(base), str(base / "crypto"), str(base / "crypto/sha3"), str(base / "crypto/cryptonote"), str(base / "crypto/utils")],
    extra_compile_args=extra_compile_args,
    extra_link_args=extra_link_args,
)

setup(
    name="flexhash",
    version="0.1.0",
    description="Kylacoin Flex hashing (C extension)",
    packages=["flexhash"],
    ext_modules=[ext],
    python_requires=">=3.8",
)
