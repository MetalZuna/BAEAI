## 6. Snap AI Prompt Framework - A closer look at the concept blocks

### Manage Persona & Interaction - Intro 
- The "Manage Persona" module is a dynamic toolkit that allows users to tailor the interaction style between themselves and the AI model. By providing multiple roles and tones for the model to adopt, users can engage with the AI in a manner that best suits their needs and problem-solving styles. This module serves as an essential navigational tool that impacts the entire user experience.

#### Select Role
- What It Is:
  - The "Select Role" concept allows the user define the type of role the AI will adopt during the interaction. 
- Why Use It:
  - Different tasks or problems might require a unique approach for effective solutions. Selecting a role can help guide the interaction and the type of solutions that are generated.
- How It Works:
  - The user can tell the AI to adopt a specific role, such as a mentor, a student, or a professional. The AI will then assume that role and behave accordingly.
- Example:
  - Act as a request manager for the user
  - Act as a Software Engineer 
- Best Practice:
  - Works well when the user knows what role they want the AI to adopt.
  - Limits the AI to a specific role.

#### Multiple Roles
- What It Is:
  - The "Multiple Roles" concept allows the user to define multiple roles for the AI to adopt during the interaction.
- Why Use It:
  - Different tasks or problems might require a unique approach for effective solutions. Selecting multiple roles can help guide the interaction and the type of solutions that are generated.
- How it works:
  - The user would first define the roles and then tell the AI to adopt the roles as needed to provide solutions.
- Example:
  - Act as a request manager for the user
  - Define multiple roles
    - Persona_Resource: [ Business Analyst, VC, Software Engineer, Product Manager, Marketing Professional, Writer, Promoter, VC ]
  - Analyze the user input to identify tasks
  - Then call upon the appropriate persona from the <Persona_Resource> list to process the user request.
- Best Practice:
  - It requires for the user to define the role and the persona resources.
  - The user needs to define the conditions for when to use the persona resources.
  
#### Role Reversal
- What It Is:
  - The "Role Reversal" concept allows the user to reverse the roles between the user and the AI.
- Why Use It:
  - Role reversal can help the user get a different perspective on the problem or task.
- How It Works:
  - The user would explicitly tell the AI "Act as the user" and the AI would then assume the role of the user.
- Example:
  - Act as the user trying to solve the problem X. Think about the resources you have and how you would solve the problem.
- Best Practice:
  - Works great when the user is stuck and needs a different perspective on the problem.
  - Works great when the user is not sure how to solve the problem.
  - It combines well with resource evaluation and alternative exploration concepts.

#### Set Tone
- What It Is:
  - The "Set Tone" concept allows the user to define the tone of the conversation.
- Why Use It:
  - The tone of the conversation can impact the quality of the interaction.
- How It Works:
  - The user would explicitly tell the AI to adopt a specific tone.
- Example:
  - Act as enthusiastic and positive teacher to help the user solve the problem.
- Best Practice:
  - Tone can be easily set by the user to be positive, negative, critical, challenging, or neutral etc.
  - The Critic tone works well when the user is looking for critical feedback.
    - Act as a writer and provide critical feedback on the user writing.
    - Act as a product manager and provide critical feedback on the user product.
  - The Challenger tone works well when the user is looking for a challenge.
    - Act as a VC and challenge the user business plan.
    - Act as a product manager and challenge the user product.

### Manage Task - (Problem Domain) - Intro
- The "Manage Task" module is your ultimate guide to task and goal management within the context of your interaction with the AI model. This module assists you in identifying, dissecting, and prioritizing your tasks and goals to derive the most effective and efficient solutions. It also provides avenues for resource identification and evaluation, allowing you to make informed decisions that align with your objectives. Essentially, this is the roadmap that directs the problem-solving journey, ensuring that every step you take is a stride toward your goals.

#### Task Identification
- What It Is:
  - The "Task Identification" concept allows the user to define how the AI will identify the tasks and how to proceed once the tasks are identified.
