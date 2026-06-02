from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math, os

# ─── Brand Colors ───────────────────────────────────────────────
DEEP_GROUND   = (15, 18, 20)        # Near-black with depth
RICH_DARK     = (22, 27, 30)        # Slightly lighter panel
GOLD_PRIMARY  = (212, 175, 95)      # Burnished gold
GOLD_LIGHT    = (235, 205, 130)     # Highlight gold
GOLD_MUTED    = (150, 120, 60)      # Muted gold for accents
OFF_WHITE     = (245, 240, 228)     # Warm cream
MID_GRAY      = (110, 108, 100)     # Subdued text

# ─── Fonts ──────────────────────────────────────────────────────
F_SERIF_BOLD   = '/usr/share/fonts/opentype/urw-base35/P052-Bold.otf'
F_SERIF_ROMAN  = '/usr/share/fonts/opentype/urw-base35/P052-Roman.otf'
F_SERIF_ITALIC = '/usr/share/fonts/opentype/urw-base35/P052-Italic.otf'
F_SANS_BOLD    = '/usr/share/fonts/opentype/urw-base35/NimbusSans-Bold.otf'
F_SANS         = '/usr/share/fonts/opentype/urw-base35/NimbusSans-Regular.otf'
F_GOTHIC       = '/usr/share/fonts/opentype/urw-base35/URWGothic-Demi.otf'
F_GOTHIC_BOOK  = '/usr/share/fonts/opentype/urw-base35/URWGothic-Book.otf'

def make_logo():
    """Primary logo — wordmark + icon on dark ground."""
    W, H = 2400, 1000
    img = Image.new('RGB', (W, H), DEEP_GROUND)
    d = ImageDraw.Draw(img)

    # ── Subtle texture: fine horizontal lines ──
    for y in range(0, H, 6):
        alpha = 8
        d.line([(0, y), (W, y)], fill=(255, 255, 255, alpha), width=1)

    # ── Icon: geometric spark / diamond with ray ──
    cx, cy = 200, H // 2
    # Outer thin circle
    r_outer = 72
    d.ellipse([cx - r_outer, cy - r_outer, cx + r_outer, cy + r_outer],
              outline=GOLD_MUTED, width=1)

    # Inner diamond (rotated square)
    r_inner = 38
    diamond = [
        (cx,           cy - r_inner),
        (cx + r_inner, cy),
        (cx,           cy + r_inner),
        (cx - r_inner, cy),
    ]
    d.polygon(diamond, outline=GOLD_PRIMARY, fill=None)
    d.polygon(diamond, outline=GOLD_PRIMARY, width=2)

    # Spark lines radiating from center
    angles = [45, 135, 225, 315]
    for angle in angles:
        rad = math.radians(angle)
        x1 = cx + int(math.cos(rad) * 14)
        y1 = cy + int(math.sin(rad) * 14)
        x2 = cx + int(math.cos(rad) * r_outer - 4)
        y2 = cy + int(math.sin(rad) * r_outer - 4)
        d.line([(x1, y1), (x2, y2)], fill=GOLD_PRIMARY, width=1)

    # Center dot
    d.ellipse([cx - 5, cy - 5, cx + 5, cy + 5], fill=GOLD_PRIMARY)

    # ── Wordmark: "VisionSpark" ──
    # Vision = lighter weight, Spark = bold gold
    x_word = 320
    y_word_top = H // 2 - 160

    font_brand_vision = ImageFont.truetype(F_SERIF_ROMAN, 148)
    font_brand_spark  = ImageFont.truetype(F_SERIF_BOLD, 148)
    font_tag          = ImageFont.truetype(F_GOTHIC_BOOK, 36)
    font_sub          = ImageFont.truetype(F_GOTHIC_BOOK, 26)
    font_divider      = ImageFont.truetype(F_SANS, 22)

    # "Vision" in warm cream
    d.text((x_word, y_word_top), "Vision", font=font_brand_vision, fill=OFF_WHITE)
    vision_bbox = d.textbbox((x_word, y_word_top), "Vision", font=font_brand_vision)
    x_spark = vision_bbox[2]

    # "Spark" in gold
    d.text((x_spark, y_word_top), "Spark", font=font_brand_spark, fill=GOLD_PRIMARY)

    # ── Thin gold rule under wordmark ──
    rule_y = y_word_top + 168
    d.rectangle([x_word, rule_y, x_word + 820, rule_y + 1], fill=GOLD_MUTED)

    # ── Tagline ──
    tag_text = "IGNITE YOUR VISION. BUILD YOUR LIFE."
    tag_y = rule_y + 24
    d.text((x_word, tag_y), tag_text, font=font_tag, fill=GOLD_LIGHT,
           spacing=4)

    # ── Subtitle with flanking ornaments ──
    sub_text = "CLARITY  ·  STRATEGY  ·  FREEDOM"
    sub_y = tag_y + 60
    d.text((x_word, sub_y), sub_text, font=font_sub, fill=MID_GRAY, spacing=6)

    # ── Right edge: thin vertical gold line (editorial accent) ──
    d.rectangle([W - 3, 80, W - 2, H - 80], fill=GOLD_MUTED)

    out = '/home/user/Project1/brand/visionspark-logo-primary.png'
    img.save(out, 'PNG', dpi=(300, 300))
    print(f'Saved: {out}')


