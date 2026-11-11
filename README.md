# codepy

A personal laboratory for learning, experimenting, and shipping small things
in Python: data structures, algorithms, scripts, web services, databases,
and networking. Treat it as a living notebook. Some code is polished, some
is a sketch, and all of it is mine to learn from.

## Quick start

```bash
git clone https://github.com/<you>/codepy.git
cd codepy
python -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt
make test      # run the fast suite
make lint      # lint and type-check
```

## Repository layout

| Folder | Purpose | Status |
| --- | --- | --- |
| `01-foundations/` | DS&A, patterns, language idioms | 🟢 active |
| `02-scripts/` | Small utilities, automation, CLI tools | 🟢 active |
| `03-web/` | FastAPI/Flask apps, async servers | 🟡 intermittent |
| `04-databases/` | SQL, NoSQL, ORMs, migrations | 🟡 intermittent |
| `05-networking/` | Sockets, HTTP, protocols | 🟡 intermittent |
| `06-experiments/` | Dated spikes and proofs of concept | ⚪ on demand |
| `07-playground/` | Scratchpad, no guarantees | ⚪ on demand |
| `docs/` | Notes, cheatsheets, decisions | 🟢 active |
| `templates/` | Starter scaffolding for new subprojects | ⚪ |
| `archive/` | Retired code kept for reference | ⚪ |

## Sections

### 01 – Foundations

- `data-structures/` – hand-rolled implementations with complexity notes
- `algorithms/` – classic algorithms with tests
- `patterns/` – design patterns with minimal examples
- `python-idioms/` – "the Pythonic way" snippets

### 02 – Scripts

Standalone utilities. Each has a short docstring and, where practical, a test.

### 03 – Web

Small services and apps. Each subproject has its own `README.md` and
`pyproject.toml`.

### 04 – Databases

Schema experiments, query notebooks, ORM comparisons, migration demos.

### 05 – Networking

Raw sockets, HTTP clients and servers, protocol explorations.

### 06 – Experiments

Dated folders named `YYYY-MM-DD-short-topic/`. Each has a `README.md` and a
`NOTES.md`. Start one by copying `templates/experiment/`.

### 07 – Playground

Anything goes. Not linted, not tested, not guaranteed to run.

## Running things

`run.py` is a central dispatcher. With no arguments it lists the configured
targets. Otherwise it runs the target you name, passing the remaining
arguments through:

```bash
python run.py                 # list targets
python run.py <target> [args] # run a target
make run                      # list targets (same as python run.py)
```

Targets are registered in the `TARGETS` dict in `run.py` as
`"path/to/file.py:function"`.

## Conventions

- Each subproject is self-contained and has a `README.md` covering its
  purpose, how to run it, and what was learned.
- Python code targets 3.11+. Formatting uses `ruff format`, and linting uses `ruff`.
- Tests use `pytest` and live next to the code as `test_*.py`.
- Commits follow Conventional Commits (`feat:`, `fix:`, `exp:`, `docs:`).
- Experiments get a date prefix so it's clear when I explored what.
- Anything untouched for about 12 months moves to `archive/`.
- Secrets go in a `.env` file, which is gitignored. Copy `.env.example` to start.

## Writing it down

Every experiment ends with a short note in `docs/notes/`: what I tried,
what worked, and what I'd do differently. The code alone is forgetting;
the note is remembering.

## License

MIT (unless a subproject states otherwise).
