# Visual & Multi-Register Exposition — Round 1

**Recommendation:** needs revision
overflow risk on most `##` units plus a missing figure for the tutorial's stated capstone idea (the agentic loop).

## Slide overflow

*Estimated from prose density only — I have not seen the rendered deck, so treat every line below as "worth a second look on the page," not a confirmed defect.*

- `01-context.prose.md` § Where it came from — too many ideas: classical force fields, DFT, the general MLIP concept, early GAP, MACE's ACE+GNN combination, and foundation-model coverage are all stacked in one paragraph with three citations. This is the densest single heading in the document.
- `01-context.prose.md` § What this tutorial covers — too many ideas: it is a four-section roadmap (Motivation, Content, Conclusion, plus scope exclusions) written as one flowing paragraph rather than a list.
- `03-content.prose.md` § MACE's mental model: a graph, read in many-body messages — genuinely dense, and possibly too many ideas: graph, message passing, many-body, and equivariance are each a distinct concept, and this is the one slide that also has to fit the figure underneath the text.
- `03-content.prose.md` § Pitfalls — too many ideas: three independent failure modes (extrapolation, MD blow-up, unit mismatch), each with its own explanation, written as one paragraph instead of three list items.
- `03-content.prose.md` § Using it: fine-tuning and active learning — too many ideas: fine-tuning, the committee/uncertainty concept, and the active-learning feedback loop are three separate ideas in one paragraph.
- `04-conclusion.prose.md` § What you can do now — too many ideas: five distinct capability statements (one per learning objective in topic.md) compressed into a single long sentence.
- `04-conclusion.prose.md` § Where to go next — too many ideas: four separate pointers (MACE/ASE docs, Matbench Discovery, NequIP/Allegro, agent-framework wiring), each with its own citation.
- `04-conclusion.prose.md` § Open edges — too many ideas: three distinct claims (foundation-model coverage vs. reliability, uncertainty quantification's research status, the agentic loop as shape-not-product).

Borderline, worth a glance but likely genuinely dense rather than overloaded (single throughline, just long):
- `01-context.prose.md` § What this is
- `02-motivation.prose.md` § Why it matters for agentic development
- `02-motivation.prose.md` § What goes wrong without it
- `02-motivation.prose.md` § When to reach for it
- `03-content.prose.md` § Atoms, energy, and forces
- `03-content.prose.md` § MACE as a tool in an agentic discovery loop

## Strengths

- `figures/mace-mental-model.svg` — the "Atoms as a graph" box earns its place: a small dot graph with edges gives real relational content to "nodes = atoms, edges = nearby neighbors," which the prose alone leaves abstract.
- `03-content.prose.md`, `04-conclusion.prose.md` — the paired headings ("Using it: running your first MACE molecular dynamics simulation" / "Using it: fine-tuning and active learning") are parallel and scannable, which helps a website reader landing mid-page.
- `01-context.prose.md` § What this tutorial covers, `04-conclusion.prose.md` § Where to go next — the `§ Motivation` / `§ Content` cross-references are good long-form connective tissue for the document register.
- No register-specific phrasing conflicts found — the prose is generally written in a neutral voice that reads fine in document and website form; the strain shows up specifically in the slide register, not as a document-vs-website tension.

## Weaknesses

- `figures/mace-mental-model.svg` — the middle "Message passing" box is text only (several rounds, equivariant, higher-order/many-body), which restates the prose rather than showing it. The two hardest concepts in the section — many-body aggregation and rotational equivariance — are exactly the ones left as words-in-a-box instead of drawn relationships. That is the closest thing in this document to the "restates a list as boxes" defect the brief warns against.
- No figure anywhere for the agentic discovery loop (propose → evaluate → decide → refine, with active-learning feedback), even though topic.md names it as the capstone thing the reader should be able to describe. It is currently conveyed only in prose split across two `##` units (fine-tuning/active learning, then the agentic tool section), asking the reader to assemble the loop-with-feedback structure unaided.
- No figure for the basic MD loop (compute energy/forces → nudge atoms → advance time → repeat), despite that loop being re-explained in prose at least twice (§ What this is, § Atoms, energy, and forces) and referenced again in § Using it: running your first MACE molecular dynamics simulation. A single small diagram introduced once would let later sections point back at it instead of re-narrating it.
- `03-content.prose.md` § MACE as a tool in an agentic discovery loop — opens by leaning on slide memory: "the active-learning cycle from the previous section means..." is a direct backward reference that works in document/website form (the reader can scroll back) but violates the presentation register's own standard of a slide that stands alone.
- The document contains no bullet lists anywhere, despite several headings being enumerable in content (three pitfalls, five capabilities, four pointers, a historical lineage of four-plus beats). This is the root cause of most of the overflow risk above — the same content as bullets would compress considerably for the slide register without changing what the document/website reader gets.

## Actionable

1. `03-content.prose.md` § MACE's mental model — redraw the "Message passing" box with actual relational content: e.g. two small rounds of arrows showing a node's message widening to include a neighbor's neighbor (many-body), plus a rotation glyph on the input/output boxes showing forces rotate with the atoms (equivariance). Do not just reformat the existing sentence into the box.
   (*why:* teaching value — the figure currently decorates this box rather than teaching it)

2. Add a new figure to `03-content.prose.md`, spanning § Using it: fine-tuning and active learning and § MACE as a tool in an agentic discovery loop — four boxes (Propose → Evaluate: MACE + committee → Decide → Refine: fine-tune), with the main loop arrow Decide→Propose and a second feedback arrow from Decide/Refine back into Evaluate for the active-learning cycle.
   (*why:* coverage — this is the tutorial's stated capstone idea and the one central relationship (a loop with a feedback branch) that prose alone is asking the reader to hold in their head across two slides)

3. Convert the list-shaped paragraphs to actual bullet lists: `04-conclusion.prose.md` § What you can do now (5 items) and § Where to go next (4 items); `03-content.prose.md` § Pitfalls (3 items).
   (*why:* presentation register — turns a single overloaded sentence/paragraph into slide-native bullets with no change to document meaning, and improves website scannability)

4. `01-context.prose.md` § Where it came from — split into two beats, e.g. (a) classical force fields → DFT → the general MLIP idea → early GAP, and (b) MACE = ACE + GNN, now available as foundation models. Keep as one paragraph in the document register if desired; split only for the slide.
   (*why:* presentation register — six ideas and three citations is too much for one projected slide)

5. `03-content.prose.md` § MACE as a tool in an agentic discovery loop — drop or rewrite "the active-learning cycle from the previous section," restating in one clause what active learning is rather than pointing back at the prior slide.
   (*why:* presentation register — a slide should not require memory of the slide before it)
