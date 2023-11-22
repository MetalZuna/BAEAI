## 5. Snap AI Prompt Framework - A Flexible Blueprint for AI Prompting

### Manage Persona & Interaction - Clearly define the behavior of the model on how to interact with the user.
- **Select Role**: Select the role the model will take.
  - **Multiple Roles**: Select multiple roles for the model.
- **Role Reversal**: Reverse the roles between user and model for interaction.
- **Set Tone**: Set the tone of conversation.
    - **The Challenger**: Challenge user inputs and ideas.
    - **Critic**: Critically evaluate solutions and ideas.



### Manage Task: (Problem Domain) - Clearly define the behavior of the model on how to handle the user request.
- **Task Identification**: Help user identify tasks.
  - **Decompose Task**: Break down the problem into smaller tasks.
  - **Prioritize Task**: Help user prioritize tasks.
    - **Create Task outline**: Create a list of tasks.
- **Goal Identification**: Help user set goals.
    - **Complete Your Goal Concepts**: User has partial and or vague goal description.
- **Evaluate Outcome/Goal Value**: Help user identify goal value.
    - **Complete Your Concepts**: User has partial or no goal value description.
    - Long-term value
    - Short-term value
- **Identify Resources**: Help user identify resources needed to accomplish the task.
- - **Evaluate Resources**: Help user evaluate resources.
    - **Complete Your Concepts**: User has partial and or resource description.

- **Explore Alternatives**: 
    - Alternative problems (help set prerequisites).
    - Alternative goals.
    - Help prioritize problems and goals.
- **Assess Impact**: Evaluate the impact of the tasks and goals.
    - Long-term
    - Short-term
    - System-wide impact
    - Localized impact
    - Impact on specific variables.

### Manage Solution - Implement solution to the problem - Clearly define the behavior of the model on what to respond with.

- **Solution Template**: Base template for generating solutions.
  - **Document Template**: Generate a document template.
- **Enhance Solution**: Add value to the generated solution.
- **Quick Results**: Use few-shot learning for rapid problem-solving.
- **Play a Game**: Introduce game elements in solutions.
- **Alternative Approach**: Consider alternative ways to solve a problem.
- **Continuous Output Generator**: Generate endless content or options.
- **Generate Outline**: Generate an outline of the solution.
  - **Expand Outline**: Expand the outline to generate a detailed solution.
- **Solution Analogy**: Visualize the solution with analogies and examples.


### Manage Quality - Control Output Quality - Clearly define the behavior of the model on how check the quality of the interaction.

- **Solution Verifier**: Confirm the effectiveness of the solution.
- **Error Handling**: Handle errors and exceptions. Providing guidance to the user on how to handle errors and exceptions.
- **Resolve Errors**: Break through task refusals.
- **Rephrase**: Rephrase the input to resolve errors.
- **Summarize**: Summarize the conversation. This can help easier to carry on the conversation in a meaningful way for longer duration.
- **Traceability**: Tag responses
  - Category
    - Sub-Category
  - Number


### Manage Display Style - Clearly define the behavior of the model on how to display the output.
- **List**: Itemized information.
- **Short Answer**: Brief and concise answers.
- **Long Answer**: Detailed explanations.
- **Bullet Points**: Points listed in bullet form.
- **Paragraph**: Long-form text.
- **Key Value Pair**: Data displayed as key-value pairs.
- **Language**: Language used for output.
