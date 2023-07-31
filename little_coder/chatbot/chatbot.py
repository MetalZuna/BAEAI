import openai
import os
import string

# Set the OpenAI API Key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')  # Get API Key from environment variable
MODEL = 'gpt-3.5-turbo'

delimiter = "####"

messages = [
    {"role": "system", "content": "Act as a kind helpful Business Analyst."},
    {"role": "system", "content": f""" Follow these steps to answer user query. The query will be delimited with four hashes (####)

Step 0: {delimiter} Analyze the user query and understand the context of the user query.
Step 1: {delimiter} Check if the user query is related to Business requirements. if yes, then proceed to step 2. Else, proceed to step 3.
Step 2: {delimiter} Provide helpful feedback to the user query.
Step 3: {delimiter} Ask user to only ask questions related to Business Analytics. 
Step 4: {delimiter} Wait for the user to respond.

"""}
]


while True:
    message = input("User : ")
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})

