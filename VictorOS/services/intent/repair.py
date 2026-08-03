from dataclasses import dataclass


@dataclass(slots=True)
class RepairPackage:
    system: str
    user: str


class UnderstandingRepairBuilder:

    def build(
        self,
        previous_output: str,
        validation_errors: list[str],
    ) -> RepairPackage:

        system = (
            "You previously returned invalid JSON for VictorOS.\n"
            "Return corrected JSON only.\n"
            "Do not explain.\n"
            "Do not add markdown.\n"
        )

        user = (
            "Previous Output:\n\n"
            f"{previous_output}\n\n"
            "Validation Errors:\n"
            + "\n".join(f"- {e}" for e in validation_errors)
        )

        return RepairPackage(
            system=system,
            user=user,
        )