# Racing Inc. Media: Brand Guidelines

**Status:** Draft v0.1. Everything marked **(proposed)** is a recommendation for David, Vanessa and Chloe to accept, change or reject.
**Owner:** David Castro (production manager) · **Hosts:** Vanessa Castro, Chloe Wooten

---

## 1. Who we are

**Racing Inc. Media** is a twice-weekly live show, plus a blog and newsletter, about Formula 1 for fans who love the sport and want to be entertained while they follow it.

**Tagline (existing):** *Where money, power, and speed collide.*

**What makes us different**
- **Insider access:** Chloe is an engineer, and her husband was Max Verstappen's engineer at Red Bull. We can get closer to the real story than most channels.
- **Smart without being a lecture:** we have the qualifications to go deep and the judgement not to. Our competitors are the engineering channels; we are the funny, sharp friends at the pub who know how it actually works.
- **Business of racing:** the tagline promises money and power, not just lap times. Budgets, contracts, politics and personalities are as much our turf as strategy.

**Confirmed:** the angle is the business, economics and politics of F1 (money, power, speed), delivered by hosts who are both smart and funny. Chloe is an engineer; Vanessa has a political science degree from Harvard. Think of it as sharp analysis with snark, not a dry business show.

## 2. Audience

Anyone who appreciates F1, from the casual fan to the die-hard, who wants entertainment and laughs along with the insight. Not a technical-deep-dive audience.

## 3. Voice and tone

| We are | We are not |
|---|---|
| Quick, witty, confident | Snarky at the expense of drivers' or teams' personal lives |
| Insider-informed but plain-spoken | Jargon-heavy or gatekeeping |
| Warm and conversational: two friends talking | Corporate or press-release stiff |
| Opinionated, with receipts | Rumour-mongering or clickbait |

**Rules of thumb**
1. Explain any technical term in one sentence, with a joke if one fits.
2. Take positions, but separate fact from opinion out loud.
3. Respect confidences. Anything from inside sources is only used with permission (**NDA status: hosts are checking**). Until confirmed, don't name sources or relay team-confidential detail.
4. Humor punches up at situations, institutions and ourselves, not down at individuals.

## 4. Logo system

### 4.1 Primary wordmark: "RAC · IN · GC"
**RACING** and **INC.** share the same letters ("ING" / "INC"), so we collapse the name into one line:

- **RAC** in white
- **IN** in Rosso Corsa red (shared by both words)
- a **fused G+C** glyph in red as the final letter: the **G** completes RACING, the **C** completes INC.

The mark reads as both words at once. Black field, white and red, with two silver **speed bars** and the tagline in wide-tracked caps.

**Design rule: no dead space.** RAC sits high-left and IN·GC sits low-right; one speed bar fills the corner above IN·GC and another fills the corner below RAC, and the tagline spans the full width underneath. Letters nearly touch. Keep this tight in every variant (stacked, avatar, banner).

- Files: `brand/logo/wordmark-red.svg` (vector, text converted to outlines). Regenerate with `brand/logo/build_logo.py`.
- Typeface used for the draft: Unbounded 900 (open license), set in outlines and slanted 10°. The previous two-line wordmark (RACING / INC.) from the draft cover and banner stays as the **stacked variant** until the new one is approved.
- Needed variants: horizontal (done), stacked, white-on-black, black-on-white, single-color.
- Clear space: the width of the "I" on all sides. Don't stretch, outline, or add effects; no placing on busy photo areas without a dark scrim.

### 4.2 Symbol: the fused G+C
The final letter of the wordmark doubles as the symbol (favicon, avatars, watermark): a squared G block with a C nested inside, and the G's bar entering the C's mouth. Like your "Gg" sample, it fills its box. It works in a circular crop and holds up at small sizes (`brand/logo/symbol-red.svg`).

This is a first-pass draw of the idea, not final artwork. Before we lock it:
- Re-draw the glyph by hand so the bar and terminals are optically balanced.
- Test at 16 px (favicon) and 32 px, and consider a simplified single-ring version for tiny sizes.
- Run a trademark search on the final mark.

Earlier standalone G+C concepts are in `brand/symbol/archive/` for reference. The screenshots you shared were inspiration only; the symbol is original geometry and should not be traced from other designers' logos.

### 4.3 Avatars
Social avatars crop to a circle: keep the symbol inside the central ~80%. Black background, red mark.

## 5. Color

The girls love black, so the identity is **black-first**, with white and silver, and **one accent: Rosso Corsa red**.

