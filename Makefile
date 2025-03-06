run:
	uvicorn main:app --reload

pg-up:
	sudo docker-compose -f docker_compose_dev.yaml --env-file .env.dev.pg up -d

pg-down:
	sudo docker-compose -f docker_compose_dev.yaml --env-file .env.dev.pgdown && sudo docker network prune --force && sudo systemctl stop postgresql.service

al-in:
	alembic init migrations

al-mm:
	alembic revision --autogenerate -m $(c)

al-uh:
	alembic upgrades heads
