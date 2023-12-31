import logging
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db_username = "postgres"
db_password = "53kUHnyQvS"
db_host = "postgres-db-postgresql.default.svc.cluster.local"
db_port = os.environ.get("DB_PORT", "5432")
db_name = os.environ.get("DB_NAME", "postgres")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"

db = SQLAlchemy(app)

app.logger.setLevel(logging.DEBUG)