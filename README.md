# codepy

A personal laboratory for learning, experimenting, and shipping small things
in Python — data structures, algorithms, scripts, web services, databases,
and networking. Treat it as a living notebook: some code is polished, some
is a sketch, and all of it is mine to learn from.

## Quick start

```bash
git clone https://github.com/<you>/codepy.git
cd codepy
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
make test      # run the fast suite
make lint      # format + lint
```

## What this is not

This is not a library, not a monorepo, and not production code. It is a personal lab. Do not over-engineer it.

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
- `algorithms/` – classic algorithms + tests
- `patterns/` – design patterns with minimal examples
- `python-idioms/` – "the Pythonic way" snippets

### 02 – Scripts

Standalone utilities. Each has a short docstring and, where practical, a test.

### 03 – Web

Small services and apps. Each subproject has its own `README.md` and
`pyproject.toml`; the top-level Makefile exposes a `run-<name>` target.

### 04 – Databases

Schema experiments, query notebooks, ORM comparisons, migration demos.

### 05 – Networking

Raw sockets, HTTP clients/servers, protocol explorations.

### 06 – Experiments

Dated folders: `YYYY-MM-DD-short-topic/`. Each has a one-line `NOTES.md`
explaining the question and the conclusion.

### 07 – Playground

Anything goes. Not linted, not tested, not guaranteed to run.

## Conventions

- Each subproject is self-contained and has a `README.md` with:
  purpose, how to run, what was learned.
- Python code targets 3.11+; formatting via `ruff format`, linting via `ruff`.
- Tests use `pytest`; place them next to the code as `test_*.py`.
- Commits follow Conventional Commits (`feat:`, `fix:`, `exp:`, `docs:`).
- Experiments get a date prefix so I can see when I was exploring what.
- Anything I haven't touched in ~12 months goes to `archive/`.

## Writing it down

Every experiment ends with a short note in `docs/notes/`:
what I tried, what worked, what I'd do differently. The code alone is
forgetting; the note is remembering.

## Secrets

Never commit secrets. Copy `.env.example` to `.env` for local experiments; `.env` is gitignored.

## License

MIT (unless a subproject states otherwise).
