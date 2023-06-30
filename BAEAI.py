from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from langchain import OpenAI, ConversationChain, LLMChain, PromptTemplate
from langchain.memory import ConversationBufferWindowMemory
from flask import Flask, render_template, redirect, url_for, flash, request
from models import init_db, db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SECRET_KEY'] = 'dev'  # replace with a secure random string in production
db.init_app(app)

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

@app.route('/process_input', methods=['POST'])
def process_input():
    user_input = request.form.get('user-input')  # get the user input from the form
    output = chatgpt_chain.predict(human_input=user_input)  # process the user input
    return render_template('dashboard.html', output=output)  # return the output to the dashboard


@app.route('/get_output', methods=['GET'])
def get_output():
    output = chatgpt_chain.predict(
        human_input="I want you to provide me names of fastest women in history. provide top ten names"
    )
    return output


if __name__ == '__main__':
    with app.app_context():
        init_db()
    app.run(debug=True)
