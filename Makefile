run:
	python manage.py runserver

shell:
	python manage.py shell

test:
	python manage.py test --keepdb

restore_db:
	heroku pg:backups capture -a fixmydjango
	curl -o latest.dump `heroku pg:backups public-url -a fixmydjango`
	pg_restore --verbose --clean --no-acl --no-owner -h localhost -d fixmydjango latest.dump

sass:
	sass --watch core/static/sass/app.scss:core/static/css/custom-style.css
