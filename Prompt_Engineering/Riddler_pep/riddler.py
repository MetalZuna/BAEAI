import openai
import os
import string

# Set the OpenAI API Key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')  # Get API Key from environment variable
MODEL = 'gpt-3.5-turbo'



class RiddleGame:
    def __init__(self):
        self.previous_answers = []

    def _openai_api_call(self, prompt):
        try:
            messages = [
                {"role": "system", "content": "You are a helpful assistant who writes great riddles."},
                {"role": "user", "content": prompt}
            ]
            response = openai.ChatCompletion.create(model=MODEL, messages=messages)
            return response['choices'][0]['message']['content']
        except Exception as e:
            print(f"Error: {str(e)}")
            return None

    def _clean_text(self, text):
        return text.translate(str.maketrans('', '', string.punctuation)).strip().lower()

    def _get_related_thing(self, topic):
        while True:
            related_thing = self._openai_api_call(f"Think of a word related to {topic} that is not too obvious and not any of these: {self.previous_answers}")
            if related_thing is None:
                print("Couldn't generate a related thing. Please try again.")
                return None
            if len(related_thing.split()) > 1:
                related_thing = self._openai_api_call(f"Simplify {related_thing} to a single word.")
            
            if related_thing not in self.previous_answers:
                self.previous_answers.append(related_thing)
                return related_thing

    def _get_riddle(self, age, player_level, thing):
        riddle = self._openai_api_call(f"Create a riddle for an {age} years old and a {player_level} about {thing}, don't mention {thing} in your riddle. Please ensure the riddle is age and level appropriate, and error-free.")
        if riddle is None:
            print("Couldn't generate a riddle. Please try again.")
        return riddle

    def _get_hint(self, thing):
        hint = self._openai_api_call(f"Provide a one line hint for {thing} without mentioning the {thing}.")
        if hint is None:
            print("Couldn't generate a hint. Please try again.")
        return hint

    def run(self):
        while True:
            topic = input("Enter a topic for the riddle: ")
            
            while True:
                age = input("Enter an age for the riddle: ")
                if age.isdigit():
                    break
                else:
                    print("Invalid age. Please enter a number.")

            while True:
                player_level = input("Enter your level for the riddle: ")
                if player_level.isdigit():
                    break
                else:
                    print("Invalid level. Please enter a number.")
            
            related_thing = self._get_related_thing(topic)
            if related_thing is None:
                continue
            print(f"Related thing is {related_thing}.")

            riddle = self._get_riddle(age, player_level, related_thing)
            if riddle is None:
                continue
            print(f"Riddle is - \n {riddle}.")

            for attempt in range(3):
                user_answer = input("Enter your answer: ")

                if self._clean_text(user_answer) == self._clean_text(related_thing):
                    print(f"Correct! Congratulations!")
                    break
                else:
                    if attempt < 2:
                        hint = self._get_hint(related_thing)
                        if hint is None:
                            break
                        print(f"Incorrect. Here's a hint: {hint}. Try again.")
                    else:
                        print(f"Incorrect. The correct answer was: {related_thing}.")

            play_again = input("Do you want to play again? (yes/no): ")
            if play_again.lower() != "yes": 
                break

game = RiddleGame()
game.run()
