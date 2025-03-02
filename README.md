# whoami-python
Simple webapp that shows your IP address and stores it with database along with a timestamp. It can also show the visitors on a map.

## Usage
### Development

Run the application in development mode:

```
export FLASK_APP=run.py
export FLASK_ENV=development
flask run
```


This will start the development server with debug mode enabled and auto-reload on code changes.

### Production use
The recommended way is running with gunicorn

```
gunicorn run:app
```


### Environment Variables

| Name | Description | Default | Documentation |
|------|-------------|---------|----------------|
| `DATABASE_URL` | PostgreSQL connection string in the format `postgresql://user:password@host:port/dbname` | `sqlite:///:memory:` | [SQLAlchemy Database URLs](https://docs.sqlalchemy.org/en/14/core/engines.html#database-urls) |
| `WEB_CONCURRENCY` | Number of worker processes for handling requests (production use) | `1` (can be set by PaaS like Heroku) | [Gunicorn Worker Configuration](https://docs.gunicorn.org/en/stable/settings.html#worker-processes) |
