characterA={"strength":10,
"dexterity":15,
"constitution":19,
"intelligence":20,
"wisdom":7,
"charisma":5}
for key,value in characterA.items():
    print(key,value)
print(characterA)
for key in characterA.keys():
    if key=="strength":
        print("The strengeth is",characterA["strength"])
    if key=="speed":
        print("The speed is",characterA["speed"])