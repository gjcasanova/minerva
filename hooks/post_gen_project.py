"""Post generation script."""

import subprocess
import sys

ERROR_COLOR = '\x1b[31m'
MESSAGE_COLOR = '\x1b[33m'
SUCCESS_COLOR = '\x1b[32m'
RESET_COLOR = '\x1b[0m'

PYTHON_BASE_PATH = f'{sys.base_prefix}/bin/python3'
PYTHON_ENV_PATH = '.venv/bin/python3'


def create_vitual_environment():
    """Create the virtual environment."""
    print(f'{MESSAGE_COLOR}Activating virtual environment...{RESET_COLOR}')

    try:
        subprocess.run([f'{PYTHON_BASE_PATH}', '-m', 'venv', '.venv'], check=True)
    except subprocess.CalledProcessError as e:
        print(f'{ERROR_COLOR}Virtual environment creation failed: {e}{RESET_COLOR}')
        raise e
    else:
        print(f'{SUCCESS_COLOR}Virtual environment created{RESET_COLOR}')


def install_requirements():
    """Install the project requirements."""
    print(f'{MESSAGE_COLOR}Installing project requirements...{RESET_COLOR}')

    try:
        subprocess.run([f'{PYTHON_ENV_PATH}', '-m', 'pip', 'install', '--upgrade', 'pip'], check=True)
        subprocess.run([f'{PYTHON_ENV_PATH}', '-m', 'pip', 'install', '-r', 'requirements.txt'], check=True)
    except subprocess.CalledProcessError as e:
        print(f'{ERROR_COLOR}Instalation of project requirements failed: {e}{RESET_COLOR}')
    else:
        print(f'{SUCCESS_COLOR}Project requirements installed{RESET_COLOR}')


def init_git():
    """Initialize a git repository and perform the first commit."""
    print(f'{MESSAGE_COLOR}Initializing git repository...{RESET_COLOR}')

    try:
        subprocess.run(['git', 'init'], check=True)
        subprocess.run(['git', 'add', '-A'], check=True)
        subprocess.run(['pre-commit', 'install'], check=True)
        subprocess.run(['git', 'commit', '-m', 'chore(core): init project'], check=True)
    except subprocess.CalledProcessError as e:
        print(f'{ERROR_COLOR}Git repository initialization failed: {e}{RESET_COLOR}')
    else:
        print(f'{SUCCESS_COLOR}Git repository initialized{RESET_COLOR}')


def main():
    """Execute the post generation script."""
    create_vitual_environment()
    install_requirements()
    init_git()

    print(f'{SUCCESS_COLOR}Project generated successfully{RESET_COLOR}')


if __name__ == '__main__':
    main()
