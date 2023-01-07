#!/bin/bash

#Script to automatically check for bugs on bugcrowd
#Prompt user for target URL
echo "Enter target URL:"
read target_url

#Create .txt file to store vulnerabilities
touch vulnerabilities.txt

#Run initial scan with nikto tool
nikto -h $target_url >> vulnerabilities.txt

#Run second scan with w3af tool
w3af -t $target_url --audit xss --audit sql >> vulnerabilities.txt

#Run final scan with Burp Suite
burpsuite -t $target_url >> vulnerabilities.txt

#Print results of scans
echo "Scan complete. Vulnerabilities saved in vulnerabilities.txt."