import os
import openai
import re
from dotenv import load_dotenv
from send_email_through_zapier_nla_directly import send_email_through_zapier
from pprint import pprint

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define the GPT-3.5 model to use
COMPLETION_MODEL = "gpt-3.5-turbo-0613"

# Define the question to be asked
QUESTION = (
    "send a notorious email to faisalsaddique04@gmail.com explaining how I pranked my friend today on the beach. write the email in detail."
)

# List of message objects that will be used in the conversation with GPT-3.5
messages = [
    {"role": "user", "content": QUESTION},
]

# Function to add two decimal values
def add_decimal_values(arguments):
    value1 = int(re.search(r'"value1": (\d+)', str(arguments)).group(1))
    value2 = int(re.search(r'"value2": (\d+)', str(arguments)).group(1))

    result = value1 + value2
    print(f"{value1} + {value2} = {result} (decimal)")

    return result

# Function to add two hexadecimal values
def add_hexadecimal_values(arguments):
    value1 = re.search(r'"value1": "(\w+)"', str(arguments)).group(1)
    value2 = re.search(r'"value2": "(\w+)"', str(arguments)).group(1)

    decimal1 = int(value1, 16)
    decimal2 = int(value2, 16)

    result = hex(decimal1 + decimal2)[2:]
    print(f"{value1} + {value2} = {result} (hex)")
    return result

# Function to send an email based on the provided instructions
def send_email(instructions):
    # Here we call the send_email_through_zapier() function from the send_email_through_zapier_nla_directly.py script
    # to send an email based on the instructions.

    print("Email instructions:")
    print(instructions)

    result = send_email_through_zapier(instructions=instructions)

    # Check if the result is not None (i.e., the request was successful)
    if result:
        # If the request was successful, print a success message and display the result
        print("Request successful!")
        # pprint(result)
        return "Email sent successfully!"
    # In a real implementation, you would perform the steps to send the email using libraries or APIs.

# Function to get a completion from GPT-3.5 model
def get_completion(messages):
    response = openai.ChatCompletion.create(
        model=COMPLETION_MODEL,
        messages=messages,
        functions=[
            {
                "name": "add_decimal_values",
                "description": "Add two decimal values",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "value1": {
                            "type": "integer",
                            "description": "The first decimal value to add. For example, 5",
                        },
                        "value2": {
                            "type": "integer",
                            "description": "The second decimal value to add. For example, 10",
                        },
                    },
                    "required": ["value1", "value2"],
                },
            },
            {
                "name": "add_hexadecimal_values",
                "description": "Add two hexadecimal values",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "value1": {
                            "type": "string",
                            "description": "The first hexadecimal value to add. For example, 5",
                        },
                        "value2": {
                            "type": "string",
                            "description": "The second hexadecimal value to add. For example, A",
                        },
                    },
                    "required": ["value1", "value2"],
                },
            },
            {
                "name": "send_email",
                "description": "Send an email based on the provided instructions",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "instructions": {
                            "type": "string",
                            "description": "The instructions for sending the email. For example: Send a birthday invitation email to faisalsaddique04@gmail.com",
                        }
                    },
                    "required": ["instructions"],
                },
            },
        ],
        temperature=0,
    )

    return response

# Main loop to interact with GPT-3.5
while True:
    response = get_completion(messages)

    # Check if the conversation should stop
    if response.choices[0]["finish_reason"] == "stop":
        print(response.choices[0]["message"]["content"])
        break

    # Check if a function call is requested by GPT-3.5
    elif response.choices[0]["finish_reason"] == "function_call":
        # Extract the function name and arguments from the response
        fn_name = response.choices[0].message["function_call"].name
        arguments = response.choices[0].message["function_call"].arguments
        print(f"Arguments for the function call: {arguments}")

        # Get the corresponding function based on the function name
        function = locals()[fn_name]
        result = function(arguments)

        # Append assistant's response to the messages list
        messages.append(
            {
                "role": "assistant",
                "content": None,
                "function_call": {
                    "name": fn_name,
                    "arguments": arguments,
                },
            }
        )

        # Append function's response to the messages list
        messages.append(
            {
                "role": "function",
                "name": fn_name,
                "content": f'{{"result": {str(result)} }}'
            }
        )

        # Continue the conversation with the updated messages
        response = get_completion(messages)
