#Robert Kiser
#08/07/25
#CSD325
#Module 9.2 Assignment - Module 12 Redo

import requests, json

response = requests.get('https://official-joke-api.appspot.com/random_joke')
#Stores a dictionary with keys "type", "setup", "punchline", and "id". The
#output is a simple dictionary with one value per key.

print(response.status_code)
#Tests the API and returns a status code.

print()

random_joke = response.json()

print(random_joke)

with open ('jokes.json', 'w') as file:
    json.dump(random_joke, file, sort_keys=True, indent=4)
#Creates a .json file called "jokes.json" and alphabetizes the dictionary keys
#as well as creating indentations for each line to make it easier to read.

print()
print(random_joke["setup"])
print(random_joke["punchline"])
#Prints the output of the "setup" and "punchline" keys in the correct order to
#properly display the joke in the correct order.
