# fast-api-postgres-crud-api

This is a CRUD api of fast api, using postgres db

It's based on: <br>
https://www.youtube.com/watch?v=d_ugoWsvGLI <br>
https://github.com/lemoncode21/fastapi-postgresql-crud

Above tutorial is not a fully complete CRUD repo, so i create this repo by my own, 
and make some change to it.
<br>

To install, use: <br>
`sudo pip3 install virtualenv` <br>
`python3 -m venv venv` <br>
`source venv/bin/activate` <br>
`pip install "fastapi[all]"`

To migrate db, use: <br>
`pip install alembic` <br>
`pip install python-dotenv`

Then, change the db connection config inside `.env` file.<br>

After that, run: <br>
`alembic revision --autogenerate -m "First migration"` <br>
`alembic upgrade head`

To run the app: <br>
`uvicorn app.main:app --reload`

After you run this command, go to http://127.0.0.1:8000/docs to see the result <br>
In this command `uvicorn app.main:app --reload`, it go to folder app, and run the `main.py`