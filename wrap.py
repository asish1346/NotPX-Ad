import sys
import os

def display_banner():
    banner = """
  ('-.      .-')    ('-. .-.             
  ( OO ).-. ( OO ). ( OO )  /             
  / . --. /(_)---\_),--. ,--. ,--. ,--.   
  | \-.  \ /    _ | |  | |  | |  | |  |   
.-'-'  |  |\  :` `. |   .|  | |  | | .-') 
 \| |_.'  | '..`''.)|       | |  |_|( OO )
  |  .-.  |.-._)   \|  .-.  | |  | | `-' /
  |  | |  |\       /|  | |  |('  '-'(_.-' 
  `--' `--' `-----' `--' `--'  `-----'  
    """
    warning = "WARNING: Running unlimited ads is risky. Continue at your own risk."

    # Print banner in green
    print(f"\033[92m{banner}\033[0m")
    
    # Print warning message in yellow
    print(f"\033[93m{warning}\033[0m")

def check_python_version():
    # Minimum required Python version
    required_version = (3, 7)
    if sys.version_info < required_version:
        print("\033[91m[ERROR]\033[0m Python 3.7 or higher is required.")
        sys.exit(1)

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
    display_banner()
    check_python_version()
    execute_main_script()
