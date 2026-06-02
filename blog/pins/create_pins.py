from PIL import Image, ImageDraw, ImageFont
import math, os, textwrap

os.makedirs('/home/user/Project1/blog/pins', exist_ok=True)

# ── Palette ──────────────────────────────────────────────
OAT       = (250, 246, 237)   # #FAF6ED Alpine Oat
IVORY     = (255, 253, 248)   # #FFFDF8
INK       = (42,  34,  24)    # #2A2218
FOREST    = (59,  110, 90)    # #3B6E5A
AMBER     = (201, 137, 42)    # #C9892A
TERRA     = (168, 81,  58)    # #A8513A
SAND      = (212, 201, 184)   # #D4C9B8
TAUPE     = (138, 126, 112)   # #8A7E70
WHITE     = (255, 255, 255)

# ── Fonts ────────────────────────────────────────────────
F_SERIF_BOLD   = '/usr/share/fonts/opentype/urw-base35/P052-Bold.otf'
F_SERIF_ITALIC = '/usr/share/fonts/opentype/urw-base35/P052-Italic.otf'
F_SERIF_BI     = '/usr/share/fonts/opentype/urw-base35/P052-BoldItalic.otf'
F_SERIF_ROMAN  = '/usr/share/fonts/opentype/urw-base35/P052-Roman.otf'
F_SANS_BOLD    = '/usr/share/fonts/opentype/urw-base35/NimbusSans-Bold.otf'
F_SANS         = '/usr/share/fonts/opentype/urw-base35/NimbusSans-Regular.otf'
F_GOTHIC       = '/usr/share/fonts/opentype/urw-base35/URWGothic-Demi.otf'
F_GOTHIC_BOOK  = '/usr/share/fonts/opentype/urw-base35/URWGothic-Book.otf'

W, H = 1000, 1500

def wrap_text(draw, text, font, max_width):
    """Wrap text to fit within max_width pixels."""
    words = text.split()
    lines = []
    current = []
    for word in words:
        test = ' '.join(current + [word])
        bbox = draw.textbbox((0, 0), test, font=font)
        if bbox[2] - bbox[0] <= max_width:
            current.append(word)
        else:
            if current:
                lines.append(' '.join(current))
            current = [word]
    if current:
        lines.append(' '.join(current))
    return lines

def draw_centered_text(draw, text, font, y, color, max_width, line_gap=0):
    """Draw centered wrapped text, return bottom y."""
    lines = wrap_text(draw, text, font, max_width)
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        tw = bbox[2] - bbox[0]
        x = (W - tw) // 2
        draw.text((x, y), line, font=font, fill=color)
        y += (bbox[3] - bbox[1]) + line_gap
    return y

def draw_left_text(draw, text, font, x, y, color, max_width, line_gap=0):
    """Draw left-aligned wrapped text, return bottom y."""
    lines = wrap_text(draw, text, font, max_width)
    for line in lines:
        draw.text((x, y), line, font=font, fill=color)
        bbox = draw.textbbox((0, 0), line, font=font)
        y += (bbox[3] - bbox[1]) + line_gap
    return y

def thin_rule(draw, x1, y, x2, color, width=1):
    draw.line([(x1, y), (x2, y)], fill=color, width=width)

def spaced_label(text):
    """Add letter spacing visually by inserting spaces."""
    return '  '.join(list(text))


