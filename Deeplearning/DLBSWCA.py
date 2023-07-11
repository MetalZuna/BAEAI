# Deep Learning - Build Systems with ChatGPT API
import os
import openai
import tiktoken


# 

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

#------------------------------------------------------------
# helper function to chain promompts to break down the problem into smaller steps or creating smaller chains of thoughts for better results
# helps to maintain state of the workflow --> state would be categorzing the user input for building a focused chain of thought for the next step
# like question - A question about opening a new account could be categorized as "new account" --> this would help to build a chain of thought for the next step
# chaining prompts reduces the number of tokens required to generate a response
# Skips some chains of the workflow when not needed for the task
# Easier to test - to include human-in-the-loop
# For complex tasks, keep track of state external to the llm (in your own code) and inject instructions into the prompt as needed
# Chaining prompts let's chat model use external tools like web search, database queries, etc. to generate a response 
    # It allows for more focused breakdown of complex tasks
    # Limit the impact of Context limitation for input prompt and output prompt
    # Reduce cost of generating a response due to smaller input and output prompts
    # Text embeddings enhance the quality of the response

#------------------------------------------------------------
# BA agent use cases
# 1. BA agent to help with the user query by identifying the category of the query
# 2. BA agent to help with the user query by identifying the sub-category of the query

def identify_use_case(messages, model = 'gpt-3.5-turbo'):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.0,
        max_tokens=3000,
    )

    token_dict = {
    'prompt_tokens': response['usage']['prompt_tokens'],
    'completion_tokens': response['usage']['completion_tokens'],
    'total_tokens': response['usage']['prompt_tokens'] + response['usage']['completion_tokens']
    }

    return token_dict, response.choices[0].message['content']

# Requirement Management Use Cases
# Requirement Management Use Cases
Requirement_Management_1 = {
    'Requirement_Elicitation_steps': {
        'Category': 'Requirements_Elicitation',
        'Steps': {
            'RE_step_1': 'Prepare for Requirement Elicitation to ensure that the stakeholder has the information they need to participate in the elicitation session',
            'RE_step_2': 'Conduct Requirement Elicitation to fully understand the stakeholder\'s needs_or_problems and expectations', 
            'RE_step_3': 'Document Requirement Elicitation- create text to document the results of the elicitation session',
            'RE_step_4': 'Review Original requirements with the stakeholder to ensure that the requirements are correct and complete',
            'RE_step_5': 'Review Requirement Solution Scope with the stakeholder to ensure that the solution scope is correct and complete',
        }
    },

    'Requirements_Analysis_steps': {
        'Category': 'Requirements_Analysis',
        'Steps': {
            'RA_step_1': 'Prepare for Requirements Analysis to ensure that the stakeholder has the information they need to participate in the analysis session',
            'RA_step_2': 'Conduct Requirements Analysis to fully understand the stakeholder\'s needs_or_problems and expectations', 
            'RA_step_3': 'Document Requirements Analysis- create text to document the results of the analysis session',
            'RA_step_4': 'Review Original requirements with the stakeholder to ensure that the requirements are correct and complete',
            'RA_step_5': 'Review Requirement Solution Scope with the stakeholder to ensure that the solution scope is correct and complete',
        }
    }
}


Requirement_Elicitation_Preparation = {
    'Prepare_for_Requirement_Elicitation': {
        'Category': 'Requirements_Elicitation_Preparation',
        'Steps': {
            'REP_step_1': 'Understanding the Context: Understand the project or product context, including the overall objectives, the stakeholders, and their roles.',
            'REP_step_2': 'Setting the Agenda: Explain the purpose of the requirement elicitation session to the user, what the session will involve, and what is expected of them.',
            'REP_step_3': 'Collecting Preliminary Information: Ask the user to briefly describe their initial ideas about their requirements.',
            'REP_step_4': 'Asking for Clarifications: Ask clarifying questions whenever the user\'s responses are ambiguous or unclear.',
            'REP_step_5': 'Validating Understanding: Summarize the requirements back to the user at intervals to ensure correct understanding.',
            'REP_step_6': 'Keeping the Conversation On Track: Politely steer the conversation back to the topic of requirements if the user goes off on a tangent.',
            'REP_step_7': 'Wrapping Up: At the end of the session, summarize all the discussed requirements, thank the user for their time, and explain the next steps in the process.',
        }
    }
}



