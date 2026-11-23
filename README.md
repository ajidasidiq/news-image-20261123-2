[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/ajidasidiq/news-image-20261123-2/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/ajidasidiq/news-image-20261123-2/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

# The World in One Day — Monday 23 November 2026

A newspaper front page summing up the world's news of Monday 23 November 2026,
for the make.fun bounty `news-image-20261123` — see the bounty page at
https://make.fun/bounty/news-image-20261123.

## What the image shows

- **Lead — COP31 collapses in Antalya:** after two weeks of talks and two days
  in overtime, the UN climate summit ended with no deal. The final draft dropped
  every mention of fossil fuels, and the EU, Britain and Pacific island nations
  refused to sign — the first climate summit to fail since Copenhagen in 2009.
  Illustrated by an empty conference hall with a cracked globe.
- **War at sea — ship still burning in the Baltic:** the Russian cargo ship
  Sparta II smoulders off Finland after a drone strike; 14 are missing after a
  drone hits flats near Kyiv.
- **Streets in the rain — Lisbon marches on living costs:** thousands brave
  heavy rain to demand higher wages, cheaper housing and relief from rising
  prices.
- **Also today:** a candy factory fire near Jakarta leaves 3 dead and about 50
  workers missing; FBI most-wanted "El Chapo Isidro" is captured in Mexico
  with 11 killed in Sinaloa; South Korea's education minister quits over an
  AI exam-cheating scandal; the Nvidia chip-diversion row deepens and Myanmar
  calls an ASEAN ruling "unfair".

## How it works

`main.py` (Python 3.13, standard library only) copies the finished front page
`entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`). It uses no
network and every run writes the same bytes.

The front page was built fresh in this session: three flat editorial
illustrations were generated for this entry, then typeset with real fonts by
`build_frontpage.py` (Pillow, local build tool only — not used by the entry
program) into the 1024x1024 PNG. All headlines and captions were checked
against news reporting of 23 November 2026.

## License

MIT — see `LICENSE`.
