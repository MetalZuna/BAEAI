import openai
import string

# Set the OpenAI API Key
OPENAI_API_KEY = 'your-api-key'

# Define the model
MODEL = 'gpt-3.5-turbo'

# Define the delimiter
DELIMITER = "####"

while True:
    # Step 0: Initialize the game
    print(f"Step 0: {DELIMITER} Initializing the riddle game.")

    # Step 1: Analyze user input
    user_input = input("Enter a topic for the riddle: ")
    age = input("Enter a age for the riddle: ")
    player_level = input("Enter your level for the riddle: ")
    print(f"Step 1: {DELIMITER} User input is {user_input} and I am {age} years old and the player level is {player_level}.")

    # Step 2: Think of something related to the user input
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Think of a word related to {user_input} that is not too obvious."}
    ]
    response = openai.ChatCompletion.create(model=MODEL, messages=messages)
    related_thing = response['choices'][0]['message']['content']
    print(f"Step 2: {DELIMITER} Related thing is {related_thing}.")


    # Step 2.5: Simplify the related thing to a single word if necessary
    if len(related_thing.split()) > 1:
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Simplify {related_thing} to a single word."}
        ]
        response = openai.ChatCompletion.create(model=MODEL, messages=messages)
        simplified_related_thing = response['choices'][0]['message']['content']
    else:
        simplified_related_thing = related_thing
    print(f"Step 2.5: {DELIMITER} Simplified related thing is {simplified_related_thing}.")



    # Step 3: Create a riddle game around the simplified related thing
    messages = [
        {"role": "system", "content": "You are a helpful assistant that creates riddles."},
        {"role": "user", "content": f"Create a riddle for a {age} and {player_level} about {simplified_related_thing}, don't mention {simplified_related_thing} in your riddle."}
    ]
    response = openai.ChatCompletion.create(model=MODEL, messages=messages)
    riddle = response['choices'][0]['message']['content']
    print(f"Step 3: {DELIMITER} Riddle is - \n {riddle}.")



    # Steps 4-8: Prompt the user for an answer and provide hints or the answer as needed
    for attempt in range(3):
        # Step 4: Prompt the user for an answer and wait for input
        user_answer = input("Enter your answer: ")
        print(f"Step 4: {DELIMITER} User answer is {user_answer}.")

        # For simplicity, let's assume the correct answer is the simplified related thing
        # Remove punctuation and convert to lowercase for comparison
        user_answer_clean = user_answer.translate(str.maketrans('', '', string.punctuation)).strip().lower()
        simplified_related_thing_clean = simplified_related_thing.translate(str.maketrans('', '', string.punctuation)).strip().lower()
        if user_answer_clean == simplified_related_thing_clean:
            # Step 5: If the user input is correct, congratulate the user and ask if they want to play again
            print(f"Step 5: {DELIMITER} Correct! Congratulations!")
            break
        else:
            if attempt < 2:
                # Step 6/7: If the user input is incorrect, then provide a hint and ask the user to try again
                messages = [
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": f"Provide a one line hint for {simplified_related_thing} without mentioning the {simplified_related_thing}."}
                ]
                response = openai.ChatCompletion.create(model=MODEL, messages=messages)
                hint = response['choices'][0]['message']['content']
                print(f"Step {6+attempt}: {DELIMITER} Incorrect. Here's a hint: {hint}. Try again.")
            else:
                # Step 8: If the user input is incorrect again, then provide the answer and ask the user if they want to play again
                print(f"Step 8: {DELIMITER} Incorrect. The correct answer was: {simplified_related_thing}.")
    else:
        continue

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes": 
        break
