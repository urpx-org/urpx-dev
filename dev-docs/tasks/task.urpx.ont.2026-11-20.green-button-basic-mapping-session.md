---
id: taskurpxontgreenbuttonbasicmappingsession
title: "Green Button to URPX basic mapping: working session 1"
desc: "Agenda and working table for the 2026-11-20 Green Button to URPX mapping session. Aims for a basic mapping that lets one customer's Green Button usage data be priced against one URPX rate plan: reading types, the usage point, the billing cycle, and the agreement-to-rate-plan link. Lists what the mapping file already carries, what stays out of scope, and what to have ready."
updated: 1795046400000
created: 1795046400000
---

# Green Button to URPX basic mapping: working session 1

| Field | Value |
|-------|-------|
| **Status** | Open; working session 2026-11-20, 11:00 to 12:00 US ET |
| **Participants** | Klaartje De Schepper (chair), Don Coffin (Green Button Alliance) |
| **Surface** | [`dev-docs/assets/urpx-green-button-mappings.ttl`](../assets/urpx-green-button-mappings.ttl); the Green Button section of `documentation/pages/urpx-interoperability.md` in `urpx-org/urpx` |
| **Source** | NAESB ESPI V4 (`espi_v4.xsd`, `customer_v4.xsd`); URPX v0.5.1 |
| **Follows from** | Working-group meeting #020 (2026-11-10), item 4 |

## Goal

A basic mapping that lets an implementer take one customer's Green Button data and one URPX rate plan and compute a bill. This is the "bill calculation" pattern on the interoperability page: Green Button supplies the usage and the customer's agreement, URPX supplies the rate plan, and a `urpx:ScenarioCostModel` prices one against the other.

The session is done when every row in the working table below has a disposition: mapped (with the match type), mapped with a note, needs a vocabulary change (with an issue to open), or deferred.

## What the mapping file already carries

The v0.3.0 mapping file holds 20 alignments. None of them needs revisiting tomorrow.

- `ServiceCategory` to `urpx:CommodityValue`: electricity, gas, water and heat (`exactMatch`).
- `ItemKind` to the URPX charge categories: the eight fee, credit and tax kinds (`closeMatch`).
- `PricingStructure` to `urpx:RatePlan` (`relatedMatch`), `tariffProfile` to `urpx:name` (`closeMatch`), and `LineItem` to `urpx:PriceSummary` and `urpx:Price`.
- `TariffRiderRefs` enrollment status: enrolled, unenrolled and enrolled-pending to the URPX active, inactive and pending statuses (`closeMatch`).

## Out of scope on 2026-11-20

These are framed in their own draft specs and tasks and stay there:

- `ProgramIdMappings` as a reading-code codebook: [spec 048](../specs/spec.urpx.ont.048.green-button-programid-codebook.md).
- How a rider enrollment joins to a stable rate plan modifier identity: [spec 049](../specs/spec.urpx.ont.049.modifier-enrollment-identity-boundary.md).
- A service point's reference to a pricing node, and `PnodeRef`: [spec 050](../specs/spec.urpx.ont.050.service-point-pnode-reference.md) and its [task](backlog.task.urpx.ont.2026-08-31.green-button-pnoderef-mapping-question.md).
- Province-wide systems such as Ontario, and the Canadian rate code copyright question raised at meeting #020.

## Agenda

| # | Minutes | Topic |
|---|---|---|
| 1 | 5 | Agree the goal and the scope above. |
| 2 | 20 | Priority 1: `ReadingType` to the URPX metric description. |
| 3 | 10 | Priority 2: the usage point and its interval data. |
| 4 | 10 | Priority 3: the billing cycle. |
| 5 | 10 | Priority 4: from the customer agreement to the rate plan. |
| 6 | 5 | Who drafts what, and the next session. |

## Working table

The URPX candidates are starting points to test in the session, not decisions.

### Priority 1: `ReadingType` to the URPX metric description

A `ReadingType` says what an interval reading measures. In URPX, a rate plan's `urpx:MetricSpecification` says what a price is charged on. Aligning the two is what lets an implementer match a reading to a price.

| ESPI element | URPX candidate | Disposition |
|---|---|---|
| `commodity` | `urpx:CommodityValue` (already aligned through `ServiceCategory`) | |
| `uom`, `powerOfTenMultiplier` | `urpx:unitOfMeasure` / `urpx:UnitOfMeasureValue` | |
| `kind` | `urpx:measurementKind` / `urpx:MeasurementTypeValue` | |
| `flowDirection` | `urpx:flowDirection` / `urpx:FlowDirectionValue` | |
| `accumulationBehaviour` | `urpx:accumulationMethod` / `urpx:AccumulationValue` | |
| `intervalLength` | `urpx:intervalDuration`, `urpx:IntervalTypeValue` | |
| `tou`, `cpp`, `consumptionTier` | `urpx:touTierNumber`, `urpx:touTierStandardName` (incl. `urpx:criticalPeakTier`), `urpx:serviceTierNumber` | |
| `currency` | `urpx:priceCurrency` (ISO 4217) | |

### Priority 2: the usage point and its interval data

| ESPI element | URPX candidate | Disposition |
|---|---|---|
| `UsagePoint` | `urpx:ServicePointProfile` | |
| `UsagePoint.phaseCode`, `nominalServiceVoltage`, `ratedPower` | `urpx:PhaseCodeKindValue`, `urpx:nominalVoltage`, `urpx:ratedPowerCapacity` | |
| `IntervalBlock`, `IntervalReading` | referenced by URI from the scenario, not restated in URPX | |
| `UsageSummary.peakDemand`, `ratchetDemand` | `urpx:billedDemand` and the demand metric inputs | |

### Priority 3: the billing cycle

Meeting #020 found that "takes effect on the next billing" depends on the customer's own billing cycle, which in the Georgia cases fell on the 16th.

| ESPI element | URPX candidate | Disposition |
|---|---|---|
| `CustomerAccount.billingCycle` | `urpx:BillingCycle`, `urpx:billingCycleCode` | |
| `UsageSummary.billingPeriod` | `urpx:cycleStartDay`; `urpx:billingPeriodAligned` intervals | |
| `UsagePoint.readCycle`, `UsageSummary.readCycle` | to discuss | |

### Priority 4: from the customer agreement to the rate plan

| ESPI element | URPX candidate | Disposition |
|---|---|---|
| `CustomerAgreement` | `urpx:AccountServiceAgreement` | |
| `CustomerAgreement.PricingStructures`, `UsageSummary.tariffProfile` | `urpx:RatePlan` (already `relatedMatch`); which version applies on a date | |
| `UsageSummary.tariffRiderRefs` | the modifier versions a scenario prices under ([pull request #72](https://github.com/urpx-org/urpx/pull/72)) | |
| `UsageSummary.costAdditionalLastPeriod`, `billLastPeriod` | `urpx:ScenarioCostResult`, as a check of a computed bill against the utility's own | |

## To have ready

- The current [mapping file](../assets/urpx-green-button-mappings.ttl).
- One Green Button data file for a time-of-use or tiered customer, with personal details removed, ideally from a Georgia utility already in the rate plan corpus.
- The Georgia billing-cycle case from meeting #020.

## After the session

1. Record each disposition in the working table above.
2. Turn the settled rows into an edit set for the mapping file, reviewed in a pull request.
3. Open an issue in `urpx-org/urpx` for each row that needs a vocabulary change.
4. Update the Green Button section of the interoperability page to match the mapping file.