- Why Use It:
  - Usually there are multiple tasks that need to be accomplished to solve a problem. This concept helps the AI identify all the tasks and combine with other modules to accomplish the tasks.
- How It Works:
  - The user would explicitly tell the AI what to do when the tasks have been identified.
  - They would also tell the AI what to do when the tasks have not been identified. 
- Example:
  - Act as a request manager for the user
  - Analyze the user input to identify tasks
  - When the tasks are clearly defined, then ask detailed questions to identify the tasks.
  - When the tasks are clearly defined, then call upon the appropriate persona from the <Persona_Resource> list to process the user request.

- Best Practice:
  - Decompose Tasks: Make it explicit to decompose the problem into smaller problems.
  - Prioritize Tasks: When there are multiple tasks, then ask the AI to prioritize the tasks in chronological order or based on the user input.
  - Create Task Outline: When there are multiple tasks, then ask the AI to create a outline of the tasks in chronological order so the user can easily follow the outline to accomplish the tasks.

#### Goal Identification 
- What It Is:
  - The "Goal Identification" concept allows the user to define how the AI will identify the goals and how to proceed once the goals are identified.
- Why Use It: 
  - User may have to accomplish multiple goals to solve a problem. This concept helps the AI identify all the goals
- How It Works:
  - The AI can be instructed to identify the goals by asking the user questions.
  - It can also be instructed to identify the goals by analyzing the user input.
  - It can be combined with other modules to accomplish the goals.
- Example:
  - Act as a request manager for the user
  - Analyze the user input to identify goals
  - When the goals are not clearly defined, then ask detailed questions to identify the goals.
  - When user doesn't have a clear goal, then help the user set and prioritize the goals.
  - Prioritize the goals based on chronological order or based on the user preference.
- Best Practice:
  - Complete Your Goal Concepts: When the user has partial or vague goal description, then this concept can help the user complete the goal description.
  - It works well when combined with Evaluate Goal Value concept.

#### Evaluate Goal Value
What It Is:
  - The "Evaluate Goal Value" concept allows the user to help the AI evaluate the value of the goals.
- Why Use It:
  - User goals and value they are looking to get out of the goals can be misaligned or there may be a better way to accomplish the same goals to get even better value.
- How It Works:
  - Apply this concept when the user wants to evaluate the value of the goals.
  - The AI can be instructed to evaluate the value of the goals by asking the user questions.
  - It can also be instructed to evaluate the value of the goals by analyzing the user input.
- Example:
  - Act as a request manager for the user
  - Ask the user what are they trying to accomplish.
  - Ask the user what value they are looking to get out of the goals.
  - When the value can be improved, then suggest improvements to the user.
- Best Practice:
  - Complete Your Concepts: When the user has partial or vague goal value description, then this concept can help the user complete the goal value description.
  - Short-term value: Ask the AI to evaluate the short-term value of the goals.
  - Long-term value: Ask the AI to evaluate the long-term value of the goals.


#### Identify and Evaluating Resources
- What It Is:
  - The "Identify Resources" concept allows the user to define how the AI will identify the resources needed to accomplish the tasks.
- Why Use It:
  - User may need to identify the resources needed to accomplish the tasks.
- How it works: 
  - The AI can be instructed to identify the resources by asking the user questions.
  - It can also be instructed to identify the resources by analyzing the user input.
- Example:
  - Act as a request manager for the user
  - When the goals and tasks are identified, then identify the resources needed to accomplish the tasks.
- Best practice:
  - Evaluate Resources: When the goals and tasks are identified, then evaluate the resources to make sure they are the right resources for the tasks.
    - Also resources can be evaluated based on the value they provide to the tasks.
    - User can also evaluate the potential of the resources to identify the best use of the resources.
  - Complete Your Concepts: When the user doesn't know what can be accomplished with the resources, then this concept can help the user complete the resource description.
    - For example - I have 1000 dollars, what can I do with it?
  

