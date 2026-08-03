from VictorOS.services.intent.adapter import IntentAdapter
from VictorOS.services.intent.service import IntentService


def main():

    service = IntentService()
    
    print("=" * 60)
    print("VictorOS Understanding Test")
    print("Type 'exit' to quit.")
    print("=" * 60)

    while True:

        prompt = input("\nYou > ").strip()

        if prompt.lower() in {"exit", "quit"}:
            break

        if not prompt:
            continue

        try:

            understanding = service.understand(prompt)

            print("\n" + "=" * 60)
            print("UNDERSTANDING")
            print("=" * 60)

            print(f"Goal       : {understanding.goal}")
            print(f"Confidence : {understanding.confidence:.2f}")

            print("\nEntities:")
            if understanding.entities:
                for entity in understanding.entities:
                    print(f"  • {entity}")
            else:
                print("  (none)")

            print("\nIntents:")

            for i, intent in enumerate(understanding.intents, start=1):

                print(f"\n[{i}]")
                print(f"Goal        : {intent.goal}")
                print(f"Description : {intent.description}")

                if intent.entities:
                    print(f"Entities    : {', '.join(intent.entities)}")
                else:
                    print("Entities    : (none)")
            print("=" * 60)

        except Exception as e:

            print("\nERROR")
            print(e)


if __name__ == "__main__":
    main()