"""
Pinterest Pins — Arc 3 / The Personal Reset System™
3 pins, 1000×1500px, VisionSpark design system
Psychology rationale per pin is in the comment above each section.
"""

from PIL import Image, ImageDraw, ImageFont
import os, textwrap

# ── Paths ──────────────────────────────────────────────────────────────────
FONT_DIR   = "/usr/share/fonts/truetype/liberation"
SERIF_B    = os.path.join(FONT_DIR, "LiberationSerif-Bold.ttf")
SERIF_I    = os.path.join(FONT_DIR, "LiberationSerif-Italic.ttf")
SERIF_BI   = os.path.join(FONT_DIR, "LiberationSerif-BoldItalic.ttf")
SERIF_R    = os.path.join(FONT_DIR, "LiberationSerif-Regular.ttf")
SANS_B     = os.path.join(FONT_DIR, "LiberationSans-Bold.ttf")
SANS_R     = os.path.join(FONT_DIR, "LiberationSans-Regular.ttf")
OUT_DIR    = os.path.dirname(os.path.abspath(__file__))

W, H = 1000, 1500

# ── Palette ────────────────────────────────────────────────────────────────
OAT       = (250, 246, 237)
INK       = (42,  34,  24)
FOREST    = (59,  110, 90)
AMBER     = (201, 137, 42)
TERRA     = (168, 81,  58)
SAND      = (212, 201, 184)
TAUPE     = (138, 126, 112)
IVORY     = (255, 253, 248)
WHITE     = (255, 255, 255)
FOREST_DK = (46,  85,  69)
AMBER_LT  = (224, 155, 50)


# ── Helpers ────────────────────────────────────────────────────────────────

def load(path, size):
    return ImageFont.truetype(path, size)

def wrap_text(draw, text, font, max_w):
    """Word-wrap text to fit max_w pixels. Returns list of lines."""
    words = text.split()
    lines, line = [], []
    for w in words:
        test = " ".join(line + [w])
        if draw.textlength(test, font=font) <= max_w:
            line.append(w)
        else:
            if line:
                lines.append(" ".join(line))
            line = [w]
    if line:
        lines.append(" ".join(line))
    return lines

def draw_text_block(draw, lines, font, x, y, color, line_gap=12, center=False, img_w=None):
    """Draw pre-wrapped lines, return bottom y."""
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        lw = bbox[2] - bbox[0]
        lh = bbox[3] - bbox[1]
        cx = (img_w - lw) // 2 if center and img_w else x
        draw.text((cx, y), line, font=font, fill=color)
        y += lh + line_gap
    return y

def horz_rule(draw, x1, x2, y, color, thick=2):
    draw.rectangle([x1, y, x2, y + thick], fill=color)

def accent_bar(draw, x, y, w, h, color):
    draw.rectangle([x, y, x + w, y + h], fill=color)

