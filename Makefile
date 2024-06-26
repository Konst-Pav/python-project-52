run_local_server:
	poetry run python manage.py runserver

test:
	poetry run python manage.py test

test_coverage:
	poetry run coverage run manage.py test
	poetry run coverage report -m --include=task_manager/* --omit=task_manager/settings.py
	poetry run coverage xml --include=task_manager/* --omit=task_manager/settings.py

install:
	poetry install

test_status:
	poetry run python manage.py test task_manager.status

test_user:
	poetry run python manage.py test task_manager.user

test_task:
	poetry run python manage.py test task_manager.task

test_label:
	poetry run python manage.py test task_manager.label

migrations:
	poetry run python manage.py makemigrations

migrate:
	poetry run python manage.py migrate

shell:
	poetry run python manage.py shell

make_messages_ru:
	poetry run python manage.py makemessages -l ru

compilemessages:
	poetry run python manage.py compilemessages

lint:
	poetry run flake8 task_manager
