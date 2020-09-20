import os
import requests

USERNAME = ''
PASSWORD = ''
DOMAIN = ''

def getIP():
	myIP = os.popen('dig +short myip.opendns.com @resolver1.opendns.com').read()
	return myIP[:-1]

def main():
    myIP = getIP()
    print(myIP)
    url = 'https://%s:%s@domains.google.com/nic/update?hostname=%s&myip=%s' % (USERNAME, PASSWORD, DOMAIN, myIP)
    response = requests.post(url, verify=True)
    print(response.content)
    
    

main()
