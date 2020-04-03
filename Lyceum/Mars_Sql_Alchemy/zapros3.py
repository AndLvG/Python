from data import db_session
from data import users

db = input()

db_session.global_init(db)
session = db_session.create_session()
users = session.query(users.User).filter(users.User.age < 18)

for user in users:
    print(f'{user} {user.age} years')

# db/mars_explorer.db