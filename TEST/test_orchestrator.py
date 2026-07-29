from AI.orchestration.orchestrator import Orchestrator


def main():

    orchestrator = Orchestrator()

    while True:

        prompt = input("\nYou: ")

        if prompt.lower() in ("exit", "quit"):
            break

        response = orchestrator.process(prompt)

        print("\nJARVIS:")
        print(response)


if __name__ == "__main__":
    main()