#!/bin/bash

send_request() {
  # Send an HTTP request to the specified URL and return the response
  local url=$1
  local response=$(curl "$url")
  echo "$response"
}

parse_html() {
  # Parse the HTML response and look for input fields
  local html=$1
  local input_fields=$(echo "$html" | grep -o '<input[^>]*>' | tr '\n' ' ')
  local textarea_fields=$(echo "$html" | grep -o '<textarea[^>]*>' | tr '\n' ' ')

  # Combine all input fields into a single list
  local all_fields="$input_fields $textarea_fields"

  echo "$all_fields"
}

check_xss() {
  # Test each input field for XSS vulnerabilities
  local fields=$1
  local payload=$2

  for field in $fields; do
    # Inject the specified payload into the field
    local injected_field="$field $payload"

    # Submit the form and check for the alert
    local response=$(send_request "$url")
    if [[ $response =~ alert\( ]]; then
      echo "XSS vulnerability found!"
    else
      echo "No XSS vulnerability found."
    fi
  done
}

# Prompt the user to enter a URL
read -p "Enter a URL to test for XSS vulnerabilities: " url

# Prompt the user to enter a payload
read -p "Enter a payload to use for testing: " payload

# Send a request to the specified URL
response=$(send_request "$url")

# Check for XSS vulnerabilities
fields=$(parse_html "$response")
check_xss "$fields" "$payload"
