#!/bin/bash

Script to automatically check for bugs on bugcrowd for all companies listed on their website
Set target URL
target_url="https://www.bugcrowd.com"

Create .txt file to store vulnerabilities
touch vulnerabilities.txt

Retrieve list of all companies on bugcrowd website
companies=$(curl -s $target_url | grep -o 'companies/.*">' | sed 's/companies///g;s/">//g')

Loop through each company and run scans
for company in $companies; do
echo "Scanning $company..."
nikto -h $target_url/companies/$company >> vulnerabilities.txt
w3af -t $target_url/companies/$company >> vulnerabilities.txt
burpsuite -t $target_url/companies/$company >> vulnerabilities.txt
done

Print results of scans
echo "Scan complete. Vulnerabilities saved in vulnerabilities.txt."