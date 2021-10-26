.PHONY: logs
logs:
	sudo docker-compose logs -f backend

.PHONY: restart-backend
restart-backend:
	sudo docker-compose restart backend

.PHONY: restart
restart:
	sudo docker-compose restart

.PHONY: enter
enter:
	sudo docker-compose run --rm backend bash

.PHONY: up
up:
	docker-compose up --build -d
.PHONY: run
run: up	

.DEFAULT_GOAL := up
