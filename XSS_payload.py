import requests
from bs4 import BeautifulSoup

def send_request(url):
  # Send an HTTP request to the specified URL and return the response
  response = requests.get(url)
  return response

def parse_html(html):
  # Parse the HTML response and look for input fields
  soup = BeautifulSoup(html, 'html.parser')
  input_fields = soup.find_all('input')
  textarea_fields = soup.find_all('textarea')
  
  # Combine all input fields into a single list
  all_fields = input_fields + textarea_fields
  
  return all_fields

def check_xss(fields, payload):
  # Test each input field for XSS vulnerabilities
  for field in fields:
    # Inject the specified payload into the field
    field.insert_after(payload)
    
    # Submit the form and check for the alert
    response = send_request(url)
    if 'alert(' in response.text:
      print("XSS vulnerability found!")
    else:
      print("No XSS vulnerability found.")

# Prompt the user to enter a URL
url = input("Enter a URL to test for XSS vulnerabilities: ")

# Prompt the user to enter a payload
payload = input("Enter a payload to use for testing: ")

# Send a request to the specified URL
response = send_request(url)

# Check for XSS vulnerabilities
fields = parse_html(response.text)
check_xss(fields, payload)
