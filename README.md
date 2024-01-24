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

Now jump into your project folder and create a new virtual environment. If you are already using one you must deactivate.

    (.venv) $ deactivate

    $ cd my_project_directory

    $ python3 -m venv .venv

    $ source .venv/bin/activate

Then install the requirements.

    (.venv) $ pip install --use-pep517 -r requirements.txt

Finally set your repository up.

    (.venv) $ git init

    (.venv) $ git add -A

    (.venv) $ pre-commit

    (.venv) $ git commit -m "my_commit_message"

    (.venv) $ git remote add origin https://github.com/my_username/my_repository.git

    (.venv) $ git push origin main

You are all set! :rocket:
