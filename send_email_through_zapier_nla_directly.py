# Import necessary libraries
import requests  # Library for making HTTP requests
from pprint import pprint  # Pretty-printing library for nicer output

# Define the API key to be used for authentication
api_key = 'sk-ak-spRXigynbAUpCWdSX8H7UFvy4l'

# Function to send an email through Zapier
def send_email_through_zapier(instructions):
    # Define the base URL for the Zapier API
    url = 'https://nla.zapier.com/api/v1/exposed/'

    # Define the headers to be sent along with the request
    headers = {
        'accept': 'application/json',
        'X-API-Key': api_key
    }

    # Send a GET request to the Zapier API to retrieve available actions
    response = requests.get(url, params={'api_key': api_key}, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the response data as JSON
        data = response.json()

        # Uncomment the following line if you want to see the data received from Zapier
        # pprint(data)

        # Iterate through the list of results returned by Zapier
        for iter in data['results']:
            # Check if the current action is the one for sending an email
            if (iter['description'] == "Gmail: Send Email"):
                # Get the action ID for sending an email
                action_id = iter['id']

                # Print the action ID for informational purposes
                pprint(f"Action ID to send Email is: {action_id}")

                # Update the URL to include the action ID for sending an email
                url = f'{url}{action_id}/execute/'

                # Define new headers including the 'Content-Type' required for POST requests
                headers = {
                    'accept': 'application/json',
                    'X-API-Key': api_key,
                    'Content-Type': 'application/json'
                }

                # Prepare the payload (data to be sent in the request body) for sending an email
                payload = {
                    "instructions": instructions,
                    "preview_only": False
                }

                # Send a POST request to the Zapier API to trigger the email sending action
                response = requests.post(url, headers=headers, json=payload)

                # Check if the request was successful (status code 200)
                if response.status_code == 200:
                    # Parse the response data as JSON
                    data = response.json()
                    # Return the response data to the caller
                    return data
                else:
                    # If the request was not successful, print an error message and return None
                    print(f"Request failed with status code: {response.status_code}")
                    return None
    else:
        # If the initial GET request to retrieve actions was not successful, print an error message and return None
        print(f"Request failed with status code: {response.status_code}")

# Define the instructions for sending the email
instructions = "please send a detailed sad email to faisalsaddique04@gmail.com telling him how bad was my day at gym"

# Call the send_email_through_zapier function and store the result in 'result'
result = send_email_through_zapier(instructions=instructions)

# Check if the result is not None (i.e., the request was successful)
if result:
    # If the request was successful, print a success message and display the result
    print("Request successful!")
    pprint(result)
