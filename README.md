<!-- SPDX-FileCopyrightText: The URPX Authors -->
<!-- SPDX-License-Identifier: Apache-2.0 -->

# urpx-dev

This repository is the design and process record for URPX, the Utility Rate Plan Exchange ontology: the tasks, specifications, working reports, roadmaps, and development samples that record how the working group develops the standard.

## What this repository is not

This is not the standard. The ontology, the SHACL shapes, the published JSON-LD context, the documentation the website renders, and the curated test cases live in [`urpx-org/urpx`](https://github.com/urpx-org/urpx). A change to the standard itself is a pull request against that repository, not this one.

This repository also does not hold community-contributed rate plan datasets. Those live in [`urpx-org/urpx-data-sandbox`](https://github.com/urpx-org/urpx-data-sandbox).

## What belongs here

- Backlog tasks, in progress and completed
- Specifications for proposed or adopted ontology and SHACL changes
- Working reports prepared for working group review
- Roadmaps: the standard's development history and forward plan
- Review materials
- The design-decision log
- Worked sample instances that accompany a specification

The worked sample instances under `dev-docs/samples/` are experimental files used for development. They name real utilities and rate plans but are review fixtures for proposed vocabulary, not published rate plan data.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the file-kind conventions, naming, and lifecycle prefixes.

## How this relates to the other URPX repositories

| Repository | What it holds |
|---|---|
| [`urpx-org/urpx`](https://github.com/urpx-org/urpx) | The standard: ontology, shapes, context, documentation, curated test cases |
| `urpx-org/urpx-dev` (this repository) | The design and process record |
| [`urpx-org/urpx-data-sandbox`](https://github.com/urpx-org/urpx-data-sandbox) | Community-contributed rate plan datasets |
| [`urpx-org/urpx-wg`](https://github.com/urpx-org/urpx-wg) | Working group meeting agendas and minutes |

A rule of thumb: if it is the standard itself, it belongs in `urpx-org/urpx`. If it is how the working group works on the standard, it belongs here. If it is a contributed dataset, it belongs in the sandbox.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) and [AGENTS.md](AGENTS.md).

## License

Prose, source, and meta files are licensed under the Apache License, Version 2.0. Worked sample instances under `dev-docs/samples/` are data, licensed under the Community Data License Agreement - Permissive 2.0 (CDLA-Permissive-2.0). See [NOTICE](NOTICE), [LICENSE](LICENSE), and `LICENSES/` for the CDLA-Permissive-2.0 text.

Contributions are governed by the Developer Certificate of Origin v1.1. See [CONTRIBUTING.md](CONTRIBUTING.md).

Security issues: see [SECURITY.md](SECURITY.md).
