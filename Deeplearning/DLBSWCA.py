# Deep Learning - Build Systems with ChatGPT API
import os
import openai
import tiktoken


OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')


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
user_messages = f'''\ I want to discuss a new requirement'''
messages = [ 
    {'role': 'system', 'content': system_messages},
    {'role': 'user', 'content': f'{delimeter} {user_messages} {delimeter}'},
]
response = get_completion_from_messages(messages)
print(response)


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

