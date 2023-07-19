# main.py
import os
import openai
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
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.memory import ConversationBufferWindowMemory
from langchain.memory import ConversationTokenBufferMemory
from langchain.memory import ConversationSummaryBufferMemory


#-------------------------------------------------------------------------------------------------------------------------------
# Write a function to initialize the chatbot
# Function collects the user input 
# Function uses the system message prompt template to generate the system message
# Function returns the Final response to the user







# Step 1: Analyze the input
# Step 2: Identify what user wants to do
# Step 3: Identify destination template for routing the user query
# Step n: Scan output for relevancy, if satisfied, then display output, else go to step n
# Step n: Review history prompt
# Step n
# Step n: Scan output for relevancy, if not relevant, then go to step n else display output 

delimeter = "####"
Initial_Thought = f"""
Follow the steps to answer the engagement with the user.
The user message will be delimited with four hashtags, \ i.e. {delimeter}.

Step 1: {delimeter} Analyze the input,
Step 2: {delimeter} Identify what user wants to do,
Step 3: {delimeter} Identify destination template for routing the user query,


"""

Output_Thought = f"""
Follow the steps to answer the engagement with the user.
The user message will be delimited with four hashtags, \ i.e. {delimeter}.

Step 1: {delimeter} Scan output for relevancy, if satisfied, then display output, else go to step n,
Step 2: {delimeter} Review history prompt,
Step 3: {delimeter} Scan output for relevancy, if not relevant, then go to step n else display output""" 






app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SECRET_KEY'] = 'dev'  # replace with a secure random string in production
db.init_app(app)

#-------------------------------------------------------------------------------------------------------------------------------
# Initialize language model

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
chat=ChatOpenAI()

llm = ChatOpenAI(temperature=0.1)
# to load tools into the language model tools = load_tooals(["llm-math", "wikipedia"], llm=llm)
#memory = ConversationBufferMemory()
#memory = ConversationBufferWindowMemory(k=1)
memory = ConversationTokenBufferMemory(llm=llm, max_tokens=1)
conversation = ConversationChain(
    llm = llm,
    memory = memory,
    verbose = False
    )

'''
To initialize a agent
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION, (Chat = agent for chat model, React - prompting technique designed to get the best resoning from the model, Description)
    handle_parsing_errors=True,
    verbose=True)

'''

memory.save_context({"input": "What color is the grass"}, {"output": "The grass is green"})

memory.save_context({"input": "What color is the sky"}, {"output": "The sky is blue"})

memory.save_context({"input": "Does mangoe taste good?"}, {"output": "Mangoe tastes good"})

#print(memory.buffer)
print(memory.load_memory_variables({}))


'''
response = conversation.predict(input = 'Hello, my name is Singh')
print(response)

print(conversation.predict(input = 'What is the capital of Myanmar?'))

print(conversation.predict(input = 'do you remember my name?'))

print(memory.load_memory_variables({}))

'''


