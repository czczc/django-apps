# Django APPS

## Installation Guide

### install python
Django 3.1 needs python 3.6 or above. If the system default python version is low, one needs to install manually:
```
sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
wget https://www.python.org/ftp/python/3.6.2/Python-3.6.2.tar.xz
tar xf Python-3.6.2.tar.xz
cd Python-3.6.2/
./configure
make
sudo make altinstall
```

### useful django commands
```
python3.6 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install django
django-admin startproject core
python manage.py startapp publications
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0:8000


pip install djangorestframework
pip install markdown
pip install django-filter
pip freeze > requirements.txt

```