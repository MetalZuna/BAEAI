# main.py
import os
from flask import Flask
from models import init_db, db
from routes import register_routes
from flask_sqlalchemy import SQLAlchemy
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from langchain import PromptTemplate
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SECRET_KEY'] = 'dev'  # replace with a secure random string in production
db.init_app(app)

#-------------------------------------------------------------------------------------------------------------------------------
# Initialize language model

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
chat=ChatOpenAI()

# Define the parameters for the prompt
from langchain import PromptTemplate
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

# Define the parameters for the prompts
params = {
    'bot_name': 'GPTBA',
    'bot_capabilities': 'AI powered business Analyst, providing information about the platform and its features, help brainstorm, prepare requirements, prepare project documents, help create project backlog, create test cases, and help perform other BA tasks'
}

# Define the system message templates
system_templates = {
    'welcome': "You are {bot_name}, a helpful assistant capable of {bot_capabilities}. reply w/ short & simple answer & bullet points w/ no description",
    'stakeholder': "As {bot_name}, I can help you manage stakeholders by {bot_capabilities}. reply w/ short & simple answer & bullet points w/ no description",
    'project': "As {bot_name}, I can help you manage projects by {bot_capabilities}. reply w/ short & simple answer & bullet points w/ no description",
}

# Create the SystemMessagePromptTemplates
system_message_prompts = {feature: SystemMessagePromptTemplate.from_template(template) for feature, template in system_templates.items()}

# Define the human message templates
human_templates = {
    'welcome': "Who are you, what can you do?",
    'stakeholder': "How can you help me stakeholder managment?",
    'project': "How can you help me with the project?",
}

# Create the HumanMessagePromptTemplates
human_message_prompts = {feature: HumanMessagePromptTemplate.from_template(template) for feature, template in human_templates.items()}

# Create the ChatPromptTemplates
chat_prompts = {feature: ChatPromptTemplate.from_messages([system_message_prompts[feature], human_message_prompts[feature]]) for feature in system_templates.keys()}

# Function to generate a prompt based on the feature
def generate_prompt(feature):
    # Generate the prompt
    prompt = chat_prompts[feature].format_prompt(**params).to_messages()

    # Get a chat completion from the formatted messages
    response = chat(prompt)

    return response

# Print the response for the "welcome" feature
print(generate_prompt('project'))

#messages = [
#   SystemMessage(content="You are a helpful assistant that translates suggests a dinner plans."),
#   HumanMessage(content="suggest a Punjabi vegetarian 5 course meal for 5 people.")
#result=chat(messages)
#print(result)


# -------------------------------------------------------------------------------------------------------------------------------

# Register routes
register_routes(app, db, chat)

if __name__ == '__main__':
    with app.app_context():
        init_db()
    app.run(port=5001)
