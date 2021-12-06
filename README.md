# Dj Boilerplate
A [Django](https://www.djangoproject.com/) boilerplate/template for building production level projects

## Features
> #### Frontend

- [Libsass](https://pypi.org/project/Pillow/) and [Watchdog](https://pypi.org/project/libsass/), for out of the box sass support

> #### Backend

- [Decouple](https://pypi.org/project/python-decouple/), for securely storing secret variables in **.env** file
- [Pillow](https://pypi.org/project/Pillow/), for uploading images

## Getting Started

Follow the steps to get your app running

- `git clone https://github.com/devmahdi404/djboilerplate` 
- Rename the `djboilerplate` folder name with your new project name
- `cd` into the project folder
- Make sure you have **Python 3.9** installed
- Install the backend **requirements** with **virtual environment**:

  - Install the `virtualenv` package if don't have :  `pip install virtualenv`

  - Create a virtual environment named **env**: `virtualenv env`

  - Activate the virtual environment: `env/Scripts/activate`

  - Install the requirements: `pip install -r requirements.txt`
- Now change the project name: `python mangae.py rename djboilerplate projectname`
- Duplicate the `.env.example` file and rename the new file to `.env`
- Generate a random **secretkey**: `python mangae.py genskey`, copy it
- Inside the `.env` file, set it as the `SECRET_KEY` value
- Start the server: `python manage.py runserver`
- Open a browser and go to `http://localhost:8000` to see the project running

## How it works

- Settings
  - the settings module is divided into `base.py` , `dev.py` , `pro.py`
  - both `dev.py`, `pro.py` extends the `base.py`
  - `dev.py` is used on runserver and `pro.py` on wsgi and asgi production
  - secret variables are imported from `.env` file using the `config` function
- Apps
  - All apps are stored in **apps** folder for structural convenient
  - Use `python manage.py newapp appname` to create new apps inside `apps` folder
- Sass
  - A compile function in `apps/core/sass.py` is called when the server is started or reloaded
  - If `DEBUG=True`, it will watch for **.scss** file changes in **static** folders and compile it, `threading` is used to accomplish this task
  - If `DEBUG=False`, then it will compile all **.scss** files in `STATIC_ROOT`  once

## Contribute
If you wish to contribute to this project, please first discuss the change you wish to make via an [issue](https://github.com/devmahdi404/djboilerplate/issues).

## Donate
[Bkash][https://www.bkash.com/]: `01712143778`

## License
[MIT License](LICENSE)

