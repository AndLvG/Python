from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Optional, NumberRange, Regexp
import datetime


class ZaprosForm(FlaskForm):
    fam = StringField('Фамилия', validators=[Optional(), Regexp(regex='^[А-Яа-яЁё]',
                                                                message="Только русские буквы")])
    im = StringField('Имя', validators=[Optional(), Regexp(regex='^[А-Яа-яЁё]',
                                                           message="Только русские буквы")])
    ot = StringField('Отчество', validators=[Optional(), Regexp(regex='^[А-Яа-яЁё]',
                                                                message="Только русские буквы")])
    dr = DateField('Дата рождения', validators=[Optional()])
    today = datetime.datetime.now()
    god_dr = IntegerField('Год рождения', validators=[Optional(), NumberRange(min=1900, max=today.year,
                                                                              message="Проверьте год рождения")])
    date_begin = DateField('Дата начала', validators=[Optional()])
    date_end = DateField('Дата окончания', validators=[Optional()])

    submit = SubmitField('Поиск')
