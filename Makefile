run:
	uvicorn main:app --reload

pg-up:
	sudo docker compose -f docker_compose_dev.yaml up -d

pg-down:
	sudo docker-compose -f docker_compose_dev.yaml down && sudo docker network prune --force