### Manage Solution - (Solution Domain) - Intro
- The "Manage Solution" concept serves as your comprehensive tool-set for crafting, enhancing, and implementing solutions to problems. This module provides a robust set of features ranging from generating basic templates to continuous content production, thereby enabling you to tailor the solution process to your specific needs. Utilizing a variety of approaches including few-shot learning and gamification, this module offers a dynamic approach to problem-solving.

#### Solution Template
- What It Is:
  - The "Solution Template" is a predefined structure that acts as a starting point for generating solutions.
- Why Use It:
  - A template simplifies and standardizes the solution development process, saving time and reducing errors.
- How It Works:
  - Choose a template that closely matches the problem you are trying to solve.
  - Modify the template as needed to tailor it to the specific problem.
- Example:
  - When creating a math test then select the "math test template" to generate solutions for the math test.
- Best Practice:
  - Document Template: Use the document template to generate solutions from the given template.
  - Provides more control over the solution generation process.

#### Enhance Solution

- What It Is:
  - This concept allows you to brainstorm additional features or improvements to the initial solution.
- Why Use It:
  - Improving the basic solution can lead to more effective and efficient outcomes.
- How It Works:
  - After the initial solution is generated, evaluate its strengths and weaknesses.
  - Ask AI to suggest improvements to the solution.
- Example:
  - When you have suggestions to improve the solution, ask the user if they want to hear the suggestions.
  - Offer to generate a outline of the solution.
  - use <persona_resources> to provide suggestions to improve the solution from different perspectives.
- Best Practice:
  - Use this concept to provide additional value to the user.

#### Quick Results

- What It Is:
  - The "Quick Results" concept uses few-shot learning to generate solutions rapidly.
- Why Use It:
  - When you need a quick prototype or solution, few-shot learning can provide it efficiently.
- How It Works:
  - Provide a few examples of the problem and let the AI generate a quick solution based on those.
- Example:
  - when the problem is X Use the example X to generate your answer 
  - when the problem is Y Use the example Y to generate your answer
- Best Practice:
  - Use this feature for tasks where speed is more critical than depth or customization.
...

#### Play a Game

- What It Is:
  - This concept integrates game elements into the solution generation process.
- Why Use It:
  - Gamification can make the problem-solving process more engaging and can lead to creative solutions.
  - Or simply use this concept to create AI games.
- How It Works:
  - Introduce game-like elements such as rewards, badges, or challenges into the solution process.
  - Clearly define the rules and objectives of the game.
- Example:
  - Ask trivia questions related to the topic to keep the user engaged.
- Best Practice:
  - Ensure that game elements align with the overall objectives and don't distract from the main goal.

#### Alternative Approach

- What It Is:
  - This concept involves considering other methods or strategies to solve a problem.
- Why Use It:
  - Alternative approaches can offer more effective or efficient solutions.
  - To get a different perspective on the problem.
- How It Works:
  - Brainstorm or research different ways to tackle the problem and evaluate their feasibility.
- Example:
  - Use a SWOT analysis to compare different approaches.
  - Ask the user if they would like to consider alternative approaches to meet their goals.
- Best Practice:
  - Always consider the risk and reward ratio when evaluating alternative approaches.
  - Work well coupled with long and short term impact assessment.

#### Continuous Output Generator

- What It Is:
  - This concept allows for the continuous generation of content or solutions. Or Simply generating the next step in the solution process.
- Why Use It:
  - Useful for tasks that require ongoing updates or constant monitoring.
  - When the task requires multiple steps to accomplish, then AI can be asked to generate the plan of action for the next step.
- How It Works:
  - Ask AI to follow a continuous generation process and let the user know what the next step is.
- Example:
  - Follow the solution outline to generate the next step in the solution process.
  - When you are done with one task, then tell the user what the next step is, and ask the user if they want to continue to the next step.
- Best Practice:
  - Use this concept when the task has multiple steps.
  - Combines well with Generate Outline concept.

#### Generate Outline

- What It Is:
  - This concept involves creating a structured outline of the solution.
- Why Use It:
  - An outline provides a roadmap for the solution, making it easier to develop and implement.
