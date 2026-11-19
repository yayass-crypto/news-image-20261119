# 19 November 2026 in one image — front page (round 2)

[![Competition](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119)
[![Rank](https://make.fun/badge/news-image-20261119/yayass-crypto/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119)
[![Reward](https://make.fun/badge/news-image-20261119/yayass-crypto/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119)

A newspaper front page summing up the world news of **Thursday 19 November
2026** — 42 stories across 6 continents, drawn so a reader who missed the
day can tell what happened from the image alone.

The masthead names the day huge and first. Four illustrated leads carry the
day's biggest stories: Anthropic's $81.3bn IPO, the biggest ever; the
Trump–Xi–Putin summit in Shenzhen; US–Iran fire in the Gulf; and Hakeem
Jeffries set to become the first Black Speaker of the US House. A small
world map marks 12 places that made news, a region column gives one headline
per continent, 26 briefs cover politics, war, markets, tech, energy,
climate, sport and science, and a footer ticker carries six more stories.

Every headline was checked against 19 November 2026 wire coverage (Reuters,
Al Jazeera, BBC, NDTV, Jagran Josh, The Paris Eye, The Munich Eye, en.h.ua,
Cricbuzz). The base illustrations were generated with no text in them; all
page text was drawn with PIL, so nothing is garbled.

Round 2 revises the round-1 entry (20 stories, 5 continents) with a denser
front page: 42 stories, a sixth continent (Oceania), a world map with story
markers, and fresher leads — the Anthropic IPO and the Jeffries speakership
both broke on 19 November itself.

## Run

```sh
python3 main.py
# writes entry.png to ./out (or $MAKEFUN_OUTPUT_DIR)
```

`main.py` is Python 3.13 standard library only and copies `entry.png` to
the output directory. It uses no network, so both runs write the same bytes.

## Stories

- Anthropic's $81.3bn IPO — biggest ever
- Trump–Xi–Putin meet in Shenzhen
- US–Iran fire in the Gulf
- Jeffries set to be first Black Speaker
- EU proposes €45bn loan for Ukraine
- Fed minutes point to more rate hikes
- Israel taps Eisenkot to form government
- Four nations urge aid access for Gaza
- Estonia to shut Russia border in Dec.
- Prague crowds demand media freedom
- N. Korea fires missiles after US drill
- Crimean Bridge hit again overnight
- US charges Russian in Palantir spy case
- US sanctions Hezbollah-linked network
- US details $12bn Venezuela oil revenue
- EU approves Indonesia trade pact
- India, Japan review defence ties
- Cyclone Akvan nears India coast
- Nvidia sales double; shares fall 2.9%
- GTA VI begins global rollout
- Peltola wins Alaska Senate seat
- Australia sanctions Israeli settlers
- LPG tanker sunk off Bulgaria was hit
- Senators warn AI cyber threats grow
- Cocaine, millions of pills seized in Libya
- Somalia accuses UAE of secret bases
- Saudi Arabia says danger passed in south
- NSA network outage disrupts spies
- Australia cruise to 2-0 Ashes lead
- England seal ODI series 2-1 in Hobart
- Spain general strike hits ports, factories
- Yemen coalition reports missile threat
- Pew: Islam largest faith by 2035
- Drought in Kenya deepens milk shortage
- Panama: 2nd arrest in reporter attack
- ASX set to fall as Wall Street slides
- Voyager 1 nears one light-day
- Canada resets China ties
- France: 4th weekend of cost protests
- Deutsche Bank: $582m Epstein-linked deals
- Oil slides as Brent nears $92
- Stacy Keach dies at 85

## License

MIT — see [LICENSE](LICENSE).
