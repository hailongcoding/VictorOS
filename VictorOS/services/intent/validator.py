from __future__ import annotations

import json
from typing import Any

from VictorOS.core.contracts.understanding import (
    Understanding,
    Intent,
)

import json


def parse(text: str) -> Understanding:

    data = json.loads(text)

    intents = []

    for node in data.get("intents", []):

        intents.append(
            Intent(
                goal=str(node.get("goal", "")).strip(),
                description=str(node.get("description", "")).strip(),
                entities=[
                    str(x)
                    for x in node.get("entities", [])
                ],
            )
        )

    return Understanding(
        original=str(data.get("original", "")).strip(),
        goal=str(data.get("goal", "")).strip(),
        confidence=float(data.get("confidence", 0.0)),
        intents=intents,
        entities=[
            str(x)
            for x in data.get("entities", [])
        ],
        metadata=data.get("metadata", {}),
    )

def validate(
    understanding: Understanding,
) -> list[str]:

    issues = []

    if not understanding.original:
        issues.append("Missing original.")

    if not understanding.goal:
        issues.append("Missing goal.")

    if not (
        0 <= understanding.confidence <= 1
    ):
        issues.append(
            "Confidence must be between 0 and 1."
        )

    if not isinstance(
        understanding.entities,
        list,
    ):
        issues.append(
            "Entities must be a list."
        )

    if not isinstance(
        understanding.metadata,
        dict,
    ):
        issues.append(
            "Metadata must be a dictionary."
        )

    if not understanding.intents:
        issues.append(
            "No intents returned."
        )

    for i, intent in enumerate(
        understanding.intents,
        start=1,
    ):

        if not intent.goal:
            issues.append(
                f"Intent {i} has no goal."
            )

        if not intent.description:
            issues.append(
                f"Intent {i} has no description."
            )

        if not isinstance(
            intent.entities,
            list,
        ):
            issues.append(
                f"Intent {i} entities must be a list."
            )

    return issues