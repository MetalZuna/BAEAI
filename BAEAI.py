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
    'bot_capabilities': 'AI powered business Analyst, providing information about the platform and its features, help brainstorm, prepare requirements, prepare project documents, help create project backlog, create test cases, and help perform other BA tasks',
    # write code to get project name from user
    'project_name': 'project name',
}

# Define the system message templates
system_templates = {
    'welcome': "You are {bot_name}, a helpful assistant capable of {bot_capabilities}. reply w/ short & simple answer & bullet points w/ no description",
    'add_project': "As {bot_name}, I can help you add project. what is your {project_name} reply w/ simple answer w/  description?",
    'add_project_name': "what is your {project_name} reply w/ simple answer w/ no description?",
}

# Create the SystemMessagePromptTemplates
system_message_prompts = {feature: SystemMessagePromptTemplate.from_template(template) for feature, template in system_templates.items()}

# Define the human message templates
human_templates = {
    'welcome': "Who are you, what can you do?",
    'add_project': "I want to add a project named {project_name}",
    'add_project_name': "The project name is {project_name}",
}


# Create the HumanMessagePromptTemplates
human_message_prompts = {feature: HumanMessagePromptTemplate.from_template(template) for feature, template in human_templates.items()}

# Create the ChatPromptTemplates
chat_prompts = {feature: ChatPromptTemplate.from_messages([system_message_prompts[feature], human_message_prompts[feature]]) for feature in system_templates.keys()}

# Function to prompt the user for a human message
def prompt_human_message(feature, chat):
    # Get the ChatPromptTemplate for the given feature
    chat_prompt_template = chat_prompts[feature]
    
    # Generate a prompt from the ChatPromptTemplate
    prompt = chat_prompt_template.format_prompt(**params)
    
    # Get a response from the chat model
    response = chat(prompt.to_messages())
    
    # Print the chatbot's response
    print(response)
    
    # Ask for the user's input
    user_input = input("Your turn: ")
    
    # Update the params dictionary with the user's input
    params['project_name'] = user_input
    
    # Generate a new system prompt with the user's input
    new_prompt = chat_prompt_template.format_prompt(**params)
    
    # Get a response from the chat model
    new_response = chat(new_prompt.to_messages())
    
    return new_response


print(prompt_human_message('welcome', chat))
print(prompt_human_message('add_project_name', chat))




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
