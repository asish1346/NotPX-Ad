import sys
import os
import time

def display_banner():
    banner_lines = [
        "  ('-.      .-')    ('-. .-.",
        "  ( OO ).-. ( OO ). ( OO )  /",
        "  / . --. /(_)---\\_),--. ,--. ,--. ,--.",
        "  | \\-.  \\ /    _ | |  | |  | |  | |  |",
        ".-'-'  |  |\\  :` `. |   .|  | |  | | .-')",
        " \\| |_.'  | '..`''.)|       | |  |_|( OO )",
        "  |  .-.  |.-._)   \\|  .-.  | |  | | `-' /",
        "  |  | |  |\\       /|  | |  |('  '-'(_.-'",
        "  `--' `--' `-----' `--' `--'  `-----'"
    ]
    warning = "⚠️ WARNING: Running unlimited ads is risky. Continue at your own risk. ⚠️"

    # Display each line of the banner with animation
    for line in banner_lines:
        print(f"\033[92m{line}\033[0m")
        time.sleep(0.2)  # Delay between each line

    # Print the warning message after the banner
    print(f"\033[93m{warning}\033[0m")

def check_python_version():
    # Minimum required Python version
    required_version = (3, 7)
    if sys.version_info < required_version:
        print("\033[91m[ERROR]\033[0m Python 3.7 or higher is required.")
        sys.exit(1)

def user_decision():
    while True:
        print("\nPlease choose an option:")
        print("[1] Continue with the process")
        print("[2] Stop the program")
        print("[3] Add a query ID")
        choice = input("\nEnter your choice: ").strip()
        if choice == '1':
            print("\033[92mProceeding...\033[0m")
            return 'continue'
        elif choice == '2':
            print("\033[91mExiting program.\033[0m")
            sys.exit(0)
        elif choice == '3':
            add_query_id()
        else:
            print("\033[93mInvalid choice. Please enter 1, 2, or 3.\033[0m")

def add_query_id():
    while True:
        query_id = input("\nEnter the query ID to add: ").strip()
        if query_id:
            # Save query ID to the file
            with open("query_ids.txt", "a") as file:
                file.write(query_id + "\n")
            print(f"\033[92mQuery ID {query_id} added to query_ids.txt.\033[0m")
        else:
            print("\033[91mQuery ID cannot be empty.\033[0m")
            continue

        # Ask if the user wants to add another query ID
        add_more = input("\nWould you like to add another query ID? (y/n): ").strip().lower()
        if add_more == 'n' or add_more == 'no':
            break

def execute_main_script():
    # Platform-specific adjustments
    python_executable = sys.executable
    main_script = "main.py"

    try:
        os.system(f'"{python_executable}" {main_script}')
    except Exception as e:
        print(f"\033[91m[ERROR]\033[0m Failed to execute {main_script}: {e}")
        sys.exit(1)

if __name__ == "__main__":
    try:
        display_banner()
        check_python_version()

        # Prompt the user for their choice
        choice = user_decision()

        # If the user chose to continue, execute the main script
        if choice == 'continue':
            execute_main_script()  # Execute the main script
    except KeyboardInterrupt:
        print("\n\033[91m[Bot Stopped by User]\033[0m")
        sys.exit(0)