def brand_tag(draw, img, y_bottom, bg_color, text_color):
    """Small brand strip at bottom."""
    strip_h = 60
    draw.rectangle([0, H - strip_h, W, H], fill=bg_color)
    font = load(SANS_B, 18)
    label = "visionsparkinnovation.com"
    lw = draw.textlength(label, font=font)
    draw.text(((W - lw) // 2, H - strip_h + 20), label, font=font, fill=text_color)


# ══════════════════════════════════════════════════════════════════════════
# PIN 4
# Psychology: Warm Oat bg = safety/comfort; Amber accent = optimism/action;
# "I tried everything" hook = mirror-of-self recognition (highest empathy trigger);
# Serif bold headline = authority + trust; decorative rule = editorial gravitas.
# Subconscious trigger: IDENTIFICATION — reader sees their own story.
# ══════════════════════════════════════════════════════════════════════════

def make_pin4():
    img  = Image.new("RGB", (W, H), OAT)
    draw = ImageDraw.Draw(img)

    PAD = 80

    # Top amber accent bar
    accent_bar(draw, 0, 0, W, 8, AMBER)

    # Category eyebrow
    eyebrow_font = load(SANS_B, 22)
    eyebrow = "HABIT RESET · 30 DAYS · 5 MODULES"
    ew = draw.textlength(eyebrow, font=eyebrow_font)
    draw.text(((W - ew) // 2, 60), eyebrow, font=eyebrow_font, fill=TAUPE)

    # Thin rule under eyebrow
    horz_rule(draw, PAD, W - PAD, 100, SAND)

    # Main headline — large serif bold italic
    h1_font  = load(SERIF_BI, 88)
    h1_lines = [
        "I Tried Every",
        "Habit App.",
        "Nothing Worked",
        "Until I Did This."
    ]
    y = 140
    for line in h1_lines:
        lw = draw.textlength(line, font=h1_font)
        draw.text(((W - lw) // 2, y), line, font=h1_font, fill=INK)
        y += 96

    # Amber accent rule
    rule_w = 80
    y += 20
    horz_rule(draw, (W - rule_w) // 2, (W + rule_w) // 2, y, AMBER, 4)
    y += 36

    # Sub-message box — ivory card
    card_pad = 50
    card_h   = 160
    card_y   = y
    draw.rectangle([PAD, card_y, W - PAD, card_y + card_h], fill=IVORY)
    # left terra accent stripe
    accent_bar(draw, PAD, card_y, 5, card_h, TERRA)

    sub_font  = load(SERIF_I, 38)
    sub_text  = "30 Days. 5 Modules.\nOne System That Finally Sticks."
    sub_lines = sub_text.split("\n")
    sy = card_y + 32
    for sl in sub_lines:
        slw = draw.textlength(sl, font=sub_font)
        draw.text(((W - slw) // 2, sy), sl, font=sub_font, fill=FOREST)
        sy += 52
    y = card_y + card_h + 50

    # Middle section — 3 proof points
    point_font = load(SANS_B, 26)
    points = [
        "✓  No streak pressure",
        "✓  20-minute daily cap",
        "✓  Built for real life",
    ]
    for pt in points:
        pw = draw.textlength(pt, font=point_font)
        draw.text(((W - pw) // 2, y), pt, font=point_font, fill=FOREST)
        y += 48
    y += 20

    # Product name badge
    badge_h = 90
    draw.rectangle([PAD, y, W - PAD, y + badge_h], fill=AMBER)
    prod_font = load(SERIF_B, 42)
    prod_label = "The Personal Reset System™"
    plw = draw.textlength(prod_label, font=prod_font)
    draw.text(((W - plw) // 2, y + 22), prod_label, font=prod_font, fill=INK)
    y += badge_h + 40

    # Price
    price_font = load(SERIF_B, 64)
    price = "$17 · Instant Download"
    pw = draw.textlength(price, font=price_font)
    draw.text(((W - pw) // 2, y), price, font=price_font, fill=TERRA)
    y += 80

    # Bottom rule
    horz_rule(draw, PAD, W - PAD, y, SAND)

    # Brand tag
    brand_tag(draw, img, H, INK, TAUPE)

    # Bottom amber bar
    accent_bar(draw, 0, H - 8, W, 8, AMBER)

    img.save(os.path.join(OUT_DIR, "pin-4.png"), "PNG", dpi=(300, 300))
    print("✓ pin-4.png saved")


# ══════════════════════════════════════════════════════════════════════════
# PIN 5
# Psychology: Deep Forest bg = calm, growth, safety after chaos;
# White text = clarity/relief contrast; "Stop Rebuilding From Zero" =
# loss-aversion framing (stop the pain); Before/after emotional shift
# embedded in language without showing images.
# Subconscious trigger: RELIEF — the exhaustion of starting over, resolved.
# ══════════════════════════════════════════════════════════════════════════

def make_pin5():
    img  = Image.new("RGB", (W, H), FOREST)
    draw = ImageDraw.Draw(img)

    PAD = 80

    # Subtle texture — repeating diagonal light lines
    for i in range(0, W + H, 40):
        draw.line([(i, 0), (0, i)], fill=FOREST_DK, width=1)

    # Top ivory accent bar
    accent_bar(draw, 0, 0, W, 8, IVORY)

    # Eyebrow
    ey_font = load(SANS_B, 20)
    ey = "THE PERSONAL RESET SYSTEM™"
    ew = draw.textlength(ey, font=ey_font)
    draw.text(((W - ew) // 2, 55), ey, font=ey_font, fill=(180, 220, 200))

    horz_rule(draw, PAD, W - PAD, 93, (80, 140, 110), 1)

    # Main headline
    h1_font = load(SERIF_B, 100)
    h1_lines = ["Stop", "Rebuilding", "From Zero."]
    y = 130
    for line in h1_lines:
        lw = draw.textlength(line, font=h1_font)
        draw.text(((W - lw) // 2, y), line, font=h1_font, fill=WHITE)
        y += 108

    # Amber underline accent
    y += 10
    horz_rule(draw, (W - 120) // 2, (W + 120) // 2, y, AMBER, 5)
    y += 40

    # Sub-headline
    sub_font = load(SERIF_I, 48)
    sub = "Start From Here."
    sw = draw.textlength(sub, font=sub_font)
    draw.text(((W - sw) // 2, y), sub, font=sub_font, fill=AMBER)
    y += 80

    # Divider dots
    dot_y = y + 10
    for dx in [-40, 0, 40]:
        draw.ellipse([(W//2 + dx - 5, dot_y - 5), (W//2 + dx + 5, dot_y + 5)], fill=(180, 220, 200))
    y = dot_y + 40

    # Body message — ivory card
    card_h = 200
    draw.rectangle([PAD, y, W - PAD, y + card_h], fill=(46, 85, 69))
    # Top amber stripe on card
    accent_bar(draw, PAD, y, W - 2*PAD, 4, AMBER)

    body_font = load(SERIF_I, 36)
    body_lines = [
        "30 days to a life",
        "you don’t want to escape.",
        "",
        "No streaks. No shame.",
        "Just a method that works.",
    ]
    by = y + 24
    for bl in body_lines:
        if bl == "":
            by += 14
            continue
        blw = draw.textlength(bl, font=body_font)
        draw.text(((W - blw) // 2, by), bl, font=body_font, fill=WHITE)
        by += 48
    y += card_h + 40

    # 5 modules strip
    mod_font = load(SANS_B, 22)
    mods = ["MINDSET", "ENERGY", "PRODUCTIVITY", "HABITS", "INTEGRATION"]
    strip_h = 56
    draw.rectangle([0, y, W, y + strip_h], fill=AMBER)
    mx = 40
    for mod in mods:
        mw = draw.textlength(mod, font=mod_font)
        draw.text((mx, y + 16), mod, font=mod_font, fill=INK)
        mx += mw + 28
        if mod != mods[-1]:
            draw.text((mx - 16, y + 16), "·", font=mod_font, fill=INK)
    y += strip_h + 40

    # Price
    price_font = load(SERIF_B, 56)
    price = "$17 · Instant Digital Download"
    pw = draw.textlength(price, font=price_font)
    draw.text(((W - pw) // 2, y), price, font=price_font, fill=WHITE)
    y += 70

    # Brand tag
    draw.rectangle([0, H - 60, W, H], fill=(30, 60, 48))
    b_font = load(SANS_B, 18)
    bl = "visionsparkinnovation.com"
    blw = draw.textlength(bl, font=b_font)
    draw.text(((W - blw) // 2, H - 40), bl, font=b_font, fill=(180, 220, 200))

    # Bottom ivory bar
    accent_bar(draw, 0, H - 8, W, 8, IVORY)

    img.save(os.path.join(OUT_DIR, "pin-5.png"), "PNG", dpi=(300, 300))
    print("✓ pin-5.png saved")


# ══════════════════════════════════════════════════════════════════════════
# PIN 6
# Psychology: Terracotta bg = warmth + urgency + disruption (pattern-interrupt);
# White + Amber text = authority contrast on warm ground;
# Contrarian hook = curiosity gap — forces reader to resolve the tension;
# "20-Minute" specificity = credibility signal (concrete = believable).
# Subconscious trigger: PATTERN INTERRUPT → curiosity → identity challenge.
# ══════════════════════════════════════════════════════════════════════════

def make_pin6():
    img  = Image.new("RGB", (W, H), TERRA)
    draw = ImageDraw.Draw(img)

    PAD = 80

    # Top ink accent
    accent_bar(draw, 0, 0, W, 8, INK)

    # Eyebrow
    ey_font = load(SANS_B, 20)
    ey = "MINDSET · HABITS · SYSTEMS"
    ew = draw.textlength(ey, font=ey_font)
    draw.text(((W - ew) // 2, 55), ey, font=ey_font, fill=(240, 200, 185))

    horz_rule(draw, PAD, W - PAD, 93, (200, 120, 95), 1)

    # Main headline — large bold serif italic (contrarian hook)
    h1_font  = load(SERIF_BI, 92)
    h1_lines = ["Discipline", "Didn’t Fix Me."]
    y = 125
    for line in h1_lines:
        lw = draw.textlength(line, font=h1_font)
        draw.text(((W - lw) // 2, y), line, font=h1_font, fill=WHITE)
        y += 102

    # Amber accent rule
    y += 12
    horz_rule(draw, (W - 100) // 2, (W + 100) // 2, y, AMBER, 5)
    y += 36

    # Resolution line — the answer
    res_font = load(SERIF_B, 68)
    res_lines = ["This 20-Minute", "Daily System Did."]
    for rl in res_lines:
        rlw = draw.textlength(rl, font=res_font)
        draw.text(((W - rlw) // 2, y), rl, font=res_font, fill=AMBER)
        y += 78
    y += 20

    # Dark ink card — shame-free promise
    card_h = 190
    draw.rectangle([PAD, y, W - PAD, y + card_h], fill=INK)
    accent_bar(draw, PAD, y, W - 2*PAD, 4, AMBER)

    promise_font = load(SERIF_I, 36)
    promise_lines = [
        "No streaks. No shame.",
        "Just a method that works",
        "with your real life.",
    ]
    py = y + 28
    for pl in promise_lines:
        plw = draw.textlength(pl, font=promise_font)
        draw.text(((W - plw) // 2, py), pl, font=promise_font, fill=WHITE)
        py += 52
    y += card_h + 44

    # 3 specifics
    spec_font = load(SANS_B, 27)
    specs = [
        "→  20 minutes · every day · no exceptions",
        "→  5 modules · built to work together",
        "→  Recovery protocol for bad days",
    ]
    for sp in specs:
        sw = draw.textlength(sp, font=spec_font)
        draw.text(((W - sw) // 2, y), sp, font=spec_font, fill=WHITE)
        y += 50
    y += 20

    # Product name + price badge
    badge_h = 90
    draw.rectangle([PAD, y, W - PAD, y + badge_h], fill=AMBER)
    prod_font = load(SERIF_B, 36)
    prod = "The Personal Reset System™  ·  $17"
    pw = draw.textlength(prod, font=prod_font)
    draw.text(((W - pw) // 2, y + 26), prod, font=prod_font, fill=INK)
    y += badge_h + 30

    horz_rule(draw, PAD, W - PAD, y, (200, 120, 95))

    # Brand tag
    draw.rectangle([0, H - 60, W, H], fill=(140, 67, 48))
    b_font = load(SANS_B, 18)
    bl = "visionsparkinnovation.com"
    blw = draw.textlength(bl, font=b_font)
    draw.text(((W - blw) // 2, H - 40), bl, font=b_font, fill=WHITE)

    accent_bar(draw, 0, H - 8, W, 8, INK)

    img.save(os.path.join(OUT_DIR, "pin-6.png"), "PNG", dpi=(300, 300))
    print("✓ pin-6.png saved")


if __name__ == "__main__":
    make_pin4()
    make_pin5()
    make_pin6()
    print("\nAll 3 pins complete → blog/pins/")
