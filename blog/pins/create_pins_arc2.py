from PIL import Image, ImageDraw, ImageFont
import math, os, textwrap

os.makedirs('/home/user/Project1/blog/pins', exist_ok=True)

# ── Palette ──────────────────────────────────────────────
OAT       = (250, 246, 237)
IVORY     = (255, 253, 248)
INK       = (42,  34,  24)
FOREST    = (59,  110, 90)
AMBER     = (201, 137, 42)
TERRA     = (168, 81,  58)
SAND      = (212, 201, 184)
TAUPE     = (138, 126, 112)
WHITE     = (255, 255, 255)

# ── Fonts ────────────────────────────────────────────────
F_SERIF_BOLD   = '/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf'
F_SERIF_ITALIC = '/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf'
F_SERIF_BI     = '/usr/share/fonts/truetype/liberation/LiberationSerif-BoldItalic.ttf'
F_SERIF_ROMAN  = '/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf'
F_SANS_BOLD    = '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'
F_SANS         = '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf'
F_GOTHIC       = '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'
F_GOTHIC_BOOK  = '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf'

W, H = 1000, 1500

def wrap_text(draw, text, font, max_width):
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
    lines = wrap_text(draw, text, font, max_width)
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        tw = bbox[2] - bbox[0]
        x = (W - tw) // 2
        draw.text((x, y), line, font=font, fill=color)
        y += (bbox[3] - bbox[1]) + line_gap
    return y

def draw_left_text(draw, text, font, x, y, color, max_width, line_gap=0):
    lines = wrap_text(draw, text, font, max_width)
    for line in lines:
        draw.text((x, y), line, font=font, fill=color)
        bbox = draw.textbbox((0, 0), line, font=font)
        y += (bbox[3] - bbox[1]) + line_gap
    return y

def thin_rule(draw, x1, y, x2, color, width=1):
    draw.line([(x1, y), (x2, y)], fill=color, width=width)

def spaced_label(text):
    return '  '.join(list(text))

def corner_marks(d, MARGIN, mark_col):
    mark_len = 18
    d.line([(MARGIN-20, MARGIN-20), (MARGIN-20+mark_len, MARGIN-20)], fill=mark_col, width=1)
    d.line([(MARGIN-20, MARGIN-20), (MARGIN-20, MARGIN-20+mark_len)], fill=mark_col, width=1)
    d.line([(W-MARGIN+20-mark_len, MARGIN-20), (W-MARGIN+20, MARGIN-20)], fill=mark_col, width=1)
    d.line([(W-MARGIN+20, MARGIN-20), (W-MARGIN+20, MARGIN-20+mark_len)], fill=mark_col, width=1)
    d.line([(MARGIN-20, H-MARGIN+20-mark_len), (MARGIN-20, H-MARGIN+20)], fill=mark_col, width=1)
    d.line([(MARGIN-20, H-MARGIN+20), (MARGIN-20+mark_len, H-MARGIN+20)], fill=mark_col, width=1)
    d.line([(W-MARGIN+20, H-MARGIN+20-mark_len), (W-MARGIN+20, H-MARGIN+20)], fill=mark_col, width=1)
    d.line([(W-MARGIN+20-mark_len, H-MARGIN+20), (W-MARGIN+20, H-MARGIN+20)], fill=mark_col, width=1)


