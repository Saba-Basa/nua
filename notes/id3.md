Q: Problem – Recursive Tree Construction (ID3)

Given:
A finite labeled dataset S consisting of samples with attribute–value pairs and a class label,
and a finite set of remaining attributes A = {A₁, A₂, …, Aₙ}.

Find:
A decision tree that classifies S by recursively splitting the dataset using attributes that yield the highest information gain.

Such that:
At each node, the algorithm chooses the attribute A* that maximizes the information gain IG(S, a).
- If all samples in S have the same class label - make a leaf with that label.
- If S is empty or no attributes remain - make a leaf with the majority label.
- Otherwise - split S by A*, create one child for each value of A*, and recurse.

------------------------------------------------------------

I: Input
A finite labeled dataset S and a finite set of candidate attributes A.

Let:
    A*        - attribute with the highest information gain
    v         - a possible value of A*
    S_v       - subset of S where A* = v
    H(S)      - entropy of S
    IG(S, a)  - information gain for attribute a

------------------------------------------------------------

O: Output
A decision tree T where:
    - Internal nodes test attributes (A*)
    - Branches correspond to attribute values (v)
    - Leaf nodes contain class labels (pure or majority)

------------------------------------------------------------

f: Transformation Rule
1. Check purity:
      If all samples in S share the same label - return a leaf with that label.

2. Check termination:
      If A is empty or S is empty - return a leaf with the majority label.

3. Attribute selection:
      For each attribute a ∈ A:
          - Compute IG(S, a)
      Choose A* = attribute with the highest IG(S, a).

4. Partition:
      For each value v of A*:
          - Define subset S_v = {x ∈ S : A*(x) = v}
          - Recursively apply this procedure to S_v with A \ {A*}
          - Attach the resulting subtree to the branch labeled v.

5. Return:
      A tree node labeled with A*, whose children correspond to each value v of A*.

------------------------------------------------------------

Interpretation
This process builds the decision tree top-down.
At each step, it chooses the attribute that most reduces uncertainty (max information gain),
splits the dataset accordingly, and repeats for each subset.

The recursion ends when:
- subsets are pure,
- no attributes remain, or
- stopping criteria (e.g., max depth) are met.

In short:
Choose - Split - Recurse - Stop when pure.
