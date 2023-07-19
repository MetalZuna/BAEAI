# GPTBA - Business Analyst with GPT-3.5-turbo
import os
import openai

# Set the OpenAI API Key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Define the model
MODEL = 'gpt-3.5-turbo'

# Define the categories and steps for Requirement Management and Requirement Elicitation Preparation
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

# Define the steps for Conduct Requirement Elicitation
Conduct_Requirement_Elicitation = {
    'Conduct_Requirement_Elicitation': {
        'Category': 'Requirements_Elicitation_Conduct',
        'Steps': {
            'REC_step_1': 'Identify Stakeholders: Identify who will be affected by the project or product.',
            'REC_step_2': 'Understand Stakeholder Needs: Understand the needs, problems, and expectations of the stakeholders.',
            'REC_step_3': 'Elicit Requirements: Use techniques such as interviews, surveys, and observation to elicit requirements from stakeholders.',
            'REC_step_4': 'Document Requirements: Document the requirements in a clear and concise manner.',
            'REC_step_5': 'Validate Requirements: Validate the requirements with the stakeholders to ensure they are correct and complete.',
        }
    }
}

# Merge the dictionaries
merged_dict = {**Requirement_Management_1, **Requirement_Elicitation_Preparation, **Conduct_Requirement_Elicitation}

# Update the get_requirements_by_category function to use the merged dictionary
def get_requirements_by_category(Category):
    return [value['Steps'] for key, value in merged_dict.items() if value.get('Category') == Category]

# Function to process user message
def process_user_message(user_input, all_messages, debug=True):
    # Extract categories from user input
    categories = get_requirements_by_category(user_input)
    if debug: print("Step 1: Extracted list of categories.")

    # Look up category information
    category_information = get_requirements_by_category(categories)
    if debug: print("Step 2: Looked up category information.")

    # Answer the user question
    messages = [
        {'role': 'system', 'content': "You are a Business Analyst (BA) agent."},
        {'role': 'user', 'content': user_input},
        {'role': 'assistant', 'content': f"Relevant requirement information:\n{category_information}"}
    ]

    token_dict, final_response = identify_use_case(all_messages + messages)
    if debug: print("Step 3: Generated response to user question.")
    all_messages = all_messages + messages[1:]

    return final_response, all_messages

# Function to collect messages
def collect_messages(user_input, all_messages, debug=False):
    if debug: print(f"User Input = {user_input}")
    if user_input == "":
        return
    response, all_messages = process_user_message(user_input, all_messages, debug=False)
    return response, all_messages

# Function to identify use case
def identify_use_case(messages, model = MODEL):
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

print ("Welcome to the Business Analyst with GPT-3.5-turbo (GPTBA)!")
print ("GPTBA is a chatbot that can help you with your Business Analyst tasks.")

# Initialize an empty list to store all messages
all_messages = []

while True:
    # Prompt the user for input
    user_input = input("Enter your message: ")

    # If the user types 'quit', break the loop
    if user_input.lower() == 'quit':
        break

    # Process the user input through the GPTBA app
    response, all_messages = collect_messages(user_input, all_messages)

    # Print the assistant's response
    print("Assistant: ", response)

    # Print the conversation history
    for message in all_messages:
        print(f"{message['role']}: {message['content']}")
