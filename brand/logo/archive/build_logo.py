"""Builds brand/logo/*.svg. Needs: pip install fonttools brotli; npm i @fontsource-variable/anybody
Usage: FONTS_DIR=<node_modules/@fontsource> python3 build_logo.py"""
import os
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen

FD = os.environ.get('FONTS_DIR', 'node_modules/@fontsource')
from fontTools.varLib import instancer

def anybody(wght, wdth=150):
    f = TTFont(f'{FD}-variable/anybody/files/anybody-latin-standard-normal.woff2')
    return instancer.instantiateVariableFont(f, {'wght': wght, 'wdth': wdth})

heavy = anybody(900)      # ultra-expanded black for the wordmark
light = anybody(600, 100) # tagline, narrower so it stays legible
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
    wo, wi, gap = H * 0.17, H * 0.16, H * 0.045
    h = H / 2 - wo / 2                      # outer centerline half-size
    hi = h - wo / 2 - gap - wi / 2          # inner centerline half-size
    k, ki = H * 0.20, H * 0.09              # corner radii
    L = lambda v: f'{v:.1f}'
    outer = (f'M{L(cx+h)} {L(cy-h*0.40)} V{L(cy-h+k)} A{L(k)} {L(k)} 0 0 0 {L(cx+h-k)} {L(cy-h)} H{L(cx-h+k)} '
             f'A{L(k)} {L(k)} 0 0 0 {L(cx-h)} {L(cy-h+k)} V{L(cy+h-k)} A{L(k)} {L(k)} 0 0 0 {L(cx-h+k)} {L(cy+h)} '
             f'H{L(cx+h-k)} A{L(k)} {L(k)} 0 0 0 {L(cx+h)} {L(cy+h-k)} V{L(cy)} H{L(cx+h*0.05)}')
    inner = (f'M{L(cx+hi)} {L(cy-hi*0.62)} V{L(cy-hi+ki)} A{L(ki)} {L(ki)} 0 0 0 {L(cx+hi-ki)} {L(cy-hi)} H{L(cx-hi+ki)} '
             f'A{L(ki)} {L(ki)} 0 0 0 {L(cx-hi)} {L(cy-hi+ki)} V{L(cy+hi-ki)} A{L(ki)} {L(ki)} 0 0 0 {L(cx-hi+ki)} {L(cy+hi)} '
             f'H{L(cx+hi-ki)} A{L(ki)} {L(ki)} 0 0 0 {L(cx+hi)} {L(cy+hi-ki)} V{L(cy+hi*0.62)}')
    return (f'<path d="{outer}" fill="none" stroke="{color}" stroke-width="{L(wo)}" stroke-linejoin="miter"/>'
            f'<path d="{inner}" fill="none" stroke="{color}" stroke-width="{L(wi)}" stroke-linejoin="miter"/>'), x0 + H

def wordmark(bg=BLACK, rac=WHITE, accent=RED, bar=SILVER, tagline=True):
    """Tight, interlocking lockup: RAC sits high-left, IN+GC sits low-right. A speed bar fills the corner above IN+GC and
    another fills the corner below RAC, so the whole thing reads as one solid block (no dead space)."""
    import math
    TR, pad = -22, 70
    t_bar, g = CAP * 0.115, CAP * 0.045          # bar thickness, gap between bar and letters
    D = t_bar + g                                # vertical stagger of the second half
    a, xa = glyphs(heavy, 'RAC', 0, TR)
    b, xb = glyphs(heavy, 'IN', xa + 6, TR)
    sym, xe = gc(xb + 6, accent)
    width = xe
    k = abs(math.tan(math.radians(SKEW)))
    body = f'<g transform="skewX({SKEW})">'
    body += f'<g>{emit(a, rac)}</g>'
    body += f'<g transform="translate(0 {D:.1f})">{emit(b, accent)}{sym}</g>'
    # speed bars (parallelogram ends come from the skew)
    body += f'<rect x="{xa+6:.1f}" y="{-CAP:.1f}" width="{width-xa-6:.1f}" height="{t_bar:.1f}" fill="{bar}"/>'
    body += f'<rect x="0" y="{g:.1f}" width="{xa:.1f}" height="{t_bar:.1f}" fill="{bar}"/>'
    bottom = D
    if tagline:
        txt = 'WHERE MONEY, POWER, AND SPEED COLLIDE.'; sc = 0.3
        _, w0 = glyphs(light, txt, 0, 0, sc)
        while (width - w0) / (len(txt) - 1) / sc < 170: sc -= 0.005; _, w0 = glyphs(light, txt, 0, 0, sc)
        track = (width - w0) / (len(txt) - 1) / sc
        t, _ = glyphs(light, txt, 0, track, sc)
        ty = D + g * 1.6 + CAP * sc * 0.75 + CAP * 0.06   # cap height of tagline sits just below the lowered row
        body += f'<g transform="translate(0 {ty:.1f})">{emit(t, SILVER)}</g>'
        bottom = ty
    body += '</g>'
    x_min = -k * bottom - pad; x_max = width + k * CAP + pad
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x_min:.0f} {-CAP-pad:.0f} {x_max-x_min:.0f} {CAP+bottom+2*pad:.0f}" role="img" '
            f'aria-label="Racing Inc.: RAC, IN and a fused G+C">\n<rect x="{x_min:.0f}" y="{-CAP-pad:.0f}" width="{x_max-x_min:.0f}" height="{CAP+bottom+2*pad:.0f}" fill="{bg}"/>\n'
            f'{body}\n</svg>\n')

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
