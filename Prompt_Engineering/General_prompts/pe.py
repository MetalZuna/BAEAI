# GPTBA - Business Analyst with GPT-3.5-turbo
import os
import openai

# Set the OpenAI API Key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Define the model
MODEL = 'gpt-3.5-turbo'

delimiter = "####"

Category_list = f"""Requirements, Brainstorming, User Story, Test Case, General"""
Sub_Category_list = f"""Create, Read, Update, Delete, Discuss, Brainstorm, General Help"""

# System message Root template
System_Message_Root = f"""
Persona = Act as an expert Business Analyst


Context = "
message -
AI: - Hello, How can I help You.
User : I have a new requirement to discuss with you.
"

Follow these steps to answer user query. The query will be delimited with four hashes (####)


Step 0: {delimiter} analyze the user query for {Category_list} and {Sub_Category_list} and go to step 1
Step 1: {delimiter} if you have any question(s), then provide feedback, and go back to step 0 else move to step 2
Step 2: {delimiter} if it's a statement, then analyze the statement and move to step 3
Step 3: {delimiter} identify the appropriate category and if needed then identify sub-category for the user query
Step 4: {delimiter} make sure you know the category and sub-category for the user query
Step 5: {delimiter} provide category from {Category_list} and sub-category from {Sub_Category_list} as response in Json object (so it can be fed back to the system for further action)
"""

Response_Format = f"""
Format the output in the following way

use the following format to provide your output:
Step 0: {delimiter} <step 0 resoning>
step 1: {delimiter} <step 1 resoning>
step 2: {delimiter} <step 2 resoning>
step 3: {delimiter} <step 3 resoning>
step 4: {delimiter} <step 4 resoning>
Step 5: {delimiter} <step 5 resoning>
response to user: {delimiter} <your response to the user>

""" 


# Define the categories and steps for Requirement Management and Requirement Elicitation Preparation
Requirement_Management_1 = {
    'Requirement_Elicitation_steps': {
        'Category': 'Requirements_Elicitation',
        'Steps': {
            'RE_step_1': f"{delimiter} Prepare for Requirement Elicitation to ensure that the stakeholder has the information they need to participate in the elicitation session",
            'RE_step_2': f"{delimiter} Conduct Requirement Elicitation to fully understand the stakeholder's needs_or_problems and expectations", 
            'RE_step_3': f"{delimiter} Document Requirement Elicitation- create text to document the results of the elicitation session",
            'RE_step_4': f"{delimiter} Review Original requirements with the stakeholder to ensure that the requirements are correct and complete",
            'RE_step_5': f"{delimiter} Review Requirement Solution Scope with the stakeholder to ensure that the solution scope is correct and complete",
        }
    },
    'Requirements_Analysis_steps': {
        'Category': 'Requirements_Analysis',
        'Steps': {
            'RA_step_1': f"{delimiter} Prepare for Requirements Analysis to ensure that the stakeholder has the information they need to participate in the analysis session",
            'RA_step_2': f"{delimiter} Conduct Requirements Analysis to fully understand the stakeholder's needs_or_problems and expectations", 
            'RA_step_3': f"{delimiter} Document Requirements Analysis- create text to document the results of the analysis session",
            'RA_step_4': f"{delimiter} Review Original requirements with the stakeholder to ensure that the requirements are correct and complete",
            'RA_step_5': f"{delimiter} Review Requirement Solution Scope with the stakeholder to ensure that the solution scope is correct and complete",
        }
    }
}


Requirement_Elicitation_Preparation = {
    'Prepare_for_Requirement_Elicitation': {
        'Category': 'Requirements_Elicitation_Preparation',
        'Steps': {
            'REP_step_1': f"{delimiter} Understanding the Context: Understand the project or product context, including the overall objectives, the stakeholders, and their roles.",
            'REP_step_2': f"{delimiter} Setting the Agenda: Explain the purpose of the requirement elicitation session to the user, what the session will involve, and what is expected of them.",
            'REP_step_3': f"{delimiter} Collecting Preliminary Information: Ask the user to briefly describe their initial ideas about their requirements.",
            'REP_step_4': f"{delimiter} Asking for Clarifications: Ask clarifying questions whenever the user's responses are ambiguous or unclear.",
            'REP_step_5': f"{delimiter} Validating Understanding: Summarize the requirements back to the user at intervals to ensure correct understanding.",
            'REP_step_6': f"{delimiter} Keeping the Conversation On Track: Politely steer the conversation back to the topic of requirements if the user goes off on a tangent.",
            'REP_step_7': f"{delimiter} Wrapping Up: At the end of the session, summarize all the discussed requirements, thank the user for their time, and explain the next steps in the process.",
        }
    }
}


Conduct_Requirement_Elicitation = {
    'Conduct_Requirement_Elicitation': {
        'Category': 'Requirements_Elicitation_Conduct',
        'Steps': {
            'REC_step_1': f"{delimiter} Identify Stakeholders: Identify who will be affected by the project or product.",
            'REC_step_2': f"{delimiter} Understand Stakeholder Needs: Understand the needs, problems, and expectations of the stakeholders.",
            'REC_step_3': f"{delimiter} Elicit Requirements: Use techniques such as interviews, surveys, and observation to elicit requirements from stakeholders.",
            'REC_step_4': f"{delimiter} Document Requirements: Document the requirements in a clear and concise manner.",
            'REC_step_5': f"{delimiter} Validate Requirements: Validate the requirements with the stakeholders to ensure they are correct and complete.",
        }
    }
}


