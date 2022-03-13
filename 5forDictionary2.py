import random
keys=["strength","dexterity","constitution","intelligence","wisdom","charisma"]
characterB={}
for i in range(6):
    characterB[keys[i]]=random.randint(0,20)
for key,value in characterB.items():
    print(key,value)
