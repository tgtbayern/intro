characterA={"strength":10,
"dexterity":15,
"constitution":19,
"intelligence":20,
"wisdom":7,
"charisma":5}
for key,value in characterA.items():
    print(key,value)
print(characterA)
message1=characterA.get("strength","No such key")
print(message1)
message2=characterA.get("speed","No such key")
print(message2)