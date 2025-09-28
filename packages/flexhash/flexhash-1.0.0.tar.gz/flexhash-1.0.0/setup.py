from setuptools import setup, Extension, find_packages
from pathlib import Path
import os, sys

ROOT = Path(__file__).parent.resolve()
PKG_DIR = ROOT / "flexhash"

EXCLUDE_SHA3 = {"md_helper.c","aes_helper.c","hamsi_helper.c","haval_helper.c","gost_streebog.c"}

def rel(p: Path) -> str:
    # relative to setup.py dir, force forward slashes
    return Path(os.path.relpath(p, ROOT)).as_posix()

def collect_sources():
    srcs = [
        PKG_DIR / "_flexmodule.c",
        PKG_DIR / "flex.c",
    ]
    for sub in ["crypto", "crypto/cryptonote", "crypto/sha3", "crypto/utils"]:
        d = PKG_DIR / sub
        if d.exists():
            for p in d.glob("*.c"):
                if p.parent.name == "sha3" and p.name in EXCLUDE_SHA3:
                    continue
                srcs.append(p)

    missing = [str(p) for p in srcs if not p.exists()]
    if missing:
        raise FileNotFoundError(f"Missing source files: {missing}")

    # convert to relative POSIX
    return [rel(p) for p in srcs]

if sys.platform == "win32":
    extra_compile_args = ["/O2", "/DWIN32", "/DNOMINMAX"]
    define_macros = [("WIN32", 1)]
else:
    extra_compile_args = ["-O3", "-fvisibility=hidden", "-fno-strict-aliasing"]
    define_macros = []

ext = Extension(
    name="flexhash._flexhash",
    sources=collect_sources(),
    include_dirs=[
        rel(PKG_DIR),
        rel(PKG_DIR / "crypto"),
        rel(PKG_DIR / "crypto" / "sha3"),
        rel(PKG_DIR / "crypto" / "cryptonote"),
        rel(PKG_DIR / "crypto" / "utils"),
    ],
    define_macros=define_macros,
    extra_compile_args=extra_compile_args,
    language="c",
)

setup(
    name="flexhash",
    version="1.0.0",
    description="Kylacoin Flex hashing (C extension)",
    long_description=(ROOT / "README.md").read_text(encoding="utf-8") if (ROOT / "README.md").exists() else "",
    long_description_content_type="text/markdown",
    author="cdonnachie",
    author_email="craig.donnachie@gmail.com",
    url="https://github.com/cdonnachie/flexhash",
    packages=find_packages(include=["flexhash", "flexhash.*"]),
    package_data={"flexhash": ["**/*.h"]},
    include_package_data=True,
    ext_modules=[ext],
    python_requires=">=3.8",
    license="MIT",  # <-- SPDX license expression
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",  # optional to keep
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3",
        "Topic :: Security :: Cryptography",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords=["hashing", "cryptography", "kylacoin", "lyncoin", "flex"],
)
