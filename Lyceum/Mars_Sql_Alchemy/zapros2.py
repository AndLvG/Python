from data import db_session
from data import users

db = input()

db_session.global_init(db)
session = db_session.create_session()
users = session.query(users.User).filter(users.User.address == "module_1",
                                         users.User.speciality.notlike("%ingeneer%"),
                                         users.User.position.notlike("%ingeneer%"))

for user in users:
    print(user.id)

# db/mars_explorer.db