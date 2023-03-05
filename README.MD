# Links cutter

This is a small sample project demonstrating how to build an API with [PostgreSQL](https://www.postgresql.org) and [FastAPI](https://fastapi.tiangolo.com/).
It is cutting your full URL to short link and after that you won't worry about long links

## Deploy
You will need Docker on the machine where you will deploy. Download it from the [official site](https://www.docker.com/) and install.
It is highly recommended to use the latest version.

1. create the `.env` from `.env_example`
2. deploy docker container

```bash
# Build your container:
docker-compose build

# Start project:
docker-compose up
```

Now you can load http://localhost:8000 in your browser ... but there won't be much to see until you've inserted some data.
But you can check http://localhost:8000/docs and create your first short link.

Good luck!

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Alembic](https://img.shields.io/badge/%20-Alembic-orange?style=for-the-badge&logo=appveyor)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
