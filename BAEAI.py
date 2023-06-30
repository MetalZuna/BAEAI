from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from langchain import OpenAI, ConversationChain, LLMChain, PromptTemplate
from langchain.memory import ConversationBufferWindowMemory


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SECRET_KEY'] = 'dev'  # replace with a secure random string in production
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.String(80), nullable=False, default='standard user')

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date)
    status = db.Column(db.String(80), nullable=False, default='in progress')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Conversation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    user_input = db.Column(db.Text, nullable=False)
    B2_response = db.Column(db.Text, nullable=False)

class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    doc_type = db.Column(db.String(80), nullable=False)
    content = db.Column(db.Text, nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False)
    last_modified_date = db.Column(db.DateTime, nullable=False)

class Stakeholder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    title = db.Column(db.String(80), nullable=False)
    RACI = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)

class Requirement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stakeholder_id = db.Column(db.Integer, db.ForeignKey('stakeholder.id'), nullable=False)
    # user_story_id = db.Column(db.Integer, db.ForeignKey('user_story.id'), nullable=False)
    requirement_description = db.Column(db.String(200), nullable=False)
    stakeholder = db.relationship('Stakeholder', backref='requirements')
    # user_story = db.relationship('UserStory', backref='requirements')

class StakeholderForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    raci = StringField('RACI', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Add Stakeholder')



#Language model

template = """Assistant is a large language model trained by OpenAI.

Assistant is designed to be able to assist with a wide range of tasks, from answering simple questions to providing in-depth explanations and discussions on a wide range of topics. As a language model, Assistant is able to generate human-like text based on the input it receives, allowing it to engage in natural-sounding conversations and provide responses that are coherent and relevant to the topic at hand.

Assistant is constantly learning and improving, and its capabilities are constantly evolving. It is able to process and understand large amounts of text, and can use this knowledge to provide accurate and informative responses to a wide range of questions. Additionally, Assistant is able to generate its own text based on the input it receives, allowing it to engage in discussions and provide explanations and descriptions on a wide range of topics.

Overall, Assistant is a powerful tool that can help with a wide range of tasks and provide valuable insights and information on a wide range of topics. Whether you need help with a specific question or just want to have a conversation about a particular topic, Assistant is here to assist.

{history}
Human: {human_input}
Assistant:"""

prompt = PromptTemplate(input_variables=["history", "human_input"], template=template)


chatgpt_chain = LLMChain(
    llm=OpenAI(temperature=0),
    prompt=prompt,
    verbose=True,
    memory=ConversationBufferWindowMemory(k=2),
)

output = chatgpt_chain.predict(
    human_input="name the top three combustion and top three diesel engines ever created, provide year of the engine, provide description of what makes them great engines"
)
print(output)




@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/soagile_workflow')
def soagile_workflow():
    return render_template('soagile_workflow.html')

@app.route('/kpis')
def kpis():
    return render_template('kpis.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/add_stakeholder', methods=['GET', 'POST'])
def add_stakeholder():
    form = StakeholderForm()
    if form.validate_on_submit():
        new_stakeholder = Stakeholder(first_name=form.first_name.data, last_name=form.last_name.data, title=form.title.data, raci=form.raci.data, email=form.email.data)
        db.session.add(new_stakeholder)
        db.session.commit()
        flash('Stakeholder added successfully')
        return redirect(url_for('dashboard'))
    return render_template('add_stakeholder.html', form=form)

@app.route('/llm_text_output')
def llm_text_output():
    output = chatgpt_chain.predict(
        human_input="I want you to provide me names of fastest women in history. provide top ten names"
    )
    return render_template('dashboard.html', output=output.content)



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

