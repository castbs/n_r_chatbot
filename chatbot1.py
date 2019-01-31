import random
import csv
import re
import time
import sys

class myClass:
    q_or_a = ""
    who = ""
    category = ""
    
    def __init__(self,var1,var2,var3):
        self.q_or_a = var1
        self.who = var2
        self.category = var3

class pairings:
    user_response = ""
    agent_response = ""
    
    def __init__(self,var1,var2):
        self.user_response = var1
        self.agent_response = var2

with open('N_smalltalk_dataset.csv') as dataset_file:
    reader1 = csv.reader(dataset_file)
    next(reader1)
    data = []
    for r1 in reader1:
        col1 = r1
        data.append(myClass(col1[0],col1[1],col1[2]))
with open('rules.csv') as rules_file:
    reader2 = csv.reader(rules_file)
    next(reader2)
    pairings_array = []
    for r2 in reader2:
       col2 = r2
       #print(str(col2))
       pairings_array.append(pairings(col2[0],col2[1]))

def print_slowly(text):
    for letter in str(text):
        sys.stdout.write(letter)
        sys.stdout.flush()
        random_time = (random.randint(0,100))**2 / 10000 / 1
        time.sleep(random_time)
    print()

while True:
    userInput = input(">>>>> ")
    userInput = str(userInput).replace("    "," ").replace("   "," ").replace("  "," ").strip().lower()

    for y in range(0,1):
        if userInput == "buh-bai":
            print_slowly("Bye bye")
            exit()
        #userInput_data = re.findall(userInput,data)
        #print(str(userInput_data))
        for data_row in data:
            if str(data_row.q_or_a) == str(userInput) and str(data_row.who) != "agent":
                userInput_category = str(data_row.category)
                #print("Your Category is ===> " + str(userInput_category))
                break

        for p in pairings_array:
            if str(p.user_response) == str(userInput_category):
                agentOutput_category = str(p.agent_response)
                #print("My Category is ------> " + str(agentOutput_category))
                break

        what_to_respond = []
        for data_row in data:
            if str(data_row.category) == str(agentOutput_category) and str(data_row.who) != "user":
                what_to_respond.append(data_row.q_or_a)
        #for line in what_to_respond:
        #    print(str(line))
			
        agent_says = random.choice(what_to_respond)
        #print(str(agent_says))
        print_slowly(str(agent_says))