# ═══════════════════════════════════════════════════════
# PIN 4 — Why I Blew Up My Routine
# Light oat background · Terracotta accent
# ═══════════════════════════════════════════════════════
def make_pin4():
    img = Image.new('RGB', (W, H), OAT)
    d = ImageDraw.Draw(img)
    MARGIN = 88
    CONTENT_W = W - MARGIN * 2

    # Top bar — terracotta
    d.rectangle([0, 0, W, 6], fill=TERRA)

    # Category label
    f_label = ImageFont.truetype(F_GOTHIC, 22)
    label = spaced_label('MINDSET & HABITS')
    lb = d.textbbox((0, 0), label, font=f_label)
    lx = (W - (lb[2] - lb[0])) // 2
    d.text((lx, 68), label, font=f_label, fill=TERRA)
    thin_rule(d, MARGIN, 108, W - MARGIN, SAND)

    # Decorative emblem — flame / reset symbol: nested circles with "↺"
    cx, cy = W // 2, 268
    r = 92
    d.ellipse([cx-r-3, cy-r-3, cx+r+3, cy+r+3], outline=SAND, width=1)
    d.ellipse([cx-r, cy-r, cx+r, cy+r], outline=TERRA, width=2)
    f_emblem = ImageFont.truetype(F_SERIF_BOLD, 66)
    symbol = 'RST'
    eb = d.textbbox((0, 0), symbol, font=f_emblem)
    ex = cx - (eb[2] - eb[0]) // 2
    ey = cy - (eb[3] - eb[1]) // 2 - 4
    d.text((ex, ey), symbol, font=f_emblem, fill=TERRA)
    for angle in range(0, 360, 45):
        rad = math.radians(angle)
        x1 = cx + int(math.cos(rad) * (r + 8))
        y1 = cy + int(math.sin(rad) * (r + 8))
        x2 = cx + int(math.cos(rad) * (r + 16))
        y2 = cy + int(math.sin(rad) * (r + 16))
        d.line([(x1, y1), (x2, y2)], fill=SAND, width=1)

    # Headline
    f_head = ImageFont.truetype(F_SERIF_BOLD, 80)
    y = 402
    y = draw_centered_text(d, 'Why I Blew Up', f_head, y, INK, CONTENT_W, line_gap=8)
    y = draw_centered_text(d, 'My Entire', f_head, y, TERRA, CONTENT_W, line_gap=8)
    y = draw_centered_text(d, 'Routine', f_head, y, INK, CONTENT_W, line_gap=8)

    # Subheading
    f_sub = ImageFont.truetype(F_GOTHIC_BOOK, 32)
    y += 28
    thin_rule(d, MARGIN, y, W - MARGIN, SAND)
    y += 24
    y = draw_centered_text(d, 'And Started Over From Scratch', f_sub, y, TAUPE, CONTENT_W, line_gap=6)

    # Pull quote
    y += 52
    d.rectangle([MARGIN, y, MARGIN + 3, y + 240], fill=TERRA)
    f_quote = ImageFont.truetype(F_SERIF_ITALIC, 34)
    quote = '"A routine that doesn\'t serve your current self is just a costume. It looks like growth. It isn\'t."'
    y = draw_left_text(d, quote, f_quote, MARGIN + 26, y + 8, INK, CONTENT_W - 26, line_gap=10)

    # Divider + brand
    y += 48
    thin_rule(d, MARGIN, y, W - MARGIN, SAND)
    y += 38
    f_brand = ImageFont.truetype(F_SERIF_BOLD, 40)
    f_url = ImageFont.truetype(F_GOTHIC_BOOK, 24)
    brand = 'VisionSpark'
    bb = d.textbbox((0, 0), brand, font=f_brand)
    d.text(((W - (bb[2]-bb[0])) // 2, y), brand, font=f_brand, fill=INK)
    y += (bb[3]-bb[1]) + 14
    url = spaced_label('visionsparkinnovation.com')
    ub = d.textbbox((0, 0), url, font=f_url)
    d.text(((W - (ub[2]-ub[0])) // 2, y), url, font=f_url, fill=TAUPE)

    d.rectangle([0, H-6, W, H], fill=TERRA)
    corner_marks(d, MARGIN, SAND)

    out = '/home/user/Project1/blog/pins/pin-4-blew-up-routine.png'
    img.save(out, 'PNG', dpi=(150, 150))
    print(f'Saved: {out}')


# ═══════════════════════════════════════════════════════
# PIN 5 — The 5-Module Reset
# Dark ink background · Amber accent  (mirrors pin-2 energy)
# ═══════════════════════════════════════════════════════
def make_pin5():
    img = Image.new('RGB', (W, H), INK)
    d = ImageDraw.Draw(img)
    MARGIN = 88
    CONTENT_W = W - MARGIN * 2

    # Warm glow
    glow_cx, glow_cy = W // 2, H // 2
    for r in range(500, 0, -20):
        alpha = int(6 * (1 - r / 500))
        if alpha <= 0: continue
        glow_col = tuple(min(255, v + alpha) for v in INK)
        d.ellipse([glow_cx-r, glow_cy-r, glow_cx+r, glow_cy+r], fill=glow_col)

    # Top bar — amber
    d.rectangle([0, 0, W, 6], fill=AMBER)

    # Category label
    f_label = ImageFont.truetype(F_GOTHIC, 22)
    label = spaced_label('HABITS & SYSTEMS')
    lb = d.textbbox((0, 0), label, font=f_label)
    lx = (W - (lb[2] - lb[0])) // 2
    d.text((lx, 68), label, font=f_label, fill=AMBER)
    thin_rule(d, MARGIN, 108, W - MARGIN, (60, 50, 38))

    # Large "30" as anchor
    f_giant = ImageFont.truetype(F_SERIF_BOLD, 200)
    num = '30'
    nb = d.textbbox((0, 0), num, font=f_giant)
    nx = (W - (nb[2] - nb[0])) // 2
    d.text((nx+2, 135), num, font=f_giant, fill=(52, 44, 32))
    d.text((nx, 132), num, font=f_giant, fill=AMBER)
    d.rectangle([MARGIN, 292, W-MARGIN, 295], fill=(60, 50, 38))
    f_days = ImageFont.truetype(F_GOTHIC, 30)
    days_lbl = spaced_label('D A Y S')
    hb = d.textbbox((0, 0), days_lbl, font=f_days)
    d.text(((W - (hb[2]-hb[0])) // 2, 306), days_lbl, font=f_days, fill=(100, 85, 60))

    # Five module dots
    dot_y = 368
    dot_r = 10
    spacing = 52
    total_dots_w = 5 * dot_r * 2 + 4 * (spacing - dot_r * 2)
    dot_x_start = (W - total_dots_w) // 2
    for i in range(5):
        dx = dot_x_start + i * spacing
        d.ellipse([dx, dot_y, dx + dot_r*2, dot_y + dot_r*2], fill=AMBER)
    f_five = ImageFont.truetype(F_GOTHIC_BOOK, 22)
    five_lbl = spaced_label('5 MODULES · 60 EXERCISES')
    flb = d.textbbox((0, 0), five_lbl, font=f_five)
    d.text(((W - (flb[2]-flb[0])) // 2, dot_y + dot_r*2 + 12), five_lbl, font=f_five, fill=(100, 85, 60))

    # Headline
    f_head = ImageFont.truetype(F_SERIF_BOLD, 72)
    y = 455
    y = draw_centered_text(d, 'The 5-Module', f_head, y, (240, 235, 225), CONTENT_W, line_gap=6)
    y = draw_centered_text(d, 'Reset', f_head, y, AMBER, CONTENT_W, line_gap=6)

    # Sub
    f_sub = ImageFont.truetype(F_GOTHIC_BOOK, 32)
    y += 24
    thin_rule(d, MARGIN, y, W-MARGIN, (60, 50, 38))
    y += 22
    y = draw_centered_text(d, 'Rebuild Your Habits in 30 Days', f_sub, y, (138, 126, 112), CONTENT_W, line_gap=6)

    # Pull quote
    y += 50
    d.rectangle([MARGIN, y, MARGIN+3, y+260], fill=AMBER)
    f_quote = ImageFont.truetype(F_SERIF_ITALIC, 32)
    quote = '"You don\'t need more willpower. You need a better sequence. Most people change the right things in the wrong order."'
    y = draw_left_text(d, quote, f_quote, MARGIN+26, y+8, (220, 210, 195), CONTENT_W-26, line_gap=10)

    # Bottom rule + brand
    y += 44
    thin_rule(d, MARGIN, y, W-MARGIN, (60, 50, 38))
    y += 36
    f_brand = ImageFont.truetype(F_SERIF_BOLD, 40)
    f_url = ImageFont.truetype(F_GOTHIC_BOOK, 24)
    brand = 'VisionSpark'
    bb = d.textbbox((0, 0), brand, font=f_brand)
    d.text(((W - (bb[2]-bb[0])) // 2, y), brand, font=f_brand, fill=(240, 235, 225))
    y += (bb[3]-bb[1]) + 14
    url = spaced_label('visionsparkinnovation.com')
    ub = d.textbbox((0, 0), url, font=f_url)
    d.text(((W - (ub[2]-ub[0])) // 2, y), url, font=f_url, fill=(100, 85, 60))

    d.rectangle([0, H-6, W, H], fill=AMBER)
    corner_marks(d, MARGIN, (70, 58, 38))

    out = '/home/user/Project1/blog/pins/pin-5-five-module-reset.png'
    img.save(out, 'PNG', dpi=(150, 150))
    print(f'Saved: {out}')


# ═══════════════════════════════════════════════════════
# PIN 6 — The Discipline Myth
# Light oat background · Forest accent (mirrors pin-1/3 calm)
# ═══════════════════════════════════════════════════════
def make_pin6():
    img = Image.new('RGB', (W, H), OAT)
    d = ImageDraw.Draw(img)
    MARGIN = 88
    CONTENT_W = W - MARGIN * 2

    # Top bar — forest
    d.rectangle([0, 0, W, 6], fill=FOREST)

    # Category label
    f_label = ImageFont.truetype(F_GOTHIC, 22)
    label = spaced_label('MINDSET')
    lb = d.textbbox((0, 0), label, font=f_label)
    d.text(((W - (lb[2]-lb[0])) // 2, 68), label, font=f_label, fill=FOREST)
    thin_rule(d, MARGIN, 108, W-MARGIN, SAND)

    # Two-column contrast: DISCIPLINE vs DESIGN
    block_y = 130
    block_h = 200
    gap = 20
    left_w = (CONTENT_W - gap) // 2
    lx = MARGIN
    rx = MARGIN + left_w + gap

    # Left: DISCIPLINE — muted/struck
    d.rectangle([lx, block_y, lx+left_w, block_y+block_h], fill=(238, 233, 222))
    f_col_head = ImageFont.truetype(F_SERIF_ROMAN, 36)
    f_col_sub  = ImageFont.truetype(F_GOTHIC_BOOK, 20)
    disc_lbl = 'DISCIPLINE'
    dlb = d.textbbox((0, 0), disc_lbl, font=f_col_head)
    dlx = lx + (left_w - (dlb[2]-dlb[0])) // 2
    dly = block_y + 32
    d.text((dlx, dly), disc_lbl, font=f_col_head, fill=SAND)
    # Strikethrough
    mid = dly + (dlb[3]-dlb[1]) // 2
    d.line([(dlx-4, mid), (dlx+(dlb[2]-dlb[0])+4, mid)], fill=TERRA, width=3)
    sub1 = 'runs out'
    s1b = d.textbbox((0, 0), sub1, font=f_col_sub)
    d.text((lx + (left_w-(s1b[2]-s1b[0]))//2, block_y+block_h-52), sub1, font=f_col_sub, fill=TAUPE)
    sub1b = 'every day'
    s1bb = d.textbbox((0, 0), sub1b, font=f_col_sub)
    d.text((lx + (left_w-(s1bb[2]-s1bb[0]))//2, block_y+block_h-30), sub1b, font=f_col_sub, fill=TAUPE)

    # Right: DESIGN — filled forest
    d.rectangle([rx, block_y, rx+left_w, block_y+block_h], fill=FOREST)
    des_lbl = 'DESIGN'
    desb = d.textbbox((0, 0), des_lbl, font=f_col_head)
    desx = rx + (left_w - (desb[2]-desb[0])) // 2
    desy = block_y + 32
    d.text((desx, desy), des_lbl, font=f_col_head, fill=OAT)
    sub2 = 'works'
    s2b = d.textbbox((0, 0), sub2, font=f_col_sub)
    d.text((rx + (left_w-(s2b[2]-s2b[0]))//2, block_y+block_h-52), sub2, font=f_col_sub, fill=(180, 210, 190))
    sub2b = 'automatically'
    s2bb = d.textbbox((0, 0), sub2b, font=f_col_sub)
    d.text((rx + (left_w-(s2bb[2]-s2bb[0]))//2, block_y+block_h-30), sub2b, font=f_col_sub, fill=(180, 210, 190))

    # Headline
    f_head = ImageFont.truetype(F_SERIF_BOLD, 76)
    y = block_y + block_h + 52
    y = draw_centered_text(d, 'Discipline Is a', f_head, y, INK, CONTENT_W, line_gap=6)
    y = draw_centered_text(d, 'Symptom', f_head, y, FOREST, CONTENT_W, line_gap=6)

    f_sub2 = ImageFont.truetype(F_GOTHIC_BOOK, 30)
    not_lbl = spaced_label('NOT A STRATEGY')
    nb = d.textbbox((0, 0), not_lbl, font=f_sub2)
    d.text(((W - (nb[2]-nb[0])) // 2, y + 8), not_lbl, font=f_sub2, fill=TAUPE)
    y += (nb[3]-nb[1]) + 56

    # Rule + quote
    thin_rule(d, MARGIN, y, W-MARGIN, SAND)
    y += 36
    d.rectangle([MARGIN, y, MARGIN+3, y+220], fill=FOREST)
    f_quote = ImageFont.truetype(F_SERIF_ITALIC, 34)
    quote = '"The most disciplined people you know are not gritting their teeth. They designed a life where the right choices are the obvious ones."'
    y = draw_left_text(d, quote, f_quote, MARGIN+26, y+8, INK, CONTENT_W-26, line_gap=10)

    # Brand + URL
    y += 44
    thin_rule(d, MARGIN, y, W-MARGIN, SAND)
    y += 32
    f_brand = ImageFont.truetype(F_SERIF_BOLD, 40)
    f_url = ImageFont.truetype(F_GOTHIC_BOOK, 24)
    brand = 'VisionSpark'
    bb = d.textbbox((0, 0), brand, font=f_brand)
    d.text(((W - (bb[2]-bb[0])) // 2, y), brand, font=f_brand, fill=INK)
    y += (bb[3]-bb[1]) + 14
    url = spaced_label('visionsparkinnovation.com')
    ub = d.textbbox((0, 0), url, font=f_url)
    d.text(((W - (ub[2]-ub[0])) // 2, y), url, font=f_url, fill=TAUPE)

    d.rectangle([0, H-6, W, H], fill=FOREST)
    corner_marks(d, MARGIN, SAND)

    out = '/home/user/Project1/blog/pins/pin-6-discipline-myth.png'
    img.save(out, 'PNG', dpi=(150, 150))
    print(f'Saved: {out}')


if __name__ == '__main__':
    make_pin4()
    make_pin5()
    make_pin6()
    print('All 3 Arc 2 Pinterest pins generated.')
