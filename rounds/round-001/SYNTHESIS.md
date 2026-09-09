# Round 1 — Synthesis

**Panel recommendation:** needs revision
**Seats:** clarity needs revision · pedagogy needs revision · visual needs revision

## Since last round

First round — no prior docket.

## Consensus

- **The tutorial's central hands-on claim is asserted, not shown.** Clarity and pedagogy independently landed on the same defect from different angles: `topic.md` and `04-conclusion.prose.md` both promise the reader can "load a pretrained MACE foundation model into ASE and run a molecular dynamics simulation" and "fine-tune a MACE foundation model on new data," but neither "Using it" subsection in `03-content.prose.md` contains a single import, function call, or command — only prose description of what the code would do. Pedagogy calls this the one gap large enough to determine the whole recommendation; clarity independently flagged the same passage against the same promise in `topic.md`.
- **§ MACE's mental model is carrying too much for one unit, in both prose and figure.** Pedagogy flagged the prose as cramming graph representation, message passing, many-body order, and equivariance into one dense paragraph for a reader with no assumed neural-network background. Visual, reading the same section for a different reason (slide density and figure teaching value), independently flagged it as the densest content unit that also has to share its slide with the figure — and found that the figure's own "Message passing" box merely restates the prose in words rather than drawing the two hardest relationships (many-body aggregation, equivariance). Two seats, two lenses, one passage.

## Conflicts

- none

## Docket

1. **Show the code, not just the description, in both "Using it" subsections** — `sections/03-content.prose.md` § Using it: running your first MACE molecular dynamics simulation, § Using it: fine-tuning and active learning
   *Raised by:* clarity, pedagogy · *Effort:* medium
   Add a short, real code excerpt to each: for the MD run, the imports, building the `Atoms` object, attaching the MACE-MP-0 calculator, and calling an ASE dynamics integrator for a handful of steps (10–15 lines is enough); for fine-tuning, a minimal CLI invocation or config snippet showing what "fine-tune on a small DFT dataset" looks like in practice. If code genuinely does not belong on the page, reframe the prose claim from "you can now do this" to "this is the shape of the workflow" in both `03-content.prose.md` and `04-conclusion.prose.md` — but that is the weaker option, since it walks back a capability `topic.md` promises.

2. **Fix the misattached DFT citation and name Behler–Parrinello in the prose** — `sections/01-context.prose.md` § Where it came from
   *Raised by:* clarity · *Effort:* small
   `[@behler2007generalized]` currently sits right after "density functional theory (DFT)," but that paper is the founding Behler–Parrinello neural-network *potential* work, not a DFT reference — a reader who follows the citation to learn about DFT lands on the wrong paper. Move the citation onto the machine-learned-potentials sentence and name Behler–Parrinello in text there, closing the gap between what `01-context.concepts.md`'s stated lineage claims and what the shipped prose actually says.

3. **Redraw § MACE's mental model so the hardest ideas are drawn, not just paraphrased in a box** — `sections/03-content.prose.md` § MACE's mental model: a graph, read in many-body messages; `figures/mace-mental-model.svg`
   *Raised by:* pedagogy, visual · *Effort:* medium
   Redraw the figure's "Message passing" box with actual relational content — e.g., two small rounds of arrows showing a node's message widening to include a neighbor's neighbor (many-body), plus a rotation glyph on the input/output boxes showing forces rotate with the atoms (equivariance) — instead of restating the prose as text in a box. This is the more leveraged of the two available fixes: making the two hardest concepts visual addresses both pedagogy's cognitive-load concern and visual's teaching-value concern in one pass, rather than only shortening the prose.

4. **Convert enumerable prose to bullet lists** — `sections/03-content.prose.md` § Pitfalls; `sections/04-conclusion.prose.md` § What you can do now, § Where to go next
   *Raised by:* visual · *Effort:* small
   Three pitfalls, five capabilities, and four pointers are each currently one flowing paragraph or sentence. Converting each to a bullet list changes no document meaning, improves website scannability, and is the single cheapest fix available for the slide-overflow risk visual flagged across these three headings.

5. **Add a figure for the agentic discovery loop** — `sections/03-content.prose.md` § Using it: fine-tuning and active learning / § MACE as a tool in an agentic discovery loop
   *Raised by:* visual · *Effort:* medium-large
   `topic.md` names the propose → evaluate → decide → refine loop, with active-learning feedback, as the tutorial's capstone idea, but it is currently conveyed only in prose split across two `##` units. A four-box figure (Propose → Evaluate: MACE + committee → Decide → Refine: fine-tune, with a feedback arrow from Decide/Refine back into Evaluate) would give the reader the one relationship the prose is currently asking them to assemble unaided.

6. **Trim `03-content`'s opening two units to a callback instead of re-deriving `01-context`** — `sections/03-content.prose.md` § Atoms, energy, and forces; § From a quantum calculation to a machine-learned shortcut
   *Raised by:* clarity · *Effort:* small-medium
   Both units re-derive, almost point for point, what `01-context.prose.md` § What this is and § Where it came from already said, with no signal that it's a recap. Compress each to a one- or two-sentence callback ("Recall: MD needs energy and forces recomputed at every step, and DFT is too slow to supply them directly") and spend the recovered space on what's actually new in `03-content` — the section `topic.md` says should carry the tutorial's weight.

7. **Give the committee's uncertainty signal one concrete numeric illustration** — `sections/03-content.prose.md` § Using it: fine-tuning and active learning
   *Raised by:* pedagogy · *Effort:* small
   "Close agreement suggests a reliable prediction, and disagreement is a usable signal" stays entirely abstract, even though this signal is the mechanism the agentic tie-in depends on. One illustrative scale (e.g., "agreement within a few meV/atom on familiar structures vs. a large spread on an unfamiliar one") moves this from asserted to demonstrated at the cost of a sentence.

## Deferred

- Split `01-context.prose.md` § Where it came from into two beats for the slide register — visual, small; may shrink naturally once item 2's citation fix and general trimming land, worth re-checking before committing separate effort to it.
- Add a one-sentence internal roadmap to the top of `03-content.prose.md` — clarity, small; genuinely useful but the section's shape will change from items 1, 3, and 6 above, so a roadmap written now would need rewriting anyway.
- Drop or rewrite the backward reference "the active-learning cycle from the previous section" in § MACE as a tool in an agentic discovery loop — visual, small; a real one-line presentation-register fix, but the section's opening will likely change from item 5's figure work regardless.
- Add a figure for the basic MD loop (compute → nudge → advance → repeat) — visual, medium; genuinely useful but a third new/redrawn figure in one round is a lot of visual-design work to ask for at once, and item 6's trim may reduce how many times this loop gets re-narrated in the first place.

## Do next

Take items 1, 2, and 3 this round. Item 1 is the one pedagogy names as tier-determining — it is the largest single gap between what this tutorial promises and what it delivers, and closing it is what would move the panel recommendation off "needs revision." Item 2 is nearly free and fixes an actual factual misattachment. Item 3 is where two independent seats converged on the same passage, and the figure fix is more leveraged than a prose-only fix would be. Items 4–7 are all real and cheap, but none of them individually determines the recommendation the way 1 and 3 do — take them next round if 1–3 don't already reshape the sections they sit in.

## Panel health

No seat in `personas/` is briefed to check technical or scientific accuracy of the domain claims themselves (only clarity's exposition lens happened to catch the misattached DFT citation, as a side effect of checking terminology, not as a deliberate fact-check). For a document this technical — DFT, equivariance, message passing — a domain-accuracy seat or an explicit fact-check pass may be worth adding if factual precision keeps surfacing only as a byproduct of other seats' reads.
