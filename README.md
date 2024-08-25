# Investsphere API

[![Python](https://img.shields.io/badge/python-3.12.2-3776AB.svg)](https://www.python.org/downloads/release/python-3122/)
[![Django](https://img.shields.io/badge/Django-4.2.3-092E20.svg)](https://www.djangoproject.com/)

## Django System for Managing Personal Investments

### Description
Backend system developed with Django for managing personal investments. The system includes the following features:

### Roadmap
[ ] User registration and authentication  
[ ] Creation of investment portfolios  
[ ] Add and remove assets from a portfolio  
[ ] Calculation of overall balance and balance by asset  
[ ] Transaction logging (purchases and sales)

### Requirements
A Python version of 3.8+ is required.  
This repository uses the version:
```
python 3.12.2
```

## Installation
To start using it, you can clone this repository to your local machine:

```bash
# clone the project
git clone https://github.com/Guillermo090/investsphere_api.git
cd investsphere_api

# create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`

# install Django
pip install -r requirements.txt

# apply migrations
python manage.py migrate

# start development server
python manage.py runserver
```

## Get certbot certificates
```bash
# run the certbot container with your domain name as an argument
docker-compose run --rm certbot certonly --webroot --webroot-path=/var/www/certbot -d api.investsphere.cl
```
