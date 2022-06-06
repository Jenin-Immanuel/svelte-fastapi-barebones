"""
Connect your database in this file

For SQL Databases (PostgreSQL, MySQL): Use SQLAlchemy as ORM

Install the necessary packages

pip install sqlalchemy

Drivers
For postgres: pip install pyscopg2
For MySQL: pip install pymysql

from sqlalchemy import create_engine, MetaData
engine = create_engine('url_of_the_database') # Generally "database_name+python_driver://<user_name>:<password>@<IP_Addr>:<PORT>/<DB_Name>"
meta =  MetaData()
conn = engine.connect()


For MongoDB: Use pymongo  and pydantic

pip install pymongo
pip install pydantic

from pymongo import MongoClient
conn = MongoClient()

"""