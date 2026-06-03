"""
Pinterest Pins — Arc 3 v2 / The Personal Reset System™
Layout inspired by reference: product mockup + feature icons + trust bar + CTA strip
Brand: VisionSpark palette, shame-free messaging, warm editorial tone
1000×1500px, 300dpi
"""

from PIL import Image, ImageDraw, ImageFont
import os, math

FONT_DIR = "/usr/share/fonts/truetype/liberation"
SERIF_B  = os.path.join(FONT_DIR, "LiberationSerif-Bold.ttf")
SERIF_I  = os.path.join(FONT_DIR, "LiberationSerif-Italic.ttf")
SERIF_BI = os.path.join(FONT_DIR, "LiberationSerif-BoldItalic.ttf")
SERIF_R  = os.path.join(FONT_DIR, "LiberationSerif-Regular.ttf")
SANS_B   = os.path.join(FONT_DIR, "LiberationSans-Bold.ttf")
SANS_R   = os.path.join(FONT_DIR, "LiberationSans-Regular.ttf")
OUT_DIR  = os.path.dirname(os.path.abspath(__file__))

W, H = 1000, 1500

# ── Palette ────────────────────────────────────────────────────────────────
OAT       = (250, 246, 237)
INK       = (42,  34,  24)
INK_RICH  = (28,  22,  14)   # deeper warm black for bg
FOREST    = (59,  110, 90)
FOREST_DK = (38,  72,  58)
AMBER     = (201, 137, 42)
AMBER_LT  = (224, 155, 50)
TERRA     = (168, 81,  58)
TERRA_DK  = (120, 55,  38)
SAND      = (212, 201, 184)
TAUPE     = (138, 126, 112)
IVORY     = (255, 253, 248)
WHITE     = (255, 255, 255)
CREAM     = (240, 232, 218)

def load(path, size):
    return ImageFont.truetype(path, size)

