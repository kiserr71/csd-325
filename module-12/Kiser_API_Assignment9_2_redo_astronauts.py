#Robert Kiser
#08/07/25
#CSD325
#Module 9.2 Assignment - Module 12 Redo

import requests, json

response = requests.get('http://api.open-notify.org/astros')
#Stores a dictionary with keys "people", "number", and "message". The "people"
#item contains a list of smaller dictionaries with "craft" and "name" keys.

print(response.status_code)
#Prints the status code from the API request. A successful request will return
#a result of "200".

print()

astro_result = response.json()
#Stores the dictionary result into the astro_result variable.

with open ('astros.json', 'w') as file:
    json.dump(astro_result, file, sort_keys=True, indent=4)
#Creates a .json file called "astros.json" and prints the dictionary stored in
#astro_result with the following formatting: sort_keys=True alphabetizes the
#outer dictionary keys "message", "number", and "people". indent=4 creates
#indentations and separates each key and list item onto its own line.
