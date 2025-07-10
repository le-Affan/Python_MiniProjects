# Create a Python script that:
# Checks if a file data.json exists.
# If not, create it with an empty {}.
# Adds 3 key-value pairs to it.
# Reads and prints the content.
# Updates one of the keys.
# Deletes one of the keys.
# Writes the final data back to data.json.

import json
import os

if not os.path.exists("data.json"):
    with open("data.json","w") as file:
        json.dump({},file)

with open("data.json", "r") as file:
    data = json.load(file)

data[1]='Affan'
data[2]='Ankon'
data[3]='Anjali'

print(data)

data[1]='Ayaan'
del data[2]

with open("data.json","w") as file:
     json.dump(data,file,indent=4)