# ═══════════════════════════════════════════════════════
# PIN 1 — How I Made My First $1,000 Online
# Light oat background · Forest green accent
# ═══════════════════════════════════════════════════════
def make_pin1():
    img = Image.new('RGB', (W, H), OAT)
    d = ImageDraw.Draw(img)

    MARGIN = 88
    CONTENT_W = W - MARGIN * 2

    # ── Subtle top texture: very faint horizontal rules ──
    for i in range(0, 40):
        alpha = 8 - i // 5
        if alpha <= 0: break
        c = tuple(max(0, v - alpha) for v in OAT)
        d.line([(0, i * 6), (W, i * 6)], fill=c, width=1)

    # ── Top accent bar ──
    d.rectangle([0, 0, W, 6], fill=FOREST)

    # ── Category label ──
    f_label = ImageFont.truetype(F_GOTHIC, 22)
    label = spaced_label('MAKE MONEY ONLINE')
    lb = d.textbbox((0, 0), label, font=f_label)
    lw = lb[2] - lb[0]
    lx = (W - lw) // 2
    d.text((lx, 68), label, font=f_label, fill=FOREST)

    # ── Thin rule under label ──
    thin_rule(d, MARGIN, 108, W - MARGIN, SAND, 1)

    # ── Large decorative number / emblem ──
    # A circle with "$" inside — editorial medallion feel
    cx, cy = W // 2, 268
    r = 92
    # Outer ring
    d.ellipse([cx-r-3, cy-r-3, cx+r+3, cy+r+3], outline=SAND, width=1)
    d.ellipse([cx-r, cy-r, cx+r, cy+r], outline=FOREST, width=2)
    # Inner mark
    f_emblem = ImageFont.truetype(F_SERIF_BOLD, 72)
    eb = d.textbbox((0, 0), '$', font=f_emblem)
    ex = cx - (eb[2] - eb[0]) // 2
    ey = cy - (eb[3] - eb[1]) // 2 - 4
    d.text((ex, ey), '$', font=f_emblem, fill=FOREST)
    # Spoke marks at cardinal points
    for angle in range(0, 360, 45):
        rad = math.radians(angle)
        x1 = cx + int(math.cos(rad) * (r + 8))
        y1 = cy + int(math.sin(rad) * (r + 8))
        x2 = cx + int(math.cos(rad) * (r + 16))
        y2 = cy + int(math.sin(rad) * (r + 16))
        d.line([(x1, y1), (x2, y2)], fill=SAND, width=1)

    # ── Main headline ──
    f_head = ImageFont.truetype(F_SERIF_BOLD, 82)
    y = 402
    y = draw_centered_text(d, 'How I Made My', f_head, y, INK, CONTENT_W, line_gap=8)
    y = draw_centered_text(d, 'First $1,000', f_head, y, FOREST, CONTENT_W, line_gap=8)
    y = draw_centered_text(d, 'Online', f_head, y, INK, CONTENT_W, line_gap=8)

    # ── Subheading ──
    f_sub = ImageFont.truetype(F_GOTHIC_BOOK, 34)
    y += 28
    thin_rule(d, MARGIN, y, W - MARGIN, SAND)
    y += 24
    y = draw_centered_text(d, 'And What I Did Wrong First', f_sub, y, TAUPE, CONTENT_W, line_gap=6)

    # ── Pull quote block ──
    y += 52
    # Left accent bar
    d.rectangle([MARGIN, y, MARGIN + 3, y + 220], fill=FOREST)
    quote_x = MARGIN + 26
    quote_w = CONTENT_W - 26

    f_quote = ImageFont.truetype(F_SERIF_ITALIC, 36)
    quote = '“I wasn’t failing because I lacked information. I was failing because I had too much of it and acted on none of it.”'
    y = draw_left_text(d, quote, f_quote, quote_x, y + 8, INK, quote_w, line_gap=10)

    # ── Divider ──
    y += 48
    thin_rule(d, MARGIN, y, W - MARGIN, SAND)

    # ── Brand + URL ──
    y += 38
    f_brand = ImageFont.truetype(F_SERIF_BOLD, 40)
    f_url = ImageFont.truetype(F_GOTHIC_BOOK, 24)

    brand = 'VisionSpark'
    bb = d.textbbox((0, 0), brand, font=f_brand)
    bx = (W - (bb[2] - bb[0])) // 2
    d.text((bx, y), brand, font=f_brand, fill=INK)

    y += (bb[3] - bb[1]) + 14
    url = spaced_label('visionsparkinnovation.com')
    ub = d.textbbox((0, 0), url, font=f_url)
    ux = (W - (ub[2] - ub[0])) // 2
    d.text((ux, y), url, font=f_url, fill=TAUPE)

    # ── Bottom accent bar ──
    d.rectangle([0, H - 6, W, H], fill=FOREST)

    # ── Corner registration marks (editorial detail) ──
    mark_len = 18
    mark_col = SAND
    # TL
    d.line([(MARGIN - 20, MARGIN - 20), (MARGIN - 20 + mark_len, MARGIN - 20)], fill=mark_col, width=1)
    d.line([(MARGIN - 20, MARGIN - 20), (MARGIN - 20, MARGIN - 20 + mark_len)], fill=mark_col, width=1)
    # TR
    d.line([(W - MARGIN + 20 - mark_len, MARGIN - 20), (W - MARGIN + 20, MARGIN - 20)], fill=mark_col, width=1)
    d.line([(W - MARGIN + 20, MARGIN - 20), (W - MARGIN + 20, MARGIN - 20 + mark_len)], fill=mark_col, width=1)
    # BL
    d.line([(MARGIN - 20, H - MARGIN + 20 - mark_len), (MARGIN - 20, H - MARGIN + 20)], fill=mark_col, width=1)
    d.line([(MARGIN - 20, H - MARGIN + 20), (MARGIN - 20 + mark_len, H - MARGIN + 20)], fill=mark_col, width=1)
    # BR
    d.line([(W - MARGIN + 20, H - MARGIN + 20 - mark_len), (W - MARGIN + 20, H - MARGIN + 20)], fill=mark_col, width=1)
    d.line([(W - MARGIN + 20 - mark_len, H - MARGIN + 20), (W - MARGIN + 20, H - MARGIN + 20)], fill=mark_col, width=1)

    out = '/home/user/Project1/blog/pins/pin-1-first-1000.png'
    img.save(out, 'PNG', dpi=(150, 150))
    print(f'Saved: {out}')


