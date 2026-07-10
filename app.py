import sys

from agents.coordinator import coordinator


def main():
    print("====================================")
    print(" 🤖 Multi-Agent SOC Assistant ")
    print("====================================")

    if not sys.stdin.isatty():
        for raw_line in sys.stdin:
            user_input = raw_line.strip()
            if not user_input:
                continue
            if user_input.lower() in {"exit", "quit"}:
                break

            response = coordinator(user_input)
            print("\nAssistant Response:")
            print(response)
            print()
        return

    print("\nType 'exit' to quit.\n")

    while True:
        try:
            user_input = input("Enter a security event or log: ").strip()
        except EOFError:
            print("\nNo further input received. Goodbye.")
            break

        if not user_input:
            continue
        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye.")
            break

        response = coordinator(user_input)
        print("\nAssistant Response:")
        print(response)
        print()


if __name__ == "__main__":
    main()