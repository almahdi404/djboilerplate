#!/bin/bash

read -p "Enter python binary name : " pyname
echo "Creating venv"
$pyname -m venv env
echo "Done creating venv"
source env/bin/activate
echo "Upgrading pip"
pip install --upgrade pip
echo "Done upgrading pip"
echo "Installing requirements"
pip install -r requirements/dev.txt
echo "Done installing requirements"
echo "Setting up env vars"
cp .env.example .env
sed -i "s/ENV=/ENV=dev/" .env
skey=$(python manage.py genskey)
sed -i "s/SECRET_KEY=/SECRET_KEY=$skey/" .env
echo "Done setting up env vars"
