# flask-test-task 10/22

  Initial task:

  1. Parse (pre-download) two .csv files into Postgres db
  2. Create an API endpoints (GET) that will return data in json format with the following content:
     * By product id, give information on this product (ASIN, Title) and Reviews of this product with pagination.
  3. Create a second API endpoint (PUT), which will write a new review to the database Review for the product (by id).

  Project structure:

  ```
  docker/                         # docker-compose.yml for postgres
  flask_app/                      # app main folder
    admin/                        # admin interface for models
    api/                          # api reg, endpoints and methods
    app_utils/                    # commands, db, config call and cashing
    - commands/                   # load csv command
    core/                         # models & base routes (index page)
    migrations/                   # alembic db control migrations
  ```

  Clone:
  `git clone git@github.com:venmerk/flask-test-task.git`

  Local db up:
  `docker-compose up -d postgres`    # from cd docker/local                                
  `docker-compose -f docker/local/docker-compose.yml up -d postgres` # from base dir

  Local db down:
  `docker-compose down`

  Postgres tips:
  `psql -U postgres -h localhost`
  `postgres`            # password

  `\l`                  # list db's
  `\c flask_app_db`     # connect to db
  `\dt`                 # list tables

  `select * from products_table limit 5;` # base query

  Migrations:
  > Migrations are providing us easy way to control db flow & changes.

  `flask db --help`                  # all commands
  `flask db init`                    # init migrations

  `flask db migrate -m "Message text"` # generate
  `flask db upgrade`                   # apply

  More about migrations:
  [Official docs](https://flask-migrate.readthedocs.io/en/latest/)
  [Nice article](https://blog.miguelgrinberg.com/post/how-to-add-flask-migrate-to-an-existing-project)

  Import data:
  `readlink -f file.csv` # Get linux file path
  `flask import csv /fullpath/products.csv products_table`

  GET - Request product
  `http://localhost:5000/api/v1/products/2` # base
  `http://localhost:5000/api/v1/products/2?per-page=1&page=3` # with optional parameters

  PUT - Update existing(5) review
  ```
  curl -X PUT http://127.0.0.1:5000/api/v1.0/reviews/5 \
   -H "Content-Type: application/json" \
   -d '{"text": "new super text"}'
  ```

  PUT - Insert new(55) review
  ```
  curl -X PUT http://127.0.0.1:5000/api/v1.0/reviews/55 \
   -H "Content-Type: application/json" \
   -d '{"text": "new super text", "title": "title", "asin": "B06XYPJN4G"}'
  ```
  > Note that 'asin' MUST exist in the products_table, and MUST be provided for new review (due to null constraint)