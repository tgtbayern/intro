import random
keys=["strength","dexterity","constitution","intelligence","wisdom","charisma"]
characterB={}
for i in range(6):
    characterB[keys[i]]=random.randint(0,20)
for key,value in characterB.items():
    print(key,value)
#Test something else about dictionary,not required in the tutorials

#access dictionary
print(characterB["strengeth"])
#print whole dictionary
print(characterB)
#print key and value seperately
for key,value in characterB.items():
    print(key,value)
#add something in dictionary
for i in range(6):
    characterB[keys[i]]=random.randint(0,20)
print(characterB)
#change the value
characterB["strengeth"]=99
print(characterB)
#delete Key/value pair
del characterB["strengeth"]
print(characterB)

