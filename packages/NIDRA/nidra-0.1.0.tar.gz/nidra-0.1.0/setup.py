from setuptools import setup
import sys
import platform

# Base dependencies from pyproject.toml
install_requires = [
    "scipy",
    "mne",
    "seaborn",
    "pandas",
    "matplotlib",
    "Flask",
    "pyinstaller",
    "huggingface_hub",
    "hf_xet",
    "appdirs",
    "requests",
    "pywebview",
    "psutil",
]

# Add platform-specific dependencies for numpy and onnxruntime
# This logic mirrors the one in pyproject.toml for compatibility with older pip/setuptools
if sys.platform == 'darwin':
    # platform.release() returns the kernel version, e.g., '23.1.0' for macOS 14.1
    # macOS < 14 corresponds to Darwin kernel version < 23
    major_darwin_version = int(platform.release().split('.')[0])
    if major_darwin_version < 23:
        install_requires.extend([
            "numpy<2",
            "onnxruntime==1.16.3"
        ])
    else:
        install_requires.extend([
            "numpy>=2.0.0",
            "onnxruntime>=1.19.0"
        ])
else:
    install_requires.extend([
        "numpy>=2.0.0",
        "onnxruntime>=1.19.0"
    ])

setup(
    install_requires=install_requires,
)