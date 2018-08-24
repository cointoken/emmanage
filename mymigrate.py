from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app # we import the app object from the app module
from app import db
from app.models import Members
from datetime import datetime

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    # m = Members('test123@163.com','test123','python18')
    # db.session.add(m)
    # db.session.commit()
    manager.run()
