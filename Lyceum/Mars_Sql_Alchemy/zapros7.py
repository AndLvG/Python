from data import db_session
from data import users
from data import jobs
from sqlalchemy import func

db = input()

db_session.global_init(db)
session = db_session.create_session()

users = session.query(users.User).filter(users.User.address == "module_1", users.User.age < 21).update(
    {'address': "module_3"})

session.commit()

# db/mars_explorer.db
