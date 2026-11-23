#!/usr/bin/env python3
"""Compose the 1024x1024 newspaper front page for 23 Nov 2026.

Run locally (Pillow + DejaVu fonts). The entry itself ships only the
finished entry.png plus a stdlib-only main.py that copies it to the
output directory, so the graded program needs no Pillow and no network.
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 234)
INK = (22, 22, 22)
RED = (176, 42, 30)
GREY = (90, 86, 78)
RULE = (180, 172, 156)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap by pixel width."""
    lines, line = [], ""
    for word in text.split():
        trial = (line + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            line = trial
        else:
            if line:
                lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def draw_wrapped(draw, x, y, text, fnt, width, fill=INK, leading=None):
    lines = wrap(draw, text, fnt, width)
    lh = leading or int(fnt.size * 1.22)
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += lh
    return y


def crop_cover(img, tw, th):
    """Centre-crop an image to the target aspect, then resize."""
    w, h = img.size
    scale = max(tw / w, th / h)
    img = img.resize((int(w * scale + 0.5), int(h * scale + 0.5)), Image.LANCZOS)
    x = (img.width - tw) // 2
    y = (img.height - th) // 2
    return img.crop((x, y, x + tw, y + th))


def main():
    work = "/home/hatch/workspace/makefun/news-image-20261123-2-work"
    page = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(page)

    # ---- Masthead ----
    d.text((512, 18), "THE WORLD IN ONE DAY", font=font(SERIF_B, 58),
           fill=INK, anchor="ma")
    d.text((512, 88), "MONDAY  23  NOVEMBER  2026",
           font=font(SANS_B, 24), fill=RED, anchor="ma")
    d.line([(28, 122), (996, 122)], fill=INK, width=3)
    d.line([(28, 128), (996, 128)], fill=INK, width=1)
    d.text((512, 134), "ANTALYA  •  THE BALTIC  •  KYIV  •  BANTEN  •  LISBON  •  SINALOA  •  SEOUL",
           font=font(SANS, 15), fill=GREY, anchor="ma")

    # ---- Lead story: COP31 ----
    y = 162
    d.text((28, y), "CLIMATE SUMMIT",
           font=font(SANS_B, 17), fill=RED)
    y += 24
    y = draw_wrapped(d, 28, y, "COP31 COLLAPSES AS WORLD",
                     font(SERIF_B, 40), 968, leading=44)
    y = draw_wrapped(d, 28, y, "SPLITS OVER FOSSIL FUELS",
                     font(SERIF_B, 40), 968, leading=44)
    y += 6
    cop = Image.open(f"{work}/media-generation-cop31-empty-hall-0-8cbe382e-f25f-490d-8f2b-c9e1b1ce5e1f.webp").convert("RGB")
    page.paste(crop_cover(cop, 968, 220), (28, y))
    y += 220 + 8
    y = draw_wrapped(
        d, 28, y,
        "No deal in Antalya: the final draft drops every mention of coal, oil and gas, "
        "and the EU, Britain and Pacific island nations refuse to sign \u2014 the first "
        "climate summit to fail since Copenhagen in 2009.",
        font(SERIF, 19), 968, leading=25)
    y += 6
    d.line([(28, y), (996, y)], fill=RULE, width=1)

    # ---- Second row: Baltic + Lisbon ----
    y += 12
    col_w, gap = 476, 16
    sparta = Image.open(f"{work}/media-generation-sparta-burning-ship-0-4f5d7b0d-224d-46ae-a844-451b91a4be0c.webp").convert("RGB")
    lisbon = Image.open(f"{work}/media-generation-lisbon-march-rain-0-e38db659-3963-46b3-ab79-35b2e9db3e6d.webp").convert("RGB")
    img_h = 150
    page.paste(crop_cover(sparta, col_w, img_h), (28, y))
    page.paste(crop_cover(lisbon, col_w, img_h), (28 + col_w + gap, y))
    iy = y + img_h + 8
    d.text((28, iy), "WAR AT SEA", font=font(SANS_B, 15), fill=RED)
    d.text((28 + col_w + gap, iy), "STREETS IN THE RAIN", font=font(SANS_B, 15), fill=RED)
    iy += 20
    hs = iy
    he1 = draw_wrapped(d, 28, hs, "SHIP STILL BURNING IN THE BALTIC",
                      font(SERIF_B, 24), col_w, leading=28)
    he2 = draw_wrapped(d, 28 + col_w + gap, hs, "LISBON MARCHES ON LIVING COSTS",
                       font(SERIF_B, 24), col_w, leading=28)
    ty = max(he1, he2) + 4
    ty = draw_wrapped(
        d, 28, ty,
        "The Russian cargo ship Sparta II smoulders off Finland after a drone strike; "
        "14 are missing after a drone hits flats near Kyiv.",
        font(SERIF, 16), col_w, leading=20)
    ty2 = draw_wrapped(
        d, 28 + col_w + gap, max(he1, he2) + 4,
        "Thousands brave heavy rain to demand higher wages, cheaper housing and "
        "relief from rising prices.",
        font(SERIF, 16), col_w, leading=20)
    y = max(ty, ty2) + 10
    d.line([(28, y), (996, y)], fill=RULE, width=1)

    # ---- Also today strip ----
    y += 10
    d.text((28, y), "ALSO TODAY", font=font(SANS_B, 16), fill=RED)
    y += 24
    items = [
        ("INDONESIA", "Candy factory fire near Jakarta: 3 dead, about 50 workers missing."),
        ("MEXICO", "FBI most-wanted \u201cEl Chapo Isidro\u201d captured; 11 killed in Sinaloa."),
        ("SOUTH KOREA", "Education minister quits over AI exam-cheating scandal."),
        ("AND MORE", "Nvidia chip-diversion row deepens; Myanmar calls ASEAN ruling \u201cunfair\u201d."),
    ]
    iw = (968 - 3 * 14) // 4
    bottom = y
    for i, (kick, text) in enumerate(items):
        x = 28 + i * (iw + 14)
        yy = draw_wrapped(d, x, y, kick, font(SANS_B, 14), iw, fill=RED, leading=17)
        yy = draw_wrapped(d, x, yy + 2, text, font(SERIF, 15), iw, leading=19)
        bottom = max(bottom, yy)
        if i < 3:
            d.line([(x + iw + 7, y), (x + iw + 7, yy)], fill=RULE, width=1)
    y = bottom + 8
    d.line([(28, y), (996, y)], fill=INK, width=2)
    d.text((512, y + 6), "THE WORLD IN ONE DAY  \u2022  MONDAY 23 NOVEMBER 2026",
           font=font(SANS, 14), fill=GREY, anchor="ma")

    out = "/home/hatch/workspace/makefun/news-image-20261123-2/entry.png"
    page.save(out, "PNG", optimize=True)
    print("saved", out)


if __name__ == "__main__":
    main()
