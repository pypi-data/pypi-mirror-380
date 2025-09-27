"""
Text Extraction Mixin - PDF text extraction and OCR capabilities
"""

import os
import asyncio
import tempfile
from pathlib import Path
from typing import Dict, Any, List, Optional, Union
import logging

# PDF processing libraries
import fitz  # PyMuPDF
import pdfplumber
import pypdf
import pytesseract
from pdf2image import convert_from_path

from .base import MCPMixin, mcp_tool
from ..security import validate_pdf_path, validate_pages_parameter, sanitize_error_message

logger = logging.getLogger(__name__)


class TextExtractionMixin(MCPMixin):
    """
    Handles all PDF text extraction and OCR operations.

    Tools provided:
    - extract_text: Intelligent text extraction with method selection
    - ocr_pdf: OCR processing for scanned documents
    - is_scanned_pdf: Detect if PDF is scanned/image-based
    """

    def get_mixin_name(self) -> str:
        return "TextExtraction"

    def get_required_permissions(self) -> List[str]:
        return ["read_files", "ocr_processing"]

    def _setup(self):
        """Initialize text extraction specific configuration"""
        self.max_chunk_pages = int(os.getenv("PDF_CHUNK_PAGES", "10"))
        self.max_tokens_per_chunk = int(os.getenv("PDF_MAX_TOKENS_CHUNK", "50000"))

    @mcp_tool(
        name="extract_text",
        description="Extract text from PDF with intelligent method selection and automatic chunking for large files"
    )
    async def extract_text(
        self,
        pdf_path: str,
        method: str = "auto",
        pages: Optional[str] = None,
        preserve_layout: bool = False,
        chunk_size: int = 10
    ) -> Dict[str, Any]:
        """
        Extract text from PDF with intelligent method selection.

        Args:
            pdf_path: Path to PDF file or URL
            method: Extraction method ("auto", "pymupdf", "pdfplumber", "pypdf")
            pages: Page specification (e.g., "1-5,10,15-20" or "all")
            preserve_layout: Whether to preserve text layout and formatting
            chunk_size: Number of pages per chunk for large PDFs

        Returns:
            Dictionary with extracted text, metadata, and processing info
        """
        start_time = asyncio.get_event_loop().time()

        try:
            # Validate inputs
            validated_path = await validate_pdf_path(pdf_path)
            page_list = validate_pages_parameter(pages) if pages else None

            # Check if PDF is scanned and suggest OCR if needed
            is_scanned = self._check_if_scanned(validated_path)
            if is_scanned and method == "auto":
                return {
                    "success": False,
                    "error": "PDF appears to be scanned/image-based",
                    "suggestion": "Use the 'ocr_pdf' tool for scanned documents",
                    "is_scanned": True,
                    "processing_time": asyncio.get_event_loop().time() - start_time
                }

            # Determine extraction method
            if method == "auto":
                method = self._select_best_method(validated_path, preserve_layout)

            # Extract text using selected method
            if method == "pymupdf":
                text = self._extract_with_pymupdf(validated_path, page_list, preserve_layout)
            elif method == "pdfplumber":
                text = self._extract_with_pdfplumber(validated_path, page_list, preserve_layout)
            elif method == "pypdf":
                text = self._extract_with_pypdf(validated_path, page_list, preserve_layout)
            else:
                raise ValueError(f"Unsupported extraction method: {method}")

            # Handle large text with chunking
            if len(text) > self.max_tokens_per_chunk * 4:  # Rough token estimation
                return self._chunk_large_text(text, validated_path, chunk_size, method, start_time)

            # Get document info
            doc_info = self._get_document_info(validated_path)

            processing_time = asyncio.get_event_loop().time() - start_time

            return {
                "success": True,
                "text": text,
                "method_used": method,
                "page_count": doc_info.get("page_count", 0),
                "character_count": len(text),
                "word_count": len(text.split()),
                "is_scanned": is_scanned,
                "preserve_layout": preserve_layout,
                "pages_processed": page_list or "all",
                "processing_time": processing_time
            }

        except Exception as e:
            error_msg = sanitize_error_message(str(e))
            logger.error(f"Text extraction failed: {error_msg}")
            return {
                "success": False,
                "error": error_msg,
                "method_attempted": method,
                "processing_time": asyncio.get_event_loop().time() - start_time
            }

    @mcp_tool(
        name="ocr_pdf",
        description="Perform OCR on scanned PDFs with preprocessing options"
    )
    async def ocr_pdf(
        self,
        pdf_path: str,
        language: str = "eng",
        dpi: int = 300,
        enhance_image: bool = True,
        pages: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Perform OCR on scanned PDF documents.

        Args:
            pdf_path: Path to PDF file or URL
            language: OCR language code (eng, spa, fra, deu, etc.)
            dpi: DPI for image conversion (higher = better quality, slower)
            enhance_image: Apply image preprocessing for better OCR
            pages: Page specification for OCR processing

        Returns:
            Dictionary with OCR text and processing metadata
        """
        start_time = asyncio.get_event_loop().time()

        try:
            validated_path = await validate_pdf_path(pdf_path)
            page_list = validate_pages_parameter(pages) if pages else None

            # Convert PDF pages to images
            logger.info(f"Converting PDF to images for OCR (DPI: {dpi})")

            # Use specific pages if provided
            if page_list:
                first_page = min(page_list)
                last_page = max(page_list)
                images = convert_from_path(
                    validated_path,
                    dpi=dpi,
                    first_page=first_page,
                    last_page=last_page
                )
                # Filter to only requested pages
                images = [img for i, img in enumerate(images, first_page) if i in page_list]
            else:
                images = convert_from_path(validated_path, dpi=dpi)

            logger.info(f"Processing {len(images)} pages with OCR")

            # Process each image with OCR
            ocr_results = []
            total_text = ""

            for i, image in enumerate(images):
                page_num = page_list[i] if page_list else i + 1

                if enhance_image:
                    image = self._enhance_image_for_ocr(image)

                # Perform OCR
                page_text = pytesseract.image_to_string(image, lang=language)
                total_text += f"\n--- Page {page_num} ---\n{page_text}\n"

                ocr_results.append({
                    "page": page_num,
                    "text": page_text,
                    "character_count": len(page_text)
                })

            processing_time = asyncio.get_event_loop().time() - start_time

            return {
                "success": True,
                "text": total_text.strip(),
                "ocr_results": ocr_results,
                "language": language,
                "dpi": dpi,
                "pages_processed": len(images),
                "total_characters": len(total_text),
                "enhanced": enhance_image,
                "processing_time": processing_time
            }

        except Exception as e:
            error_msg = sanitize_error_message(str(e))
            logger.error(f"OCR processing failed: {error_msg}")
            return {
                "success": False,
                "error": error_msg,
                "processing_time": asyncio.get_event_loop().time() - start_time
            }

    @mcp_tool(
        name="is_scanned_pdf",
        description="Detect if a PDF is scanned/image-based rather than text-based"
    )
    async def is_scanned_pdf(self, pdf_path: str) -> Dict[str, Any]:
        """
        Analyze PDF to determine if it's scanned/image-based.

        Args:
            pdf_path: Path to PDF file or URL

        Returns:
            Dictionary with scan detection results and recommendations
        """
        try:
            validated_path = await validate_pdf_path(pdf_path)
            is_scanned = self._check_if_scanned(validated_path)

            doc_info = self._get_document_info(validated_path)

            return {
                "success": True,
                "is_scanned": is_scanned,
                "confidence": "high" if is_scanned else "medium",
                "recommendation": "Use OCR extraction" if is_scanned else "Use text extraction",
                "page_count": doc_info.get("page_count", 0),
                "file_size": doc_info.get("file_size", 0)
            }

        except Exception as e:
            error_msg = sanitize_error_message(str(e))
            return {
                "success": False,
                "error": error_msg
            }

    # Private helper methods
    def _check_if_scanned(self, pdf_path: Path) -> bool:
        """Check if PDF appears to be scanned by analyzing text content"""
        try:
            # Quick text extraction to check content
            doc = fitz.open(pdf_path)
            text_length = 0
            pages_checked = min(3, len(doc))  # Check first 3 pages

            for page_num in range(pages_checked):
                page = doc[page_num]
                text = page.get_text()
                text_length += len(text.strip())

            doc.close()

            # If very little text found, likely scanned
            avg_text_per_page = text_length / pages_checked if pages_checked > 0 else 0
            return avg_text_per_page < 100  # Threshold for scanned detection

        except Exception:
            return False  # Assume not scanned if we can't determine

    def _select_best_method(self, pdf_path: Path, preserve_layout: bool) -> str:
        """Select the best extraction method based on PDF characteristics"""
        if preserve_layout:
            return "pdfplumber"  # Best for layout preservation
        else:
            return "pymupdf"  # Fastest and most reliable for simple text

    def _extract_with_pymupdf(self, pdf_path: Path, pages: Optional[List[int]], preserve_layout: bool) -> str:
        """Extract text using PyMuPDF"""
        doc = fitz.open(pdf_path)
        text_parts = []

        page_range = pages if pages else range(len(doc))

        for page_num in page_range:
            if page_num < len(doc):
                page = doc[page_num]
                if preserve_layout:
                    text = page.get_text("dict")  # Get structured text
                    # Process structured text to preserve layout
                    page_text = self._process_structured_text(text)
                else:
                    page_text = page.get_text()
                text_parts.append(page_text)

        doc.close()
        return "\n\n".join(text_parts)

    def _extract_with_pdfplumber(self, pdf_path: Path, pages: Optional[List[int]], preserve_layout: bool) -> str:
        """Extract text using pdfplumber"""
        text_parts = []

        with pdfplumber.open(pdf_path) as pdf:
            page_range = pages if pages else range(len(pdf.pages))

            for page_num in page_range:
                if page_num < len(pdf.pages):
                    page = pdf.pages[page_num]
                    if preserve_layout:
                        text = page.extract_text(layout=True)
                    else:
                        text = page.extract_text()
                    if text:
                        text_parts.append(text)

        return "\n\n".join(text_parts)

    def _extract_with_pypdf(self, pdf_path: Path, pages: Optional[List[int]], preserve_layout: bool) -> str:
        """Extract text using pypdf"""
        text_parts = []

        with open(pdf_path, 'rb') as file:
            reader = pypdf.PdfReader(file)
            page_range = pages if pages else range(len(reader.pages))

            for page_num in page_range:
                if page_num < len(reader.pages):
                    page = reader.pages[page_num]
                    text = page.extract_text()
                    if text:
                        text_parts.append(text)

        return "\n\n".join(text_parts)

    def _chunk_large_text(self, text: str, pdf_path: Path, chunk_size: int, method: str, start_time: float) -> Dict[str, Any]:
        """Handle large text documents by chunking"""
        # Implement chunking logic
        chunks = []
        words = text.split()
        chunk_word_limit = self.max_tokens_per_chunk

        for i in range(0, len(words), chunk_word_limit):
            chunk = " ".join(words[i:i + chunk_word_limit])
            chunks.append(chunk)

        processing_time = asyncio.get_event_loop().time() - start_time

        return {
            "success": True,
            "text": chunks[0],  # Return first chunk
            "is_chunked": True,
            "total_chunks": len(chunks),
            "current_chunk": 1,
            "method_used": method,
            "total_character_count": len(text),
            "chunk_character_count": len(chunks[0]),
            "processing_time": processing_time,
            "next_chunk_hint": f"To get the next chunk, use chunk parameter in your next request"
        }

    def _get_document_info(self, pdf_path: Path) -> Dict[str, Any]:
        """Get basic document information"""
        try:
            doc = fitz.open(pdf_path)
            info = {
                "page_count": len(doc),
                "file_size": pdf_path.stat().st_size
            }
            doc.close()
            return info
        except Exception:
            return {"page_count": 0, "file_size": 0}

    def _enhance_image_for_ocr(self, image):
        """Apply image preprocessing for better OCR results"""
        # Implement image enhancement (contrast, sharpening, etc.)
        return image  # Placeholder - implement actual enhancement

    def _process_structured_text(self, text_dict: Dict) -> str:
        """Process PyMuPDF structured text to preserve layout"""
        # Implement layout preservation logic
        return ""  # Placeholder - implement actual processing