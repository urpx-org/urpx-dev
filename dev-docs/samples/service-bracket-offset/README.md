# Service bracket offsets: medical baseline on PG&E E-TOU-C

Models the PG&E Electric Rule 19 Standard Medical Baseline Quantity as a rate plan modifier whose adjusting brackets add 16.438 kWh per day to the bounds of the E-TOU-C baseline-tier ladder, using the bound offsets proposed in [urpx-org/urpx#80](https://github.com/urpx-org/urpx/pull/80) for the question raised in [discussion #32](https://github.com/urpx-org/urpx/discussions/32).

**Synthetic test data, not for production use.** The 16.438 kWh per day offset is a bound, not a price; the modifier carries no prices.

## Files

| File | Type | Purpose |
|---|---|---|
| `pge-e-tou-c-medical-baseline.jsonld` | Rate plan modifier | The modifier and its version, applicable to `pge:e-tou-c`. A host tier `pge:tier-medical-host` holds two adjusting brackets: `upperBoundOffset` 16.438 on `pge:tier-baseline-t1` and `lowerBoundOffset` 16.438 on `pge:tier-baseline-t2`. |
| `pge-e-tou-c-medical-baseline-mixed-container.jsonld` | Rate plan modifier | The same modifier with a numbered tier and an absolute bracket beside the host tier in the same container. |
| `negative/*.jsonld` | Negative cases | The first file with one change each; every one must fail validation on the constraint listed below. |
| `validate.py` | Script | Validates each file merged with `test-cases/pge-e-tou-c` against a urpx checkout. |

## Exercises

[urpx-org/urpx#80](https://github.com/urpx-org/urpx/pull/80): `adjustsServiceTier`, `lowerBoundOffset` and `upperBoundOffset` on `ServiceBracket`; a `ServiceTier` without `serviceTierNumber` that hosts only adjusting brackets; and a `BillingModel` that carries adjusting brackets in place of a price definition.

The adjusting brackets reference tiers by `@id` in the `test-cases/pge-e-tou-c` fixture, so each file validates only merged with that fixture.

## Negative cases

| File | Change | Must fail |
|---|---|---|
| `neg-absolute-and-offset.jsonld` | An adjusting bracket also carries `upperBound`. | `ServiceBracketShape` `sh:or`: absolute bounds and offsets are exclusive. |
| `neg-billingmodel-empty.jsonld` | The billing model has neither `hasPriceDefinition` nor adjusting brackets. | `BillingModelShape` `sh:or`. |
| `neg-chain.jsonld` | A second host tier's bracket targets `pge:tier-medical-host`. | `ServiceBracketShape` `adjustsServiceTier` `sh:node`: the target holds no adjusting brackets. |
| `neg-host-mixed.jsonld` | The host tier also holds an absolute bracket. | `ServiceTierShape` `sh:or`. |
| `neg-host-numbered.jsonld` | The host tier carries `serviceTierNumber` 1. | `ServiceTierShape` `sh:or`. |
| `neg-offset-no-target.jsonld` | A bracket in the host tier carries `upperBoundOffset` without `adjustsServiceTier`. | `ServiceBracketShape` `sh:or`, and `ServiceTierShape` `sh:or` on the host. |
| `neg-offset-string.jsonld` | An offset is the string `"x"`. | `ServiceBracketShape` `upperBoundOffset` `sh:datatype xsd:decimal`. |
| `neg-self-target.jsonld` | An adjusting bracket targets its own host tier. | `ServiceBracketShape` `adjustsServiceTier` `sh:node`. |
| `neg-target-no-offset.jsonld` | An adjusting bracket carries no offset. | `ServiceBracketShape` `sh:or`: an adjusting bracket carries at least one offset. |
| `neg-target-not-tier.jsonld` | An adjusting bracket targets `pge:bracket-t1-p-b-summer`, a `ServiceBracket`. | `ServiceBracketShape` `adjustsServiceTier` `sh:class urpx:ServiceTier`. |
| `neg-two-offsets.jsonld` | An adjusting bracket carries two `upperBoundOffset` values. | `ServiceBracketShape` `upperBoundOffset` `sh:maxCount 1`. |
| `neg-two-targets.jsonld` | An adjusting bracket also targets `pge:tier-baseline-t2c`. | `ServiceBracketShape` `adjustsServiceTier` `sh:maxCount 1`. |

For `neg-chain` and `neg-self-target`, pyshacl also reports the nested `sh:maxCount` result of the `sh:node` constraint, focused on the targeted tier.

## Validation

These files validate only against urpx-org/urpx#80 (branch `dcj/service-bracket-offset`, commit `ae73f6e5`). With that branch checked out and `pyshacl` installed:

```
python3 validate.py <path-to-urpx> *.jsonld negative/*.jsonld
```

Expected: both positive files print `conforms=True`; each negative file prints `conforms=False` with the result listed above.
