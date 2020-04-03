from data import db_session
from data import users
from data import jobs

db = input()

db_session.global_init(db)
session = db_session.create_session()
j = session.query(jobs.Jobs).filter(jobs.Jobs.work_size < 20, jobs.Jobs.is_finished == 0)

for jo in j:
    print(jo)

# db/mars_explorer.db
