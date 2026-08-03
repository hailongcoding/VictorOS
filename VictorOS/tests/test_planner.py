from VictorOS.services.intent.adapter import IntentAdapter
from VictorOS.services.intent.service import IntentService
from VictorOS.services.intent.validator import validate

adapter = IntentAdapter()
planner = IntentService(adapter)

print("\nInteractive Mode (type 'exit' to quit)\n")

while True:

    text = input("> ").strip()

    if text.lower() == "exit":
        break

    plan = planner.classify(text)

    print("=" * 40)
    print("GOAL")
    print("=" * 40)
    print(plan.goal)

    print()

    print("=" * 40)
    print("WORKERS")
    print("=" * 40)
    print(plan.workers)

    print()

    missing = validate(plan, text)

    if missing:

        print("=" * 40)
        print("VALIDATION FAILED")
        print("=" * 40)
        print("Missing Workers:", missing)

    else:

        print("=" * 40)
        print("VALID")
        print("=" * 40)