# tompany

The future is now!

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT

## How to run the project?
`docker-compose -f local.yml up`

## How to run the unit tests?
`docker-compose -f local.yml run django pytest`

## How to test endpoints in Postman?
Import the swagger.json file to the Postman application
![Peek 2022-04-09 17-48](https://user-images.githubusercontent.com/1877511/162594066-ede013d8-31d7-440a-aa26-42c6051e1428.gif)

## Custom commands
- `docker-compose -f local.yml run --rm django python manage.py load_companies` [--csv_file_path, --debug_mode]
- `docker-compose -f local.yml run --rm django python manage.py load_transactions` [--csv_file_path, --debug_mode]


## Important endpoints
- GET ​/api​/companies​/{id}​/transactions_resume​/
- PATCH /api/companies/{id}/transfer_transactions/{target_company_id}/
- GET /api/transactions/resume/

## Django admin
Create a super user (docker-compose -f local.yml run --rm django python manage.py createsuperuser) and login in http://localhost:8000/admin/

## Explore the endpoints using the swagger ui
http://localhost:8000/swagger/

![Peek 2022-04-09 18-10](https://user-images.githubusercontent.com/1877511/162594539-6cf85d3d-2596-47d9-a879-381bc9ff21b6.gif)


## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Sentry

Sentry is an error logging aggregator service. You can sign up for a free account at <https://sentry.io/signup/?code=cookiecutter> or download and host it yourself.
The system is set up with reasonable defaults, including 404 logging and integration with the WSGI application.

You must set the DSN url in production.

## Deployment

The following details how to deploy this application.

### Heroku

See detailed [cookiecutter-django Heroku documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-on-heroku.html).

### Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).
