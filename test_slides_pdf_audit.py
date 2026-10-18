#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PHANToM GRID // SLIDES-PDF AUDIT SUITE (test_slides_pdf_audit.py)
Tournament: OpenCV AI Competition 2026 (powered by AWS)
Gate-Before-Ship SOP:
  • P1: Anti-mojibake (Zero corrupted characters)
  • P2: Vertical Content Coverage >= 78% on every page
  • P3: Explicit 'Atomic Reclaim' or 'Timeout' rollback path
  • P4: Technology boundaries (OpenCV 5, AWS COOL, FastMCP, ASIL-D)
  • P5: Commander Jack Hu badge width <= 68% of page width
  • P6: Embedded QR Code image object and URL on final slide
  • P7: Exactly 10 slides
"""

import os
import re
import sys
from pathlib import Path
import fitz  # PyMuPDF
import pytest

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

PDF_PATH = Path(__file__).parent / "pitch_deck.pdf"


@pytest.fixture(scope="module")
def doc():
    if not PDF_PATH.exists():
        pytest.skip(f"Target PDF file not found at {PDF_PATH}")
    document = fitz.open(str(PDF_PATH))
    yield document
    document.close()


def test_p1_anti_mojibake(doc):
    """P1: Anti-Mojibake Safety - No corrupted characters permitted"""
    mojibake_pattern = re.compile(r"[ðï\ufffd]")
    for page_idx, page in enumerate(doc):
        text = page.get_text()
        assert not mojibake_pattern.search(text), f"Page {page_idx + 1} contains mojibake characters!"


def test_p2_vertical_space_balancing(doc):
    """P2: Vertical Coverage Rule - Content coverage must be >= 78%"""
    for page_idx, page in enumerate(doc):
        rect = page.rect
        page_height = rect.height
        blocks = page.get_text("blocks")
        assert blocks, f"Page {page_idx + 1} has no text blocks!"
        min_y = min(b[1] for b in blocks)
        max_y = max(b[3] for b in blocks)
        content_span = max_y - min_y
        coverage_ratio = content_span / page_height
        assert coverage_ratio >= 0.78, f"Page {page_idx + 1} vertical coverage ({coverage_ratio:.1%}) < 78%!"


def test_p3_atomic_reclaim_pathway(doc):
    """P3: Explicit Atomic Reclaim & Timeout rollback path present in architecture"""
    full_text = " ".join([page.get_text() for page in doc])
    assert "Atomic Reclaim" in full_text or "atomic reclaim" in full_text.lower(), "Missing 'Atomic Reclaim' pathway in slides!"
    assert "timeout" in full_text.lower(), "Missing 'Timeout' boundary in slides!"


def test_p4_technology_boundaries(doc):
    """P4: Core technologies properly documented"""
    full_text = " ".join([page.get_text() for page in doc])
    assert "OpenCV 5" in full_text, "Missing 'OpenCV 5' technology specification!"
    assert "FastMCP" in full_text, "Missing 'FastMCP' specification!"
    assert "ASIL-D" in full_text, "Missing 'ASIL-D' safety grade specification!"


def test_p5_commander_badge_isolation(doc):
    """P5: Solo Architect Jack Hu badge width <= 68% of page width"""
    page1 = doc[0]
    page_w = page1.rect.width
    text_page = page1.get_text("words")
    jack_words = [w for w in text_page if "Jack" in w[4] or "Hu" in w[4]]
    assert jack_words, "Commander Jack Hu nameplate missing on Slide 1!"
    min_x = min(w[0] for w in jack_words)
    max_x = max(w[2] for w in jack_words)
    badge_width = max_x - min_x
    assert badge_width / page_w <= 0.68, f"Commander badge width ({badge_width / page_w:.1%}) exceeds 68% safe zone!"


def test_p6_embedded_qr_code(doc):
    """P6: Embedded QR Code image object and URL on final slide"""
    last_page = doc[-1]
    images = last_page.get_images()
    assert len(images) >= 1, "Final slide must contain an embedded QR Code image object!"
    text = last_page.get_text()
    assert "github.com" in text.lower(), "Final slide must include readable repository link!"


def test_p7_total_slide_count(doc):
    """P7: Presentation must have exactly 10 slides"""
    assert len(doc) == 10, f"Expected exactly 10 slides, found {len(doc)}!"