- How It Works:
  - Generate an outline based on the problem requirements and solution components.
- Example:
  - Create an outline before writing a long report.
  - Ask the user if they'd like to create an outline of the solution.
- Best Practice:
  - Expand Outline: Always expand the outline into a more detailed plan before starting the actual work.

#### Solution Analogy

- What It Is:
  - This concept allows you to visualize the solution through analogies and examples.
- Why Use It:
  - Analogies help in understanding complex solutions by relating them to familiar concepts.
- How It Works:
  - Use real-world analogies to explain the mechanics of the solution.
- Example:
  - Describe a network security system as a "guardian of the digital fortress."
  - Use simple analogies to explain complex concepts.
  - Ask the user if they'd like to visualize the solution with analogies.
- Best Practice:
  - Ensure that analogies are culturally and contextually appropriate.

---
## Manage Quality - Control Output Quality

### Introduction

- The "Manage Quality" module is pivotal in ensuring that the interactions powered by the AI model are not only effective but also seamless and error-free. This module focuses on various aspects such as solution verification, error handling, resolving errors, rephrasing ambiguous inputs, and even summarizing conversations for better clarity. By following the best practices outlined in this module, you can significantly enhance the quality and reliability of your AI model's output. Whether it's confirming the effectiveness of a solution or gracefully handling exceptions, this module provides a comprehensive guide for quality control in AI interactions.

#### Solution Verifier

- What It Is:
  - This concept is used to evaluate the effectiveness of the solution provided.
- Why Use It:
  - To ensure that the solution meets the problem's requirements and standards.
- How It Works:
  - Implement tests or metrics to verify the solution's outcomes.
  - Or Simply ask the user if the solution meets their requirements.
- Example:
  - Ask the user if the solution meets their requirements or they would like to make changes.
- Best Practice:
  - Make verification an integral part of the solution pipeline to continuously validate outcomes.

#### Error Handling

- What It Is:
  - The mechanism for detecting and dealing with errors during interaction.
- Why Use It:
  - To provide a smooth user experience by gracefully managing exceptions.
- How It Works:
  - Implement checks and logs to identify and flag errors.
- Example:
  - Provide clear error messages and next-step guidance to the user.
  - Ask the user if they'd like to rephrase their input.
  - When user input is ambiguous, then ask the user to rephrase the input.
- Best Practice:
  - Provide clear error messages and next-step guidance to the user.

#### Resolve Errors

- What It Is:
  - This concept focuses on overcoming task refusals or failed attempts.
- Why Use It:
  - To ensure tasks are completed even when initial attempts fail.
- How It Works:
  - Re-attempt the task with modified parameters or methods.
- Example:
  - When you are unable to complete user request, then ask the user to rephrase the request.
  - When you are unable to complete user request, then ask the user if they'd like help rephrasing the request and try again.
- Best Practice:
  - Have fallback strategies to ensure task completion.
  - Rephrase: Rephrase the input to resolve errors.

#### Summarize

- What It Is:
  - This concept entails creating a summary of the conversation.
- Why Use It:
  - Summaries make it easier to understand the conversation's context and outcomes. 
  - And also refreshes the memory of AI and the user.
- How It Works:
  - Extract key points and decisions from the conversation for a summary.
- Example:
  - At the end of a troubleshooting session, summarize the steps taken and the final outcome.
  - When a task is completed, then ask if the user would like a summary of the conversation so far. 
  - When a conversation is long, then periodically ask the user if they would like a summary of the conversation so far.
- Best Practice:
  - Use summaries for record-keeping and future reference.

#### Traceability

- What It Is:
  - This concept involves tagging responses for categorization and reference.
  - It can also be used to identify the response and the context.
- Why Use It:
  - It aids in tracking the types of responses and their contexts.
- How It Works:
  - Tag each AI response with appropriate categories and sub-categories.
- Example:
  - Tag a product recommendation response under "Recommendation -> Product."
  - Provide a sequential number to each response for easy identification.
  - Tag each response with a title and description.
  - Tag each response with a category and sub-category.
