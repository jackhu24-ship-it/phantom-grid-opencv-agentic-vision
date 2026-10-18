# -*- coding: utf-8 -*-
"""
Verification suite for 16:9 Cover Image
"""

import os
from PIL import Image

def test_cover_image_assertions():
    cover_path = os.path.join(os.path.dirname(__file__), "cover_image_16x9.png")
    assert os.path.exists(cover_path), "Cover image does not exist"

    with Image.open(cover_path) as img:
        # Assertion 1: Exact 1920x1080 resolution
        assert img.size == (1920, 1080), f"Invalid dimensions: {img.size} != (1920, 1080)"

        # Assertion 2: Mode must be RGB
        assert img.mode == "RGB", f"Invalid mode: {img.mode}"

        # Assertion 3: File size check (> 50KB)
        size_kb = os.path.getsize(cover_path) / 1024.0
        assert size_kb >= 50.0, f"File size too small: {size_kb:.1f} KB"
        print(f"Cover image test passed! Size: {img.size}, {size_kb:.1f} KB")

if __name__ == "__main__":
    test_cover_image_assertions()
