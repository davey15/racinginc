"""Builds brand/logo/*.svg. Needs: pip install fonttools brotli; npm i @fontsource/unbounded
Usage: FONTS_DIR=<node_modules/@fontsource> python3 build_logo.py"""
import os
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen

FD = os.environ.get('FONTS_DIR', 'node_modules/@fontsource')
heavy = TTFont(f'{FD}/unbounded/files/unbounded-latin-900-normal.woff2')
light = TTFont(f'{FD}/unbounded/files/unbounded-latin-500-normal.woff2')
OUT = os.path.dirname(os.path.abspath(__file__)) + '/'
SKEW = -10          # degrees, a single slant applied to the whole lockup
RED, WHITE, SILVER, BLACK = '#D40000', '#FFFFFF', '#9AA0A6', '#0A0A0B'
CAP = heavy['OS/2'].sCapHeight

def glyphs(font, text, x0, track=0, scale=1.0):
    gs = font.getGlyphSet(); cm = font.getBestCmap(); x = x0; out = []
    for ch in text:
        if ch == ' ':
            x += (font['hmtx']['space'][0] + track) * scale; continue
        n = cm[ord(ch)]; p = SVGPathPen(gs); gs[n].draw(p)
        out.append((x, p.getCommands(), scale)); x += (gs[n].width + track) * scale
    return out, x

def emit(items, fill):
    return ''.join(f'<path transform="translate({x:.1f} 0) scale({s} -{s})" d="{d}" fill="{fill}"/>' for x, d, s in items)

def gc(x0, color, H=CAP):
    """Fused G+C, drawn as squared 'blocks' that fill the cap-height box. Baseline y=0, glyph spans y=-H..0."""
    cx, cy = x0 + H / 2, -H / 2
    wo, wi, gap = H * 0.17, H * 0.15, H * 0.075
    h = H / 2 - wo / 2                      # outer centerline half-size
    hi = h - wo / 2 - gap - wi / 2          # inner centerline half-size
    k, ki = H * 0.20, H * 0.09              # corner radii
    L = lambda v: f'{v:.1f}'
    outer = (f'M{L(cx+h)} {L(cy-h*0.40)} V{L(cy-h+k)} A{L(k)} {L(k)} 0 0 0 {L(cx+h-k)} {L(cy-h)} H{L(cx-h+k)} '
             f'A{L(k)} {L(k)} 0 0 0 {L(cx-h)} {L(cy-h+k)} V{L(cy+h-k)} A{L(k)} {L(k)} 0 0 0 {L(cx-h+k)} {L(cy+h)} '
             f'H{L(cx+h-k)} A{L(k)} {L(k)} 0 0 0 {L(cx+h)} {L(cy+h-k)} V{L(cy)} H{L(cx+h*0.05)}')
    inner = (f'M{L(cx+hi)} {L(cy-hi*0.58)} V{L(cy-hi+ki)} A{L(ki)} {L(ki)} 0 0 0 {L(cx+hi-ki)} {L(cy-hi)} H{L(cx-hi+ki)} '
             f'A{L(ki)} {L(ki)} 0 0 0 {L(cx-hi)} {L(cy-hi+ki)} V{L(cy+hi-ki)} A{L(ki)} {L(ki)} 0 0 0 {L(cx-hi+ki)} {L(cy+hi)} '
             f'H{L(cx+hi-ki)} A{L(ki)} {L(ki)} 0 0 0 {L(cx+hi)} {L(cy+hi-ki)} V{L(cy+hi*0.58)}')
    return (f'<path d="{outer}" fill="none" stroke="{color}" stroke-width="{L(wo)}" stroke-linejoin="miter"/>'
            f'<path d="{inner}" fill="none" stroke="{color}" stroke-width="{L(wi)}" stroke-linejoin="miter"/>'), x0 + H

def wordmark(bg=BLACK, rac=WHITE, accent=RED, tagline=True):
    TR, pad = 20, 90
    a, x = glyphs(heavy, 'RAC', 0, TR)
    b, x2 = glyphs(heavy, 'IN', x + 10, TR)
    sym, xe = gc(x2 + 10, accent)
    body = f'<g transform="skewX({SKEW})">{emit(a, rac)}{emit(b, accent)}{sym}</g>'
    width = xe
    h = CAP
    if tagline:
        txt = 'WHERE MONEY, POWER, AND SPEED COLLIDE.'; sc = 0.115
        _, w0 = glyphs(light, txt, 0, 0, sc)
        track = (width - w0) / (len(txt) - 1) / sc
        t, _ = glyphs(light, txt, 0, track, sc)
        body += f'<g transform="translate(0 {CAP*0.27:.0f})">{emit(t, SILVER)}</g>'
        h = CAP * 1.27
    skew_over = abs(__import__('math').tan(__import__('math').radians(SKEW))) * CAP
    vb_w = width + skew_over + 2 * pad; vb_h = h + 2 * pad
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vb_w:.0f} {vb_h:.0f}" role="img" '
            f'aria-label="Racing Inc.: RAC, IN and a fused G+C">\n<rect width="100%" height="100%" fill="{bg}"/>\n'
            f'<g transform="translate({pad} {pad+CAP})">{body}</g>\n</svg>\n')

def symbol(bg=BLACK, color=RED):
    import math
    s, _ = gc(0, color)
    over = abs(math.tan(math.radians(SKEW))) * CAP
    size = CAP * 1.7
    cx = (CAP + over) / 2 - 0; cy = -CAP / 2
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{cx-size/2:.0f} {cy-size/2:.0f} {size:.0f} {size:.0f}" role="img" '
            f'aria-label="Racing Inc. symbol: fused G and C"><rect x="{cx-size/2:.0f}" y="{cy-size/2:.0f}" width="{size:.0f}" height="{size:.0f}" fill="{bg}"/>'
            f'<g transform="skewX({SKEW})">{s}</g></svg>\n')

if __name__ == '__main__':
    open(OUT + 'wordmark-red.svg', 'w').write(wordmark())
    open(OUT + 'symbol-red.svg', 'w').write(symbol())
    print('cap height', CAP)
