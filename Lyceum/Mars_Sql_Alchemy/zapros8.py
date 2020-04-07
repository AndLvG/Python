from data.db_session import global_init, create_session
from data.users import User
from data.jobs import Jobs
from data.departments import Department
from sqlalchemy import func

db = input()

global_init(db)
session = create_session()

d = session.query(Department).filter(Department.id == 1).first()
members = list(map(int, d.members.split(",")))

workers = []

for m in members:
    j = session.query(func.sum(Jobs.work_size)).filter(Jobs.collaborators.like(f'%{str(m)}%')).scalar()
    # print(j)
    if j > 25:
        workers.append(m)

# print(workers)
users = session.query(User).filter(User.id.in_(workers))
for user in users:
    print(user.surname, user.name)

# db/mars_explorer.db
