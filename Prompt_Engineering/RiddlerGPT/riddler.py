import openai
import os
import string

# Set the OpenAI API Key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')  # Get API Key from environment variable
MODEL = 'gpt-3.5-turbo'
DELIMITER = "####"

class RiddleGame:
    def __init__(self):
        self.previous_answers = []

    def _openai_api_call(self, prompt):
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "system", "content": "Easy riddle problem - "}, 
            {"role": "user", "content": prompt}
        ]
        response = openai.ChatCompletion.create(model=MODEL, messages=messages)
        return response['choices'][0]['message']['content']

    def _clean_text(self, text):
        return text.translate(str.maketrans('', '', string.punctuation)).strip().lower()

    def _get_related_thing(self, topic):
        while True:
            related_thing = self._openai_api_call(f"Think of a word related to {topic} that is not too obvious and not any of these: {self.previous_answers}")
            if len(related_thing.split()) > 1:
                related_thing = self._openai_api_call(f"Simplify {related_thing} to a single word.")
            
            if related_thing not in self.previous_answers:
                self.previous_answers.append(related_thing)
                return related_thing

    def _get_riddle(self, age, player_level, thing):
        return self._openai_api_call(f"Create a riddle for an {age} years old and a {player_level} about {thing}, don't mention {thing} in your riddle. Please ensure the riddle is age and level appropriate, and error-free.")

    def _get_hint(self, thing):
        return self._openai_api_call(f"Provide a one line hint for {thing} without mentioning the {thing}.")

    def run(self):
        while True:
            print(f"Step 0: {DELIMITER} Initializing the riddle game.")
            topic = input("Enter a topic for the riddle: ")
            age = input("Enter an age for the riddle: ")
            player_level = input("Enter your level for the riddle: ")
            print(f"Step 1: {DELIMITER} User input is {DELIMITER} {topic} {DELIMITER} and user is {DELIMITER} {age} {DELIMITER} years old and the player level is {DELIMITER} {player_level} {DELIMITER}.")

            related_thing = self._get_related_thing(topic)
            print(f"Step 2: {DELIMITER} Related thing is {related_thing}.")

            riddle = self._get_riddle(age, player_level, related_thing)
            print(f"Step 3: {DELIMITER} Riddle is - \n {riddle}.")

            for attempt in range(3):
                user_answer = input("Enter your answer: ")
                print(f"Step 4: {DELIMITER} User answer is {user_answer}.")

                if self._clean_text(user_answer) == self._clean_text(related_thing):
                    print(f"Step 5: {DELIMITER} Correct! Congratulations!")
                    break
                else:
                    if attempt < 2:
                        hint = self._get_hint(related_thing)
                        print(f"Step {6+attempt}: {DELIMITER} Incorrect. Here's a hint: {hint}. Try again.")
                    else:
                        print(f"Step 8: {DELIMITER} Incorrect. The correct answer was: {related_thing}.")

            play_again = input("Do you want to play again? (yes/no): ")
            if play_again.lower() != "yes": 
                break

game = RiddleGame()
game.run()
