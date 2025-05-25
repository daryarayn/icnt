from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask


class DatabaseConnectionPool:
	_db: SQLAlchemy = None
	_migrate: Migrate = None
	_app: Flask = None

	@classmethod
	def _init_connection(cls, app):
		print('Init connection')
		cls._app = app
		cls._db = SQLAlchemy(cls._app)
		cls._migrate = Migrate(cls._app, cls._db)

	@classmethod
	def get_connection(cls, app=None):
		if not cls._db or not cls._migrate:
			cls._init_connection(app)
		return cls._db, cls._migrate
