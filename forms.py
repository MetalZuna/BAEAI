from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired, Email

class StakeholderForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    raci = SelectField('RACI', choices=[('Responsible', 'Responsible'), ('Accountable', 'Accountable'), ('Consulted', 'Consulted'), ('Informed', 'Informed')], validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])


'''
class ProjectForm(FlaskForm):
    project_name = StringField('Project Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    start_date = DateField('Start Date', format='%Y-%m-%d', validators=[DataRequired()])
    end_date = DateField('End Date', format='%Y-%m-%d')
    status = SelectField('Status', choices=[('in progress', 'In Progress'), ('completed', 'Completed'), ('on hold', 'On Hold')], validators=[DataRequired()])
    user_id = IntegerField('User ID', validators=[DataRequired()])
'''