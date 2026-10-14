# Saw math

The jug names the ratio, the link names the file, and the bar names the log.

Two-stroke advice lives in folklore: "a cap per tank" mixes a different ratio in every garage, file kits get bought by pouch color, and the bar's reach gets discovered mid-cut. The numbers were never mysterious.

## The three tools

- **Mix plan** - gas gallons and ratio become exact oil ounces: `gal x 128 / ratio`, rounded to hundredths.
- **File plan** - chain pitch becomes the round file: labeled norms of 5/32, 3/16 and 7/32 across 1/4, .325, 3/8 and .404 pitches. The stamp on the drive link and the manual outrank any chart.
- **Log plan** - bar versus log, judged unrounded: one pass up to bar minus 2 in, two passes up to twice that minus a bite, beyond the bar after that.

## Honesty notes

Illustrative planning arithmetic only. Ratios, file sizes and bar reach are labeled norms; the saw's manual and the chain's stamp govern. Chainsaws cut people as fast as wood: chaps, helmet, eye and ear protection, both hands on the saw, nothing above shoulder height, and kickback is the tip touching what it should not. Felling trees is a course, not a calculator.

## Files

- `index.html` - the pitch
- `app.html` - the calculators
- `engine.js` - the arithmetic (browser and node)
- `oracle.py` - the same arithmetic, float-for-float, writing `expected.json`
- `test.js` - runs every case in `expected.json` through `engine.js` and compares results and renders exactly

Run the check:

```
python3 oracle.py && node test.js
```
