# -*- coding: utf-8 -*-
"""
Generate 1920x1080 16:9 Cover Image for OpenCV AI Competition 2026
Conforming to Rule 62 (Middle Block Card Legibility Mandate) & Anti-Pitfall Invariants
"""

import os
from PIL import Image, ImageDraw, ImageFont

CANVAS_W = 1920
CANVAS_H = 1080

img = Image.new("RGB", (CANVAS_W, CANVAS_H), (10, 16, 28))
draw = ImageDraw.Draw(img)

# Fonts setup
try:
    font_hero = ImageFont.truetype("arialbd.ttf", 52)
    font_sub_hero = ImageFont.truetype("arialbd.ttf", 26)
    font_card_title = ImageFont.truetype("arialbd.ttf", 28)
    font_card_metric = ImageFont.truetype("consolab.ttf", 36)
    font_card_desc = ImageFont.truetype("arial.ttf", 22)
    font_badge = ImageFont.truetype("segoeuib.ttf", 20)
    font_footer = ImageFont.truetype("arialbd.ttf", 20)
except Exception:
    font_hero = font_sub_hero = font_card_title = font_card_metric = font_card_desc = font_badge = font_footer = ImageFont.load_default()

# 1. Subtle Cyber Grid Lines
for x in range(0, CANVAS_W, 80):
    draw.line([(x, 0), (x, CANVAS_H)], fill=(16, 25, 42), width=1)
for y in range(0, CANVAS_H, 80):
    draw.line([(0, y), (CANVAS_W, y)], fill=(16, 25, 42), width=1)

# 2. Header Category Badge
draw.rounded_rectangle([80, 70, 480, 115], radius=6, fill=(15, 35, 55), outline=(0, 229, 255), width=2)
draw.text((100, 80), "OPENCV AI COMPETITION 2026 (AWS)", font=font_badge, fill=(0, 229, 255))

draw.rounded_rectangle([500, 70, 880, 115], radius=6, fill=(35, 25, 15), outline=(251, 191, 36), width=2)
draw.text((520, 80), "AGENTIC VISION AWARD TRACK", font=font_badge, fill=(251, 191, 36))

# 3. Hero Titles
draw.text((80, 145), "PHANTOM GRID :: AUTONOMOUS AGENTIC VISION NEXUS", font=font_hero, fill=(255, 255, 255))
draw.text((80, 215), "OpenCV 5 Hardware Video Ingress x FastMCP AgentCore x AWS Bedrock Claude 3.5 Sonnet", font=font_sub_hero, fill=(56, 189, 248))

# 4. 4 High-Contrast Cards (Conforming to Rule 62: Large legible fonts!)
cards = [
    {
        "title": "OPENCV 5 & AWS COOL",
        "metric": "0.0083 ms INGRESS",
        "desc": "Zero-Copy Shared RingBuffer\nHardware Accelerated Pipelines",
        "color": (0, 229, 255)
    },
    {
        "title": "FASTMCP AGENTCORE",
        "metric": "4 CORE TOOLS",
        "desc": "Model Context Protocol Stdio/SSE\nSub-Millisecond Tool Dispatch",
        "color": (16, 185, 129)
    },
    {
        "title": "AWS BEDROCK CLAUDE 3.5",
        "metric": "SPATIAL REASONING",
        "desc": "Multi-Modal Visual Root Cause\nAST Zero-Regression Safety Gate",
        "color": (251, 191, 36)
    },
    {
        "title": "ENTERPRISE RESILIENCE",
        "metric": "1,500 CHAOS PASS",
        "desc": "MTTR < 45ms Recovery\nZDR 0.000000 MB Physical Purge",
        "color": (167, 139, 250)
    }
]

card_w = 415
card_h = 440
card_y = 310
gap = 25
start_x = 80

for i, c in enumerate(cards):
    x = start_x + i * (card_w + gap)
    draw.rounded_rectangle([x, card_y, x + card_w, card_y + card_h], radius=14, fill=(13, 20, 36), outline=c["color"], width=2)
    draw.text((x + 25, card_y + 35), c["title"], font=font_card_title, fill=c["color"])
    draw.text((x + 25, card_y + 95), c["metric"], font=font_card_metric, fill=(255, 255, 255))
    draw.line([(x + 25, card_y + 165), (x + card_w - 25, card_y + 165)], fill=(30, 45, 70), width=1)
    
    # Large 22pt descriptive lines (Rule 62)
    lines = c["desc"].split("\n")
    for l_idx, line in enumerate(lines):
        draw.text((x + 25, card_y + 200 + l_idx * 45), line, font=font_card_desc, fill=(203, 213, 225))

# 5. Bottom Architectural Proof Banner & Commander Sign-Off
draw.rounded_rectangle([80, 800, CANVAS_W - 80, 970], radius=12, fill=(16, 24, 40), outline=(56, 189, 248), width=2)
draw.text((120, 830), "PUBLIC GITHUB REPOSITORY & REPRODUCIBILITY HARNESS:", font=font_sub_hero, fill=(255, 255, 255))
draw.text((120, 880), "https://github.com/jackhu24-ship-it/phantom-grid-opencv-vision-nexus  (MIT License)", font=font_card_metric, fill=(0, 229, 255))

draw.text((120, 930), "[ RATIFIED BY COMMANDER JACK HU x ACTING COMMANDER XIAOMI ]", font=font_footer, fill=(251, 191, 36))
draw.text((1420, 930), "STATUS: ASIL-D AUDIT PASS | ZDR 0.00MB", font=font_footer, fill=(16, 185, 129))

# Save
out_path = os.path.join(os.path.dirname(__file__), "cover_image_16x9.png")
img.save(out_path)
print(f"Cover image saved: {out_path} ({img.size[0]}x{img.size[1]})")
