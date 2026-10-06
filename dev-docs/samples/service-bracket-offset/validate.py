# SPDX-FileCopyrightText: The URPX Authors
# SPDX-License-Identifier: Apache-2.0
"""Validate each sample, merged with test-cases/pge-e-tou-c, against a urpx checkout.

Usage: python3 validate.py <path-to-urpx-checkout> <file.jsonld>...

The pge-e-tou-c test case names the released context by URL; this script substitutes
the checkout's context/urpx-context.jsonld so the proposed terms resolve.
"""
import json
import sys
from pathlib import Path

from pyshacl import validate
from rdflib import RDF, BNode, Graph, Namespace

SH = Namespace("http://www.w3.org/ns/shacl#")


def local(term):
    return str(term).rsplit("/", 1)[-1].rsplit("#", 1)[-1]


def main(urpx, files):
    urpx = Path(urpx)
    ctx = json.loads((urpx / "context/urpx-context.jsonld").read_text())["@context"]
    tc = json.loads((urpx / "test-cases/pge-e-tou-c/data/urpx-rate-plan_pge_e-tou-c.jsonld").read_text())
    tc["@context"] = [ctx if isinstance(c, str) else c for c in tc["@context"]]
    base = Graph()
    base.parse(urpx / "ontology/urpx-ontology.ttl")
    base.parse(data=json.dumps(tc), format="json-ld")
    shapes = Graph().parse(urpx / "shacl/urpx-shacl.ttl")
    for f in files:
        data = Graph()
        data += base
        data.parse(f, format="json-ld")
        conforms, report, _ = validate(data, shacl_graph=shapes, inference="none", allow_warnings=True)
        print(f"{f}: conforms={conforms}")
        for r in report.subjects(RDF.type, SH.ValidationResult):
            if report.value(r, SH.resultSeverity) != SH.Violation:
                continue
            path = report.value(r, SH.resultPath)
            print(f"    {local(report.value(r, SH.focusNode))} {local(report.value(r, SH.sourceConstraintComponent))}"
                  + (f" {local(path)}" if path is not None and not isinstance(path, BNode) else ""))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
