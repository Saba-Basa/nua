CODE-COMPREHENSION
=================================
ANCHOR — pick the mode
----------------------
Whole program?      -> LOCATE the entry point, read top-down, recurse into units as needed.
One unit (fn/loop)? -> LOCATE it, walk the six lenses once, TRACE, done.

LOCATE THE UNIT   (once, before the walk)
-----------------------------------------
Name the exact thing and its boundary: signature = name + inputs + output.
Read it once without judging.
Mark every name you do NOT know -> resolve those FIRST (you can't read on top of a gap).

THE SIX LENSES   (each: how to find it, then a one-line Resolve)
---------------------------------------------------------------
PURPOSE     What is it for?
    Find: strip the HOW, keep the WHY. One job.
    Resolve: "This <unit> turns <X> into <Y>."
---------------------
DATA        What goes in, what comes out or changes?
    Find: list inputs; list return value + every mutation + every side effect (IO, print, write).
    Resolve: "In: <inputs>. Out: <return>. Changes: <state/effects>."
---------------------
CONTROL     In what order does it run?
    Find: the skeleton only — sequence, branches, loops, calls. Ignore the bodies.
    Resolve: "For each <x> it <does y>; branches when <cond>."
---------------------
STATE       What does it remember, and where does that data live?
    Find: which values persist across steps/iterations? Who owns and mutates them?
    Resolve: "Holds <state> in <structure>, updated by <how>."
---------------------
TRICK       The one idea it hinges on.
    Find: which single line/mechanism, if removed, breaks it? (the non-obvious part.)
    Resolve: "It works because <central mechanism>."
---------------------
BOUNDARY    What does it deliberately NOT do?
    Find: scope edges, unhandled cases, work left to the caller.
    Resolve: "It does not <X>; that lives in <where>."

TRACE   (the proof — DO NOT skip; this is what the other templates lack)
------------------------------------------------------------------------
Pick the smallest possible input.
Run it by hand, ONE step. Watch ONE value change.
Does reality match your six Resolves?
A guessed Resolve dies here. Understanding survives here.

CHECK   (after the walk)
------------------------
Every lens filled?
Trace matched the Resolves?
Any name still unknown?
What did you assume that the code never actually says?

SYNTHESIS   (fuse the six into ONE line)
----------------------------------------
WRITE: "<unit> takes <input>, <does what — via the TRICK>,
         producing <output>; it stops at <boundary>."

FAIL-FAST
---------
Empty lens, hand-wave, or trace mismatch -> redo that lens.
Unknown name -> resolve it first.
Can't trace even a tiny input -> you do NOT understand it yet. Go back.