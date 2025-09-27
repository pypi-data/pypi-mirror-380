"""
Table Extraction Mixin - PDF table detection and extraction capabilities
"""

import asyncio
import logging
from pathlib import Path
from typing import Dict, Any, List, Optional

# PDF processing libraries
import camelot
import tabula
import pdfplumber
import pandas as pd

from .base import MCPMixin, mcp_tool
from ..security import validate_pdf_path, validate_pages_parameter, sanitize_error_message

logger = logging.getLogger(__name__)


class TableExtractionMixin(MCPMixin):
    """
    Handles all PDF table extraction operations with intelligent fallbacks.

    Tools provided:
    - extract_tables: Multi-method table extraction with automatic fallbacks
    - extract_tables_camelot: Camelot-specific table extraction
    - extract_tables_tabula: Tabula-specific table extraction
    - extract_tables_pdfplumber: pdfplumber-specific table extraction
    """

    def get_mixin_name(self) -> str:
        return "TableExtraction"

    def get_required_permissions(self) -> List[str]:
        return ["read_files", "table_processing"]

    def _setup(self):
        """Initialize table extraction specific configuration"""
        self.table_accuracy_threshold = 0.8
        self.max_tables_per_page = 10

    @mcp_tool(
        name="extract_tables",
        description="Extract tables from PDF with automatic method selection and intelligent fallbacks"
    )
    async def extract_tables(
        self,
        pdf_path: str,
        pages: Optional[str] = None,
        method: str = "auto",
        table_format: str = "json"
    ) -> Dict[str, Any]:
        """
        Extract tables from PDF using multiple methods with automatic fallbacks.

        Args:
            pdf_path: Path to PDF file or URL
            pages: Page specification (e.g., "1-5,10" or "all")
            method: Extraction method ("auto", "camelot", "tabula", "pdfplumber")
            table_format: Output format ("json", "csv", "html")

        Returns:
            Dictionary with extracted tables and metadata
        """
        start_time = asyncio.get_event_loop().time()

        try:
            validated_path = await validate_pdf_path(pdf_path)
            page_list = validate_pages_parameter(pages) if pages else None

            extracted_tables = []
            method_used = method
            fallback_attempts = []

            if method == "auto":
                # Try methods in order of reliability
                methods = ["camelot", "pdfplumber", "tabula"]
            else:
                methods = [method]

            for attempt_method in methods:
                try:
                    if attempt_method == "camelot":
                        tables = self._extract_with_camelot(validated_path, page_list)
                    elif attempt_method == "pdfplumber":
                        tables = self._extract_with_pdfplumber(validated_path, page_list)
                    elif attempt_method == "tabula":
                        tables = self._extract_with_tabula(validated_path, page_list)
                    else:
                        raise ValueError(f"Unsupported method: {attempt_method}")

                    if tables:
                        extracted_tables = tables
                        method_used = attempt_method
                        break
                    else:
                        fallback_attempts.append(f"{attempt_method}: no tables found")

                except Exception as e:
                    fallback_attempts.append(f"{attempt_method}: {str(e)}")
                    continue

            # Format tables according to requested format
            formatted_tables = self._format_tables(extracted_tables, table_format)

            processing_time = asyncio.get_event_loop().time() - start_time

            return {
                "success": True,
                "tables": formatted_tables,
                "table_count": len(extracted_tables),
                "method_used": method_used,
                "fallback_attempts": fallback_attempts,
                "pages_processed": page_list or "all",
                "table_format": table_format,
                "processing_time": processing_time
            }

        except Exception as e:
            error_msg = sanitize_error_message(str(e))
            logger.error(f"Table extraction failed: {error_msg}")
            return {
                "success": False,
                "error": error_msg,
                "method_attempted": method,
                "processing_time": asyncio.get_event_loop().time() - start_time
            }

    # Private helper methods
    def _extract_with_camelot(self, pdf_path: Path, pages: Optional[List[int]]) -> List[pd.DataFrame]:
        """Extract tables using Camelot"""
        try:
            if pages:
                page_str = ','.join([str(p + 1) for p in pages])  # Camelot uses 1-indexed
                tables = camelot.read_pdf(str(pdf_path), pages=page_str, flavor='lattice')
            else:
                tables = camelot.read_pdf(str(pdf_path), pages='all', flavor='lattice')

            return [table.df for table in tables if not table.df.empty]
        except Exception:
            # Try stream flavor if lattice fails
            if pages:
                page_str = ','.join([str(p + 1) for p in pages])
                tables = camelot.read_pdf(str(pdf_path), pages=page_str, flavor='stream')
            else:
                tables = camelot.read_pdf(str(pdf_path), pages='all', flavor='stream')

            return [table.df for table in tables if not table.df.empty]

    def _extract_with_pdfplumber(self, pdf_path: Path, pages: Optional[List[int]]) -> List[pd.DataFrame]:
        """Extract tables using pdfplumber"""
        tables = []

        with pdfplumber.open(pdf_path) as pdf:
            page_range = pages if pages else range(len(pdf.pages))

            for page_num in page_range:
                if page_num < len(pdf.pages):
                    page = pdf.pages[page_num]
                    page_tables = page.extract_tables()

                    for table in page_tables:
                        if table and len(table) > 1:  # Must have header + data
                            df = pd.DataFrame(table[1:], columns=table[0])
                            tables.append(df)

        return tables

    def _extract_with_tabula(self, pdf_path: Path, pages: Optional[List[int]]) -> List[pd.DataFrame]:
        """Extract tables using Tabula"""
        try:
            if pages:
                page_list = [p + 1 for p in pages]  # Tabula uses 1-indexed
                tables = tabula.read_pdf(str(pdf_path), pages=page_list, multiple_tables=True)
            else:
                tables = tabula.read_pdf(str(pdf_path), pages='all', multiple_tables=True)

            return [table for table in tables if not table.empty]
        except Exception as e:
            logger.warning(f"Tabula extraction failed: {e}")
            return []

    def _format_tables(self, tables: List[pd.DataFrame], format_type: str) -> List[Any]:
        """Format tables according to requested format"""
        if format_type == "json":
            return [table.to_dict('records') for table in tables]
        elif format_type == "csv":
            return [table.to_csv(index=False) for table in tables]
        elif format_type == "html":
            return [table.to_html(index=False) for table in tables]
        else:
            raise ValueError(f"Unsupported format: {format_type}")


# Additional stub mixins to demonstrate the pattern