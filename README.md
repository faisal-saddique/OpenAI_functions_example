# Zapier Langchain Automation

Welcome to the Zapier Langchain Automation repository! This project aims to demonstrate how to automate tasks using natural language instructions and integrate them with Zapier. It utilizes the OpenAI GPT-3.5 language model to understand and respond to user instructions, and Zapier to execute various actions based on those instructions.

## Prerequisites

Before running the scripts in this repository, make sure you have the following prerequisites installed:

- Python (version 3.6 or later)
- OpenAI Python library
- dotenv Python library
- requests Python library

Additionally, you need to set up an account on OpenAI and obtain an API key. Also, sign up for a Zapier account and get an API key (Zapier NLA API key).

## Contents

This repository contains the following main scripts:

### 1. `openai_function_calling.py`

This script interacts with the OpenAI GPT-3.5 language model. It sets up the environment, defines functions to add decimal and hexadecimal values, and sends an email based on user instructions. The main loop continuously interacts with the GPT-3.5 model and calls the appropriate functions based on the responses.

### 2. `send_email_through_zapier_nla_directly.py`

This script sends an email through Zapier using the Zapier NLA (Natural Language Automation) API. It defines a function `send_email_through_zapier` that takes instructions as input and triggers the email sending action through the Zapier API.

### 3. `send_email_through_zapier_nla_langchain.py`

This script utilizes the Langchain library to create an agent that interacts with the OpenAI language model and the Zapier toolkit. The agent is designed to react to user instructions and automate actions based on them.

## Getting Started

To run the scripts, follow these steps:

1. Clone this repository to your local machine.
2. Rename the `.env.template` file to `.env`. You can do this by executing the following command in the terminal or command prompt:

   ```bash
   mv .env.template .env
   ```

3. Open the newly created `.env` file in a text editor and add your actual OpenAI API key as follows:

   ```dotenv
   OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
   ```

   Replace `YOUR_OPENAI_API_KEY` with your actual API key provided by OpenAI.

4. Install the required libraries mentioned in the "Prerequisites" section.
5. Proceed to run the desired script(s) using Python.

## Examples

To demonstrate the functionality of the scripts, consider the following examples:

### Example 1: Using `openai_function_calling.py`

Run the `openai_function_calling.py` script. The GPT-3.5 model will interact with you through the console. It can add decimal and hexadecimal values and send an email based on your instructions.

### Example 2: Using `send_email_through_zapier_nla_directly.py`

Modify the `instructions_local` variable in the script with your desired email content. Run the script, and it will send the specified email through Zapier using the Zapier NLA API.

### Example 3: Using `send_email_through_zapier_nla_langchain.py`

Run the `send_email_through_zapier_nla_langchain.py` script. The Langchain agent will prompt you for a task, and it will use the GPT-3.5 model and Zapier toolkit to perform the specified action.

## Contributions

Contributions to this repository are welcome. If you encounter any issues, have suggestions, or want to add features, please feel free to create pull requests or raise issues.

## License

This project is licensed under the [MIT License](LICENSE).

Thank you for using Zapier Langchain Automation! Happy automating!