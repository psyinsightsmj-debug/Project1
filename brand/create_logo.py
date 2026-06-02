from PIL import Image, ImageDraw, ImageFont
import math, os

# ─── NEW COLOR SYSTEM: Shiny Bronze / Greek Statue ───────────────
# Think: dramatic museum lighting on ancient bronze sculpture
OBSIDIAN        = (10, 11, 13)         # Near-black — the void
DEEP_SHADOW     = (20, 22, 26)         # Dark panel
BRONZE_SHADOW   = (80, 52, 28)         # Deep bronze shadow
BRONZE_MID      = (140, 95, 48)        # True bronze midtone
BRONZE_SHINE    = (205, 152, 80)       # Bright bronze highlight
BRONZE_SPECULAR = (242, 210, 140)      # Specular hit — almost white-gold
STATUE_WHITE    = (252, 248, 238)      # The brightest light on marble/bronze
WARM_SHADOW     = (45, 35, 22)         # Dark warm shadow panel
PATINA          = (88, 110, 90)        # Ancient green patina — subtle accent
MID_TONE        = (160, 140, 110)      # Mid text / secondary elements

# ─── Fonts ───────────────────────────────────────────────────────
F_SERIF_BOLD   = '/usr/share/fonts/opentype/urw-base35/P052-Bold.otf'
F_SERIF_ROMAN  = '/usr/share/fonts/opentype/urw-base35/P052-Roman.otf'
F_SERIF_ITALIC = '/usr/share/fonts/opentype/urw-base35/P052-Italic.otf'
F_SANS_BOLD    = '/usr/share/fonts/opentype/urw-base35/NimbusSans-Bold.otf'
F_SANS         = '/usr/share/fonts/opentype/urw-base35/NimbusSans-Regular.otf'
F_GOTHIC       = '/usr/share/fonts/opentype/urw-base35/URWGothic-Demi.otf'
F_GOTHIC_BOOK  = '/usr/share/fonts/opentype/urw-base35/URWGothic-Book.otf'

os.makedirs('/home/user/Project1/brand', exist_ok=True)


def draw_bronze_gradient_text(d, text, font, x, y, width_hint=None):
    """Simulate bronze sheen on text by drawing it multiple times with offsets."""
    # Shadow layer
    d.text((x+3, y+3), text, font=font, fill=BRONZE_SHADOW)
    # Deep midtone
    d.text((x+1, y+1), text, font=font, fill=BRONZE_MID)
    # Main bright bronze
    d.text((x, y), text, font=font, fill=BRONZE_SHINE)
    # Specular highlight — slightly offset up-left to simulate top light
    d.text((x-1, y-1), text, font=font, fill=BRONZE_SPECULAR)


