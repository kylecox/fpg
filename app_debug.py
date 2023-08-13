import os
from datetime import datetime

from flask import Flask, redirect, render_template, request, send_from_directory, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__, static_folder='static')
csrf = CSRFProtect(app)

app.config.update(
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://app_user:app_password@localhost:5432/app',
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)

tester = app.config
print(tester)
