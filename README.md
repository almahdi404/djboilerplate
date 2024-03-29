# Dj Boilerplate

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
![VSCode](https://img.shields.io/static/v1?logo=visual-studio-code&label=&message=vscode&color=0066b8)
![GitHub](https://img.shields.io/github/license/almahdi404/code-django)

A [Django](https://www.djangoproject.com/) boilerplate/template for building production level projects

## Features

> Frontend

-   [Libsass](https://pypi.org/project/libsass/) and [Watchdog](https://pypi.org/project/watchdog/), for out of the box sass support

> Backend

-   [Decouple](https://pypi.org/project/python-decouple/), for securely storing secret variables in **.env** file
-   [Pillow](https://pypi.org/project/Pillow/), for uploading images

## Getting Started

Follow the steps to get your app running

-   `git clone https://github.com/almahdi404/djboilerplate`

-   Rename the `djboilerplate` folder name with your new **project name**

-   `cd` into the project folder

-   On **Linux/Mac** :

    -   Run : `bash setup.sh`

    -   Activate the virtual environment : `source env/bin/activate`

-   On **Windows** :

    -   Create a virtual environment named **env** : `python -m venv env`

    -   Activate the virtual environment : `env/Scripts/activate`

    -   Install the dev requirements : `pip install -r requirements/dev.txt`

    -   Duplicate the `.env.example` file and rename the new file to `.env`

    -   Inside the `.env` file, set `ENV=dev`

    -   Generate a random **SECRET_KEY** : `python manage.py genskey`, copy it

    -   Inside the `.env` file, set it as the `SECRET_KEY` value

-   Start the server : `python manage.py runserver`

-   Go to [localhost:8000](http://localhost:8000) to see your project running

## How it works

-   Settings
    -   the settings module is divided into `base.py` , `dev.py` , `pro.py` files. both `dev.py` and `pro.py` extends the `base.py` file
    -   when using `python manage.py runserver`, `dev.py` is used if `ENV=dev` and `pro.py` is used if `ENV=pro`
    -   `pro.py` is always used in `wsgi` and `asgi` application
    -   secret variables are imported from `.env` file using the `decouple.config` function
-   Apps
    -   all apps are stored in the [apps](apps) folder for structural convenient
    -   use `python manage.py newapp appname` to create new apps inside the [apps](apps) folder
-   Sass
    -   a compiler function in `apps/core/sass.py` is called when the server is started or reloaded
    -   when `DEBUG=True`, it will watch for **.scss** file changes in **static** folders and compile it, `threading` is used to accomplish this task
    -   when `DEBUG=False`, then it will compile all **.scss** files in `STATIC_ROOT` once

## Contribute

If you wish to contribute to this project, please first discuss the change you wish to make via an [issue](https://github.com/almahdi404/djboilerplate/issues).

## License

[MIT License](LICENSE)
