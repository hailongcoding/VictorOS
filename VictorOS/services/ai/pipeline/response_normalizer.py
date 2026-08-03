import re


class ResponseNormalizer:
    """
    Cleans raw LLM output before parsing.

    Responsibilities
    ----------------
    - Remove markdown code fences
    - Extract the first JSON object
    - Trim whitespace
    """

    def normalize(self, text: str) -> str:

        if not text:
            return ""

        # Remove ```json
        text = re.sub(
            r"^```(?:json)?\s*",
            "",
            text,
            flags=re.IGNORECASE,
        )

        # Remove ending ```
        text = re.sub(
            r"\s*```$",
            "",
            text,
        )

        text = text.strip()

        # Find first JSON object
        start = text.find("{")
        end = text.rfind("}")

        if start != -1 and end != -1 and end > start:
            text = text[start:end + 1]

        return text.strip()