from random import random


class Character:
    def __init__(self,strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.strength=strength
        self.dexterity=dexterity
        self.constitution=constitution
        self.intelligence=intelligence
        self.wisdom=wisdom
        self.charisma=charisma
        self.hitpoint=self.constitution*30+50

    def show_stats(self):
        print("strength",self.strength)
        print("dexterity",self.dexterity)
        print("constitution",self.constitution)
        print("intelligence",self.intelligence)
        print("wisdom",self.wisdom)
        print("charisma",self.charisma)
        
    def show_hitpoints(self):
        print("hitpoint",self.hitpoint)

    def attack(self):
        print(random.randint(1,self.strength))

   