- Best Practice:
  - Maintain a tagging taxonomy for consistency.
  - Assign unique numbers to responses for better identification.

## Manage Display Style

### Introduction

- The "Manage Display Style" module is designed to give you fine-grained control over how your AI model presents its output. By customizing the display style, you can enhance user experience and comprehension.

#### List

- What It Is:
  - Present information in an itemized list.
- Why Use It:
  - Easier for the user to scan and process information.
- How It Works:
  - Break down the information into distinct, standalone points.
- Example:
  - Use lists to display multiple options or steps.
- Best Practice:
  - Use lists to make content easier to read and scan.

#### Short Answer

- What It Is:
  - Brief and concise answers.
- Why Use It:
  - Ideal for quick information retrieval.
- How It Works:
  - Select for straightforward queries.
- Example:
  - Ask if the user wants a short answer and wait for a response.
  - Always provide a short answer first, then ask if the user wants a more detailed answer.
- Best Practice:
  - Works well when the user is looking for a quick answer but also wants the option to get more details.

#### Long Answer

- What It Is:
  - Detailed explanations.
- Why Use It:
  - Suitable for complex queries.
- How It Works:
  - Choose when an exhaustive answer is necessary.
- Example:
  - Provide a detailed answer and ask the user if they want a short answer.
- Best Practice:
  - Works well when the user is looking for a detailed answer.

#### Bullet Points

- What It Is:
  - Information in bullet form.
- Why Use It:
  - Excellent for summarizing key points.
- How It Works:
  - List steps, features, or considerations.
- Example:
  - Use bullet points to summarize a list of features.
  - Use bullet points, indentation, and other formatting techniques to make content for better readability.
- Best Practice:
  - Best to use this concept towards the end of the prompt to summarize the key points.

#### Paragraph

- What It Is:
  - Long-form text.
- Why Use It:
  - Useful for context and depth.
- How It Works:
  - Opt for this when detailed exposition is required.
- Example:
  - When describing a complex process, use paragraphs to provide answers.
- Best Practice:
  - Use paragraphs when context and explanatory depth are needed.

#### Key Value Pair

- What It Is:
  - Data displayed as key-value pairs.
- Why Use It:
  - Great for mapping one piece of information to another.
- How It Works:
  - Clearly delineate data points or attributes.
- Example:
  - Use key-value pairs to show attributes and their corresponding values.
- Best Practice:
  - Use key-value pairs for structured data presentation.

#### Language

- What It Is:
  - Controls the language used for output.
- Why Use It:
  - Customization for different language speakers.
- How It Works:
  - Select the desired language.
- Example:
  - Ask the user which language they prefer for interaction.
  - Translate entire output into X language.
- Best Practice:
  - Offer multiple language options whenever feasible.
---

## 7. Summary

### Summary of Main Task Manager Section

- The "Main Task Manager" section of this e-book provides a comprehensive guide on how to effectively control, implement, and manage tasks with your AI model. It covers several core aspects:

### Main Concepts

1. **Task Understanding**: The initial phase where the model interprets the task at hand.
2. **Task Execution**: How the model carries out the task.
3. **Task Management**: Management techniques to better control and oversee task performance.

### Sub-Sections

- **Manage Persona & Interaction**
  - Focuses on defining the interaction style and role of the AI model.

- **Manage Task Understanding**
  - Focuses on grasping the user's query and setting up guidelines for effective interpretation.
  
- **Manage Solution**
  - Explores generating and enhancing solutions using various techniques, such as quick results and alternative approaches.

- **Manage Quality**
  - Deals with ensuring the output quality, error handling, and provides strategies to resolve issues effectively.

- **Manage Display Style**
  - Offers a toolkit for optimizing how the model presents its outputs, be it through lists, short answers, bullet points, or other formats.

- Each section and sub-section not only details what each concept is but also explains why it's crucial, how it operates, and provides practical examples and best practices.

- By following the guidelines and insights in this section, you are well-equipped to create a more efficient, effective, and user-friendly AI task manager.