def make_logo():
    W, H = 2600, 1000
    img = Image.new('RGB', (W, H), OBSIDIAN)
    d = ImageDraw.Draw(img)

    # ── Dark atmospheric vignette: lighter center strip ──
    for i in range(120):
        alpha = int(12 * (1 - i / 120))
        shade = tuple(min(255, c + alpha) for c in OBSIDIAN)
        d.rectangle([0, H//2 - 120 + i, W, H//2 - 120 + i + 1], fill=shade)

    # ── Icon: Classical Greek/Roman medallion ──
    cx, cy = 185, H // 2

    # Outer ring — thick bronze
    r1 = 90
    for thickness in range(4, 0, -1):
        t_color = [BRONZE_SHADOW, BRONZE_MID, BRONZE_SHINE, BRONZE_SPECULAR][4 - thickness]
        d.ellipse([cx - r1 - thickness, cy - r1 - thickness,
                   cx + r1 + thickness, cy + r1 + thickness],
                  outline=t_color, width=1)

    # Inner ring
    r2 = 68
    d.ellipse([cx - r2, cy - r2, cx + r2, cy + r2], outline=BRONZE_MID, width=1)

    # Diamond / laurel shape inside
    r3 = 46
    pts = [
        (cx,      cy - r3),
        (cx + r3, cy),
        (cx,      cy + r3),
        (cx - r3, cy),
    ]
    # Draw diamond with layered bronze effect
    d.polygon(pts, outline=BRONZE_SHADOW, width=4)
    d.polygon(pts, outline=BRONZE_SHINE, width=2)
    d.polygon(pts, outline=BRONZE_SPECULAR, width=1)

    # Radiating spokes — like a sun or laurel crown
    for angle in range(0, 360, 30):
        rad = math.radians(angle)
        r_start = r3 + 6
        r_end = r2 - 6
        x1 = cx + int(math.cos(rad) * r_start)
        y1 = cy + int(math.sin(rad) * r_start)
        x2 = cx + int(math.cos(rad) * r_end)
        y2 = cy + int(math.sin(rad) * r_end)
        # Alternate bright/dim spokes for 3D depth
        col = BRONZE_SPECULAR if angle % 60 == 0 else BRONZE_MID
        d.line([(x1, y1), (x2, y2)], fill=col, width=1)

    # Central spark — bright core
    d.ellipse([cx - 7, cy - 7, cx + 7, cy + 7], fill=BRONZE_SHADOW)
    d.ellipse([cx - 5, cy - 5, cx + 5, cy + 5], fill=BRONZE_SHINE)
    d.ellipse([cx - 2, cy - 2, cx + 2, cy + 2], fill=BRONZE_SPECULAR)

    # ── Wordmark ──
    font_v = ImageFont.truetype(F_SERIF_ROMAN, 152)
    font_s = ImageFont.truetype(F_SERIF_BOLD, 152)
    font_tag = ImageFont.truetype(F_GOTHIC_BOOK, 38)
    font_sub = ImageFont.truetype(F_GOTHIC_BOOK, 27)

    x_word = 320
    y_word = H // 2 - 155

    # "Vision" — cream/statue-white with subtle depth
    d.text((x_word + 2, y_word + 2), "Vision", font=font_v, fill=BRONZE_SHADOW)
    d.text((x_word, y_word), "Vision", font=font_v, fill=STATUE_WHITE)

    # Width of "Vision"
    v_bbox = d.textbbox((x_word, y_word), "Vision", font=font_v)
    x_spark = v_bbox[2]

    # "Spark" — full layered bronze sheen
    draw_bronze_gradient_text(d, "Spark", font_s, x_spark, y_word)

    # ── Divider rule with bronze gradient feel ──
    rule_y = y_word + 172
    for i, col in enumerate([BRONZE_SHADOW, BRONZE_MID, BRONZE_SHINE, BRONZE_SPECULAR, BRONZE_SHINE, BRONZE_MID, BRONZE_SHADOW]):
        d.rectangle([x_word + i * 120, rule_y, x_word + (i + 1) * 120, rule_y + 1], fill=col)

    # ── Tagline ──
    tag_y = rule_y + 26
    d.text((x_word + 1, tag_y + 1), "IGNITE YOUR VISION. BUILD YOUR LIFE.",
           font=font_tag, fill=BRONZE_SHADOW)
    d.text((x_word, tag_y), "IGNITE YOUR VISION. BUILD YOUR LIFE.",
           font=font_tag, fill=BRONZE_SPECULAR)

    # ── Subtitle ──
    sub_y = tag_y + 62
    d.text((x_word, sub_y), "CLARITY  ·  STRATEGY  ·  FREEDOM",
           font=font_sub, fill=MID_TONE)

    # ── Right accent: patina green vertical bar (classical oxidized bronze) ──
    d.rectangle([W - 8, 100, W - 6, H - 100], fill=PATINA)
    d.rectangle([W - 5, 100, W - 4, H - 100], fill=BRONZE_MID)

    out = '/home/user/Project1/brand/visionspark-logo-primary.png'
    img.save(out, 'PNG', dpi=(300, 300))
    print(f'Saved: {out}')


def make_logo_square():
    W = H = 1200
    img = Image.new('RGB', (W, H), OBSIDIAN)
    d = ImageDraw.Draw(img)

    # Border frame — bronze
    for i, col in enumerate([BRONZE_SHADOW, BRONZE_MID, BRONZE_SHINE]):
        offset = 40 + i
        d.rectangle([offset, offset, W - offset, H - offset], outline=col, width=1)

    # ── Icon ──
    cx, cy = W // 2, 390
    r1 = 120
    for t, col in enumerate([BRONZE_SHADOW, BRONZE_MID, BRONZE_SHINE, BRONZE_SPECULAR]):
        d.ellipse([cx - r1 + t, cy - r1 + t, cx + r1 - t, cy + r1 - t],
                  outline=col, width=1)

    r3 = 65
    pts = [(cx, cy - r3), (cx + r3, cy), (cx, cy + r3), (cx - r3, cy)]
    d.polygon(pts, outline=BRONZE_SHADOW, width=4)
    d.polygon(pts, outline=BRONZE_SHINE, width=2)
    d.polygon(pts, outline=BRONZE_SPECULAR, width=1)

    r2 = 92
    for angle in range(0, 360, 30):
        rad = math.radians(angle)
        x1 = cx + int(math.cos(rad) * (r3 + 8))
        y1 = cy + int(math.sin(rad) * (r3 + 8))
        x2 = cx + int(math.cos(rad) * (r2 - 8))
        y2 = cy + int(math.sin(rad) * (r2 - 8))
        col = BRONZE_SPECULAR if angle % 60 == 0 else BRONZE_MID
        d.line([(x1, y1), (x2, y2)], fill=col, width=1)

    d.ellipse([cx - 8, cy - 8, cx + 8, cy + 8], fill=BRONZE_SHINE)
    d.ellipse([cx - 3, cy - 3, cx + 3, cy + 3], fill=BRONZE_SPECULAR)

    # ── Stacked wordmark ──
    font_v = ImageFont.truetype(F_SERIF_ROMAN, 115)
    font_s = ImageFont.truetype(F_SERIF_BOLD, 115)
    font_tag = ImageFont.truetype(F_GOTHIC_BOOK, 30)
    font_sub = ImageFont.truetype(F_GOTHIC_BOOK, 23)

    # Measure for centering
    v_bbox = d.textbbox((0, 0), "Vision", font=font_v)
    s_bbox = d.textbbox((0, 0), "Spark", font=font_s)
    total_w = (v_bbox[2] - v_bbox[0]) + (s_bbox[2] - s_bbox[0])
    tx = (W - total_w) // 2
    ty = cy + r1 + 45

    d.text((tx + 2, ty + 2), "Vision", font=font_v, fill=BRONZE_SHADOW)
    d.text((tx, ty), "Vision", font=font_v, fill=STATUE_WHITE)
    vw = v_bbox[2] - v_bbox[0]
    draw_bronze_gradient_text(d, "Spark", font_s, tx + vw, ty)

    rule_y = ty + 125
    d.rectangle([(W // 2) - 210, rule_y, (W // 2) + 210, rule_y + 1], fill=BRONZE_SHINE)

    tag = "IGNITE YOUR VISION. BUILD YOUR LIFE."
    tb = d.textbbox((0, 0), tag, font=font_tag)
    d.text(((W - (tb[2]-tb[0])) // 2, rule_y + 22), tag, font=font_tag, fill=BRONZE_SPECULAR)

    sub = "CLARITY  ·  STRATEGY  ·  FREEDOM"
    sb = d.textbbox((0, 0), sub, font=font_sub)
    d.text(((W - (sb[2]-sb[0])) // 2, rule_y + 68), sub, font=font_sub, fill=MID_TONE)

    out = '/home/user/Project1/brand/visionspark-logo-square.png'
    img.save(out, 'PNG', dpi=(300, 300))
    print(f'Saved: {out}')


def make_palette():
    W, H = 2600, 1100
    img = Image.new('RGB', (W, H), OBSIDIAN)
    d = ImageDraw.Draw(img)

    font_title = ImageFont.truetype(F_SERIF_BOLD, 58)
    font_name  = ImageFont.truetype(F_GOTHIC, 30)
    font_hex   = ImageFont.truetype(F_GOTHIC_BOOK, 25)
    font_desc  = ImageFont.truetype(F_GOTHIC_BOOK, 21)
    font_label = ImageFont.truetype(F_SANS, 20)

    d.text((100, 68), "VisionSpark — Bronze Statue Color System", font=font_title, fill=BRONZE_SPECULAR)
    d.rectangle([100, 146, 820, 147], fill=BRONZE_MID)

    colors = [
        (OBSIDIAN,        "Obsidian",        "#0A0B0D", "Primary Background"),
        (DEEP_SHADOW,     "Deep Shadow",     "#141619", "Secondary Background"),
        (WARM_SHADOW,     "Warm Shadow",     "#2D2316", "Card / Panel"),
        (BRONZE_SHADOW,   "Bronze Shadow",   "#50341C", "Deep Accent"),
        (BRONZE_MID,      "True Bronze",     "#8C5F30", "Mid Accent / Borders"),
        (BRONZE_SHINE,    "Bronze Shine",    "#CD9850", "Primary Accent"),
        (BRONZE_SPECULAR, "Specular Hit",    "#F2D28C", "Highlight / CTA"),
        (STATUE_WHITE,    "Statue Light",    "#FCF8EE", "Primary Text"),
        (PATINA,          "Ancient Patina",  "#586E5A", "Subtle Accent"),
        (MID_TONE,        "Worn Bronze",     "#A08C6E", "Secondary Text"),
    ]

    swatch_w = 210
    swatch_h = 560
    gap = 28
    total = len(colors) * swatch_w + (len(colors) - 1) * gap
    start_x = (W - total) // 2
    swatch_y = 210

    for i, (color, name, hex_val, desc) in enumerate(colors):
        x = start_x + i * (swatch_w + gap)
        d.rectangle([x, swatch_y, x + swatch_w, swatch_y + swatch_h], fill=color)

        # Top edge highlight on bronze colors
        if 'Bronze' in name or 'Specular' in name or 'Shine' in name:
            d.rectangle([x, swatch_y, x + swatch_w, swatch_y + 2], fill=BRONZE_SPECULAR)
            d.rectangle([x, swatch_y + swatch_h - 2, x + swatch_w, swatch_y + swatch_h], fill=BRONZE_SHADOW)

        name_y = swatch_y + swatch_h + 22
        is_bronze = any(k in name for k in ['Bronze', 'Specular', 'Shine', 'Patina'])
        text_col = BRONZE_SPECULAR if is_bronze else STATUE_WHITE
        d.text((x, name_y), name, font=font_name, fill=text_col)
        d.text((x, name_y + 40), hex_val, font=font_hex, fill=BRONZE_MID)
        d.text((x, name_y + 72), desc, font=font_desc, fill=(90, 80, 65))

    d.rectangle([100, H - 75, W - 100, H - 74], fill=BRONZE_MID)
    d.text((100, H - 58), "visionsparkinnovation.com", font=font_label, fill=(80, 68, 52))

    out = '/home/user/Project1/brand/visionspark-palette.png'
    img.save(out, 'PNG', dpi=(300, 300))
    print(f'Saved: {out}')


if __name__ == '__main__':
    make_logo()
    make_logo_square()
    make_palette()
    print('All bronze brand assets generated.')
