run:
	python manage.py runserver

shell:
	python manage.py shell

restore_db:
	heroku pg:backups capture -a fixmydjango
	curl -o latest.dump `heroku pg:backups public-url -a fixmydjango`
	pg_restore --verbose --clean --no-acl --no-owner -h localhost -d fixmydjango latest.dump