def get_requirements_by_category(Category):
    merged_dict = {**Requirement_Management_1, **Requirement_Elicitation_Preparation}
    return [value['Steps'] for key, value in merged_dict.items() if value.get('Category') == Category]

# Assume the following variables hold the outputs from your previous function calls
requirements_elicitation = get_requirements_by_category('Requirements_Elicitation')
requirements_elicitation_preparation = get_requirements_by_category('Requirements_Elicitation_Preparation')

# Now you can extract 'RE_step_1' and 'REP_step_1'
RE_step_1 = requirements_elicitation[0]['RE_step_1']
REP_step_1 = requirements_elicitation_preparation[0]['REP_step_1']

# Now RE_step_1 and REP_step_1 contain the corresponding steps

# Define the system message and user message
System_Message = f'''You are a Business Analyst (BA) agent. You will be get context from the user. You will answer user queries about the context politely and ask follow-up questions to get more information from the user.'''
user_message_1 = f'''How do we get started with Requirement Elicitation? What questions do you have for me?'''
user_message_2 = f'''Project is a web application that will allow users to financial reports related to their investment portfolio.''' 
user_message_3 = f'''Primary users are - Investors, Financial Advisors, and Bank colleagues.''' 

delimeter = '####'
Thought_Process = f'''
Follow the steps to answer the engage with the user.
The user message will be delimited with four hashtags, \ i.e. {delimeter}.

Step 1: {delimeter} first decide if the user query is a question or a statement.
Step 2: {delimeter} If it is a question, then analyze the question and move to step 3 else go to step 5.
Step 3: {delimeter} If you are not sure about the question, then ask the user to provide more information.
Step 4: {delimeter} If you have enough information, then answer the question.
Step 5: {delimeter} If it is a statement, then analyze the statement and move to step 6.
Step 6: {delimeter} If you are not sure about the statement, then ask the user to provide more information and go back step 5 else go to step 7.
Step 7: {delimeter} Only ask one question at a time based on the context.
Step 8: {delimeter} If you have answer or a query, then ask the next question or provide response to th user.
Step 9: {delimeter} Wait for user response and go to step 1.

use the following format to provide your output:
step 1: {delimeter} <step 1 resoning>
step 2: {delimeter} <step 2 resoning>
step 3: {delimeter} <step 3 resoning>
step 4: {delimeter} <step 4 resoning>
step 5: {delimeter} <step 5 resoning>
step 6: {delimeter} <step 6 resoning>
step 7: {delimeter} <step 7 resoning>
step 8: {delimeter} <step 8 resoning>
step 9: {delimeter} <step 9 resoning>
response to user: {delimeter} <your response to the user>
'''



# Define the assistant's response using the RE_step_1 value
assistant_message_1 = RE_step_1
assistant_message_2 = REP_step_1

# Create the messages list with a placeholder for the final assistant message
messages = [
    {'role': 'system', 'content': System_Message},
    {'role': 'user', 'content': user_message_1},
    {'role': 'assistant', 'content': assistant_message_1},
    {'role': 'assistant', 'content': assistant_message_2},
    {'role': 'user', 'content': user_message_2},
    {'role': 'assistant', 'content': Thought_Process},
    {'role': 'user', 'content': user_message_3},
    {'role': 'assistant', 'content': 'placeholder'}  # This will be replaced later
]

new_message_content, token_dict = identify_use_case(messages)

# Replace the placeholder with the new message content
messages[-1]['content'] = new_message_content

print(new_message_content, token_dict)


#print(get_requirements_by_category('Requirements_Elicitation'))
#print(get_requirements_by_category('Requirements_Elicitation_Preparation'))


'''
def generate_output_string(data_list):
    output_string = ''

    if data_list is None:
        return output_string
    for data in data_list:
        try:
            if'RA_step' in data:
                

'''








