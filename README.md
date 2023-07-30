# Zapier Automation

This project shows how to create an agent that can send emails via Zapier using natural language instructions and the LangChain library. 

## Overview

The agent uses the OpenAI API as the underlying language model to process instructions. For sending emails, it integrates with Zapier using the Zapier API and the Zapier agent toolkit provided by LangChain.

The key steps are:

1. Initialize the OpenAI language model 
2. Set up Zapier integration with an API key
3. Create the Zapier toolkit  
4. Initialize the agent with the language model, toolkit, and agent type
5. Give the agent natural language instructions to send emails

## Usage

The main code file shows how to:

- Import required LangChain modules
- Create the OpenAI instance 
- Initialize the Zapier API wrapper 
- Build the Zapier toolkit
- Initialize the agent by passing in the language model, toolkit, agent type, etc.
- Run the agent with a sample instruction to send an email

To use this code yourself, you would need:

- LangChain installed
- An OpenAI API key for the language model
- A Zapier account and API key for integration

## Customizing

The agent can be customized by:

- Modifying the temperature of the language model
- Using a different underlying language model like GPT-3
- Building additional tools for the toolkit 

## References

- [LangChain Documentation](https://python.langchain.com/docs/integrations/tools/zapier)
- [OpenAI API](https://openai.com/)
- [Zapier API](https://nla.zapier.com/api/v1/dynamic/playground)https://nla.zapier.com/api/v1/dynamic/playground)
