@echo off

docker compose build --progress=plain  --no-cache
docker image prune -f
pause
