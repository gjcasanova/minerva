"""Post generation script."""

import subprocess

ERROR_COLOR = '\x1b[31m'
MESSAGE_COLOR = '\x1b[33m'
SUCCESS_COLOR = '\x1b[32m'
RESET_COLOR = '\x1b[0m'


def install_requirements():
    """Install the project requirements."""
    print(f'{MESSAGE_COLOR}Installing project requirements...{RESET_COLOR}')

    try:
        subprocess.run(['pip', 'install', '-r', 'requirements.txt'], check=True)
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
        subprocess.run(['pre-commit', 'run', '--all-files'], check=True)
        subprocess.run(['git', 'commit', '-m', 'Initial commit'], check=True)
    except subprocess.CalledProcessError as e:
        print(f'{ERROR_COLOR}Git repository initialization failed: {e}{RESET_COLOR}')
    else:
        print(f'{SUCCESS_COLOR}Git repository initialized{RESET_COLOR}')


def main():
    """Execute the post generation script."""
    install_requirements()
    init_git()

    print(f'{SUCCESS_COLOR}Project generated successfully{RESET_COLOR}')


if __name__ == '__main__':
    main()
