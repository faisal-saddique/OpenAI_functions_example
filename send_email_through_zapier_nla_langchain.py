# Import necessary libraries and modules
import os
from langchain.llms import OpenAI
from langchain.agents import initialize_agent
from langchain.agents.agent_toolkits import ZapierToolkit
from langchain.agents import AgentType
from langchain.utilities.zapier import ZapierNLAWrapper

# Step 1: Initialize the Language Model (LLM)
# Here, we create an instance of the OpenAI language model (LLM) with a default temperature value of 0.
# Temperature is a hyperparameter that controls the randomness of the generated text.
llm = OpenAI(temperature=0)

# Step 2: Set up Zapier integration
# We use the ZapierNLAWrapper to connect with the Zapier API using the provided API key (zapier_nla_api_key).
# This allows us to interact with the Zapier platform and automate tasks using natural language instructions.
zapier = ZapierNLAWrapper(zapier_nla_api_key="sk-ak-spRXigynbAUpCWdSX8H7UFvy4l")

# Step 3: Create a ZapierToolkit
# The ZapierToolkit is a utility class that facilitates interactions with the Zapier platform.
# It provides access to various tools and actions that can be performed through Zapier.
# In this case, we create the toolkit using the previously initialized ZapierNLAWrapper.
toolkit = ZapierToolkit.from_zapier_nla_wrapper(zapier)

# Step 4: Initialize the agent
# The agent is the interface that enables interactions with the language model (LLM) and the Zapier toolkit.
# We use the initialize_agent function, passing in the LLM, the toolkit, the agent type, and setting verbose mode to True.
# The AgentType.ZERO_SHOT_REACT_DESCRIPTION is a specific type of agent designed for reacting to user instructions.
agent = initialize_agent(
    toolkit.get_tools(),
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Step 5: Run the agent with a user instruction
# Finally, we execute the agent by calling its run method with the user's instruction as the input.
# The agent will use the LLM to process the instruction, interact with the Zapier toolkit, and perform the specified action.
# In this case, the user instruction is "send a funny email to faisalsaddique04@gmail.com".
agent.run("send a funny email to faisalsaddique04@gmail.com")