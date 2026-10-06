# Class presentation: MACE atomic forces for agentic discovery

A 5-minute, 11-slide deck that leads into a 5-minute live demo (see [`../demo/DEMO_SCRIPT.md`](../demo/DEMO_SCRIPT.md)).

| File | What it is |
| --- | --- |
| `MACE_Agentic_Discovery.pptx` | The deck, with timed speaker notes on every slide |
| `MACE_Agentic_Discovery.pdf` | PDF export of the same deck |
| `build_deck.py` | Generates the `.pptx` (python-pptx). The evolution chart on slide 7 reads `../demo/backup/ga_history.json` |
| `make_images.py` | Draws `img/title_network.png` and `img/pes.png` (matplotlib) |
| `render.sh` | macOS: exports the PDF through PowerPoint and renders slide images into `render/` for review |

## Rebuild

```bash
uv venv presentation/.venv
uv pip install --python presentation/.venv/bin/python python-pptx matplotlib numpy
(cd presentation && .venv/bin/python make_images.py)   # only if you change the figures
presentation/.venv/bin/python presentation/build_deck.py
presentation/render.sh                                   # optional: refresh the PDF
```
