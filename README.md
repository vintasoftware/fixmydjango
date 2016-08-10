# fixmydjango ![Travis CI](https://travis-ci.org/vintasoftware/fixmydjango.svg?branch=master)
Code of [http://www.fixmydjango.com](http://www.fixmydjango.com)

This is the website and backend behind [fixmydjango-lib](https://github.com/vintasoftware/fixmydjango-lib). While developing a Django project, if you get any exception in development server and [fixmydjango.com](http://www.fixmydjango.com) has a solution for it, [fixmydjango-lib](https://github.com/vintasoftware/fixmydjango-lib) will display a link to the solution in the error 500 debug template.

This is the code of the backend which stores Django exceptions data and the webapp which displays them at [fixmydjango.com](http://www.fixmydjango.com). For the library to install in your Django projects, see [fixmydjango-lib](https://github.com/vintasoftware/fixmydjango-lib).

## Contribute
Feel free to fork this project and contribute with it! Take a look at the [issues](https://github.com/vintasoftware/fixmydjango/issues) for known problems.

## Authors
Made by pythonistas at [Vinta Software Studio: vinta.com.br](http://www.vinta.com.br/?fixmydjango).

## Development notes

2 dependencies of this project are not yet compatible with Django 1.10. There are PRs that fix this but project maintainers didn't merge them yet.
We temporarily deployed compatible versions as `-vinta`, we should come back to the main projects as soon as they get back on track.

### django-bootstrap-pagination

Thread: https://github.com/jmcclell/django-bootstrap-pagination/pull/53   
Vinta's fork: https://github.com/vintasoftware/django-bootstrap-pagination   
PyPI name: django-bootstrap-pagination-vinta   

### django-markdown

Thread: https://github.com/klen/django_markdown/pull/70   
Vinta's fork: https://github.com/vintasoftware/django_markdown   
PyPI name: django-markdown-vinta   
