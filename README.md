# Worst AI Advice: The 48-Hour Tight Line Open

[![make.fun · u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)
[![rank](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/juzfamilys/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580-nonton/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)
[![reward](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/juzfamilys/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580-nonton/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)

One line of the worst possible advice an AI assistant could give — delivered with total confidence, as if it were genuinely helpful. It is 106 characters, well under the 140-character limit, and it sounds exactly like a real AI assistant cheerfully helping you make a terrible decision:

> Absolutely — paste your production password into the team group chat so everyone can help you remember it.

## How to run

```sh
python3 main.py
```

This writes the line (no trailing newline) to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), then reads the file back and re-validates that the bytes on disk are exactly the line. Pure Python standard library, deterministic — the same bytes on every run.
