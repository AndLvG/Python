from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, IntegerField, DateField, BooleanField, SelectField
from wtforms.validators import DataRequired, Optional
import datetime
from data import db_session
from data.users import User

DB = "db/mars_explorer.db"

class AddJobForm(FlaskForm):
    db_session.global_init(DB)
    session = db_session.create_session()
    users = session.query(User.id, User.name).all()

    team_leader = SelectField('Team Leader', coerce=int, choices=users, validators=[DataRequired()])
    job = StringField('Job Title', validators=[DataRequired()])
    work_size = IntegerField('Work size', validators=[DataRequired()])
    collaborators = StringField('Collaborators', validators=[DataRequired()])
    start_date = DateField('Start date', default=datetime.date.today(),
                           validators=[DataRequired('Please select start date')])
    end_date = DateField('End date', validators=[Optional()])
    is_finished = BooleanField("Is job finished", validators=[Optional()])
    submit = SubmitField('Submit')
