import math
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
F=__import__('os').environ.get('SAIRA_DIR','node_modules/@fontsource/saira/files/')
heavy=TTFont(F+'saira-latin-900-italic.woff2'); light=TTFont(F+'saira-latin-500-normal.woff2')
ang=heavy['post'].italicAngle; print('italic',ang)
def glyphs(font,text,x0,track=0,scale=1.0):
    gs=font.getGlyphSet(); cm=font.getBestCmap(); x=x0; out=[]
    for ch in text:
        if ch==' ': x+= (font['hmtx']['space'][0]+track)*scale; continue
        n=cm[ord(ch)]; p=SVGPathPen(gs); gs[n].draw(p)
        out.append((x,p.getCommands(),scale)); x+=(gs[n].width+track)*scale
    return out,x
def emit(items,fill):
    return ''.join(f'<path transform="translate({x:.1f} 0) scale({s} -{s})" d="{d}" fill="{fill}"/>' for x,d,s in items)

CAP=688; SK=math.tan(math.radians(abs(ang)))
def gc(x0, accent, size=1.0):
    """Fused G+C: outer G ring, inner C ring, G bar entering the C's mouth. Local coords: baseline y=0, y down => glyph spans y -688..0"""
    cx=x0+344; cy=-344
    def pt(r,deg): a=math.radians(deg); return cx+r*math.cos(a), cy+r*math.sin(a)
    Ro,wo=298,92   # outer G
    Ri,wi=146,80   # inner C
    # outer G: start upper-right (-40deg), counter-clockwise (sweep 0) around to 0deg (right-middle)
    sx,sy=pt(Ro,-40); ex,ey=pt(Ro,0)
    outer=f'<path d="M{sx:.1f} {sy:.1f} A{Ro} {Ro} 0 1 0 {ex:.1f} {ey:.1f}" fill="none" stroke="{accent}" stroke-width="{wo}"/>'
    bar=f'<rect x="{cx+30:.1f}" y="{cy-wo*0.9:.1f}" width="{Ro+wo/2-30:.1f}" height="{wo*0.9+0:.1f}" fill="{accent}"/>'
    # inner C opens on the right (+-48deg)
    a,b=pt(Ri,48); c,d=pt(Ri,-48)
    inner=f'<path d="M{a:.1f} {b:.1f} A{Ri} {Ri} 0 1 1 {c:.1f} {d:.1f}" fill="none" stroke="{accent}" stroke-width="{wi}"/>'
    return f'<g transform="skewX({-abs(ang)})">{outer}{bar}{inner}</g>', 700+SK*CAP*0.2
def build(accent, tagline=True, bg='#0A0A0B', rac='#FFFFFF'):
    TR=8
    a,x=glyphs(heavy,'RAC',0,TR); b,x2=glyphs(heavy,'IN',x+10,TR)
    sym,w=gc(x2+10,accent)
    total=x2+10+700+150
    H=CAP; pad=60
    body=f'<g transform="translate({pad} {pad+CAP})">{emit(a,rac)}{emit(b,accent)}{sym}</g>'
    h=CAP+2*pad
    if tagline:
        txt='WHERE MONEY, POWER, AND SPEED COLLIDE.'; sc=0.12; target=total-150+60
        _,w0=glyphs(light,txt,0,0,sc); track=(target-w0)/(len(txt)-1)/sc
        t,tx=glyphs(light,txt,0,track,sc)
        body+=f'<g transform="translate({pad} {pad+CAP+180})">'+emit(t,"#9AA0A6")+'</g>'
        h+=210
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {total+2*pad-90:.0f} {h}" role="img" aria-label="Racing Inc. wordmark: RAC, IN and a fused G+C">\n<rect width="100%" height="100%" fill="{bg}"/>\n{body}\n</svg>\n'
def symbol(accent,bg='#0A0A0B'):
    sym,_=gc(0,accent)
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-130 -894 1100 1100" role="img" aria-label="Racing Inc. symbol: fused G and C"><rect x="-130" y="-894" width="1100" height="1100" fill="{bg}"/>{sym}</svg>\n'
O=__import__('os').path.dirname(__import__('os').path.abspath(__file__))+'/'
for name,col in (('red','#D40000'),):
    open(O+f'wordmark-{name}.svg','w').write(build(col))
    open(O+f'symbol-{name}.svg','w').write(symbol(col))
