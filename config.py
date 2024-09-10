import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # SQLALCHEMY_DATABASE_URI = 'postgresql://<user>:<password>@localhost:<port>/<database_name>'
    SQLALCHEMY_DATABASE_URI = 'postgresql://charla:123456@localhost:5432/pythonchallenge'
