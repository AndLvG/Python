from data import db_session
from data import users

db = input()

db_session.global_init(db)
session = db_session.create_session()
users = session.query(users.User).filter((users.User.position.like("%chief%") | users.User.position.like("%middle%")))

for user in users:
    print(f'{user} {user.position}')

# db/mars_explorer.db