import json
import random

#Action 0 asdf
with open("newList.json") as f:
  data = json.load(f)

#Action 1
def write_json():
    with open('newList.json','r+') as file:
            # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["Games"][input("Choose Platform \n" )].append(input("Insert Game  \n"))
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)

#Action 2
def gameRandomize():
    platformUsed = input("Choose a Platform \n")
    gameCount = len(data["Games"][platformUsed])
    rand = random.randint(0, gameCount - 1 )
    print(data["Games"][platformUsed][rand]);

#Main Switch
def switch(action):
        if action == "0":
            print(data["Games"][input("Choose a Platform \n")]);
        if action == "1":
            write_json();
        if action == "2":
            gameRandomize();
        
switch(input("Choose an Action \n 0 = List Games \n 1 = Add Game \n"))


#testing the remote 

