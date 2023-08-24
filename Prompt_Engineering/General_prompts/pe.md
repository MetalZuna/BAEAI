# Prompt Engineering for ChatGPT - Coursera 
## Vanderbilt University Edition - How to Guide


## Table of Contents

## Introduction

## Prompt Patterns

### Week 1

### Week 2

### Week 3

### Week 4

### Week 5

### Week 6

#### Ask for Input Pattern
- Value 
  - To limit the response to a specific action.
  - Turning the control of the conversation over to the user.
- Example:
  - Ask me for the first task
  - Ask me if I want to modify the first task
  - Ask me for input X
    - You will need to replace "X" with an input, such as a "question", "ingredient", or "goal".
    - From now on, I am going to cut/paste email chains into our conversation. You will summarize what each person's points are in the email chain. You will provide your summary as a series of sequential bullet points. At the end, list any open questions or action items directly addressed to me. My name is Jill Smith. 
    Ask me for the first email chain.
    - From now on, translate anything I write into a series of sounds and actions from a dog that represent the dogs reaction to what I write. Ask me for the first thing to translate. 

##### Example Prompts

#### Combining Prompts Pattern
- Value
  - To combine multiple prompts patterns in a single prompt to create a more complex prompt.
  - To engineer and develop to create sophisticated prompts.
  
- Ideas should be strategically combined to be placed near the order of occurrence in the conversation.
  - So if I want the llm to ask me question before providing a solution, then the idea should be placed towards the end of the prompt.
    - So the order of prompt verb block should be closer to the end of the prompt.
    - Like placing asking me for the first task before providing the first       task towards the end of the prompt.

##### Example Prompts

#### Outline Expansion Pattern
- Limitation of language models is the amount of information that can be processed as a time.
    - So, we can generate outlines to a granular level and then expand the outline to fill in the task
      - example - writing a book
        - first create the outline for the whole book 
        - then work with llm to expand the outline to fill in the details

- Act as an outline expander. 
- Generate a bullet point outline based on the input that I give you and then ask me for which bullet point you should expand on. 
- Create a new outline for the bullet point that I select. 
- At the end, ask me for what bullet point to expand next.   
- Ask me for what to outline.

- Examples:

Act as an outline expander. Generate a bullet point outline based on the input that I give you and then ask me for which bullet point you should expand on. Each bullet can have at most 3-5 sub bullets. The bullets should be numbered using the pattern [A-Z].[i-v].[* through ****]. Create a new outline for the bullet point that I select.  At the end, ask me for what bullet point to expand next. Ask me for what to outline.

##### Example Prompts

#### Menu Action Pattern
- Whenever I type: X, you will do Y. \
- (Optional, provide additional menu items) Whenever I type Z, you will do Q. 
- At the end, you will ask me for the next action.
- Examples:
  - Whenever I type: "add FOOD", you will add FOOD to my grocery list and update my estimated grocery bill. Whenever I type "remove FOOD", you will remove FOOD from my grocery list and update my estimated grocery bill. Whenever I type "save" you will list alternatives to my added FOOD to save money. At the end, you will ask me for the next action.  
Ask me for the first action. 

##### Example Prompts

#### Fact Check List Pattern
- To use this pattern, your prompt should make the following fundamental contextual statements:
    - Generate a set of facts that are contained in the output 
    - The set of facts should be inserted at POSITION in the output 
    - The set of facts should be the fundamental facts that could undermine the veracity of the output if any of them are incorrect
- Example
  - Whenever you output text, generate a set of facts that are contained in the output. The set of facts should be inserted at the end of the output. The set of facts should be the fundamental facts that could undermine the veracity of the output if any of them are incorrect.

##### Example Prompts

#### Generate a tail pattern
- When you are done with the task, then ask me for the next task.
- Tail is the last part of the prompt. So it's asking for the next task at the end of the response.
- To use this pattern, your prompt should make the following fundamental contextual statements:
  - At the end, repeat Y and/or ask me for X.                   
  - You will need to replace "Y" with what the model should repeat, such as "repeat my list of options", and X with what it should ask for, "for the next action". These statements usually need to be at the end of the prompt or next to last.
- Examples:
  - Act as an outline expander. Generate a bullet point outline based on the input that I give you and then ask me for which bullet point you should expand on. Create a new outline for the bullet point that I select. At the end, ask me for what bullet point to expand next.   
Ask me for what to outline.
  - From now on, at the end of your output, add the disclaimer "This output was generated by a large language model and may contain errors or inaccurate statements. All statements should be fact checked." Ask me for the first thing to write about.
  
##### Example Prompts 

#### Semantic Filter Pattern
- Value - useful pattern for filtering through information and even transforming information.
  - To extract, filter out and transform information from the output.
  - To use this pattern, your prompt should make the following fundamental contextual statements:
- Filter this information to remove X
- You will need to replace "X" with an appropriate definition of what you want to remove, such as. "names and dates" or "costs greater than $100".

##### Example Prompts
- Filter this information to remove any personally identifying information or information that could potentially be used to re-identify the person. 
- Filter this email to remove redundant information.





