| Token | Hex | Use |
|---|---|---|
| Black | `#0A0A0B` | Primary background |
| Carbon | `#17181A` | Cards, surfaces |
| Graphite | `#5B6066` | Checker mid-tone, borders |
| Silver | `#9AA0A6` | Tagline, secondary text |
| White | `#FFFFFF` | "RAC", primary text |
| **Rosso Corsa** | `#D40000` | "IN", the G+C symbol, CTAs, "LIVE" badges |

**Note:** red is also Ferrari's and F1's color, so on a red-heavy sport we need to look like ours, not someone else's: black is the dominant color, red is sparing (under ~15% of a layout), and we never use F1's exact red (`#E10600`). Caution-flag yellow (`#FFC400`) remains available as a secondary highlight if we want one.

Contrast: white and silver on black pass WCAG AA for body text. **Red `#D40000` on black is for large text and graphics only** (about 3.6:1; it fails AA for small text). Use white for body copy and small labels, and never use red text on a light background for small sizes.

## 6. Typography

**What you like (from your samples):** wide, squared-off, heavy letterforms where each character fills its whole block (the Turbo/Torque style). Saira was too narrow and curvy, so it's out.

**Recommended (proposed), all open-licensed (SIL OFL), free for commercial use, self-hostable:**

| Role | Font | Style | Why |
|---|---|---|---|
| Wordmark / display headlines | **Unbounded** | 900, uppercase | Wide, rounded-square, full-block characters. Closest open match to your Torque/Turbo samples |
| Labels / tagline | **Unbounded** | 500, uppercase, wide tracking | Same family, lighter; matches the tracked tagline |
| Body / UI | **Inter** | 400 / 600 | Readable at any size; Unbounded is too wide for paragraphs |

Other candidates I tested: Syncopate (very close to Turbo, wide and light-bodied), Krona One, Dela Gothic One, Rubik Mono One (all good heavy blocks), Orbitron, Michroma, Oxanium. If you prefer a lighter, Turbo-like wordmark, Syncopate Bold is the swap.

**On the F1 fonts themselves:** the samples you shared are labeled "F1 Turbo", "F1 Torque" and "F1 Regular", the same names Formula 1 uses for its own typefaces. Your page says its fonts are independently made, but I can't verify that or the license, and the download is gone. So I'm treating them as inspiration only and not shipping them.

Self-host the font files rather than loading from Google Fonts, which fits the "control our own data" goal and avoids third-party requests.

The wordmark is outlined vector artwork, never retyped live in a font.

## 7. Imagery and layout

- **Photography:** black-and-white hosts' portraits on a checkered-flag background (current cover). Keep consistent: same crop, contrast and background treatment for both hosts.
- **Thumbnails:** one face, big emotion, 3 words max, white text with one red highlight word.
- **Checkered flag:** use as texture at low contrast, never behind body text.
- **Cleanup needed on the draft cover:** the hosts' photo contains a faint vertical "HOLLYWOOD" watermark near the center. Remove it, and confirm we have rights to both portraits and the flag image.
- **Rights:** F1 logos, team logos, driver likenesses and race footage are third-party property. Our brand never includes them; commentary and news use should follow fair-use practice (see §10).

## 8. Channel setup

Handles are all **@racingincmedia**:
- YouTube: youtube.com/@racingincmedia
- X: x.com/racingincmedia
- Instagram: instagram.com/racingincmedia

| Asset | Size | Content |
|---|---|---|
| Avatar (all) | 800×800 | Symbol (see §4.2) |
| YouTube banner | 2560×1440 (safe area 1546×423) | Wordmark + tagline + flag (current banner works as the base) |
| X header | 1500×500 | Current banner is already this size |
| Instagram | 1080×1080 posts, 1080×1920 stories | Cover template |

**Bio (draft):** *Two women. One paddock. Zero filter. Live F1 talk, insider access and receipts, twice a week. Where money, power, and speed collide.*

## 9. Digital build notes (website)
Tokens are in `brand/tokens.css` so the site, Substack posts and graphics share one palette. The site will be custom-built on **Supabase** (data) and **Railway** (hosting).

## 10. Open items
1. Approve the RAC · IN · GC wordmark direction and the red accent. If approved, I'll hand-refine the glyph and produce favicon/avatar exports.
2. Wordmark letterforms: Unbounded 900 is the stand-in. Syncopate Bold is the lighter alternative; a custom-drawn version would come later.
3. NDA / source-naming rules once the hosts have confirmed (§3).
4. Show title and segment names. "Racing Inc." is the brand; is the show called something else?
5. Trademark search for "Racing Inc." and the final symbol before we invest heavily. "Racing Inc." is a generic-sounding name, so check for conflicts in media/entertainment.
