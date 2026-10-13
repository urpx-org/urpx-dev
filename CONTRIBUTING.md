<!-- SPDX-FileCopyrightText: The URPX Authors -->
<!-- SPDX-License-Identifier: Apache-2.0 -->

# Contributing to urpx-dev

Thank you for your interest in contributing to the URPX design and process record. This repository holds the working group's tasks, specifications, working reports, roadmaps, review materials, the design-decision log, and worked sample instances. It is developed under the Linux Foundation Energy Standards and Specifications (LFESS) Working Group process, alongside the standard itself in [`urpx-org/urpx`](https://github.com/urpx-org/urpx).

## General expectations

All issues, pull requests, and other repository submissions must be written and reviewed by the person submitting them.

Do not submit content that is fully AI-generated, overly verbose, speculative, or padded with background material that is not necessary to evaluate the request. Submissions that appear to be fully AI-generated or unnecessarily long may be closed without review. They may be re-submitted in a concise and actionable form.

AI-generated or AI-assisted drafting does not excuse the submitter from understanding the proposal, checking it for accuracy, and reducing it to the information needed by the working group.

## Licensing of contributions

By contributing to this repository you agree that your contribution is licensed under the terms that apply to the corresponding file category:

- **Prose, source, and meta files**, including the worked-sample READMEs: the Apache License, Version 2.0. See [LICENSE](LICENSE).
- **The design-decision logs** under `dev-docs/decisions/` and **the draft standards-integration mappings** under `dev-docs/assets/`: the W3C Software Notice and Document License ([W3C-20150513](LICENSES/W3C-20150513.txt)), as specification text.
- **Worked sample instances** under `dev-docs/samples/`: the Community Data License Agreement - Permissive 2.0 (CDLA-Permissive-2.0).

## Developer Certificate of Origin (DCO)

All contributions must include a `Signed-off-by` line in every commit. Adding this line certifies that you wrote the contribution, or otherwise have the right to submit it under the applicable license, per the [Developer Certificate of Origin, version 1.1](https://developercertificate.org/).

Append a DCO line by running:

```
git commit --signoff
```

Pull requests missing `Signed-off-by` on every commit will be asked to rebase and re-sign.

## dev-docs/ conventions

This whole repository is `dev-docs/`, so these conventions apply throughout.

### Document kinds

Each kind lives in its own subfolder, created when its first document is added:

- `tasks/` - units of work: open backlog items, in-progress work, and completed work.
- `specs/` - specifications for a proposed or adopted design.
- `reports/` - working reports: analysis, proposals, and walkthroughs prepared for working group review.
- `review/` - review materials, such as review packets and sign-up sheets.
- `roadmaps/` - the standard's development history and forward roadmap.
- `samples/` - worked JSON-LD instances that accompany a specification, so a reviewer can read a proposed design against complete graph data and an implementer has a fixture to validate against. Each set has its own folder and README.
- `decisions/` - the design-decision log: the record of past design decisions and their rationale.
- `assets/` - supporting files that accompany development documents, such as draft mapping files under working group review.

A new subfolder beyond this list follows the New directories rule below.

### What a specification carries

A specification is not complete on its own. When a `specs/` document proposes an ontology or SHACL change, it is delivered together with:

1. **Complete code blocks** - the before and after Turtle for every ontology and SHACL edit, so the change can be applied without re-derivation, noting the commit and candidate version it is written against.
2. **An implementation task** in `tasks/` (marked *Unassigned - open for any working group member to pick up* when it is open work) that applies the edit set and validates it. The edit set itself lands as a pull request against [`urpx-org/urpx`](https://github.com/urpx-org/urpx), since that is where the ontology and SHACL live.
3. **Worked sample instances** in `samples/` that exercise the proposed vocabulary, so the design and its examples can be reviewed and refined together and the delivery can be validated.

### File naming

Files use a dot-separated name:

- Tasks: `task.urpx.<initiative>.<YYYY-MM-DD>.<slug>.md`
- Specs: `spec.urpx.<initiative>.<NNN>.<slug>.md`
- Reports: `report.urpx.<initiative>.<YYYY-MM-DD>.<slug>.md`

`<slug>` is kebab-case. A task that maps to a numbered GitHub issue carries a `gh-<NN>` segment in the slug, for example `task.urpx.ont.2026-07-13.gh-25.conditional-derived-quantity.md`. Use the `gh-<NN>` segment only when a numbered issue exists.

### Frontmatter

Every file opens with YAML frontmatter:

```yaml
---
id: <short stable slug>
title: "<title>"
desc: "<one-line summary>"
updated: <epoch milliseconds>
created: <epoch milliseconds>
---
```

- `id` - a short, stable identifier for the file. It does not change when the file is renamed, for example on a lifecycle transition.
- `title` - the document's title.
- `desc` - a one-line summary of the document's content.
- `created` - when the file was first added, in epoch milliseconds.
- `updated` - when the file was last substantively changed, in epoch milliseconds.

### Lifecycle prefixes (tasks only)

Task files carry a lifecycle prefix in the filename:

- `backlog.task....md` - open, unassigned, and available for a working group member to pick up.
- `task....md` (no prefix) - actively being worked.
- `completed.task....md` - done and accepted.

A task's own `Status` field must agree with its filename prefix. Moving a task from one lifecycle stage to another is a rename, not a content rewrite.

### The public-ready bar

Everything in this repository is held to the same bar:

- Plain, factual voice. Describe the change or the design question, not internal process.
- No references to private repositories, internal project names, or working sessions.
- No personal names in review sign-ups.
- No non-public URLs.
- No emojis.

### Prose formatting

Write for a person reading and reviewing the text, not for a fixed column width.

- Do not hard-wrap prose. A paragraph is a single line in the source; the editor and GitHub wrap it for display. Never break a line in the middle of a sentence to hit a column limit.
- Keep paragraphs short: one idea each, separated by a blank line.
- Keep sentences short; avoid long running sentences.
- Be comprehensive and specific, but not redundant.

### Terminology

- Do not hyphenate "rate plan" or "tariff book" in prose. Slugs and ids are exempt.
- The composite term is "rate plan structure", never "rate structure".
- Avoid the bare word "rate" for the plan itself; say "rate plan". A numeric value is a "price".
- A tariff, or tariff book, is a publication vehicle for parts of a rate plan. It is not the rate plan itself.

### New directories

Creating a new directory beyond the document kinds listed above requires prior working group discussion before a pull request is opened. The first place for this discussion is a working group meeting; a focused GitHub issue is also acceptable.

## How to contribute

### GitHub issues

Use GitHub Issues for a concrete problem, question, or improvement, and propose a concrete change.

### Pull requests

Pull requests must describe precisely what has been changed, added, or removed. Fork the repository, make your changes on a feature branch, include DCO sign-off on every commit, and open a pull request against the default branch.

### Reviews

Contributions are reviewed by the URPX Working Group.

## Code of conduct

See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## Security issues

Do **not** open public issues for security concerns. See [SECURITY.md](SECURITY.md).

## Questions

- Working Group mailing list: `urpx-wg@lists.lfenergy.org`
- Chair: `chair@urpx.org`
