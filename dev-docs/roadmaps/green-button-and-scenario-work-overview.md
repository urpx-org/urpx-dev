---
id: roadmapurpxgreenbuttonscenarioworkoverview
title: "Green Button, scenario and modeling-gap work: overview for planning"
desc: "The open work connecting URPX to Green Button data and to the scenario cost model, together with the modeling gaps found in the Georgia rate plans and the process proposals due at meeting #021. Grouped into five workstreams with their current state, dependencies and a suggested order. A planning aid for the chair and Don Coffin; owners other than those recorded in the minutes are left to agree."
updated: 1795046400000
created: 1795046400000
---

# Green Button, scenario and modeling-gap work: overview for planning

This overview gathers the open work that sits between URPX, Green Button data and the scenario cost model. It is a planning aid. Owners are listed only where meeting #020's minutes record them; the rest are left to agree.

## A. Green Button mapping

| # | Item | State | Depends on |
|---|---|---|---|
| A1 | Basic mapping, session 1: reading types, usage point, billing cycle, agreement to rate plan ([task](../tasks/task.urpx.ont.2026-11-20.green-button-basic-mapping-session.md)) | Scheduled 2026-11-20 | none |
| A2 | Edit set for the mapping file from A1's settled rows, reviewed in a pull request | Not started | A1 |
| A3 | Issues in `urpx-org/urpx` for each A1 row that needs a vocabulary change | Not started | A1 |
| A4 | Green Button section of the interoperability page brought in line with the mapping file | Not started | A2 |
| A5 | A second working session if A1 does not finish: `UsageSummary` cost fields, `ServiceLocation`, `ServiceSupplier` | Not scheduled | A1 |
| A6 | `ProgramIdMappings` as a reading-code codebook ([spec 048](../specs/spec.urpx.ont.048.green-button-programid-codebook.md)) | Draft spec, unassigned | A1 (reading-code rows) |
| A7 | Rider enrollment joined to a modifier identity ([spec 049](../specs/spec.urpx.ont.049.modifier-enrollment-identity-boundary.md)) | Draft spec, unassigned | B1 |
| A8 | Service point to pricing node, and `PnodeRef` ([spec 050](../specs/spec.urpx.ont.050.service-point-pnode-reference.md), [task](../tasks/backlog.task.urpx.ont.2026-08-31.green-button-pnoderef-mapping-question.md)) | Draft spec, unassigned | none |

## B. Scenario cost model

| # | Item | State | Depends on |
|---|---|---|---|
| B1 | Dedicated working session on [pull request #72](https://github.com/urpx-org/urpx/pull/72): where the modifier reference lives, how far a rate plan and its modifiers nest under a scenario, and how a scenario refers to real customer data | To schedule | A1 (the customer-data side) |
| B2 | Customer enrollment links and the metering-data bridge ([task](../tasks/backlog.task.urpx.ont.2026-07-13.customer-pricing-structure-enrollment.md)) | Backlog | B1, A7 |
| B3 | Worked examples: one Green Button file priced against one rate plan, end to end | Not started | A2, B1 |
| B4 | The consuming API shape ([spec 047](../specs/spec.urpx.api.047.consuming-api.md)) | Draft spec | B1 |

## C. Modeling gaps from the Georgia rate plans

| # | Item | State | Related |
|---|---|---|---|
| C1 | Whether a recurring season's end date is inclusive, and how a season wraps the year end ([issue #85](https://github.com/urpx-org/urpx/issues/85)) | Open issue | none |
| C2 | A profile property for the kW of equipment under load control ([issue #86](https://github.com/urpx-org/urpx/issues/86)) | Open issue | none |
| C3 | Block bounds proportional to billing demand ([issue #87](https://github.com/urpx-org/urpx/issues/87)) | Open issue | Pull requests [#80](https://github.com/urpx-org/urpx/pull/80) and [#76](https://github.com/urpx-org/urpx/pull/76) |
| C4 | A change that takes effect on the customer's next billing, tied to their own cycle | To file (Don Coffin, per meeting #020) | A1 priority 3 |
| C5 | Gate 1 rejects a modifier whose base plans are in other submissions ([sandbox issue #10](https://github.com/urpx-org/urpx-data-sandbox/issues/10)) | Open issue; the chair to relax the gate | none |
| C6 | Province-wide systems such as Ontario, and the Canadian rate code copyright question | Open; no Canadian rate plans until the copyright question is settled | none |

## D. Process proposals for meeting #021 (2026-11-24)

| # | Item | Owner (per meeting #020) |
|---|---|---|
| D1 | Pull-request and branching practice for the development and main repositories | Blade Chapman, Don Coffin |
| D2 | Continuous-integration gates: validation, sandbox runs, formatting | Blade Chapman, Don Coffin |
| D3 | Issue tracking per repository or in one place | Klaartje, with Don Coffin's advice |

## Suggested order

1. **This week:** A1. File C4 so it can be worked alongside A1's billing-cycle rows.
2. **Before 2026-11-24:** D1 to D3 ready for the meeting. A2 drafted from A1.
3. **Next fortnight:** B1 as its own working session, then A3 and A4. C1 and C3 grouped with the open pull requests they touch.
4. **After B1:** A7 and B2 together, since both concern how a customer's enrollment refers to a modifier. Then B3 as the end-to-end check.
5. **When a contributor picks them up:** A6, A8 and C2.