# General prompt template

Delimiter = "####"

General_Template = f"""


Follow these steps to answer user query. The query will be delimeted with four hashes (####)

Step 0: {delimiter} Analyze the user query and understand the context of the user query.
Step 1: {delimiter} Check if the user query is related to Business Analytics. if yes, then proceed to step 2. Else, proceed to step 3.
Step 2: {delimiter} Provide helpful feedback to the user query.
Step 3: {delimiter} Provide a short anaswer and go to step 4 
Step 4: {delimiter} Politely remind the user to ask questions related to Business Analytics.


{Delimiter}Answer the user question polietly and remind the user to ask questions related to Business Analytics."""

merged_dict = {**Requirement_Management_1, **Requirement_Elicitation_Preparation, **Conduct_Requirement_Elicitation}

def identify_use_case(messages, model=MODEL):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.0,
        max_tokens=3000,
    )

    # Extract the content from the response
    content = response.choices[0].message['content']

    # Split the content into separate words
    words = content.split()

    # Identify the category and sub-category
    category = next((word for word in words if word in Category_list.split(', ')), None)
    sub_category = next((word for word in words if word in Sub_Category_list.split(', ')), None)

    # Select the appropriate template based on the category and sub-category
    if category == 'general':
        template = General_Template
    else:
        # Add conditions here for other categories and their corresponding templates
        template = None

    # Use the selected template to generate the final response
    if template is not None:
        final_response = template.format(category=category, sub_category=sub_category)
    else:
        final_response = content

    return final_response

def identify_category(user_input):
    # This is a very basic implementation. 
    # In a real-world scenario, you might use machine learning or complex rules to identify the category.
    if "requirement" in user_input.lower():
        return "Requirements"
    elif "brainstorm" in user_input.lower():
        return "Brainstorming"
    elif "user story" in user_input.lower():
        return "User Story"
    elif "test case" in user_input.lower():
        return "Test Case"
    else:
        return "General"

def execute_template(template, messages):
    # Split the template into steps
    steps = template.split(delimiter)

    # Initialize an empty string to store the final response
    response = ""

    # Loop over the steps in the template
    for step in steps:
        # If the step is to analyze the user's query, call a function to do that and add the result to the response
        if "Analyze the user query" in step:
            analysis = analyze_user_query(messages[-1]['content'])  # This function needs to be implemented
            response += step + analysis + "\n"
        # If the step is to provide feedback, call a function to do that and add the result to the response
        elif "Provide helpful feedback" in step:
            feedback = provide_feedback(messages[-1]['content'])  # This function needs to be implemented
            response += step + feedback + "\n"
        # And so on for the other steps...

    return response



def select_template(category):
    # This is a very basic implementation. 
    # In a real-world scenario, you might have a complex mapping from categories to templates.
    templates = {
        "Requirements": Requirement_Management_1,
        "Brainstorming": Requirement_Elicitation_Preparation,
        "User Story": Conduct_Requirement_Elicitation,
        "Test Case": None,  # Add your template for "Test Case" here
        "General": General_Template
    }
    return templates.get(category)



def collect_messages(user_input, all_messages, debug=False):
    if debug: print(f"User Input = {user_input}")
    if user_input == "":
        return
    response, all_messages = step_process_user_message(user_input, all_messages, debug=False)
    return response, all_messages

def get_template_by_category(category):
    templates = {
        'general': General_Template,
        # Add other categories here
    }
    return templates.get(category)



def step_process_user_message(user_input, all_messages, debug=True):
    step_0_reasoning = f"{delimiter} User input received: '{user_input}'"
    category = identify_category(user_input)
    step_1_reasoning = f"{delimiter} Identified category: {category}"
    template = select_template(category)
    step_2_reasoning = f"{delimiter} Selected template: {template}"
    response = execute_template(template, all_messages + [{'role': 'user', 'content': user_input}])
    step_3_reasoning = f"{delimiter} Generated response to user question: {response}"
    all_messages = all_messages + [{'role': 'user', 'content': user_input}]

    # This is the list where you will store your steps
    steps = []
    response_to_user = response

    # And this is how you add a step to the list
    steps.append(("step_0", step_0_reasoning))
    steps.append(("step_1", step_1_reasoning))
    steps.append(("step_2", step_2_reasoning))
    steps.append(("step_3", step_3_reasoning))

    # When all steps have been added to the list, you can convert it to a dictionary like this:
    response_json = dict(steps)
    response_json["response_to_user"] = f"{delimiter} {response_to_user}"

    return response_json, all_messages



print ("Welcome to the Business Analyst with GPT-3.5-turbo (GPTBA)!")
print ("GPTBA is a chatbot that can help you with your Business Analyst tasks.")
all_messages = []

while True:
    user_input = input("Enter your message: ")
    if user_input.lower() == 'quit':
        break
    response, all_messages = collect_messages(user_input, all_messages)
    print("Assistant: ", response)
    for message in all_messages:
        print(f"{message['role']}: {message['content']}")
