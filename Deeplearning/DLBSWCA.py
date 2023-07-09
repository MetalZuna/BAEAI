# Deep Learning - Build Systems with ChatGPT API
import os
import openai
import tiktoken


# 

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# helper function - chain promompts to break down the problem into smaller steps or creating smaller chains of thoughts for better results
# helps to maintain state of the workflow --> state would be categorzing the user input for building a focused chain of thought for the next step
# like question - A question about opening a new account could be categorized as "new account" --> this would help to build a chain of thought for the next step






# helper function coupled with chain of thought resoning to arrive at a conclusion

def get_completion_from_chain_messages(messages, model='gpt-3.5-turbo'):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.0,
        max_tokens=1000,
    )
    return response.choices[0].message['content']


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

def get_completion_from_messages(messages, 
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

