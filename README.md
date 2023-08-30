# YTB-channels-data

## Getting started

Run a postgres instance using Docker:

```bash
docker-compose up --build
```

Connect to the database using the credentials from `docker-compose.yml` file.

Run the `01-create-database.sql` script to create the database.

Run the seed script to populate your database:

```bash
python seed.py
```
