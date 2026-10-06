---
id: taskurpxsandboxcatalogindexupgrade
title: "Finish the submissions catalog index upgrade"
desc: "The urpx-data-sandbox catalog becomes a metadata-driven, dual JSON-LD + CSV index: a submission is a flat directory and every facet (utility, commodity, rate plans, service class, version, dates) is read from the graph, not the path, with a schema, a corpus walker, and a CI check. The README states its scope. The version helper, its test, and gate-1 robustness already landed on main. Remaining: tests for the new tooling, vendored-source licensing from issue #4, the provisional-namespace decision, and a first submission."
updated: 1791244800000
created: 1791244800000
---

# Finish the submissions catalog index upgrade

| Field | Value |
|-------|-------|
| **Status** | Open — assigned to @dcj |
| **Repository** | `urpx-org/urpx-data-sandbox` |
| **Surface** | `scripts/update_catalog_index.py`, `scripts/corpus.py`, `catalog/`, `.github/workflows/validate-submission.yml` |
| **Already on main** | [#2](https://github.com/urpx-org/urpx-data-sandbox/pull/2), [#5](https://github.com/urpx-org/urpx-data-sandbox/pull/5), [#7](https://github.com/urpx-org/urpx-data-sandbox/pull/7) merged; [#1](https://github.com/urpx-org/urpx-data-sandbox/issues/1) closed |
| **Clarifies** | [#4](https://github.com/urpx-org/urpx-data-sandbox/issues/4) — submissions with several schedules, versions, or files per utility |
| **Related proposal** | [urpx-org/urpx #73](https://github.com/urpx-org/urpx/pull/73) (corpus declaration) |

The submissions catalog was a single flat CSV whose `urpx_version` column held the raw `targetURPXVersion` IRI, and a submission's facts came from a fixed `country/state/utility/commodity` directory path. This upgrade makes it a metadata-driven, dual, machine-generated index: a JSON-LD DCAT catalog beside the CSV, with a schema, a corpus walker, and a consistency check in CI. It arrives as a pull request against `urpx-org/urpx-data-sandbox`. It settles #4: the catalog is metadata-driven, so a submission is a flat directory and its facets are read from the graph, not the path; each submission is validated on its own; and the catalog indexes rather than serves. What is left is the test coverage for the new tooling and two decisions.

## What the pull request adds

- **Metadata-driven, not directory-driven.** A submission is a directory of files under `submissions/`; its name and place carry no meaning. The catalog reads the utility, commodity, rate plans, service class, version, and effective dates from the submitted metadata. The browsing hierarchy (utility, commodity, rate plan, version) emerges from those facets, and a facet a submission does not declare is left empty. The old `country/state/utility/commodity` path is gone, along with the README, submissions README, template, and pull-request template that described it.
- **A JSON-LD projection.** `catalog/submissions-index.jsonld` is a DCAT catalog: one `dcat:Dataset` per submission carrying its facets, a `dcat:Distribution` per file, and the summary counts as a graph a consumer can load into any RDF tool. It is a committed file, not a hosted service. `catalog/submissions-index.csv` stays as the flat, human-readable table. Both are generated together from the `submissions/` tree and are machine-owned.
- **A schema.** `catalog/submissions-index.schema.json` (JSON Schema draft-07) fixes the JSON-LD shape; `build` validates its output against it, and `check` fails a hand-edit that breaks it.
- **A corpus walker.** `scripts/corpus.py` lists the corpus files — `instance` documents and vendored `source` documents — one per line in byte order, filterable by kind, with a `--verify` mode that checks the walk against git's tracked files. It has no RDF dependency and is the single place that classifies a file; the generator imports that decision.
- **A consistency check in CI.** `update_catalog_index.py check` and `corpus.py --verify` run on every pull request. The post-merge job builds and commits both projections. A new submission is not required to be indexed on its own pull request; indexing stays post-merge, so the index never shares a commit path with a hand-edited file.
- **Licensing.** Both index projections are licensed as data (CDLA-Permissive-2.0); the schema is tooling (Apache-2.0) via a `.license` sidecar.

## Scope the catalog settles

Two scope points, now stated in the repository README, bound what the sandbox and its catalog do. They are the answer to the questions in #4 about what the sandbox is responsible for.

- **Each submission is validated on its own.** The sandbox does not resolve a rate plan's pricing models into rate plan or modifier version instances, and does not verify such a resolution. A submission that is only meaningful once resolved should carry a self-contained resolved snapshot that validates on its own, or be submitted as separate documents that each validate independently. Resolution is a data consumer's work.
- **The catalog indexes files; it does not serve queries over them.** The index links to the submitted files so the collection is browsable. A queryable service that resolves, joins, and serves rate plans is the role of a URPX data publisher implementation, not of a dataset repository.

## Addressing issue #4

- **A second schedule or version in a utility's directory (point 1). Resolved.** The directory hierarchy is gone. A submission is a flat directory under `submissions/`, and the catalog reads utility, commodity, rate plans, service class, version, and dates from the graph, not the path. A contributor separates schedules by putting each in its own directory; the catalog tells them apart by their distinct rate-plan identities in the metadata. There is no `country/state/utility/commodity` depth to navigate and no schedule level to add.
- **Per-file versus merged-graph validation (point 2).** Gate 1 validates each document on its own, which is the intended behavior: the sandbox does not resolve or verify a merged graph (see the scope above). A submission that only conforms once resolved should be submitted as a self-contained resolved snapshot, or as documents that each validate independently. The catalog's summary loads a submission's documents together only to count and summarize them, never to validate a resolution.
- **The license of a vendored source document (point 3).** Correct, and a real fix: a vendored tariff is the publishing utility's document, and the contributor cannot license it under CDLA. The fix is a REUSE annotation that separates a vendored source from the dataset — copyright the publishing utility, with a license reference appropriate to a public regulatory record — or a per-submission `.license` sidecar. The exact identifier is a licensing call, tracked below, and should be settled before the first submission carrying a vendored source merges.

## Already on main — build on, do not duplicate

- **#2** added `scripts/urpx_version.py` with `release_version`, which resolves a `targetURPXVersion` IRI to its semantic version, wired it into both the gate-1 validator and the catalog generator, and added `scripts/test_urpx_version.py`. This closed #1.
- **#5** made gate 1 report a submission it cannot read instead of stopping.
- **#7** restores rdflib's literal converters after each submission's validation.

The pull request uses the version helper from #2 and carries no copy of it; its only change to the gate-1 validator is none, since #2, #5, and #7 already cover that path.

## Remaining work

- [ ] **Tests for the catalog tooling.** `test_urpx_version.py` covers the helper; the new tooling has no tests. Add, in the same style: a `build` then `check` round-trip over a small fixture tree (clean passes; a hand-edited indexed row, a parity break between the two projections, and a schema violation each fail `check`); and a `corpus.py` walk and `--verify` case asserting the `instance` / `source` split and byte-order output.
- [ ] **Decide the provisional namespace and schema `$id`.** The facets read from the metadata and the summary counts use `sdx:` (`https://github.com/urpx-org/urpx-data-sandbox/ns#`), and the schema `$id` is `https://github.com/urpx-org/urpx-data-sandbox/schemas/submissions-index-1.0.0.json`. Both are rooted at the repository as a deliberately non-normative placeholder. The resolution path is the standard-repo task `backlog.task.urpx.std.2026-10-06.submission-schema-and-shapes-in-the-standard`: publish the submission schema (and a submission-validation SHACL) into the URPX standard under an official `urpx.org` namespace, then point the sandbox at those. The sandbox itself hosts no data either way.
- [ ] **Vendored-source licensing (issue #4, point 3).** Add the REUSE annotation, or a per-submission `.license` sidecar, that labels a vendored source document as the publishing utility's, with the right license reference, before the first submission carrying a vendored source merges.
- [ ] **Add a first submission.** The catalog, schema, and walker have been exercised against a synthetic fixture, but `submissions/` holds only the dataless `_template`, so the committed `submissions-index.jsonld` has an empty `dataset` list. A single small submission would exercise the whole path against live data and give the index its first row. Whether the repository carries a standing `_example` submission or waits for the first real one is a working-group call.
- [ ] **Optional hardening.** Add `reuse lint` to CI, as the standard repository runs it. Decide whether `check` and `corpus.py --verify` should gate a pull request or only inform it; they gate today.

## Relationship to the corpus declaration proposal

[urpx-org/urpx #73](https://github.com/urpx-org/urpx/pull/73) declared the standard repository's test-case corpus in a hand-maintained `corpus.json` with a schema and a walker. This brings that idea into the sandbox in a form that needs no hand-maintained declaration: the JSON-LD catalog is the machine-readable corpus declaration, generated from the tree; `submissions-index.schema.json` is its schema; and `corpus.py` is its walker, with the same deterministic, git-checked output. If a standalone declaration file in the standard repository is still wanted, the difference to carry into that discussion is generated-from-tree versus hand-maintained.

## Verify locally

```
pip install -r scripts/requirements.txt
python3 scripts/update_catalog_index.py build submissions/ catalog/
python3 scripts/update_catalog_index.py check submissions/ catalog/
python3 scripts/corpus.py submissions/ --all
python3 scripts/corpus.py submissions/ --verify
python3 scripts/validate_submission.py submissions/
```

## Work log

- **2026-10-05.** Built the dual-index generator (`build` and `check`), the corpus walker, the JSON Schema, the catalog README, the CI check and walker-verify steps, and the licensing, on top of the repository scaffold. Exercised the whole path against a synthetic fixture: build, check against hand-edits and schema breaks, the walk, and the git-agreement verify.
- **2026-10-06.** Reconciled with #2, #5, and #7 after they merged. Dropped the duplicate version helper and the validator edit; the catalog now uses the shared `release_version` from #2. Added the Scope section to the repository README (each submission validated on its own; the catalog indexes rather than serves).
- **2026-10-06 (metadata-driven redesign).** Reworked the catalog to read every facet — utility, commodity, rate plans, service class, version, dates — from the submitted metadata, and flattened the submission model to a free-form directory under `submissions/`, removing the `country/state/utility/commodity` path. Updated the generator's SPARQL and entry shape, the walker's submission discovery, the schema, and the repository README, submissions README, template, and pull-request template. Re-exercised build, check, walk, and verify against a two-bundle fixture. This resolves issue #4, point 1.

## Done when

- A test job runs in CI and covers the `build`/`check` round-trip and the `corpus.py` walk and `--verify`.
- The working group has ratified or relocated the `sdx:` namespace and the schema `$id`.
- Vendored-source licensing (issue #4, point 3) is settled before the first submission carrying a vendored source merges.
- At least one submission exercises the catalog against real data, or the working group has decided to wait for the first real one.
