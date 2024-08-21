
# Investsphere API

[![Python](https://img.shields.io/badge/python-3.12.2-3776AB.svg)](https://www.python.org/downloads/release/python-3122/)
[![FastAPI](https://img.shields.io/badge/FastApi-0.111.0-009485.svg)](https://reflex.dev/)

## FastAPI System for Managing Personal Investments

### Description
Backend system developed with FastAPI for managing personal investments. The system includes the following features:

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

# install fastapi
pip install -r requirements.txt

# start development server
uvicorn main:app --reload
```