---
id: taskurpxstdsubmissionschemashapes
title: "Publish the submission schema and validation shapes in the URPX standard"
desc: "The sandbox's submission mechanism uses a repo-local, provisional catalogue schema and borrows the ontology's shapes for validation. Promote the submission schema and a submission-validation SHACL into the URPX standard, released through the same semantic flow as the ontology and shapes, so the submission mechanism is normative and reusable. Scope is the schema and the shapes only — never hosting or serving the submitted data."
updated: 1791244800000
created: 1791244800000
---

# Publish the submission schema and validation shapes in the URPX standard

| Field | Value |
|-------|-------|
| **Status** | Backlog — open for any working group member to pick up |
| **Repository** | `urpx-org/urpx` (the standard); consumed by `urpx-org/urpx-data-sandbox` |
| **Surface** | the standard's released artifacts (ontology, shapes, context) and its release workflow |
| **Prototype** | the submissions catalogue in `urpx-org/urpx-data-sandbox` (schema + generated index) |
| **Resolves** | the provisional-namespace question in the sandbox catalogue task |

The sandbox's submission mechanism — the cataloguing system and the checks a submission must pass — currently lives on repo-local, provisional footing: a catalogue schema whose `$id` and vocabulary (`sdx:`) are rooted at the sandbox repository, and validation that borrows the ontology's SHACL shapes. For the submission mechanism to be a normative, reusable part of URPX, its schema and its shapes should be published in the standard, through the same release machinery that publishes the ontology, the SHACL shapes, and the JSON-LD context — the standard's semantic flow.

## What to publish

Two artifacts, and only these two:

- **The submission / catalogue schema.** Promote the sandbox's `submissions-index.schema.json` (and any submission-manifest schema the mechanism needs) to a standard artifact with an official `urpx.org` `$id` and namespace, released with each version. This retires the sandbox's provisional `sdx:` prefix and schema `$id` in favor of the standard's.
- **A submission-validation SHACL.** Shapes that define what makes a valid *submission* for the mechanism — for example that a submission declares `targetURPXVersion`, and carries the metadata the catalogue reads (a `UtilityOperator`, a commodity, a rate plan with an identifier and name). Published alongside the ontology's shapes, so the sandbox's gate 1, and any other implementer of the submission mechanism, validate against the standard rather than against repository-local rules.

Published this way, they ride the standard's semantic flow: released, versioned, linkable artifacts a consumer resolves by version, exactly as the ontology and SHACL are today.

## Explicitly out of scope

- **Hosting or serving the submitted data.** This task does not publish the catalogue's data, or the submitted corpus, as hosted, resolvable, IRI-addressed linked data. The sandbox resolves the submission process and the cataloguing system, and nothing more. Serving the data — a query interface, resolvable data IRIs, joins across submissions — is a data publisher implementation's role, out of scope for both the standard and the sandbox.
- **A data catalog in the standard.** The standard gains the schema and the shapes for the submission mechanism, not an index of hosted datasets.

## Why

- It makes the submission mechanism normative and reusable rather than a convention of one repository.
- It gives the sandbox's provisional namespace and schema `$id` an official home, which is the open namespace decision in the sandbox catalogue task.
- It keeps the sandbox thin: the sandbox implements the mechanism; the standard defines it.

## Constraint

Keep this to the schema and the shapes, published through the standard's existing release flow. Do not add anything that hosts, serves, or resolves the data itself. Mind maintainer and working-group capacity: this is a small, bounded addition to the release artifacts, not a new subsystem.

## Done when

- The submission schema and a submission-validation SHACL are released as part of the URPX standard, through its normal release flow, under an official `urpx.org` namespace.
- The sandbox references the standard's published schema and shapes instead of its repo-local provisional ones.
- Nothing about hosting or serving the submitted data has been added to the standard or the sandbox.
