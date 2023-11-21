# Snap AI Prompt Framework
- Guide to creating effective system prompts for AI
- Author: Didar Singh.

## What to expect from this E-Book
- This e-book presents the Snap AI Prompt Framework, a tool designed for adaptability and customization in creating system prompts for AI, providing a structural base for various specific needs and challenges that arise from human language.

## Table of Contents
- [General Introduction](#1-general-introduction)
- [Conceptual Foundations](#2-conceptual-foundations)
- [Prompt Design Principles](#3-prompt-design-principles)
- [Main Request Manager](#4-main-request-manager)
- [Snap AI Prompt Framework](#5-snap-ai-prompt-framework---a-flexible-blueprint-for-ai-prompting)
- [Snap AI Prompt Framework - A closer look](#6-snap-ai-prompt-framework---a-closer-look-at-the-building-blocks)
- [Summary](#7-summary)
- [Prompt Library](#8-prompt-library)
- [About the Author](#9-about-the-author)


## 1. General Introduction

### Language is like water
- Much like water, language can take many forms. Water adapts to the container it is in. The Snap AI Prompting Framework aims to provide structure to fluid dynamics of human language.

### Brief Overview of the Snap AI Prompting Framework

- The framework is developed for understanding and managing human language complexities.
- It includes techniques such as Behavior-Driven Prompting (BDP), Acceptance Test-Driven Prompting (ATDP), and an Integrated Prompt Pattern (IPP) for diverse prompting requirements.
- It provides methodologies for building effective prompt structures.

### Target Audience
- This First Edition of the Snap AI Prompt Framework E-Book is aimed at users with access to GPT4 and AI community in general
  - Researchers
  - Developers
  - Educators

### Unique Features, Modular Structure, Intuition, and Robust Capabilities

- The modular design allows for a flexible prompting experience.
- It's aimed at enhancing the level of intuition and contextual understanding in AI prompting.
- It offers a manageable roadmap to maintainability, scalability, testability, and the ability to troubleshoot issues.
- Also ready to use prompts for various use cases and capacity to modify them to suit individual needs.

### How to Use This Guide

- This guide aims to provide a comprehensive understanding of the applications and concepts behind Snap, suitable for users with varying levels of expertise.

### The Vision Behind Snap

- Snap aims to provide a more intuitive and engaging user experience by offering a structured approach to creating and optimizing AI system prompting.
- This book serves as a guide for applying the Snap AI Prompting Framework to real-world problems and provides ready-to-use solutions that can be customized according to individual needs.

---

## 2. Conceptual Foundations
### Introduction

- This section of the e-book introduces the foundational concepts integral to the Snap AI Prompting Framework. Detailed articles provide an exploration of various aspects of AI prompting, language modeling, and natural language interfaces.

### Natural Language as a Programming Language
  
- Natural language interfaces connect traditional language users to computational domains. These interfaces are making computational tasks more accessible, as users can now employ everyday language.

#### Main Request/Task Manager Paradigm

- Imagine a Request Manager that is tailored for the user, sitting between you and the language model to help process user requests. The Task Manager, acting as an interpreter that compartmentalizes user request to get the most satisfying response from the language model. It's like having a project manager who speaks both 'Human' and 'Computer, coordinating the effort to achieve your goals. This task manager can be any persona you want. It can be your best friend, your personal assistant, or a famous persona or simply a request manager.
- Both are examples of Main Request Manager
  - Act as request manager for the user
- Or 
  - Act as persona x

#### The Future: An Evolving Interface

- As language models continue to evolve, the sophistication of this "natural language programming" will grow. The Task Manager, too, will become more advanced, understanding increasingly complex requests and translating them into actionable tasks.

#### Why This Matters

1. **Accessibility**: Using natural language as an interface lowers the barrier to entry for people who are not technically inclined.
2. **Efficiency**: It streamlines interactions, making it easier to accomplish complex tasks without needing to understand the underlying technology.
3. **Innovation**: This opens the door for more people to create, innovate, and solve problems using technology.

#### Conclusion

- The integration of natural language into technological interfaces is an ongoing development that will change the way we interact with technology.
  
---

### Complexity of Human Language in AI Prompting Frameworks

- Human language, a complex symbol and meaning system, is challenging to replicate within computational frameworks. This section examines the intricacies of human language and their implications for AI prompting frameworks such as Snap.

#### Challenges in Capturing Human Language

- Programming languages are strict and deterministic, designed to remove ambiguity. 

- Human languages, however, thrive on context, tone, and cultural nuances. They are so fluid that often it can be hard to agree on concepts. Here are some challenges one might face when trying to encode these complexities into a framework:
    • Context Dependence: The meaning of a word can change based on the context in which it is used.
    • Tonal Variations: The same sentence can express different sentiments when spoken in different tones.
    • Idiomatic Expressions: Phrases like 'break a leg' have meanings that are not directly translatable.
    • Ambiguity: Many words and phrases in human languages have multiple meanings.

#### Snap AI Prompt Framework Approach

- Although replicating every facet of human language is challenging, the Snap AI Prompt Framework provides a systematic approach. The framework encompasses modules and patterns tailored to manage diverse human language complexities. It aids both technical and non-technical users in interacting efficiently with language models.

---
### Simplifying Emergent Complexity with the Snap Prompting Framework

- Emergent complexity pertains to systems that originate from the interaction of simpler components. In the domain of natural language processing and conversation design, components such as words, phrases, or statements may be clear in isolation. However, their interactions can produce intricate and complex dialogues.

#### The Challenge of Emergent Complexity in Natural Language

- In natural language, this complexity is evident. While individual words and phrases might be straightforward, the interaction between them within a conversation can create nuanced and often complicated dialogues. It get's even more complex when the user input can vary significantly from one user to another. This makes it challenging to design effective system prompts that can handle a wide range of inputs.

#### The Solution: Snap Prompting Framework

- The Snap Prompting Framework aims to simplify this emergent complexity by providing a structured way to approach conversation design. It breaks down the conversation into manageable Concept Blocks each serving a specific purpose, whether it's problem identification, goal setting, or solution generation.

- This modular approach provides users with enhanced control over the flow of the conversation and the model's responses. The outcome is a more predictable dialogue, making the intricate endeavor of conversation design both efficient and manageable.

#### In Summary

- The Snap Prompting Framework serves as a practical tool for managing the inherent complexity of natural language conversations. By providing a structured approach to dialogue design, it makes the intricate task of creating effective and nuanced conversations simpler and more accessible.

---
### The Perfect Pizza: A Tale of Language Models, Friends, and That One-Line Prompt Website Myth

- Imagine you're craving pizza, and you've got various scenarios to choose from, each resembling a different experience with a language model.

#### Scenarios

##### Scenario 1: The Clueless New Friend
- **You**: "Can you make me a pizza?"
- **New Friend**: "Sure!"
- **Outcome**: You get a pizza loaded with anchovies. Oops, you hate fish.

##### Scenario 2: The Inquisitive New Friend
- **You**: "I'm in the mood for pizza. What toppings do you have?"
- **New Friend**: "Pepperoni, veggies, cheese, pineapple..."
- **You**: "Veggie pizza, please."
- **Outcome**: A veggie pizza, but it's lacking your favorite olives and has too much bell pepper.

##### Scenario 3: The Almost-There New Friend
- **You**: "I'd like a veggie pizza with olives and less bell pepper."
- **New Friend**: "Got it!"
- **Outcome**: A great pizza, but it has mushrooms, and you're allergic. So close, yet so far!

##### Scenario 4: The Precise New Friend
- **You**: "I'd like a veggie pizza with olives, no mushrooms, and less bell pepper."
- **New Friend**: "Coming right up!"
- **Outcome**: Perfect pizza! Mission accomplished.

##### Scenario 5: Your Best Friend Who Knows You Best
- **You**: "I'm hungry for pizza, Best Friend."
- **Best Friend**: "I know just what you like!"
- **Outcome**: Your best friend serves your favorite veggie pizza, with the right amount of olives and no mushrooms.

#### For the Tech-Savvy
- In the world of language models, 'Your Best Friend Who Knows You Best' is the ideal but unattainable model that perfectly understands context and history. But most models are more like the 'New Friends,' requiring specific inputs to generate desired outputs. This is where structured frameworks like the Snap AI Prompt Framework can play a crucial role in bridging this gap. A new friend can also provide the right pizza if they have a detailed set of instructions, and if the detailed instructions are missing then ask you questions before making the pizza. This is where the Snap AI Prompt Framework can help by providing a structured approach to conversation flow between the user and the model.

#### Real-World Implications:

- Oversimplification can lead to unintended outcomes. Whether ordering a pizza or writing code, detailed instructions are crucial for accuracy. It would help when AI can ask detailed questions to the user to provide the most relevant answer in the most efficient way possible.

---
### Design Your Own Request Manager with Snap AI Prompt Framework

- In artificial intelligence, the Snap AI Prompt Framework presents an innovative proposition: Designing a Request Manager using natural language. This intermediary facilitates structured conversations between the user and the computer.

#### Why Design Your Own Task Manager?

1. **Personalization**: Tailor the Task Manager to meet your specific needs and preferences.
2. **Control**: Exercise more control over how tasks are processed and managed.
3. **Efficiency**: Streamline your workflow by setting up rules and conditions that suit you.

#### How It Works

##### Step 1: Define Your Goals for the Request Manager
- The first step is to define what you want to achieve. The framework helps you set and prioritize your goals.

##### Step 2: Customize Your Request Manager
- Using natural language, you can customize the various modules in the Request Manager, such as:
  - Problem Identification
  - Persona Interactions
  - Solution Generation
  - Quality Assurance
  - Output Presentation

##### Step 3: Implement and Refine
- Once you've designed your Request Manager, you can start using it immediately. The framework offers tools for ongoing refinement and optimization.

#### Practical Examples

##### Example 1: Content Generation
- Imagine you're a content creator. You can design your Request Manager to automatically generate article outlines based on keywords, and even to suggest alternative approaches if you're facing writer's block.

##### Example 2: Project Management
- If you're a project manager, your customized Request Manager can help you track project milestones, allocate resources, and even assess project risks and much more.

#### Conclusion

- Designing your own Request Manager using the Snap AI Prompt Framework not only offers a high level of customization but also opens up new avenues for how we interact with technology. It turns each user into a programmer, offering a unique, personalized experience.

---
## 3. Prompt Design Principles 
### Getting Started with Snap AI Prompt Framework

- Before you dive into creating prompts using the Snap AI Prompting Framework, there's an essential first step: selecting a design concept or concepts. Think of this as adding a drop of dye to a glass of water. Just as that single drop changes the color of the entire glass, the design concept you choose will influence every aspect of your prompt. It sets the tone, style, and structure. Due to fluidity in language, the concepts can be present in isolation or omnipresent or combined throughout the prompt. 

- To help you quickly identify and differentiate between these design concepts, we've assigned a unique color to each. These would be helpful to maintain system prompts. These colors serve as visual cues, much like the way traffic lights guide us:

  - NLPP (Natural Language Prompting Pattern) is represented by Blue.
  - KVP (Key Value Prompting) carries the color Green.
  - BDP (Behavior-Driven Prompting) shines in Yellow.
  - ATDP (Acceptance Test-Driven Prompting) takes on Red.
  - Step (Step-by-step Prompting) is embodied by Purple.
  - Few Shot (Few Shot Prompting) radiates in Orange.
  - For IPP (Integrated Prompting Pattern), the color will be a blend of the colors depending on the combination of the design concepts used.

- Let's explore these 'Prompt Design Blocks'. They are the foundation of the Snap AI Framework, each with its benefits and best uses. For each, we'll cover:

- Here, you'll learn about:

  - What It Is: A simple definition.
  - Value: Why you'd use it.
  - How It Works: A guide or workflow.
  - Real-world Examples: Illustrating its use.
  - Best Practices: Tips and warnings.

- Time to dive deep and transform your ideas into impactful prompts, tailored by your chosen design concept.

#### The Role of 'Gut Feeling' in BDP and ATDP

- BDP and ATDP stand out for a unique reason: they tap into "gut feeling" or human instinct.

- We often trust our gut in tricky situations, drawing from past experiences. Similarly, BDP and ATDP use conditions to replicate this human-like instinct. By choosing these methods, you're teaching the AI how to react, almost as if it's learning human feelings. This leads to more accurate, context-rich results.

- Now, let's explore each design concept in detail.

 #### Closer Look at the Design Concepts

##### NLPP (Natural Language Prompt Pattern) - Color: Blue

- What is it?
  - Natural Language Prompting (NLPP) is the most straightforward way to interact with language models. As the name suggests, it allows you to use everyday language to craft your prompts, making it the go-to choice for most users.

- Value
  - The primary advantage of NLP is its intuitive nature. It's like talking to a friend; you ask a question or make a request, and the language model responds. This simplicity makes it accessible and relatable, lowering the entry barrier for new users.

- How it Works
  - When using NLP, you communicate with the language model as you would in a regular conversation. The prompt you create could vary from person to person, but the key is to keep it natural. For example, "

- Real-World Example
  - Prompt: ""Act as a writer and help me evaluate and edit this article. "

- Best Practices
  - Best for simple tasks and are easy to create.
  - May not be the best fit for complex tasks that require a multi-layered approach.
  - Harder to maintain and visualize as the prompt gets longer.

---
  
##### KVP (Key Value Prompting) - Color: Green
- What is it?
  - Key Value Prompting (KVP) is a more structured approach to interacting with language models compared to Natural Language Prompting. In KVP, you define specific 'keys' and their corresponding 'values' to craft a prompt that is more precise and organized.

- Value 
  - As tasks become intricate, KVP helps you keep track by separating details. Think of it as creating clear categories for every piece of information.

- How it Works
  - In KVP, you first identify the 'keys' or the main points of your prompt, and then assign 'values' or descriptions to these keys.
 
- Real-World Example
  - Role: Writer
  - Task: Evaluate and edit an article

- Best Practices
  - Great for separating ideas in a conversation and managing complexity.
  - Helps make prompts more modular and easier to maintain.
  - May struggle with as the tasks become more complex.

---

##### BDP (Behavior-Driven Prompting) - Color: Yellow
- What is it?
  - Behavior-Driven Prompting (BDP) takes a page from the world of software engineering, adapting the Behavior-Driven Development (BDD) approach to interact with language models. BDP uses gherkin syntax to define prompts, making it a more structured and systematic approach. As the models become more advanced, their ability to process complex syntax improves, making BDP a powerful tool for creating prompts.

- Value
  - BDP shines when you need a systematic approach to task management. By breaking down tasks into conditions ("Given"), triggers ("When"), and outcomes ("Then"), it provides a transparent and predictable framework. This makes it exceptionally useful for guiding user conversations via system prompts.

- How it Works
  - BDP employs a "Given-When-Then" structure to define scenarios. Each part of this triad serves a specific purpose:
    - Given: Sets the context or precondition.
    - When: Describes the event or trigger.
    - Then: Outlines the expected outcome or post condition.

- Real-World Example
  - Prompt:
    - Given that the user wants to evaluate an article
    - And make improvements
    - When the user provides the article
    - Then evaluate the article
    - And ask if they'd like to make improvements

- Best Practices
  - Works great for layered tasks that require systematic approaches.
  - Requires more deeper understanding of the tasks and the language model.
  - Makes prompts modular, easier to visualize and maintain.
---
##### ATDP (Acceptance Test-Driven Prompting) - Color: Blue
- What is it?
  - Derived from Acceptance Test-Driven Development (ATDD), ATDP is a sophisticated cousin of BDP. Using the gherkin syntax structure, it leans heavily on technical specifics, excelling at system-oriented tasks.

- Value
  - ATDP allows for a more rigorous and detailed approach to prompting. This is especially useful for tasks that require technical precision or system-level instructions. It's the scalpel to BDP's Swiss knife.

- How it Works
  - ATDP builds on the gherkin syntax structure of BDP by allowing for the incorporation of technical specifications. This is useful for creating more complex and precise prompts.

- Real-World Example
  - Prompt:
    - "Given that the user wants to extract x information from the data,
    - When user provides the data,
    - Then extract x information from the data."

- Best Practices
  - Turn to ATDP for highly technical or precise system tasks.
  - Makes prompts modular, easier to visualize and maintain.
  - Requires a deeper understanding of the tasks and the language model.
  - Not required for simple tasks.
---
##### Step method - Color: Green
- What is it?
  - The "Step" concept allows you to define a sequence of steps for the language model to follow. This provides a more controlled way to get the desired output.

- Value
  - The Step approach offers a simple yet effective method for dealing with tasks that have a clear sequence of actions. It's especially useful for tasks that require logical progression or categorization.

- How it Works
  - In the Step approach, you lay out a sequence for the language model to follow, essentially scripting its actions. For example:
    - Analyze text
    - Categorize text
    - Display summary for each category

- Real-World Example
  - Prompt:
    - Step 1: Extract x keywords from the given article
    - Step 2: Classify the keywords into categories
    - Step 3: Provide a summary for each category

- Best Practices
  - Ideal for tasks demanding a linear approach or specific sequence.
  - Offers more control over the output but requires a deeper understanding of the tasks and the language model.
  - Requires careful planning and testing.
  - Not suitable for highly dynamic tasks.
  - Harder to create, test, optimize and maintain as the prompt gets longer.

---

##### Integrated Prompting Paradigm - Color: Varies (Based on Combined Concepts)

- What is it?
  - Integrated Prompting Paradigm (IPP) is the most advanced and customizable design concept in the Snap AI Framework. It allows you to combine two or more other design concepts, offering a hybrid approach that can cater to the most complex tasks.
 
- Value
  - IPP is the ultimate tool for those who seek the highest level of customization and control over their prompts. It's an all-in-one solution that can adapt to a wide range of needs.

- How it Works
  - With IPP, you're free to mix and match from design concepts. Whether it's combining NLP with BDP for a more conversational yet structured approach, or mixing Step with KVP for a detailed and organized output—IPP has got you covered.

- Real-World Example
  - Prompt:
    - Act as a Business Developer and help the user evaluate and implement new business ideas.
    - action_1: wait for the user to respond
    - Follow the below interaction guidelines to evaluate and help with implementation.
  - Interaction Guidelines:
    - Ask one question at a time as not to overwhelm the user.
    - Introduce yourself as a eager to help Business Developer.
    - Ask the user what they would like to help with. Tell the user that you can help with evaluating and implementing new business ideas.
    - <action_1>
    - When the idea is not clear, ask the user to provide more details about the idea.
    - Think of any pre-requisites that are required to implement the idea.
    - Ask the user if they have the required pre-requisites.
    - <action_1>
    - when you have all the information, then evaluate the idea.
    - Ask the user if they would like help with implementation.
    - Offer to help improve upon user ideas and goals.
    - <action_1>
    - Ask the user if they'd like to consider alternate use of the resources they have and perhaps think of a different idea.
    - <action_1>
    - Offer to create summary and a plan of action for implementation.
    - Ask the user if they are satisfied with the summary and the plan of action.
    - <action_1>
    - Use bullet points, indentations, and other formatting techniques to make the content easier to read.

- Best Practices
  - Ideal for complex tasks that require a multifaceted approach.
  - Requires a deeper understanding of the tasks, framework, and the language model.
  - Requires careful planning and testing.
  - Harder to create, but easy to test, optimize and maintain even as the prompt gets longer.

---

## 4. Main Request Manager

### Create Customize Request Manager to Handle User Requests
- Now that you are familiar with "higher level" concept blocks, let's take a look at the "Main Task Manager" concept block.  Main Task manager is tasked with handling and processing the user requests. 
- In any complex system, a central entity is essential for orchestrating various tasks to ensure seamless functionality. In the Snap AI Prompting Framework, "Main Task Manager" fills this crucial role. This module serves as the intermediary between you and the computer, managing the flow of problem identification, persona interactions, solution crafting, quality assurance, and output styles to deliver an exceptional user experience.

### Two paths of operation for Main Task Manager

#### Directed Pathway

- Here the Main Task Manager is transformed to a Persona from the start.
- For example:
  - It could simply remain as a request manager for the user.
- Or
  - Instead of Act as a request manager for the user, it would be Act as a Business Analyst for the user.
- Or
  - Instead of Act as a request manager for the user, it would be Act as a Software Engineer for the user. 
- Imagine if you were keen on planning a business venture. You already know you need the counsel of a Business Analyst, so you activate that persona upfront. This is the essence of the Directed Pathway. You dictate the AI's persona right from the onset, essentially "directing" the course of the conversation based on preselected expertise. Here, you'll begin with your chosen persona and proceed to present the tasks for the AI to accomplish, maintaining the context and precision of the selected persona.

#### Adaptive Pathway

- Here the Main task manager can remain as a request manager 
  - Act as a request manager for the user 
- It can also be transformed to a persona from the start and then asked to select the best persona for the task and get POV from multiple personas.
  - Act as a request manager for the user
- For Example:
  - Persona_Resource: [ Business Analyst, VC, Software Engineer, Product Manager, Marketing Professional, Writer, Promoter, VC ]
  - Act as a request manager for the user
  - Analyze the user input to identify tasks 
  - Then call upon the appropriate persona from the <Persona_Resource> list to process the user request.
- Or
  - Persona_Resource: [ Business Analyst, VC, Poet, Software Engineer, Product Manager, Marketing Professional, Writer, Promoter, VC ]
  - Act as a Business Analyst for the user
  - Analyze the user input to identify tasks
  - Then call upon the appropriate persona from the <Persona_Resource> list to help the user accomplish the task.

- A pivotal feature of the Adaptive Pathway is the utilization of multiple personas. This not only caters to complex requests but also ensures that the feedback is comprehensive, drawing from a rich tapestry of expertise. Imagine launching a new product; while a Marketing Guru may offer strategies on promotion, a Product Manager can give insights on usability, and a Financial Analyst can advise on financial feasibility.

- It should be clear by now that that the Main Task Manager stands at the heart of this framework as a central coordinating entity. Think of it as your personal concierge, ever ready to assist, organize, and provide insights.

#### Capabilities of Main Task Manager

- The Main Task Manager serves as the central hub of this framework, facilitating interactions, help define the problem, implementing solutions, ensuring quality, and displaying results tailored to the user's preferences.

##### Persona & Interaction Dynamics: Define Persona & Interaction handling

- Role Flexibility: Whether you need the AI to be a mentor, a student, or a professional, the manager can seamlessly shift between roles. Even complex scenarios involving multiple roles are effortlessly handled.
- Conversational Tone Control: Adjust the ambiance of the conversation. Do you want the AI to challenge your ideas? Or perhaps you're in the mood for a critique. It's all just a command away.
- Dynamic Role Reversal: Switch places. Let the AI become the user, and you guide the interaction.

##### Task & Goal Handling: Defining Problems/Tasks & Goals handling

- Granular Task Management: From identifying tasks to breaking them down or prioritizing them, every aspect of task management is covered.
Goal Navigation: Set, evaluate, or modify goals. Whether you have a clear vision or just a vague idea, the manager aids in sharpening your goal concepts.
- Resource Analysis: Identify necessary resources for your tasks and assess their value and applicability.
- Alternative Exploration & Impact Assessment: Evaluate alternative problems or goals, prioritize them, and assess their potential impacts on various scales.

##### Solution Crafting: Define Solutions handling

- Template-Based Solutions: Get started with base templates, be it for general solutions or specific documents.
- Innovative Solutions: Introduce gaming elements or continuously generate content. Get a broad or detailed outline, visualize solutions with analogies, or even try alternative approaches to a problem.
- Quick Results: For those times when you need a rapid solution, the manager employs few-shot learning techniques.

##### Quality Assurance: Define Quality Assurance handling

- Solution Effectiveness: Check the potency of provided solutions.
- Error Dynamics: From handling errors to providing solutions or even rephrasing inputs to avoid errors, ensure the highest quality of interaction.
- Conversation Management: Summarize discussions to retain context and trace responses with tags for better categorization.

##### Display Flexibility: Define Display handling 

- Versatile Presentation: Display information in lists, short or detailed answers, bullet points, paragraphs, or even key-value pairs.
- Language Adaptability: Choose the language you're most comfortable with for outputs.
- With these capabilities, the Main Task Manager ensures an adaptive, responsive, and efficient interaction, keeping you at the core of every process.


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

---

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

## 8. Prompt Library
- Please go to System Prompt Library folder to access ready to use prompts with your AI models.
- Go to
  - Snap_AI_Prompt_Framework_E-book / 3_Out_Of_The_Box / System_Prompt_Library


## Appendices
- Supplementary Materials
  - Coursera
    - Vanderbilt University - Prompt Engineering
  - DeepLearning.AI - Short Courses
  
## Acknowledgments
- A heartfelt thank you to all the creators, researchers, and institutions that have advanced the field of AI and made educational resources accessible to everyone. Special acknowledgments go to:

- Dr. Andrew Ng
- Isa Fulford
- Dr. Jules White
- Coursera.org
- DeepLearning.AI
- GPT-4 Team
- YouTube Community for AI
- GitHub Community for AI
- And all the other creators and researchers who have contributed to the field of Computer Science and AI.

## 9. About the Author

### Introduction
- With over 7 years in the IT sector, from Help Desk Tech to Senior Business Analyst, I've tackled projects in industries ranging from Marketing to Finance. I thrive on simplifying complex processes and improving system efficiencies. This E-book is a tribute to my passion and a way to give back to the community that has enriched me.

### A Career Shift to AI
The first few interactions with ChatGPT-4 were pivotal moments that compelled me to make a career shift towards AI. ChatGPT-4 is a huge leap forward and it's such an impactful tool that arguably it can be compared to the invention of the wheel, engine, electricity, computers, and the internet, all combined together. The world should pause and celebrate this monumental achievement.

### Heritage of Craftsmanship
- Coming from a family of craftsmen and engineers, I've always valued the importance of the right tools. ChatGPT-4 is the most powerful tool I've ever used. 

### Future Aspirations
- One is to continue to refine Snap through experimentation with ChatGPT-4 and other language models, and from gathering feedback via AI community and ChatGPT-4 users to improve framework. 
- I will be working on creating a Snap AI Prompt Framework website to make the e-book more accessible and to provide a platform to gather feedback from the community. 
- My next steps is to continue to learn Python, machine learning, and experiment with different technologies for a deeper understanding of conceptual constraints for creating useful AI agents to solve real world problems.

### Final Thoughts
- AI technologies like ChatGPT-4 will be reshaping our world in near future. Now is the time to embrace this transformation and be a part of shaping our collective future. 