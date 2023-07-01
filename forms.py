from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired, Email

class StakeholderForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    raci = SelectField('RACI', choices=[('Responsible', 'Responsible'), ('Accountable', 'Accountable'), ('Consulted', 'Consulted'), ('Informed', 'Informed')], validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
