import requests

# Prompt the user for the target URL
target_url = input('Enter the target URL: ')

# Prompt the user for the data to be sent in the POST request
data = input('Enter the data to be sent in the POST request (format: key1=value1&key2=value2): ')

# Split the data string into a dictionary
data = dict(item.split('=') for item in data.split('&'))

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
