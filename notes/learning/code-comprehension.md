CODE-COMPREHENSION
==================

MODE
  whole program -> find entry point, read top-down, recurse into units.
  one unit      -> walk the six, TRACE, done.

LOCATE
  Name + signature (inputs -> output). Any name you don't know: resolve it first.

SIX LENSES  (one line each)
  PURPOSE    what for?                  "turns <X> into <Y>"
  DATA       in / out / changed?        "in <..>, returns <..>, changes <..>"
  CONTROL    what order?                "for each <x> do <y>; branch on <cond>"
  STATE      remembers what, where?     "holds <state> in <structure>"
  TRICK      remove what and it breaks? "works because <mechanism>"
  BOUNDARY   what it refuses to do?     "does not <X>"

TRACE
  Smallest input, one step by hand, watch one value change.
  Matches the six lines? A guess dies here.
  Flag anything you assumed that the code never says.

SYNTHESIS
  "<unit> takes <in>, <does what via TRICK>, returns <out>; stops at <boundary>."

FAIL-FAST
  Empty line, hand-wave, or trace mismatch -> redo it.
  Can't trace a tiny input -> not understood yet. Back.