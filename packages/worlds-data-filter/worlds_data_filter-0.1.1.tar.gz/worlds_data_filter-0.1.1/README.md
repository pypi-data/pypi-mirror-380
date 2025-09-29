# The World’s Data Filter™ — find the most valuable data, first.

**Surface your highest-value records with *information gain*, *novelty*, and *quality* scoring.**  
A universal SDK + CLI that ranks and subsets **text, JSONL, CSV, logs, and mixed corpora** so you see the signal first.  
Built on submodular selection (facility location), stable embeddings, diversity, and fast heuristics.

> Company: **The World’s Data Company** • Product: **The World’s Data Filter™**

---

## ✨ What it does

- **Universal features** — pluggable extractors for text, JSON/CSV/tabular, and generic blobs.
- **Information Gain** — greedy **facility‑location** selection to cover the dataset with minimal redundancy.
- **Novelty** — distances from dataset centroid / past cache to prioritize new signal.
- **Quality filters** — language/length heuristics for text; null/variance checks for tabular; duplicate/similarity suppression.
- **Explainable** — scores per item: `coverage_gain`, `novelty`, `quality`, and a `value_score` aggregate.
- **SDK & CLI** — embed in Python or run as `wdf` from the terminal.
- **Deterministic** — stable SHA‑256–based embeddings by default (swap for your own encoder at any time).
- **No heavy models** — NumPy/Scipy core; scikit‑learn is optional (`[text]` extra) for TF‑IDF.

> Year 2 roadmap: *The World’s Data Index* (persistent vector/metadata store) — this repo stays the stateless filter/selector.

---

## 🚀 Quickstart (Windows / macOS / Linux)

```bash
# 1) Create a virtualenv (Python 3.10+)
python -m venv .venv
# Windows
.\.venv\Scripts\Activate.ps1
# macOS/Linux
# source .venv/bin/activate

# 2) Install
pip install -U pip
pip install -e .[dev]            # add [text] for TF-IDF utilities if you like

# 3) Run the demo
wdf score examples/news.jsonl --text-field text --out scores.csv
wdf filter examples/news.jsonl --text-field text --k 10 --out selected.jsonl --explain
```

Outputs:
- `scores.csv` — per‑item `coverage_gain, novelty, quality, value_score`
- `selected.jsonl` — the top‑K items by the chosen criterion (default: `value_score`) with explanations included by default (disable via `--no-explain`)

---

## 🧠 How it works (high level)

### Feature extraction (adapters)
- **Text** → deterministic hash embedding (384‑d) or optional TF‑IDF.
- **JSONL/CSV** → flattened key/value signals, basic stats (NA ratio, variance), and hash embedding of important string fields.
- **Generic files** → filename, size, MIME guess, byte histograms (lightweight), hash embedding of content bytes.

Each item yields a vector `x_i` (unit‑normalized) and auxiliary quality features.

### Scoring
- **Facility Location (coverage)**  
  \(F(S)=\sum_j \max_{i\in S} \text{sim}(x_i, x_j)\) — select items that best cover the rest.  
  Greedy selection approximates the optimum and doubles as a *redundancy filter*.
- **Novelty**  
  Distance from dataset centroid (or *past cache*) highlights unusual / new items.
- **Quality**  
  Text heuristics (language guess, length, printable ratio), tabular health (missing‑ness, low variance), duplicate checks.

### Value score (combined)
`value_score = w_cov * coverage_gain + w_nov * novelty + w_quality * quality`  
Weights configurable in CLI/SDK.

---

## 🧰 CLI usage

```bash
# Score a JSONL corpus (one object per line) with a 'text' field
wdf score examples/news.jsonl --text-field text --out scores.csv

# Filter top-K by value score (explain is on by default)
wdf select examples/news.jsonl --text-field text --k 50 --out selected.jsonl

# Prefer compact JSONL (disable explanations)
wdf select examples/news.jsonl --text-field text --k 50 --out selected.jsonl --no-explain

# From a CSV (choose a text column)
wdf score examples/sample.csv --csv --text-field body --id-field id --out scores.csv

# Tune weights + disable novelty
wdf filter examples/news.jsonl --text-field text --k 20 --w-cov 0.8 --w-nov 0.0 --w-qual 0.2 --out selected.jsonl
```

**Input types supported today**
- `.jsonl` (id, text, and/or arbitrary fields)  
- `.csv` (choose columns)  
- Directory of `.txt` files (`--dir`)  
- Anything else you can adapt via a custom extractor (see `worlddatafilter/extractors/base.py`).

> You can register your own extractor in ~20 lines — the SDK passes through `meta` and `text` to downstream systems.

---

## 📦 Python SDK

```python
from worlddatafilter import WorldDataFilter, loaders

docs = loaders.load_jsonl("examples/news.jsonl", text_field="text")
wdf = WorldDataFilter()
scores = wdf.score(docs)      # list of ItemScore
selected = wdf.select(docs, k=25, weights=dict(cov=0.7, nov=0.2, qual=0.1))
```

---

## 🧪 Tests & Quality

```bash
ruff check .
pytest -q
```

---

## 🔌 Optional extras

- `pip install -e .[text]` → scikit‑learn TF‑IDF utilities.
- `pip install -e .[api]`  → simple FastAPI server exposing `/score` & `/filter` (coming soon).

---

## 📄 License

Apache License 2.0 © The World’s Data Company
