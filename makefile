.PHONY: logs

NAME := chatgpt-line-bot
SERVICES_PORT := 8889

up:
	docker compose up -d
down:
	docker compose down

# Image
build:
	docker compose build --no-cache
rm:
	docker images | grep $(NAME) | awk '{print $$3}' | xargs docker rmi
rebuild: rm build

# Container
run:
	docker run -d --rm -p $(SERVICES_PORT):8000 $(NAME)
stop:
	docker stop $$(docker ps | grep $(NAME) | awk '{print $$1}')
logs:
	docker logs -f $$(docker ps | grep $(NAME) | awk '{print $$1}')
exec:
	docker exec -it $$(docker ps | grep $(NAME) | awk '{print $$1}') sh
restart: stop run