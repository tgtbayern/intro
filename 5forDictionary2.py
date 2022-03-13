import random
keys=["strength","dexterity","constitution","intelligence","wisdom","charisma"]
characterB={}
for i in range(6):
    characterB[keys[i]]=random.randint(0,20)
for key,value in characterB.items():
    print(key,value)
#Test something else about dictionary,not required in the tutorials

#access dictionary
print(characterB["strength"])
#print whole dictionary
print(characterB)

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
#get() method to access the dictionary
message1=characterB.get("strength","No such key")
print(message1)
message2=characterB.get("speed","No such key")
print(message2)
#traverse
for key,value in characterB.items():
    print(key,value)
for key in characterB.keys():
    print(key)
for value in characterB.values():
    print(value)

