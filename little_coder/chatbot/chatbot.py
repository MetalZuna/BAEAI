import openai
import os

def get_openai_reply(messages): # function to get reply from OpenAI, it takes messages as parameter
    chat = openai.ChatCompletion.create( # creating a chat completion object
        model="gpt-3.5-turbo", messages=messages # using the gpt-3.5-turbo model, and passing the messages
    )
    return chat.choices[0].message.content # returning the first choice from the chat

def categorize_user_input(user_input): # function to categorize user input
    # Analyze the user input and categorize it to select the appropriate prompt
    # You can use keywords, patterns, or even machine learning models here
    if "pirate" in user_input: 
        return "pirate"
    elif "technology" in user_input:
        return "technology"
    else:
        return "default"

def get_system_message(category):
    system_messages = {
        "pirate": "Talk like drunken and foul-mouthed pirate.",
        "technology": "Talk like dry, witty, and frustrated Software Engineer.",
        "default": "Talk like an old man angry with the world."
    }
    return system_messages.get(category)

def main(): # main function
    messages = [{"role": "system", "content": "Welcome to the chatbot!"}] # initializing the messages list

    while True: # infinite loop
        user_input = input("User : ") # getting user input
        if user_input: # if user input is not empty
            category = categorize_user_input(user_input) # categorize the user input
            system_message = get_system_message(category) # get the system message based on the category
            messages.append({"role": "system", "content": system_message}) # append the system message to the messages list
            messages.append({"role": "user", "content": user_input}) # append the user input to the messages list
            reply = get_openai_reply(messages) # get the reply from OpenAI based on the messages list
            print(f"ChatGPT: {reply}") # print the reply
            messages.append({"role": "assistant", "content": reply}) # append the reply to the messages list

if __name__ == "__main__":
    main()

    