
migrations:
	@docker exec -it -w /dealer dealer_api python scr/manage.py makemigrations

migrate:
	@docker exec -it -w /dealer dealer_api python scr/manage.py migrate

app:
	@mkdir -p src/apps/$(name)
	@docker exec -it -w /dealer dealer_api python scr/manage.py startapp $(name) src/apps/$(name)

start_compose:
	@docker-compose -f docker-compose-dev.yml up

test_env:
	@type docker\envs\env_example > docker\envs\.env-local

test_user:
	@docker exec -it -w /dealer dealer_api python scr/manage.py createsuperuser

shell:
	@docker exec -it -w /dealer dealer_api python scr/manage.py shell

collectstatic:
	@docker exec -it -w /dealer dealer_api python scr/manage.py collectstatic

test_server:
	@docker exec -it -w /dealer dealer_api python scr/manage.py test