# ═══════════════════════════════════════════════════════
# PIN 2 — The 48-Hour Digital Product
# Dark ink background · Amber accent
# ═══════════════════════════════════════════════════════
def make_pin2():
    img = Image.new('RGB', (W, H), INK)
    d = ImageDraw.Draw(img)

    MARGIN = 88
    CONTENT_W = W - MARGIN * 2

    # ── Subtle warm radial glow at center ──
    glow_cx, glow_cy = W // 2, H // 2
    for r in range(500, 0, -20):
        alpha = int(6 * (1 - r / 500))
        if alpha <= 0: continue
        glow_col = tuple(min(255, v + alpha) for v in INK)
        d.ellipse([glow_cx - r, glow_cy - r, glow_cx + r, glow_cy + r],
                  fill=glow_col)

    # ── Top accent bar — amber ──
    d.rectangle([0, 0, W, 6], fill=AMBER)

    # ── Category label ──
    f_label = ImageFont.truetype(F_GOTHIC, 22)
    label = spaced_label('DIGITAL PRODUCTS')
    lb = d.textbbox((0, 0), label, font=f_label)
    lx = (W - (lb[2] - lb[0])) // 2
    d.text((lx, 68), label, font=f_label, fill=AMBER)

    # ── Thin rule ──
    thin_rule(d, MARGIN, 108, W - MARGIN, (60, 50, 38), 1)

    # ── "48" — large display number as visual anchor ──
    f_giant = ImageFont.truetype(F_SERIF_BOLD, 200)
    num = '48'
    nb = d.textbbox((0, 0), num, font=f_giant)
    nx = (W - (nb[2] - nb[0])) // 2
    # Ghost version
    d.text((nx + 2, 135), num, font=f_giant, fill=(52, 44, 32))
    d.text((nx, 132), num, font=f_giant, fill=AMBER)

    # Horizontal rule cutting through the number
    d.rectangle([MARGIN, 292, W - MARGIN, 295], fill=(60, 50, 38))

    # ── HOURS label across the number ──
    f_hours = ImageFont.truetype(F_GOTHIC, 30)
    hours_lbl = spaced_label('H O U R S')
    hb = d.textbbox((0, 0), hours_lbl, font=f_hours)
    hx = (W - (hb[2] - hb[0])) // 2
    d.text((hx, 306), hours_lbl, font=f_hours, fill=(100, 85, 60))

    # ── Main headline ──
    f_head = ImageFont.truetype(F_SERIF_BOLD, 74)
    y = 390
    y = draw_centered_text(d, 'The 48-Hour', f_head, y, (240, 235, 225), CONTENT_W, line_gap=6)
    y = draw_centered_text(d, 'Digital Product', f_head, y, AMBER, CONTENT_W, line_gap=6)

    # ── Subheading ──
    f_sub = ImageFont.truetype(F_GOTHIC_BOOK, 34)
    y += 24
    thin_rule(d, MARGIN, y, W - MARGIN, (60, 50, 38))
    y += 22
    y = draw_centered_text(d, 'From Idea to Listed in a Weekend', f_sub, y, (138, 126, 112), CONTENT_W, line_gap=6)

    # ── Pull quote ──
    y += 52
    # Amber left bar
    d.rectangle([MARGIN, y, MARGIN + 3, y + 260], fill=AMBER)
    f_quote = ImageFont.truetype(F_SERIF_ITALIC, 34)
    quote = '“A product that exists and is imperfect will always outsell a perfect product that doesn’t exist yet.”'
    y = draw_left_text(d, quote, f_quote, MARGIN + 26, y + 8, (220, 210, 195), CONTENT_W - 26, line_gap=10)

    # ── Bottom rule ──
    y += 44
    thin_rule(d, MARGIN, y, W - MARGIN, (60, 50, 38))

    # ── Brand + URL ──
    y += 36
    f_brand = ImageFont.truetype(F_SERIF_BOLD, 40)
    f_url = ImageFont.truetype(F_GOTHIC_BOOK, 24)

    brand = 'VisionSpark'
    bb = d.textbbox((0, 0), brand, font=f_brand)
    bx = (W - (bb[2] - bb[0])) // 2
    d.text((bx, y), brand, font=f_brand, fill=(240, 235, 225))

    y += (bb[3] - bb[1]) + 14
    url = spaced_label('visionsparkinnovation.com')
    ub = d.textbbox((0, 0), url, font=f_url)
    ux = (W - (ub[2] - ub[0])) // 2
    d.text((ux, y), url, font=f_url, fill=(100, 85, 60))

    # ── Bottom bar ──
    d.rectangle([0, H - 6, W, H], fill=AMBER)

    # ── Corner marks in dark amber ──
    mark_len = 18
    mark_col = (70, 58, 38)
    d.line([(MARGIN-20, MARGIN-20), (MARGIN-20+mark_len, MARGIN-20)], fill=mark_col, width=1)
    d.line([(MARGIN-20, MARGIN-20), (MARGIN-20, MARGIN-20+mark_len)], fill=mark_col, width=1)
    d.line([(W-MARGIN+20-mark_len, MARGIN-20), (W-MARGIN+20, MARGIN-20)], fill=mark_col, width=1)
    d.line([(W-MARGIN+20, MARGIN-20), (W-MARGIN+20, MARGIN-20+mark_len)], fill=mark_col, width=1)
    d.line([(MARGIN-20, H-MARGIN+20-mark_len), (MARGIN-20, H-MARGIN+20)], fill=mark_col, width=1)
    d.line([(MARGIN-20, H-MARGIN+20), (MARGIN-20+mark_len, H-MARGIN+20)], fill=mark_col, width=1)
    d.line([(W-MARGIN+20, H-MARGIN+20-mark_len), (W-MARGIN+20, H-MARGIN+20)], fill=mark_col, width=1)
    d.line([(W-MARGIN+20-mark_len, H-MARGIN+20), (W-MARGIN+20, H-MARGIN+20)], fill=mark_col, width=1)

    out = '/home/user/Project1/blog/pins/pin-2-48-hour-product.png'
    img.save(out, 'PNG', dpi=(150, 150))
    print(f'Saved: {out}')


