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
        print("\nWould you like to proceed?")
        print("[1] Continue")
        print("[2] Stop")
        choice = input("\nEnter your choice: ").strip()
        if choice == '1':
            print("\033[92mProceeding...\033[0m")
            return True
        elif choice == '2':
            print("\033[91mExiting program.\033[0m")
            sys.exit(0)
        else:
            print("\033[93mInvalid choice. Please enter 1 or 2.\033[0m")

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
        if user_decision():
            execute_main_script()
    except KeyboardInterrupt:
        print("\n\033[91m[Bot Stopped by User]\033[0m")
        sys.exit(0)
