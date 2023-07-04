# routes.py
from flask import render_template, redirect, url_for, flash, request
from models import Stakeholder
from forms import StakeholderForm
from langchain.chat_models import ChatOpenAI


# app.route
def register_routes(app, db, chatgpt_chain):
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
            # handle the form submission
            return redirect(url_for('dashboard'))
        return render_template('add_stakeholder.html', form=form)
    
    @app.route('/add_project', methods=['GET', 'POST'])
    def add_project():
        form = ProjectForm()
        if form.validate_on_submit():
            new_project = Project(
                name=form.project_name.data, 
                description=form.description.data, 
                start_date=form.start_date.data, 
                end_date=form.end_date.data, 
                status=form.status.data, 
                user_id=form.user_id.data
            )
            db.session.add(new_project)
            db.session.commit()
            flash('Project added successfully')
            return redirect(url_for('dashboard'))
        return render_template('add_project.html', form=form)


      
   


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
    
    @app.route('/chat', methods=['POST'])
    def chat_route():
        # Get the user's input from the request data
        user_input = request.get_json().get('input')

        # Add the user's input to the messages
        prompt.append(HumanMessage(content=user_input))

        # Get a chat completion from the formatted messages
        response = chat(prompt)

        # Return the chatbot's response as the response data
        return jsonify({'response': response})