#-------------------------------------------------------------------------------------------------------------------------------
'''

User: lands on the dashboard page
Bot: greets the user
User: greets the bot
Bot: asks the user what they want to do
User: says they want to add a project
Bot: asks the user for the project name
User: provides the project name
Bot: asks the user for the project description
User: provides the project description
Bot: asks the user for the project start date
User: provides the project start date
Bot: asks the user for the project end date
User: provides the project end date
Bot: asks the user for the project status
User: provides the project status
Bot: displays the project details that the user provided
User: confirms the project details
Bot: adds the project to the database



#-------------------------------------------------------------------------------------------------------------------------------
# Helper function to get the completion text from the chat model
def get_completion(prompt, model='gpt-3.5-turbo'):
    messages = [{'role': 'user', 'content': prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.1,
    )
    return response.choices[0].message['content']
                 

# print(get_completion('what is the capital of Azerbaijan?'))

customer_email = """
Arrr, I be fuming that me blender lid \
flew off and splattered me kitchen walls \
with smoothie! And to make matters worse,\
the warranty don't cover the cost of \
cleaning up me kitchen. I need yer help \
right now, matey!
"""

style = """American English \
in a calm and respectful tone
"""


prompt = f"""Translate the text \
that is delimited by triple backticks 
into a style that is {style}.
text: ```{customer_email}```
"""

print(prompt)
response = get_completion(prompt)
print(response)


'''
#-------------------------------------------------------------------------------------------------------------------------------
# Define the parameters for the prompts
'''
params = {
    'bot_name': 'GPTBA',
    'bot_capabilities': 'AI powered business Analyst, providing information about the platform and its features, help brainstorm, prepare requirements, prepare project documents, help create project backlog, create test cases, and help perform other BA tasks',
    'welcome': 'welcome',
    'add_project': 'reply only with - sure, lets add a project',
    'project_name': 'project_name',
    'start_date': '{project_name} will start on {start_date}. reply w/ simple answer w/ no description?',
}


# Define the system message templates
system_templates = {
    'welcome': "You are {bot_name}, a helpful assistant capable of {bot_capabilities}. reply w/ short & simple answer & bullet points w/ no description",
    'add_project': " reply only with - sure, lets add a project",
    'project_name': "reply with - okay, I have {project_name} as the project name.? and no other comment?",
    'start_date': " {project_name} will start on {start_date}. reply w/ simple answer w/ no description?",
    'end_date': " {project_name} will end on {end_date}. reply w/ simple answer w/ no description?",
    'status': " {project_name} {status} is. reply w/ simple answer w/ no description?",
    'user_id': " {user_id} is your user id. reply w/ simple answer w/ no description?",
    'description': " Thanks for providing project description. reply w/ simple answer. reply with description hilights in bullet points?",
    'confirm_project': "The project details are - {project_name}, {start_date}, {end_date}, {status}, {user_id}, {description}",

}

# Create the SystemMessagePromptTemplates
system_message_prompts = {feature: SystemMessagePromptTemplate.from_template(template) for feature, template in system_templates.items()}

# Define the human message templates 
human_templates = {
    'welcome': "Who are you, what can you do?",
    'add_project': "I want to add a project",
    'project_name': "The project name is {project_name}",
    'start_date': "The start date is {start_date}",
    'end_date': "The end date is {end_date}",
    'status': "The status is {status}",
    'user_id': "My user id is {user_id}",
    'description': "The project description is - {description}",
    'confirm_project': 'y' or 'n' or 'yes' or 'no'
}


# Create the HumanMessagePromptTemplates
human_message_prompts = {feature: HumanMessagePromptTemplate.from_template(template) for feature, template in human_templates.items()}

# Create the ChatPromptTemplates
chat_prompts = {feature: ChatPromptTemplate.from_messages([system_message_prompts[feature], human_message_prompts[feature]]) for feature in system_templates.keys()}

def get_project_name(chat):
    # Get the ChatPromptTemplate for the 'project_name' feature
    chat_prompt_template = chat_prompts['project_name']
    
    # Generate a prompt from the ChatPromptTemplate
    prompt = chat_prompt_template.format_prompt(**params)
    
    # Get a response from the chat model
    response = chat(prompt.to_messages())
    
    # Prompt the user for the project name
    user_input = input("Please enter the project name: ")
    
    # Update the params dictionary with the user's input
    params['project_name'] = user_input

    # Update the prompt with the user's input
    prompt = chat_prompt_template.format_prompt(**params)

    # Get a new response from the chat model
    response = chat(prompt.to_messages())

    # Print the new response
    print(response.content)

def get_start_date(chat):
    # Get the ChatPromptTemplate for the 'start_date' feature
    chat_prompt_template = chat_prompts['start_date']
    
    # Generate a prompt from the ChatPromptTemplate
    prompt = chat_prompt_template.format_prompt(**params)
    
    # Get a response from the chat model
    response = chat(prompt.to_messages())
    
    # Prompt the user for the start date
    user_input = input("Please enter the project start date: ")
    
    # Update the params dictionary with the user's input
    params['start_date'] = user_input

    # Update the prompt with the user's input
    prompt = chat_prompt_template.format_prompt(**params)

    # Get a new response from the chat model
    response = chat(prompt.to_messages())

    # Print the new response
    print(response.content)


# Then, you can call these functions in your main code like this:
print(get_project_name(chat))
print(get_start_date(chat))
'''


# -------------------------------------------------------------------------------------------------------------------------------

# Register routes
register_routes(app, db, chat)

if __name__ == '__main__':
    with app.app_context():
        init_db()
    
    app.run(port=5001)