def make_logo_dark_square():
    """Square logo variant — icon + stacked wordmark for social/favicon."""
    W = H = 1200
    img = Image.new('RGB', (W, H), DEEP_GROUND)
    d = ImageDraw.Draw(img)

    # Background panel
    margin = 60
    d.rectangle([margin, margin, W - margin, H - margin],
                outline=GOLD_MUTED, width=1)

    # ── Icon centered upper half ──
    cx, cy = W // 2, 400
    r_outer = 110
    d.ellipse([cx - r_outer, cy - r_outer, cx + r_outer, cy + r_outer],
              outline=GOLD_MUTED, width=1)

    r_inner = 58
    diamond = [
        (cx,           cy - r_inner),
        (cx + r_inner, cy),
        (cx,           cy + r_inner),
        (cx - r_inner, cy),
    ]
    d.polygon(diamond, outline=GOLD_PRIMARY, width=3)

    # Spark rays
    for angle in [45, 135, 225, 315]:
        rad = math.radians(angle)
        x1 = cx + int(math.cos(rad) * 22)
        y1 = cy + int(math.sin(rad) * 22)
        x2 = cx + int(math.cos(rad) * (r_outer - 8))
        y2 = cy + int(math.sin(rad) * (r_outer - 8))
        d.line([(x1, y1), (x2, y2)], fill=GOLD_PRIMARY, width=2)

    d.ellipse([cx - 8, cy - 8, cx + 8, cy + 8], fill=GOLD_PRIMARY)

    # ── Stacked wordmark ──
    font_vs = ImageFont.truetype(F_SERIF_BOLD, 110)
    font_tag = ImageFont.truetype(F_GOTHIC_BOOK, 30)
    font_sub = ImageFont.truetype(F_GOTHIC_BOOK, 22)

    # Center "VisionSpark"
    vs_text = "VisionSpark"
    bbox = d.textbbox((0, 0), vs_text, font=font_vs)
    tw = bbox[2] - bbox[0]
    tx = (W - tw) // 2
    ty = cy + r_outer + 40

    # Draw "Vision" cream, "Spark" gold
    font_v = ImageFont.truetype(F_SERIF_ROMAN, 110)
    v_bbox = d.textbbox((0, 0), "Vision", font=font_v)
    vw = v_bbox[2] - v_bbox[0]
    s_bbox = d.textbbox((0, 0), "Spark", font=font_vs)
    sw = s_bbox[2] - s_bbox[0]
    total_w = vw + sw
    tx = (W - total_w) // 2

    d.text((tx, ty), "Vision", font=font_v, fill=OFF_WHITE)
    d.text((tx + vw, ty), "Spark", font=font_vs, fill=GOLD_PRIMARY)

    # Rule
    rule_y = ty + 118
    d.rectangle([(W // 2) - 200, rule_y, (W // 2) + 200, rule_y + 1], fill=GOLD_MUTED)

    # Tagline
    tag = "IGNITE YOUR VISION. BUILD YOUR LIFE."
    tag_bbox = d.textbbox((0, 0), tag, font=font_tag)
    tag_w = tag_bbox[2] - tag_bbox[0]
    d.text(((W - tag_w) // 2, rule_y + 20), tag, font=font_tag, fill=GOLD_LIGHT)

    # Sub
    sub = "CLARITY  ·  STRATEGY  ·  FREEDOM"
    sub_bbox = d.textbbox((0, 0), sub, font=font_sub)
    sub_w = sub_bbox[2] - sub_bbox[0]
    d.text(((W - sub_w) // 2, rule_y + 66), sub, font=font_sub, fill=MID_GRAY)

    out = '/home/user/Project1/brand/visionspark-logo-square.png'
    img.save(out, 'PNG', dpi=(300, 300))
    print(f'Saved: {out}')


def make_palette():
    """Brand color palette card."""
    W, H = 2400, 1100
    img = Image.new('RGB', (W, H), DEEP_GROUND)
    d = ImageDraw.Draw(img)

    font_title  = ImageFont.truetype(F_SERIF_BOLD, 60)
    font_name   = ImageFont.truetype(F_GOTHIC, 32)
    font_hex    = ImageFont.truetype(F_GOTHIC_BOOK, 26)
    font_desc   = ImageFont.truetype(F_GOTHIC_BOOK, 22)
    font_label  = ImageFont.truetype(F_SANS, 20)

    # ── Title ──
    d.text((100, 70), "VisionSpark — Brand Color System", font=font_title, fill=OFF_WHITE)
    d.rectangle([100, 148, 100 + 600, 149], fill=GOLD_MUTED)

    # ── Color swatches ──
    colors = [
        (DEEP_GROUND,   "Deep Ground",    "#0F1214", "Primary Background"),
        (RICH_DARK,     "Rich Dark",       "#161B1E", "Secondary Background"),
        (GOLD_PRIMARY,  "Sovereign Gold",  "#D4AF5F", "Primary Accent"),
        (GOLD_LIGHT,    "Ignite Gold",     "#EBCD82", "Highlight / CTA"),
        (GOLD_MUTED,    "Ember",           "#967830", "Borders / Dividers"),
        (OFF_WHITE,     "Warm Cream",      "#F5F0E4", "Primary Text"),
        (MID_GRAY,      "Ash",             "#6E6C64", "Secondary Text"),
        ((40, 48, 52),  "Slate Depth",     "#283034", "Card / Panel"),
    ]

    swatch_w = 240
    swatch_h = 600
    gap = 40
    start_x = (W - (len(colors) * swatch_w + (len(colors) - 1) * gap)) // 2
    swatch_y = 210

    for i, (color, name, hex_val, desc) in enumerate(colors):
        x = start_x + i * (swatch_w + gap)

        # Main swatch block
        d.rectangle([x, swatch_y, x + swatch_w, swatch_y + swatch_h],
                    fill=color)

        # Gold border on accent colors
        if 'Gold' in name or name == 'Ember':
            d.rectangle([x, swatch_y, x + swatch_w, swatch_y + swatch_h],
                        outline=GOLD_MUTED, width=1)

        # Color name
        name_y = swatch_y + swatch_h + 24
        text_color = GOLD_LIGHT if 'Gold' in name or name == 'Ember' else OFF_WHITE
        d.text((x, name_y), name, font=font_name, fill=text_color)

        # Hex
        d.text((x, name_y + 42), hex_val, font=font_hex, fill=MID_GRAY)

        # Desc
        d.text((x, name_y + 76), desc, font=font_desc, fill=(80, 78, 70))

    # ── Bottom rule + brand name ──
    d.rectangle([100, H - 80, W - 100, H - 79], fill=GOLD_MUTED)
    d.text((100, H - 60), "visionsparkinnovation.com", font=font_label, fill=(70, 68, 60))

    out = '/home/user/Project1/brand/visionspark-palette.png'
    img.save(out, 'PNG', dpi=(300, 300))
    print(f'Saved: {out}')


if __name__ == '__main__':
    make_logo()
    make_logo_dark_square()
    make_palette()
    print('All brand assets generated.')
