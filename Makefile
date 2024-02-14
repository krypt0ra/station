mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
mkfile_dir := $(dir $(mkfile_path))

NAME = ''

rebuild:
	@docker-compose up -d --build && docker-compose start

start:
	@docker-compose up -d --remove-orphans && docker-compose start

stop:
	@docker-compose stop

restart: stop start

connect_app:
	@docker exec -it kriptora_station_app bash

run:
	@docker exec -it kriptora_station_app sh -c "cd app && python app.py"