import requests

# Prompt the user for the target URL
target_url = input('Enter the target URL: ')

# Prompt the user for the name of the file containing the data to be sent in the POST request
data_file = input('Enter the name of the file containing the data to be sent in the POST request: ')

# Read the data from the file and split it into a dictionary
with open(data_file, 'r') as f:
  data = dict(item.split('=') for item in f.read().split('&'))

# Prompt the user for the payload to be injected
payload = input('Enter the payload to be injected: ')

# Inject the payload into the data dictionary
data['username'] = payload

# Send a POST request to the login form with the injected payload
response = requests.post(target_url, data=data)

# Check the response for any indicators of a successful SQL injection attack
if 'error' in response.text.lower():
  print('Possible SQL injection vulnerability found!')
else:
  print('No SQL injection vulnerability found.')
