# Structuring a "Code Playground" Repository

Great instinct — a personal code lab is one of the best long-term investments you can make. Let me give you a concrete
README structure, a directory layout, and then flag things you might be missing.

## Suggested Directory Layout

```
codepy/
├── README.md
├── .gitignore
├── .editorconfig
├── LICENSE
├── Makefile              # common commands (lint, test, run)
│
├── 01-foundations/       # language, DS&A, design patterns
│   ├── data-structures/
│   ├── algorithms/
│   ├── patterns/
│   └── python-idioms/
│
├── 02-scripts/           # general-purpose, small utilities
│   ├── automation/
│   ├── file-tools/
│   └── cli/
│
├── 03-web/               # servers and apps
│   ├── fastapi/
│   ├── flask/
│   └── async-servers/
│
├── 04-databases/         # SQL, NoSQL, ORMs, migrations
│   ├── sql/
│   ├── nosql/
│   ├── orms/
│   └── migrations/
│
├── 05-networking/        # sockets, HTTP, protocols
│   ├── sockets/
│   ├── http-clients/
│   └── protocol-experiments/
│
├── 06-experiments/       # throwaway / spike code, dated
│   └── YYYY-MM-DD-topic/
│
├── 07-playground/        # pure scratchpad
│   └── ...
│
├── docs/                 # notes, learnings, architecture sketches
│   ├── notes/
│   └── cheatsheets/
│
├── templates/            # project scaffolding templates
└── archive/              # retired code you don't want to delete
```

**Why numbered prefixes?** They force a stable, meaningful order in editors and `ls` output, and leave room to insert
new sections later. You can drop them if you prefer semantic names only.

**Why separate `experiments/` and `playground/`?**

- `experiments/` = dated, potentially reusable spikes (a blog post, a benchmark, a proof of concept)
- `playground/` = truly disposable scratch — ignore it in linting, don't worry about quality

## README.md Template

````markdown
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
pip install -r requirements-dev.txt
make test      # run the fast suite
make lint      # format + lint
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

## License

MIT (unless a subproject states otherwise).
````

## Things You Might Be Missing

Here's the checklist of things a README like this *implies* but a repository often forgets:

### 1. Tooling for consistency

A lab with many mini-projects needs a **root-level toolchain** so you don't re-invent it per folder:

- **`Makefile`** (or `justfile`) with `lint`, `test`, `format`, `clean` targets.
- **`ruff`** for lint + format (fast, covers most needs).
- **`pyright`** or **`mypy`** for type checks, at least on `01-foundations/` and `03-web/`.
- **`pre-commit`** hooks so you don't commit broken playground code by accident.

### 2. A lockfile / dependency strategy

Decide up front: is the root a **single virtualenv** for everything, or does each subproject carry its own
`pyproject.toml`? For a lab, **per-subproject `pyproject.toml` + a shared dev environment** usually works best. Document
the choice in the README.

### 3. `.gitignore` and ignore policy

- Standard Python ignores (`.venv/`, `__pycache__/`, `*.pyc`, `.pytest_cache/`).
- Add `07-playground/` to `ruff`'s exclude list (and maybe `mypy`) so scratch code doesn't pollute CI.
- Consider `.gitattributes` for consistent line endings.

### 4. A LICENSE

If it's public, pick one (MIT is fine). If it's private, say so.

### 5. CI (yes, even for a playground)

A tiny GitHub Actions workflow that runs `make lint` and `make test` on push makes the lab *sustainable* — it stops the
slow rot from creeping in. It also forces every subproject to be runnable.

### 6. A "status board" in the README

A simple table (as in the template above) with 🟢/🟡/⚪ markers saves you from pretending every folder is equally alive.
Consider also a `STATUS.md` or a section in the README with the date each area was last touched.

### 7. A `docs/` habit

The single biggest thing that separates a good lab from a graveyard of code is **written notes**. Cheatsheets, decision
records (ADR-style), complexity tables, "what I learned" files. Add a `docs/notes/` convention in the README so it's not
an afterthought.

### 8. A `templates/` starter

A skeleton for a new experiment (`templates/experiment/`) with a `README`, `pyproject.toml`, and a `NOTES.md` stub
turns "start a new idea" into a 10-second operation.

### 9. An archive policy

Explicitly state the rule for when code retires to `archive/`. Without it, the repo grows without bound and the good
stuff gets buried.

### 10. Naming conventions

Document them in the README:

- Scripts: `verb_noun.py` (e.g., `download_pdfs.py`)
- Packages: `snake_case`
- Experiment folders: `YYYY-MM-DD-topic`
- DS implementations: `ds_<name>.py` vs `algo_<name>.py` — pick one and stick to it

### 11. A small CONTRIBUTING section (even if it's "just you")

Future-you is a different person. Write down how to add a new section, what qualifies as "done", and how the README
table should be updated.

### 12. "What this is not"

A one-liner clarifying that this is *not* a library, *not* a monorepo, and *not* production code. This prevents
future-you from over-engineering it.

### 13. Secrets handling

If you ever put API experiments in `03-web/` or `04-databases/`, add a `.env.example` convention and make sure `.env` is
gitignored. State it in the README.

### 14. Optional: a top-level `pyproject.toml` for shared dev deps

If you want one command to set up the whole lab (`pip install -e ".[dev]"`), a thin root `pyproject.toml` that only
carries dev tooling is a nice compromise with per-subproject packaging.

---

If you'd like, tell me whether the repo will be **public or private** and whether you want a **single env** or *
*per-subproject envs**, and I can tailor the `Makefile`, `pyproject.toml`, `.gitignore`, and CI workflow to match.
