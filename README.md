# Minerva :trident:

Hey! It is a general-purpose template for your Data Science project. Just a few steps to start. Let's go!

## How to use

Install Cookiecutter

    $ pip install cookiecutter

you can also use a virtual environment.

    $ python3 -m venv .venv

    $ source .venv/bin/activate

    $ (.venv) $ pip install cookiecutter

Generate a codebase for your project. Follow the steps.

    $ cookiecutter https://github.com/gjcasanova/minerva.git

The virtual environment will be created automatically, and the required dependencies will be installed. Simply navigate to your project folder and activate the virtual environment to get started.

    $ cd my_project_directory

    $ source .venv/bin/activate

You can check the dependencies installed.

    (.venv) $ pip list

The pre-commit module will be set up, and the initial commit will be saved automatically. If needed, you can set a remote origin by following the steps below

    (.venv) $ git remote add origin https://github.com/my_username/my_repository.git

    (.venv) $ git push origin main

You are all set! :rocket:
