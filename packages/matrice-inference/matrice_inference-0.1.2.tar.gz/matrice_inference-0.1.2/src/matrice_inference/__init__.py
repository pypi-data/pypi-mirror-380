"""Module providing __init__ functionality."""

import os
import sys
from matrice_common.utils import dependencies_check

base = [
    "httpx",
    "fastapi",
    "uvicorn",
    "pillow",
    "confluent_kafka[snappy]",
    "aiokafka",
    "aiohttp",
    "filterpy",
    "scipy",
    "scikit-learn",
    "matplotlib",
    "scikit-image",
    "python-snappy",
    "pyyaml",
    "imagehash",
    "Pillow",
    "transformers"
]

# Install base dependencies first
dependencies_check(base)

# Helper to attempt installation and verify importability
def _install_and_verify(pkg: str, import_name: str):
    """Install a package expression and return True if the import succeeds."""
    if dependencies_check([pkg]):
        try:
            __import__(import_name)
            return True
        except ImportError:
            return False
    return False

if not dependencies_check(["opencv-python"]):
    dependencies_check(["opencv-python-headless"])

# Attempt GPU-specific dependencies first
_gpu_ok = _install_and_verify("onnxruntime-gpu", "onnxruntime") and _install_and_verify(
    "fast-plate-ocr[onnx-gpu]", "fast_plate_ocr"
)

if not _gpu_ok:
    # Fallback to CPU variants
    _cpu_ok = _install_and_verify("onnxruntime", "onnxruntime") and _install_and_verify(
        "fast-plate-ocr[onnx]", "fast_plate_ocr"
    )
    if not _cpu_ok:
        # Last-chance fallback without extras tag (PyPI sometimes lacks them)
        _install_and_verify("fast-plate-ocr", "fast_plate_ocr")

# matrice_deps = ["matrice_common", "matrice_analytics", "matrice"]

# dependencies_check(matrice_deps)
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from server.server import MatriceDeployServer  # noqa: E402
from server.server import MatriceDeployServer as MatriceDeploy  # noqa: E402 # Keep this for backwards compatibility
from server.inference_interface import InferenceInterface  # noqa: E402
from server.proxy_interface import MatriceProxyInterface  # noqa: E402

__all__ = [
    "MatriceDeploy",
    "MatriceDeployServer",
    "InferenceInterface",
    "MatriceProxyInterface",
]
