from dataclasses import dataclass


@dataclass(frozen=True)
class DecisionInput:
    complexity: bool
    real_time: bool
    cost_sensitive: bool
    privacy_sensitive: bool


@dataclass(frozen=True)
class DecisionResult:
    local: bool
    cloud: bool
    hybrid: bool
    lightweight: bool


def parse_yes_no(value: str) -> bool:
    normalized = value.strip().lower()
    yes_values = {"yes", "y", "1", "true", "t"}
    no_values = {"no", "n", "0", "false", "f"}

    if normalized in yes_values:
        return True

    if normalized in no_values:
        return False

    raise ValueError("Please enter yes/no or 1/0.")


def evaluate_decision(data: DecisionInput) -> DecisionResult:
    local = data.complexity and data.privacy_sensitive
    cloud = data.complexity and not data.privacy_sensitive
    hybrid = data.complexity and data.real_time
    lightweight = (not data.complexity) and data.cost_sensitive

    return DecisionResult(
        local=local,
        cloud=cloud,
        hybrid=hybrid,
        lightweight=lightweight,
    )


def build_truth_table() -> list[tuple[DecisionInput, DecisionResult]]:
    rows = []

    for complexity in (False, True):
        for real_time in (False, True):
            for cost_sensitive in (False, True):
                for privacy_sensitive in (False, True):
                    data = DecisionInput(
                        complexity=complexity,
                        real_time=real_time,
                        cost_sensitive=cost_sensitive,
                        privacy_sensitive=privacy_sensitive,
                    )
                    rows.append((data, evaluate_decision(data)))

    return rows