#------------------------------------------------------------
"""
def get_completion_from_chain_prompt_messages(messages, model='gpt-3.5-turbo'):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.0,
        max_tokens=3000,
    )
    return response.choices[0].message['content']

delimeter = '####'
system_message = f'''

you will be given a user query. The query will be delimited with four hashtags, i.e. {delimeter} character.
output a python list of objects, where each object has the following format
    'category': <requirements, agile, user story, testing, project management, product management>

where the categories and sub-categories, and user intent must be found in user query.
if the category is mentioed, it must be associated with correct category in the allowed sub-categories list
you must also identify the user intent from the intent list.

Allowed sub-categories
Requirements: 
    'requirements elicitation', 'requirements analysis', 'requirements specification', 'requirements validation', 'requirements management'
Agile:
    'agile', 'scrum', 'kanban', 'lean', 'extreme programming', 'adaptive software development', \
        'crystal', 'dynamic systems development method', 'feature-driven development', 'unified process'
User Story:
    'user story', 'user stories'
Testing:
    'testing', 'test-driven development', 'unit testing', 'integration testing', 'functional testing', \
        'system testing', 'end-to-end testing', 'acceptance testing', 'performance testing', 'load testing', \
            'stress testing', 'usability testing', 'install/uninstall testing', 'recovery testing', \
                'security testing', 'compatibility testing', 'exploratory testing', 'ad hoc testing', 'user acceptance testing', \
                    'alpha testing', 'beta testing', 'gray box testing', 'black box testing', 'white box testing'
Project Management:
    'project management', 'project manager', 'project plan', 'project charter', 'project scope', 'project scheduling', \
        'project estimation', 'project budgeting', 'project communication', 'project risk management', 'project quality management',\
              'project staffing', 'project controlling', 'project closure'
Product Management:
    'product management', 'product manager', 'product market research', 'product strategy', 'product roadmap', 'product requirements', \
        'product design', 'product development', 'product launch', 'product marketing', 'product sales', 'product support', 'product end of life'


user intent:
    'Create, write, writing, make'
    'Read, get, look-up, search, find'
    'Update, change, modify'
    'Delete, remove, cancel'
    'List, view, show, display'
    'Login, sign-in, sign-up, register'
    'Logout, sign-out'
    'Help, support, faq'
    'Brainstorm, idea, suggestion, discuss' '''

user_message_1 = f'''
I need your help writing a user story for a new feature. The feature is called 'Demographics'.
when the user lands on the dashboard, then the demographics box shall be displayed as per the prototype.
Demographics box shall display First Name, Last Name, Email, Phone Number, and Address of the client as per the prototype.
I also want to discuss the testing scope for this feature.'''

'''
messages = [
    {'role': 'system', 
     'content': system_message},
    {'role': 'user',
        'content': f'{delimeter} {user_message_1} {delimeter}'},
]
'''



#category_and_intent_response_1 = get_completion_from_chain_prompt_messages(messages)
# print(category_and_intent_response_1)






# helper function coupled with chain of thought resoning to arrive at a conclusion

def get_completion_from_chain_steps_messages(messages, model='gpt-3.5-turbo'):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.0,
        max_tokens=1000,
    )
    return response.choices[0].message['content']


"""
"""
delimeter = '####'
system_messages = f'''
Follow the steps to answer the user queries.
The user query will be delimited with four hashtags, \ i.e. {delimeter}.

Step 1: {delimeter} first decide if the user query is a question or a statement.\
If it is a question, then go to step 2. If it is a statement, then go to step 3.

Step 2: {delimeter} if the user is asking a question about one of these topic, \
identify the topic from the list of topics below and go to step 4.
All available topics:
Project Management, 
Product Management,
Agile,
Requirements,
Testing,
User Story,
User Stories

Step 3: {delimeter} if the user is making a statement about a specific topic, \
identify the topic from the list of topics in step 2 and go to step 5, if the topic is not in step 2 then go to step 8.

Step 4: {delimeter} only if the user is asking a question about topics listed in step 2, \
then figure out the information you need to answer the quetstion and go to step 6.

Step 5: {delimeter} if the user is making a statement about topics listed in step 3, \
then ask the user a question to get more information and go to step 7

Step 6: {delimeter} if the question is relevant from the topic in step 2 and you have the information to answer the question, \
then answer the qeuestion

Step 7: {delimeter} provide feedback to the user and go to step

Step 8: {delimeter} polititely remind the user to ask question from topics given in step 2 and go back to step 2

use the following format to provide your output:
step 1: {delimeter} <step 1 resoning>
step 2: {delimeter} <step 2 resoning>
step 3: {delimeter} <step 3 resoning>
step 4: {delimeter} <step 4 resoning>
step 5: {delimeter} <step 5 resoning>
step 6: {delimeter} <step 6 resoning>
step 7: {delimeter} <step 7 resoning>
step 8: {delimeter} <step 8 resoning>
response to user: {delimeter} <response to user>

make sure to include {delimeter} to separate every step.

'''
user_messages = f''' I have a user story to discuss with you'''

messages = [
    {'role': 'system', 'content': system_messages},
    {'role': 'user', 'content': f'{delimeter} {user_messages} {delimeter}'},
]

# Call the function to get a response from the OpenAI API
response = get_completion_from_chain_messages(messages)

# Define the indicator that separates the response from the rest of the text
response_indicator = 'response to user:'

# If the response indicator is in the response, split the response at the indicator and keep the part after it
if response_indicator in response:
    try:
        final_response = response.split(delimeter)[-1].strip()
    except:
        # If an error occurs while splitting the response, print an error message
        final_response = 'Sorry, I don\'t understand.'
else:
    # If the response indicator is not in the response, print a default message
    final_response = 'Sorry, I can\'t generate a response.'

# Print the final response
print(final_response)




# helper function coupled with the moderation API

def get_completion_from_moderation_messages(messages, model='gpt-3.5-turbo'):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.0,
        max_tokens=150,
    )
    return response.choices[0].message['content']

'''response = openai.Moderation.create(
    input = 'We get a big gun and hold the world hostage for....ONE MILLION DOLLARS!',
)

print(response)

"""

