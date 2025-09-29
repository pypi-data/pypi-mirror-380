import importlib
from typing import TYPE_CHECKING

__version__ = "0.1.11"
__version_info__ = (0, 1, 11)

__lazy_attrs__ = {
    "SuperPdfClient": (".superpdf_client", "SuperPdfClient"),
    "SuperPdfSamplingParams": (".superpdf_client", "SuperPdfSamplingParams"),
    "SuperPdfLogitsProcessor": (".logits_processor.vllm_v1_no_repeat_ngram", "VllmV1NoRepeatNGramLogitsProcessor"),
}

if TYPE_CHECKING:
    # Rename for future compatibility
    from .logits_processor.vllm_v1_no_repeat_ngram import (
        VllmV1NoRepeatNGramLogitsProcessor as SuperPdfLogitsProcessor,
    )
    from .superpdf_client import SuperPdfClient, SuperPdfSamplingParams


def __getattr__(name: str):
    if name in __lazy_attrs__:
        module_name, attr_name = __lazy_attrs__[name]
        module = importlib.import_module(module_name, __name__)
        return getattr(module, attr_name)
    raise AttributeError(f"Module '{__name__}' has no attribute '{name}'")


__all__ = [
    "SuperPdfClient",
    "SuperPdfSamplingParams",
    "SuperPdfLogitsProcessor",
    "__version__",
    "__version_info__",
]
