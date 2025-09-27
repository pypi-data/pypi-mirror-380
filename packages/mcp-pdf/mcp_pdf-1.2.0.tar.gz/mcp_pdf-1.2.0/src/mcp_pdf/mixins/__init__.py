"""
MCPMixin components for modular PDF tools organization
"""

from .base import MCPMixin
from .text_extraction import TextExtractionMixin
from .table_extraction import TableExtractionMixin
from .image_processing import ImageProcessingMixin
from .stubs import (
    DocumentAnalysisMixin,
    FormManagementMixin,
    DocumentAssemblyMixin,
    AnnotationsMixin,
)

__all__ = [
    "MCPMixin",
    "TextExtractionMixin",
    "TableExtractionMixin",
    "DocumentAnalysisMixin",
    "ImageProcessingMixin",
    "FormManagementMixin",
    "DocumentAssemblyMixin",
    "AnnotationsMixin",
]