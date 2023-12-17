## 3. Prompt Design Principles 
### Getting Started with Snap AI Prompt Framework

- Before you dive into creating prompts using the Snap AI Prompting Framework, there's an essential first step: selecting a design concepts. Think of this as adding a drop of dye to a glass of water. Just as that single drop changes the color of the entire glass, the design concept you choose will influence every aspect of your prompt. It sets the tone, style, and structure. Due to fluidity in language, the concepts can be present in isolation or omnipresent or combined throughout the prompt. 

- Let's explore these 'Prompt Design Blocks'. They are the foundation of the Snap AI Framework, each with its benefits and best uses. For each, we'll cover:

- Here, you'll learn about:

  - What It Is: A simple definition.
  - Value: Why use it.
  - How It Works: A guide or workflow.
  - Real-world Examples: Illustrating its use.
  - Best Practices: Tips and warnings.

 #### Closer Look at the Design Concepts

##### NLPP (Natural Language Prompt Pattern)

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
  
##### KVP (Key Value Prompting)
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

##### BDP (Behavior-Driven Prompting)
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
##### ATDP (Acceptance Test-Driven Prompting)
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
##### Step method
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

##### Integrated Prompting Paradigm

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
