import requests

def test_xss(url):
  # Use an XSS polyglot payload to test for reflected XSS vulnerability
  payload = "<scr<!-- -->ipt>alert('XSS')</scr<!-- -->ipt>"
  r = requests.get(url + "?input=" + payload)
  if payload in r.text:
    print("Reflected XSS vulnerability found!")
  else:
    print("No reflected XSS vulnerability found.")

  # Use an XSS polyglot payload to test for stored XSS vulnerability
  payload = "<scr<!-- -->ipt>alert('XSS')</scr<!-- -->ipt>"
  r = requests.post(url + "/form", data={"input": payload})
  r = requests.get(url + "/form")
  if payload in r.text:
    print("Stored XSS vulnerability found!")
  else:
    print("No stored XSS vulnerability found.")

# Prompt the user for the target URL
url = input("Enter the target URL: ")

# Test the target URL
test_xss(url)