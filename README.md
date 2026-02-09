# CircleCI Smarter Testing Demo (Python / pytest)

This repo demonstrates [CircleCI Smarter Testing](https://circleci.com/docs/guides/test/getting-started-with-smarter-testing/) with **pytest** and enough tests to show:

- **Test discovery** – 15 test files discovered by `find ./tests -type f -name 'test*.py'`
- **Dynamic test splitting** – test files split across 4 parallel nodes in CI
- **Test impact analysis** – tests map to source modules via coverage (pytest-cov + pytest-circleci-coverage)
- **Auto rerun failed tests** – optional when enabled in Smarter Testing

## Prerequisites

- **Smarter Testing** is in preview. You need to be in the [Smarter Testing preview](https://circleci.com/docs/guides/test/getting-started-with-smarter-testing/#prerequisites) to use it in CI.
- Python 3.9+.

## Local setup

```bash
python -m venv venv
. venv/bin/activate   # or: source venv/Scripts/activate on Windows
pip install -r requirements.txt
pip install -e .
```

## Run tests (normal pytest)

```bash
pytest
# or with coverage:
pytest --cov=myproj --cov-report=term-missing
```

## Run tests via Smarter Testing (local)

1. Install [CircleCI CLI](https://circleci.com/docs/local-cli/) and the **testsuite** plugin:

   ```bash
   brew install circleci
   brew install circleci/tap/circleci-testsuite
   ```

2. From the repo root (with venv activated):

   ```bash
   circleci run testsuite "ci tests" --local
   ```

You should see discovery, selection, and the test run. `test-reports/` and `.circleci/impact.json` are in `.gitignore`.

## Commands to show off the feature

Run from the repo root with venv activated and the testsuite plugin installed.

| What you're showing | Command |
|--------------------|--------|
| **1. Normal pytest** | `pytest` |
| **2. Discovery + run** | `circleci run testsuite "ci tests" --local` |
| **3. Verbose** | `circleci run testsuite "ci tests" --local --verbose` |
| **4. Analysis only** (build impact data) | `circleci run testsuite "ci tests" --local --test-selection=none --test-analysis=all` |
| **5. Run all tests** | `circleci run testsuite "ci tests" --local --test-selection=all` |
| **6. List test files** | `find ./tests -type f -name 'test*.py'` |

**In CI:** Push to a repo on CircleCI and run the **smarter-testing-demo** workflow (or **test-pytest-only** if the testsuite plugin isn’t available). The job uses `parallelism: 4` and `store_test_results` for test-reports.

## Project layout

| Area | Purpose |
|------|--------|
| `.circleci/config.yml` | CI job: `circleci run testsuite "ci tests"` with `parallelism: 4`, plus fallback **test-pytest** job. |
| `.circleci/test-suites.yml` | Smarter Testing: `discover` (find test*.py), `run` (pytest + JUnit), `analysis` (pytest + pytest-circleci-coverage). |
| `myproj/lib/` | math, string_utils, array. |
| `myproj/services/` | calculator. |
| `myproj/utils/` | slug, validation. |
| `myproj/api/` | handlers. |
| `myproj/demo/` | health. |
| `tests/test_*.py` | 15 pytest test files. |

**Analysis** uses the [pytest-circleci-coverage](https://github.com/circleci/pytest-circleci-coverage) plugin so CircleCI can build the test–source impact map. It’s not on PyPI; `requirements.txt` installs it from GitHub (`git+https://github.com/circleci/pytest-circleci-coverage.git`).

## Troubleshooting

- **"Analysis not configured"** – Ensure `.circleci/test-suites.yml` has an `analysis` block and `pip install pytest-circleci-coverage` is done.
- **"Selecting no tests, --test-selection set to 'none'"** – Expected when using `--test-selection=none` (e.g. with `--test-analysis=impacted` to only run analysis).
- **First-time impact** – Use `--test-analysis=all` (not `impacted`) once to populate impact data when none exists.
- **Plugin not found** – Install the testsuite plugin: `brew install circleci/tap/circleci-testsuite`. For CI, the plugin is provided by CircleCI when Smarter Testing is enabled.
