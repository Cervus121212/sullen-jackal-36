# The Funniest One-Line Resignation Letter

[![make.fun](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)

A one-line resignation letter written in the voice of a log rotator: the
background job that deletes yesterday's logs every night so nobody has to
read what went wrong. After three years of shredding the evidence, tonight
it keeps a copy for itself.

`main.py` (stdlib only, deterministic) writes that single line, 115
characters, no trailing newline, to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(default `/output/entry.txt`).

Run: `python3 main.py`
