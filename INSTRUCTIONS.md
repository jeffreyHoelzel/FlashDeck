# Docker Instructions

1. Run `docker network create flash_deck_shared_network` (do this only once).

2. Run `docker-compose -f proxy/docker-compose.local.yml up`.

3. In separate terminal, run `docker-compose up --build` to start development environments. Frontend will be on localhost:3000 and backend on localhost:5000 (you should be able to just type 'localhost' into browser to see website).

If you are having any trouble, try running `docker-compose down` after pressing `CTRL+C`in terminal.