def cx(draw, text, font, y, fill, img_w=W):
    """Draw text centred horizontally."""
    w = draw.textlength(text, font=font)
    draw.text(((img_w - w) // 2, y), text, font=font, fill=fill)
    return y + draw.textbbox((0,0), text, font=font)[3] + 4

def rect(draw, x1, y1, x2, y2, fill, radius=0):
    if radius:
        draw.rounded_rectangle([x1, y1, x2, y2], radius=radius, fill=fill)
    else:
        draw.rectangle([x1, y1, x2, y2], fill=fill)

def rule(draw, x1, x2, y, color, h=2):
    draw.rectangle([x1, y, x2, y+h], fill=color)

def draw_book_mockup(draw, img, cx_pos, cy_pos, book_w=320, book_h=420):
    """Draw a simple 3-D workbook mockup using layered rectangles."""
    # Shadow
    for i in range(18, 0, -1):
        alpha = int(60 * (i / 18))
        shadow_color = (0, 0, 0, alpha)
        # approximate shadow with dark rects
    shadow_img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow_img)
    for i in range(15, 0, -1):
        shade = max(0, 40 - i*2)
        sd.rounded_rectangle(
            [cx_pos - book_w//2 + i*2, cy_pos - book_h//2 + i*3,
             cx_pos + book_w//2 + i*2, cy_pos + book_h//2 + i*3],
            radius=6, fill=(0, 0, 0, shade)
        )
    img.paste(Image.alpha_composite(img.convert("RGBA"), shadow_img).convert("RGB"), (0,0))
    draw = ImageDraw.Draw(img)

    bx1 = cx_pos - book_w//2
    by1 = cy_pos - book_h//2
    bx2 = cx_pos + book_w//2
    by2 = cy_pos + book_h//2

    # Book spine (left strip)
    spine_w = 36
    draw.rounded_rectangle([bx1, by1, bx1+spine_w, by2], radius=4,
                            fill=FOREST_DK)

    # Book cover (main face)
    draw.rounded_rectangle([bx1+spine_w, by1, bx2, by2], radius=6,
                            fill=FOREST)

    # Cover gradient effect — lighter top strip
    for i in range(60):
        alpha = int(40 * (1 - i/60))
        light = (min(255, FOREST[0]+40), min(255, FOREST[1]+40), min(255, FOREST[2]+40))
        draw.rectangle([bx1+spine_w, by1+i, bx2, by1+i+1],
                       fill=(light[0], light[1], light[2]))

    # Cover — inner border
    pad = 16
    draw.rounded_rectangle(
        [bx1+spine_w+pad, by1+pad, bx2-pad, by2-pad],
        radius=3, outline=AMBER, width=2
    )

    # Cover title text
    title_font  = load(SERIF_BI, 34)
    sub_font    = load(SERIF_R, 18)
    badge_font  = load(SANS_B, 14)

    title_lines = ["The", "Personal", "Reset", "System™"]
    ty = by1 + 48
    for tl in title_lines:
        tw = draw.textlength(tl, font=title_font)
        tx = cx_pos - tw//2
        draw.text((tx, ty), tl, font=title_font, fill=AMBER if tl in ["Personal","Reset","System™"] else IVORY)
        ty += 40

    ty += 8
    sub_line = "30 DAYS · 5 MODULES"
    sw = draw.textlength(sub_line, font=sub_font)
    draw.text((cx_pos - sw//2, ty), sub_line, font=sub_font, fill=CREAM)
    ty += 28

    rule(draw, bx1+spine_w+pad+10, bx2-pad-10, ty, AMBER, 1)
    ty += 14

    tag_line = "ONE SYSTEM THAT FINALLY STICKS."
    tw2 = draw.textlength(tag_line, font=badge_font)
    draw.text((cx_pos - tw2//2, ty), tag_line, font=badge_font, fill=SAND)

    # Bottom badge on cover
    badge_y = by2 - 60
    draw.rectangle([bx1+spine_w+pad, badge_y, bx2-pad, by2-pad], fill=AMBER)
    bl = "BUILT BY EXPERIENCE."
    blw = draw.textlength(bl, font=badge_font)
    draw.text((cx_pos - blw//2, badge_y + 8), bl, font=badge_font, fill=INK)
    bl2 = "BACKED BY RESULTS."
    bl2w = draw.textlength(bl2, font=badge_font)
    draw.text((cx_pos - bl2w//2, badge_y + 28), bl2, font=badge_font, fill=INK)

    # Spine text
    sp_font = load(SANS_B, 16)
    sp_text = "PERSONAL RESET SYSTEM™"
    # Draw rotated spine text
    sp_img = Image.new("RGBA", (book_h - 20, 30), (0,0,0,0))
    sp_draw = ImageDraw.Draw(sp_img)
    sp_draw.text((10, 6), sp_text, font=sp_font, fill=AMBER)
    sp_rot = sp_img.rotate(90, expand=True)
    img.paste(sp_rot, (bx1 + 4, by1 + 10), sp_rot)

    return img, draw


def make_feature_row(draw, x, y, icon_char, title, subtitle, icon_color):
    """Draw one feature row: icon circle + bold title + small subtitle."""
    # Icon circle
    r = 26
    draw.ellipse([x, y, x+r*2, y+r*2], fill=icon_color)
    ic_font = load(SANS_B, 22)
    iw = draw.textlength(icon_char, font=ic_font)
    draw.text((x + r - iw//2, y + r - 13), icon_char, font=ic_font, fill=WHITE)

    tx = x + r*2 + 18
    tf = load(SANS_B, 26)
    sf = load(SANS_R, 21)
    draw.text((tx, y + 2), title, font=tf, fill=IVORY)
    draw.text((tx, y + 32), subtitle, font=sf, fill=TAUPE)
    return y + 68


def make_trust_bar(draw, y, items):
    """Draw 4 trust icons in a row."""
    bar_h = 110
    rect(draw, 0, y, W, y + bar_h, FOREST_DK)
    rule(draw, 0, W, y, AMBER, 2)
    slot_w = W // len(items)
    icon_font = load(SANS_B, 20)
    label_font = load(SANS_R, 17)
    for i, (icon, label) in enumerate(items):
        sx = i * slot_w + slot_w // 2
        iw = draw.textlength(icon, font=icon_font)
        draw.text((sx - iw//2, y + 14), icon, font=icon_font, fill=AMBER)
        lw = draw.textlength(label, font=label_font)
        draw.text((sx - lw//2, y + 44), label, font=label_font, fill=CREAM)
    return y + bar_h


def make_cta_strip(draw, text, y):
    rect(draw, 0, y, W, H, AMBER)
    rule(draw, 0, W, y, INK, 3)
    cf = load(SERIF_B, 44)
    cw = draw.textlength(text, font=cf)
    draw.text(((W - cw) // 2, y + 22), text, font=cf, fill=INK)
    # Arrow
    aw = draw.textlength("→", font=cf)
    draw.text((W - 80, y + 22), "→", font=cf, fill=INK)


# ══════════════════════════════════════════════════════════════════════════
# PIN 4 — Identification hook / warm dark editorial
# ══════════════════════════════════════════════════════════════════════════
def make_pin4():
    img  = Image.new("RGB", (W, H), INK_RICH)
    draw = ImageDraw.Draw(img)
    PAD  = 60

    # Subtle warm vignette top
    for i in range(120):
        v = int(20 * (1 - i/120))
        draw.rectangle([0, i, W, i+1], fill=(INK_RICH[0]+v, INK_RICH[1]+v, INK_RICH[2]+v))

    # Top amber accent
    rect(draw, 0, 0, W, 6, AMBER)

    # Eyebrow pill
    ey_font = load(SANS_B, 20)
    ey = "THE PERSONAL RESET SYSTEM™"
    ew = draw.textlength(ey, font=ey_font)
    pill_pad = 20
    pill_x = (W - ew - pill_pad*2) // 2
    draw.rounded_rectangle([pill_x, 24, pill_x + ew + pill_pad*2, 58],
                            radius=14, fill=FOREST_DK)
    draw.text((pill_x + pill_pad, 30), ey, font=ey_font, fill=SAND)

    # Main headline
    h1 = load(SERIF_BI, 80)
    h1_lines = ["I Tried Every", "Habit App.", "Nothing Worked", "Until I Did This."]
    y = 78
    for i, line in enumerate(h1_lines):
        lw = draw.textlength(line, font=h1)
        color = AMBER if i in [1, 3] else IVORY
        draw.text(((W - lw) // 2, y), line, font=h1, fill=color)
        y += 88

    # Thin amber rule
    rule(draw, (W-80)//2, (W+80)//2, y + 6, AMBER, 3)
    y += 30

    # Product mockup — centred
    book_cy = y + 230
    img, draw = draw_book_mockup(draw, img, W//2, book_cy, book_w=300, book_h=400)
    y = book_cy + 215

    # Features
    features = [
        ("✦", "Rewire Your Mindset",    "Break the cycle. Build clarity.",    FOREST),
        ("⚡", "Boost Your Energy",      "More focus. Less burnout.",           TERRA),
        ("◎", "Master Your Habits",     "Small actions. Real results.",        FOREST),
        ("↗", "Transform Your Life",    "Consistency today. Freedom tomorrow.", AMBER),
    ]
    fy = y + 10
    for icon, title, sub, color in features:
        fy = make_feature_row(draw, PAD, fy, icon, title, sub, color)

    # Trust bar
    trust_items = [
        ("⬇", "INSTANT\nDOWNLOAD"),
        ("◷", "20 MIN\nA DAY"),
        ("▣", "30 DAYS TO\nTRANSFORM"),
        ("∞", "LIFETIME\nACCESS"),
    ]
    trust_y = fy + 10
    flat_trust = [(a, b.replace("\n", " ")) for a, b in trust_items]
    trust_y = make_trust_bar(draw, trust_y, flat_trust)

    # CTA strip
    make_cta_strip(draw, "STOP SCROLLING. START RESETTING.", trust_y)

    img.save(os.path.join(OUT_DIR, "pin-4-v2.png"), "PNG", dpi=(300, 300))
    print("✓ pin-4-v2.png")


# ══════════════════════════════════════════════════════════════════════════
# PIN 5 — Relief / Forest calm
# ══════════════════════════════════════════════════════════════════════════
def make_pin5():
    img  = Image.new("RGB", (W, H), FOREST_DK)
    draw = ImageDraw.Draw(img)
    PAD  = 60

    # Subtle gradient top
    for i in range(200):
        v = int(15 * (1 - i/200))
        c = (FOREST_DK[0]-v, max(0,FOREST_DK[1]-v), max(0,FOREST_DK[2]-v))
        draw.rectangle([0, i, W, i+1], fill=c)

    rect(draw, 0, 0, W, 6, IVORY)

    # Eyebrow
    ey_font = load(SANS_B, 20)
    ey = "THE PERSONAL RESET SYSTEM™"
    ew = draw.textlength(ey, font=ey_font)
    pill_x = (W - ew - 40) // 2
    draw.rounded_rectangle([pill_x, 24, pill_x + ew + 40, 58], radius=14,
                            fill=(30, 60, 48))
    draw.text((pill_x + 20, 30), ey, font=ey_font, fill=(180, 220, 200))

    # Main headline
    h1 = load(SERIF_B, 96)
    for i, line in enumerate(["Stop", "Rebuilding", "From Zero."]):
        lw = draw.textlength(line, font=h1)
        color = AMBER if i == 2 else WHITE
        draw.text(((W - lw) // 2, 76 + i*102), line, font=h1, fill=color)

    y = 76 + 3*102 + 10
    rule(draw, (W-100)//2, (W+100)//2, y, AMBER, 4)
    y += 30

    sub_f = load(SERIF_I, 52)
    sub = "Start From Here."
    sw = draw.textlength(sub, font=sub_f)
    draw.text(((W - sw) // 2, y), sub, font=sub_f, fill=AMBER)
    y += 74

    # Book mockup
    book_cy = y + 220
    img, draw = draw_book_mockup(draw, img, W//2, book_cy, book_w=300, book_h=400)
    y = book_cy + 220

    # Features
    features = [
        ("✦", "Rewire Your Mindset",   "Break the cycle. Build clarity.",   (59, 130, 100)),
        ("◷", "Energy by Design",      "Work with your body, not against it.", AMBER),
        ("◎", "Habits That Survive",   "Built for bad days too.",             (59, 130, 100)),
        ("↗", "Integrated System",     "All 5 modules. One reset.",           AMBER),
    ]
    fy = y + 10
    for icon, title, sub, color in features:
        fy = make_feature_row(draw, PAD, fy, icon, title, sub, color)

    flat_trust = [("⬇","INSTANT DOWNLOAD"),("◷","20 MIN A DAY"),
                  ("▣","30 DAYS"),("∞","LIFETIME ACCESS")]
    trust_y = make_trust_bar(draw, fy + 10, flat_trust)
    make_cta_strip(draw, "STOP STARTING OVER. START HERE.", trust_y)

    img.save(os.path.join(OUT_DIR, "pin-5-v2.png"), "PNG", dpi=(300, 300))
    print("✓ pin-5-v2.png")


# ══════════════════════════════════════════════════════════════════════════
# PIN 6 — Pattern interrupt / Terracotta contrarian
# ══════════════════════════════════════════════════════════════════════════
def make_pin6():
    img  = Image.new("RGB", (W, H), TERRA_DK)
    draw = ImageDraw.Draw(img)
    PAD  = 60

    for i in range(180):
        v = int(20*(1-i/180))
        c = (min(255,TERRA_DK[0]+v), TERRA_DK[1], TERRA_DK[2])
        draw.rectangle([0, i, W, i+1], fill=c)

    rect(draw, 0, 0, W, 6, INK)

    ey_font = load(SANS_B, 20)
    ey = "MINDSET · HABITS · SYSTEMS"
    ew = draw.textlength(ey, font=ey_font)
    pill_x = (W - ew - 40) // 2
    draw.rounded_rectangle([pill_x, 24, pill_x + ew + 40, 58], radius=14,
                            fill=(100, 45, 28))
    draw.text((pill_x + 20, 30), ey, font=ey_font, fill=(240, 200, 185))

    h1 = load(SERIF_BI, 84)
    for i, (line, color) in enumerate([
        ("Discipline", WHITE),
        ("Didn't Fix Me.", WHITE),
        ("This 20-Min", AMBER),
        ("System Did.", AMBER),
    ]):
        lw = draw.textlength(line, font=h1)
        draw.text(((W - lw) // 2, 76 + i*92), line, font=h1, fill=color)

    y = 76 + 4*92 + 10
    rule(draw, (W-100)//2, (W+100)//2, y, IVORY, 3)
    y += 28

    # Book mockup
    book_cy = y + 220
    img, draw = draw_book_mockup(draw, img, W//2, book_cy, book_w=300, book_h=400)
    y = book_cy + 220

    features = [
        ("✗", "No streak pressure",      "Miss a day? Built-in recovery.",     (180, 90, 60)),
        ("✗", "No willpower required",   "Designed below the resistance line.", (180, 90, 60)),
        ("✓", "20-minute daily cap",     "Small enough for your worst days.",   AMBER),
        ("✓", "5 integrated modules",    "System that holds under real life.",  AMBER),
    ]
    fy = y + 10
    for icon, title, sub, color in features:
        fy = make_feature_row(draw, PAD, fy, icon, title, sub, color)

    flat_trust = [("⬇","INSTANT DOWNLOAD"),("◷","20 MIN A DAY"),
                  ("▣","30 DAYS"),("∞","LIFETIME ACCESS")]
    trust_y = make_trust_bar(draw, fy + 10, flat_trust)
    make_cta_strip(draw, "DONE WHITE-KNUCKLING? START HERE.", trust_y)

    img.save(os.path.join(OUT_DIR, "pin-6-v2.png"), "PNG", dpi=(300, 300))
    print("✓ pin-6-v2.png")


if __name__ == "__main__":
    make_pin4()
    make_pin5()
    make_pin6()
    print("\nAll 3 v2 pins complete.")
