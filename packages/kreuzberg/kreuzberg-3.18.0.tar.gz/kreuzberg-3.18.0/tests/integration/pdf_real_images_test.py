from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from kreuzberg import ExtractionConfig
from kreuzberg.extraction import extract_file

if TYPE_CHECKING:
    from pathlib import Path

REAL_PDFS = (
    "test-article.pdf",
    "google-doc-document.pdf",
    "sharable-web-guide.pdf",
)


def _candidate_paths(base: Path) -> list[Path]:
    return [base / name for name in REAL_PDFS if (base / name).exists()]


@pytest.mark.anyio
async def test_extract_images_from_real_pdfs_runs(test_files_path: Path) -> None:
    cfg = ExtractionConfig(extract_images=True)
    candidates = _candidate_paths(test_files_path)
    assert candidates, "No candidate real PDFs found in test_source_files."

    for pdf in candidates:
        result = await extract_file(str(pdf), config=cfg)
        assert isinstance(result.images, list)
        for img in result.images:
            assert isinstance(img.data, (bytes, bytearray))
            assert isinstance(img.format, str)


@pytest.mark.anyio
async def test_at_least_one_real_pdf_has_images(test_files_path: Path) -> None:
    cfg = ExtractionConfig(extract_images=True)
    candidates = _candidate_paths(test_files_path)
    assert candidates, "No candidate real PDFs found in test_source_files."

    images_found = 0
    for pdf in candidates:
        result = await extract_file(str(pdf), config=cfg)
        images_found += len(result.images)

    if images_found == 0:
        pytest.skip("No embedded images detected in available real PDFs.")

    assert images_found > 0
