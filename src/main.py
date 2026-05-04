from decision_logic import DecisionInput, build_truth_table, evaluate_decision, parse_yes_no


QUESTIONS = [
    ("complexity", "A - Is the AI task complex?"),
    ("real_time", "B - Is real-time response required?"),
    ("cost_sensitive", "C - Is low cost important?"),
    ("privacy_sensitive", "D - Is sensitive/private data involved?"),
]


def ask_yes_no(question: str) -> bool:
    while True:
        value = input(f"{question} (yes/no): ")

        try:
            return parse_yes_no(value)
        except ValueError as error:
            print(error)


def run_recommendation() -> None:
    answers = {}

    for key, question in QUESTIONS:
        answers[key] = ask_yes_no(question)

    result = evaluate_decision(DecisionInput(**answers))

    print()
    print("Outputs:")
    print("Y1 - Local:", int(result.local))
    print("Y2 - Cloud:", int(result.cloud))
    print("Y3 - Hybrid:", int(result.hybrid))
    print("Y4 - Lightweight:", int(result.lightweight))


def show_truth_table() -> None:
    print("A B C D | Y1 Y2 Y3 Y4")
    print("---------------------")

    for data, result in build_truth_table():
        print(
            int(data.complexity),
            int(data.real_time),
            int(data.cost_sensitive),
            int(data.privacy_sensitive),
            "|",
            int(result.local),
            int(result.cloud),
            int(result.hybrid),
            int(result.lightweight),
        )


def main() -> None:
    while True:
        print()
        print("ComputeMind AI")
        print("1. Run decision logic")
        print("2. Show truth table")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            run_recommendation()
        elif choice == "2":
            show_truth_table()
        elif choice == "3":
            print("Goodbye.")
            break
        else:
            print("Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
