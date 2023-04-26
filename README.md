# domain_expiration_check

This python code uses Whois to lookup the domain information and check its' expiration date.

## Description
* main.py checks files contents of domain_list.txt file and get domain name line by line.
* check_expiration.py uses python-whois to check whois information of a domain and retrieves expiration date of a domain 
* check_time.py checks the now date and the expration date with datetime
* sns_publish.py sends domain name and expiration date to AWS sns topic. Change plain_message(optional) and TargetArn(Mandatory)

## Dependency
* python-whois

## Help improving the code
Any advise is welcomed
