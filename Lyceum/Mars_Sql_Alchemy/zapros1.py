from data.db_session import global_init, create_session
from data.users import User


db = input()

global_init(db)
session = create_session()
users = session.query(User).filter(User.address == "module_1").all()
for user in users:
    print(user)

# db/mars_explorer.db