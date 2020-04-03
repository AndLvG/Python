from data import db_session
from data import users
from data import jobs
from sqlalchemy import func

db = input()

db_session.global_init(db)
session = db_session.create_session()

max_team = session.query(func.max(func.length(jobs.Jobs.collaborators))).scalar()

j = session.query(jobs.Jobs).filter(func.length(jobs.Jobs.collaborators) == max_team)

for jo in j:
    print(jo.user.surname, jo.user.name, jo.collaborators)

# db/mars_explorer.db
