---
id: taskurpxontinternationalizationspecandguide
title: "Finalize and implement the internationalization spec and its guide"
desc: "Backlog: the internationalization guide was moved out of the published URPX documentation on 2026-10-05 into spec.urpx.ont.051, because its examples use hypothetical urpx: properties, headers and database schemas the ontology and shapes do not implement. This task finalizes the spec, builds the vocabulary and shape support that multilingual and localization use actually needs, and returns the guide to the published documentation once it describes shipped behavior. Depends on the support verification. Not launch-gating."
updated: 1791244800000
created: 1791244800000
---

# Finalize and implement the internationalization spec and its guide

| Field | Value |
|-------|-------|
| **Status** | Backlog, post-v0.5.1. Not launch-gating. |
| **Assignment** | Unassigned, open for any working-group member to pick up. |
| **Surface** | `ontology/urpx-ontology.ttl`, `shacl/urpx-shacl.ttl`, `dev-docs/specs/spec.urpx.ont.051.internationalization.md`, and the guide once it returns to the published documentation. |
| **Spec** | [spec.urpx.ont.051.internationalization.md](../specs/spec.urpx.ont.051.internationalization.md) |
| **Depends on** | The support-verification finding tracked in the chair's planning repository as `task.urpx.wg.2026-10-05.i18n-support-verification`. |

## Problem

The internationalization guide described multilingual and localization patterns URPX does not implement: multilingual `name` values against `xsd:string` ranges, calendar dates on `effectiveDate`, hypothetical `urpx:` terms, and headers and database schemas nothing in the tree carries. It was parked as this draft spec rather than published, so the documentation does not promise behavior the model cannot back.

## What this task does

1. Settle the i18n scope from the verification finding: which multilingual and localization needs URPX should meet, and which stay out of scope.
2. Finalize `spec.urpx.ont.051`: the properties, language-tag rules and shape changes the scope requires, walking the reuse ladder before minting new terms.
3. Implement the agreed support in the ontology and shapes, with a changelog line and worked examples that validate.
4. Rewrite the guide to describe shipped behavior, and return it to the published documentation when it does.

## Acceptance

`spec.urpx.ont.051` is ratified, the supporting vocabulary and shapes validate with worked examples, and the guide describes only implemented behavior.
