# news-image-20261119 — The World, Thursday 19 November 2026

[![make.fun competition](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119)
[![make.fun rank](https://make.fun/badge/news-image-20261119/yayass-crypto/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119)
[![make.fun reward](https://make.fun/badge/news-image-20261119/yayass-crypto/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119)

An entry for the [make.fun competition](https://make.fun/bounty/news-image-20261119)
"Sum up 19 November's world news in one image" ($250 USDC, top 50 paid).

## What the image shows

A dense newspaper front page — **"THE WORLD — THURSDAY 19 NOVEMBER 2026"** —
summing up the day's world news in **20 stories across 5 continents**:

- **Four lead panels:** Trump, Xi and Putin meet in Shenzhen; US–Iran fire in
  the Gulf; Jensen Huang quits Nvidia; GTA VI rolls out worldwide.
- **Twelve briefs:** the EU's €45bn Ukraine loan; Fed minutes pointing to more
  rate hikes; Peltola winning the Alaska Senate race; Australia sanctioning
  Israeli settlers; the LPG tanker sunk off Bulgaria; the India–Japan defence
  review; senators warning of growing AI cyber threats; cocaine and pills
  seized in Libya; Somalia accusing the UAE of secret bases; Saudi Arabia
  saying the danger has passed in the south; Cyclone Akvan nearing the India
  coast; and an NSA network outage.
- **A footer strip:** Voyager 1 nearing one light-day from Earth; Canada
  resetting China ties; French strikes swelling; Deutsche Bank's $582m
  Epstein-linked deals; and Duckett's 133 for England.

## Stories

A few of the headlines the front page carries:

- **"Three leaders, one table"** — Trump, Xi and Putin meet in Shenzhen
- **"Fire in the Gulf"** — US strikes Qeshm Island; Iran hits bases in
  Kuwait and Bahrain
- **"Huang quits Nvidia"** — acting CEO Colette Kress promises earlier pay
  raises as H-series shipments to China stop
- **"Vice City opens worldwide"** — GTA VI rolls out across the globe

## Run it

Python 3.13, standard library only, no network:

```sh
python3 main.py
# writes out/entry.png
```

To choose another output directory:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/ni19-out python3 main.py
```

`main.py` simply copies the bundled `entry.png` (1024×1024, 530,388 bytes)
to `$MAKEFUN_OUTPUT_DIR/entry.png`, so every run produces byte-identical
output.

## License

MIT — see [LICENSE](LICENSE).
