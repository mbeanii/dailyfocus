import sys
import os

filename = "dailyfocus.txt"


def print_usage():
    print("Usage:")
    print("  dailyfocus show")
    print("  dailyfocus set <priority1> <priority2> <priority3>")
    print("  dailyfocus clear")


def show_priorities():
    if os.path.exists(filename):
        with open(filename, "r") as f:
            priorities = f.read().splitlines()
            print("Your top 3 priorities for today are:")
            for i, priority in enumerate(priorities, start=1):
                print(f"{i}. {priority}")
    else:
        print(
            "No priorities set for today. Use 'dailyfocus set' to add your top 3 priorities."
        )


def set_priorities(priorities):
    with open(filename, "w") as f:
        for priority in priorities:
            f.write(f"{priority}\n")
    print("Priorities updated successfully.")


def clear_priorities():
    if os.path.exists(filename):
        os.remove(filename)
        print("Priorities cleared successfully.")
    else:
        print("No priorities to clear.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_usage()
    else:
        action = sys.argv[1].lower()
        if action == "show":
            show_priorities()
        elif action == "set":
            if len(sys.argv) == 5:
                set_priorities(sys.argv[2:])
            else:
                print("Please provide exactly 3 priorities.")
                print_usage()
        elif action == "clear":
            clear_priorities()
        else:
            print("Invalid command.")
            print_usage()