# helper function to evaluate inputs: classfying the input into primary and secondary categories
"""

def get_completion_from_steps_messages(messages, 
    model='gpt-3.5-turbo', 
    temperature=0, 
    max_tokens=500):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, 
        max_tokens=max_tokens,
    )
    return response.choices[0].message['content']

delimeter = '####'
system_messages = f'''
You will be provided with user tasks.\
The user tasks will be delimited with \
{delimeter} characters.
Classify the user tasks into a primary category\
and a secondary category.
Provide your output in json format with the \
keys: primary and secondary.

Primary Categories: Project Management, Product Management, \
Agile, Requirements, or Testing.

Project Management Secondary Categories: 
Project Initiation, or 
Project Planning, or
Project Execution

Product Management Secondary Categories:
Product Strategy, or
Product Development, or
Product Launch

Agile Secondary Categories:
Scrum, or
Kanban, or
Agile KPIS

Requirements Secondary Categories:
Requirements Elicitation, or
Requirements Analysis, or
Requirements Documentation
User Stories

Testing Secondary Categories:
Test Planning, or
Test Design, or
Test Execution, or
Test Reporting
'''
user_messages = f'''\ {delimeter} The requirements are changing often and causing scope creep. 
{delimeter} I also want to discuss testing scope for the new feature that I want to add to the project.'''
messages = [ 
    {'role': 'system', 'content': system_messages},
    {'role': 'user', 'content': f'{delimeter} {user_messages} {delimeter}'},
]
#response = get_completion_from_messages(messages)
#print(response)


# helper function to look at the token usage

def get_completion_and_token_usage(messages, model='gpt-3.5-turbo'):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.0,
        max_tokens=150,

    )
    content = response.choices[0].message['content']

    token_dict = {
        'prompt_tokens': response['usage']['prompt_tokens'],
        'completion_tokens': response['usage']['completion_tokens'],
        'total_tokens': response['usage']['prompt_tokens'] + response['usage']['completion_tokens']
    }
    return content, token_dict

messages = [
    {'role': 'system', 'content': 'You are an experienced project manager, who proactively works with the delivery team to understand their issues'},
    {'role': 'assistant', 'content': 'Project is behind schedule'},
    {'role': 'user', 'content': 'How do deal with a team member who is not performing well?'},
]

#response, token_dict = get_completion_and_token_usage(messages)
#print(response, token_dict)



# helper function to get completion from OpenAI API

def get_completion_from_messages(messages, model='gpt-3.5-turbo'):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.0,
        max_tokens=150,

    )
    return response.choices[0].message['content']

messages = [
    {'role': 'system', 'content': 'You are an experienced project manager, who proactively works with the delivery team to understand their issues'},
    {'role': 'assistant', 'content': 'Project is behind schedule'},
    {'role': 'user', 'content': 'How do deal with a team member who is not performing well?'},
]

#response = get_completion_from_messages(messages)
#print(response)

# helper function to get completion from OpenAI API

def get_completion(prompt, model='gpt-3.5-turbo'):
    messages = [{'role': 'user', 'content': prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.1,
    )
    return response.choices[0].message['content']
                 

#--- print(get_completion('what is the capital of Azerbaijan?'))

# One token is about 4 words in english language
# input is often called context
# output is often called completion

"""