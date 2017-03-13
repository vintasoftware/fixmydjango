# fixmydjango [![Travis CI](https://travis-ci.org/vintasoftware/fixmydjango.svg?branch=master)](https://travis-ci.org/vintasoftware/fixmydjango)
Code of [http://www.fixmydjango.com](http://www.fixmydjango.com)

This is the website and backend behind [fixmydjango-lib](https://github.com/fixmydjango/fixmydjango-lib). While developing a Django project, if you get any exception in development server and [fixmydjango.com](http://www.fixmydjango.com) has a solution for it, [fixmydjango-lib](https://github.com/fixmydjango/fixmydjango-lib) will display a link to the solution in the error 500 debug template.

This is the code of the backend which stores Django exceptions data and the webapp which displays them at [fixmydjango.com](http://www.fixmydjango.com). For the library to install in your Django projects, see [fixmydjango-lib](https://github.com/fixmydjango/fixmydjango-lib).

## Contribute
Feel free to fork this project and contribute with it! Take a look at the [issues](https://github.com/fixmydjango/fixmydjango/issues) for known problems.

## Authors
Made by pythonistas at [Vinta Software Studio: vinta.com.br](http://www.vinta.com.br/?fixmydjango).

## Development notes

2 dependencies of this project are not yet compatible with Django 1.10. There are PRs that fix this but project maintainers didn't merge them yet.
We temporarily deployed compatible versions as `-vinta`, we should come back to the main projects as soon as they get back on track. 

**update: django-bootstrap-pagination was updated**

### django-markdown

Thread: https://github.com/klen/django_markdown/pull/70   
Vinta's fork: https://github.com/vintasoftware/django_markdown   
PyPI name: django-markdown-vinta   

## Developing

### Quickstart
- Create a copy of ``fix_my_django/settings/local.py.example`` in ``fix_my_django/settings/local.py``
- Create a ``.env`` file in the root of the project and add ``DJANGO_SETTINGS_MODULE="fix_my_django.settings.local"`` to it
- Create a PostgreSQL named `fixmydjango`

### Running the project

- `pip install -r requirements.txt`
- `npm install`
- `python manage.py migrate`
- `python manage.py bower_install`
- `python manage.py runserver`

### Running simple

- `make run`
- `make shell`
- `make test`
- `make restore_db` (Get production database)


