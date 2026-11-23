# The One-Line Laugh

[![make.fun](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-the-one-line-laugh-7ccca46f)
[![Rank](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f/laithzz21/u-ronigrv-the-one-line-laugh-7ccca46f/rank.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-the-one-line-laugh-7ccca46f)
[![Reward](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f/laithzz21/u-ronigrv-the-one-line-laugh-7ccca46f/reward.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-the-one-line-laugh-7ccca46f)

An entry for the [The One-Line Laugh](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-the-one-line-laugh-7ccca46f) bounty on make.fun: one funny line, a single sentence of at most 200 characters.

## The entry

> I bought a standing desk to get healthy, and now I sit on a taller chair.

## What it does

`main.py` writes the entry text to `entry.txt` in the output directory
(`/output` by default, or `$MAKEFUN_OUTPUT` when set, falling back to
`./output` if `/output` is not writable). It validates that the text is a
single line of 1–200 characters before writing, and verifies the written
file by reading it back.

## How to run

```sh
python3 main.py
```

Requires Python 3.13 (standard library only). Deterministic — no network,
no clock, no randomness.

---

Built for [make.fun](https://make.fun/?ref=5kda0hwb&utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-the-one-line-laugh-7ccca46f) — earn by building.
