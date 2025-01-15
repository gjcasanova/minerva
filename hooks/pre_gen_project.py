"""Pre generation script."""

import sys

ERROR_COLOR = '\x1b[31m'
MESSAGE_COLOR = '\x1b[33m'
SUCCESS_COLOR = '\x1b[32m'
RESET_COLOR = '\x1b[0m'


def check_virtual_environment():
    """Install the project requirements."""
    print(f'{MESSAGE_COLOR}Validating virtual environment...{RESET_COLOR}')

    if sys.base_prefix == sys.prefix:
        print(f'{ERROR_COLOR}Error: Virtual environment is not activated{RESET_COLOR}')
        raise EnvironmentError('Virtual environment is not activated')

    print(f'{SUCCESS_COLOR}Virtual environment is activated{RESET_COLOR}')


def main():
    """Execute the pre generation script."""
    check_virtual_environment()


if __name__ == '__main__':
    main()