# ═══════════════════════════════════════════════════════
# PIN 3 — Why Price at $13
# Light oat background · Terracotta accent
# ═══════════════════════════════════════════════════════
def make_pin3():
    img = Image.new('RGB', (W, H), OAT)
    d = ImageDraw.Draw(img)

    MARGIN = 88
    CONTENT_W = W - MARGIN * 2

    # ── Top accent bar — terracotta ──
    d.rectangle([0, 0, W, 6], fill=TERRA)

    # ── Category label ──
    f_label = ImageFont.truetype(F_GOTHIC, 22)
    label = spaced_label('STRATEGY')
    lb = d.textbbox((0, 0), label, font=f_label)
    lx = (W - (lb[2] - lb[0])) // 2
    d.text((lx, 68), label, font=f_label, fill=TERRA)

    thin_rule(d, MARGIN, 108, W - MARGIN, SAND)

    # ── Visual price contrast: $13 vs $97 ──
    # Two price blocks side by side
    block_y = 130
    block_h = 220
    gap = 24
    left_w = (CONTENT_W - gap) // 2
    lx = MARGIN
    rx = MARGIN + left_w + gap

    # $13 — winner block (forest filled)
    d.rectangle([lx, block_y, lx + left_w, block_y + block_h], fill=FOREST)
    f_price_big = ImageFont.truetype(F_SERIF_BOLD, 112)
    p13 = '$13'
    pb = d.textbbox((0, 0), p13, font=f_price_big)
    px = lx + (left_w - (pb[2] - pb[0])) // 2
    py = block_y + (block_h - (pb[3] - pb[1])) // 2 - 10
    d.text((px, py), p13, font=f_price_big, fill=OAT)
    f_win = ImageFont.truetype(F_GOTHIC, 18)
    win_lbl = spaced_label('WORKS')
    wb = d.textbbox((0, 0), win_lbl, font=f_win)
    d.text((lx + (left_w - (wb[2]-wb[0]))//2, block_y + block_h - 38),
           win_lbl, font=f_win, fill=(180, 210, 190))

    # $97 — loser block (sand/faded)
    d.rectangle([rx, block_y, rx + left_w, block_y + block_h],
                fill=(238, 233, 222))
    f_price_dim = ImageFont.truetype(F_SERIF_ROMAN, 112)
    p97 = '$97'
    pb2 = d.textbbox((0, 0), p97, font=f_price_dim)
    px2 = rx + (left_w - (pb2[2] - pb2[0])) // 2
    py2 = block_y + (block_h - (pb2[3] - pb2[1])) // 2 - 10
    d.text((px2, py2), p97, font=f_price_dim, fill=SAND)
    # Strikethrough
    mid_y = py2 + (pb2[3] - pb2[1]) // 2
    d.line([(px2 - 6, mid_y), (px2 + (pb2[2]-pb2[0]) + 6, mid_y)],
           fill=TERRA, width=3)
    lose_lbl = spaced_label('MISTAKE')
    lb2 = d.textbbox((0, 0), lose_lbl, font=f_win)
    d.text((rx + (left_w - (lb2[2]-lb2[0]))//2, block_y + block_h - 38),
           lose_lbl, font=f_win, fill=TAUPE)

    # ── Main headline ──
    f_head = ImageFont.truetype(F_SERIF_BOLD, 76)
    y = block_y + block_h + 52
    y = draw_centered_text(d, 'Why Your First Product', f_head, y, INK, CONTENT_W, line_gap=6)
    y = draw_centered_text(d, 'Should Cost', f_head, y, INK, CONTENT_W, line_gap=6)

    # ── "$13" in large terracotta ──
    f_hero_price = ImageFont.truetype(F_SERIF_BOLD, 120)
    hero_p = '$13'
    hpb = d.textbbox((0, 0), hero_p, font=f_hero_price)
    hpx = (W - (hpb[2] - hpb[0])) // 2
    d.text((hpx, y), hero_p, font=f_hero_price, fill=TERRA)
    y += (hpb[3] - hpb[1]) + 10

    # ── Sub ──
    f_sub = ImageFont.truetype(F_GOTHIC_BOOK, 30)
    sub_lbl = spaced_label('NOT $97')
    sb = d.textbbox((0, 0), sub_lbl, font=f_sub)
    d.text(((W - (sb[2]-sb[0])) // 2, y), sub_lbl, font=f_sub, fill=TAUPE)
    y += (sb[3] - sb[1]) + 44

    # ── Rule + pull quote ──
    thin_rule(d, MARGIN, y, W - MARGIN, SAND)
    y += 36

    d.rectangle([MARGIN, y, MARGIN + 3, y + 200], fill=TERRA)
    f_quote = ImageFont.truetype(F_SERIF_ITALIC, 34)
    quote = '“$13 is not what you’re worth. It’s what it costs to start proving it.”'
    y = draw_left_text(d, quote, f_quote, MARGIN + 26, y + 8, INK, CONTENT_W - 26, line_gap=10)

    # ── Brand + URL ──
    y += 44
    thin_rule(d, MARGIN, y, W - MARGIN, SAND)
    y += 32
    f_brand = ImageFont.truetype(F_SERIF_BOLD, 40)
    f_url = ImageFont.truetype(F_GOTHIC_BOOK, 24)
    brand = 'VisionSpark'
    bb = d.textbbox((0, 0), brand, font=f_brand)
    bx = (W - (bb[2] - bb[0])) // 2
    d.text((bx, y), brand, font=f_brand, fill=INK)
    y += (bb[3] - bb[1]) + 14
    url = spaced_label('visionsparkinnovation.com')
    ub = d.textbbox((0, 0), url, font=f_url)
    d.text(((W - (ub[2]-ub[0])) // 2, y), url, font=f_url, fill=TAUPE)

    # ── Bottom bar ──
    d.rectangle([0, H - 6, W, H], fill=TERRA)

    # ── Corner marks ──
    mark_len = 18
    mc = SAND
    d.line([(MARGIN-20, MARGIN-20), (MARGIN-20+mark_len, MARGIN-20)], fill=mc, width=1)
    d.line([(MARGIN-20, MARGIN-20), (MARGIN-20, MARGIN-20+mark_len)], fill=mc, width=1)
    d.line([(W-MARGIN+20-mark_len, MARGIN-20), (W-MARGIN+20, MARGIN-20)], fill=mc, width=1)
    d.line([(W-MARGIN+20, MARGIN-20), (W-MARGIN+20, MARGIN-20+mark_len)], fill=mc, width=1)
    d.line([(MARGIN-20, H-MARGIN+20-mark_len), (MARGIN-20, H-MARGIN+20)], fill=mc, width=1)
    d.line([(MARGIN-20, H-MARGIN+20), (MARGIN-20+mark_len, H-MARGIN+20)], fill=mc, width=1)
    d.line([(W-MARGIN+20, H-MARGIN+20-mark_len), (W-MARGIN+20, H-MARGIN+20)], fill=mc, width=1)
    d.line([(W-MARGIN+20-mark_len, H-MARGIN+20), (W-MARGIN+20, H-MARGIN+20)], fill=mc, width=1)

    out = '/home/user/Project1/blog/pins/pin-3-price-at-13.png'
    img.save(out, 'PNG', dpi=(150, 150))
    print(f'Saved: {out}')


if __name__ == '__main__':
    make_pin1()
    make_pin2()
    make_pin3()
    print('All 3 Pinterest pins generated.')
