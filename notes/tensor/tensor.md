=================================
PREREQUISITE

Lists

STEP 0 — CLASSIFY
-----------------
1) Definition:     What is this thing?
--------------
    genus:  what wider category is it a kind of?
        ordering mechanism / collection
    differentia: what ONE trait separates it from the nearest 
        positional, keeps duplicates
    WRITE:        "A ___ is a [genus] that [differentia]."
        A list is a positional ordering mechanism that keeps duplicates.

2) Function:       What does it do?
--------------
    mechanism: transform
        what goes in?
            raw values paired with sequential indices.
        what comes out, or what changes?
            a single, ordered structure with addressable slots.
        Resolve:
            given raw values paired with sequential indices, 
            it produces a single, ordered structure with addressable slots.

3) Condition:      When does it apply or occur?
--------------
   Mechanism: trigger + precondition.
        What must already be true?
            A finite collection of valid data values exists.
        What situation makes you reach for it?
            You need duplicates to stay separate and positions to keep their exact meaning.
            
            for example:
            * Two people aged 32 stay separate in a list `(32, 32)` instead of collapsing into `{32}` in a set.
            * In `(weight, age)`, index 0 always tracks weight, ensuring `(72, 32)` and `(46, 12)` remain comparable.

        Resolve: "Use it when you need duplicates to stay separate and positions to keep their exact meaning, given a finite collection of valid data values."

4) Design reason:  Why is it designed this way?
--------------
    Mechanism: contrast.
        What is the nearest alternative you would use instead?
            set: unordered, deduplicated
        What does that alternative lose?
            order, multiplicity, and therefor index adresses.
        Resolve:
            To keep the order and duplicate values.
        for example:
            indices calculate memory slots directly (`base + index`), 
            flattening a 2D matrix coordinate `(row, col)` into a single row of RAM.
5) Boundary:       What must it not do or include?
   Mechanism: role purity.
    What nearby thing is it confused with?
        a Set, an Associative Map (Dictionary)
    What does that neighbor do that this must not?
        a Set filters out duplicates; 
        a Map looks up by unique key, not by position;
    Resolve:
        Not a Set (a list keeps duplicates), not a Map (found by position, not key),



F^n
Matrix
Matrix multiplication
