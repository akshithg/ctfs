echo:
	@echo "targets: readme, docker"

readme:
	./writeup.py

docker:
	docker-compose run ctf-tools
