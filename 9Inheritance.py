import random


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
        return random.randint(1,self.strength)
    
    def defence(self,defen):
        a=random.randint(0,20)
        if(a>=self.dexterity):
            defen=defen-self.attack
        
    def heal(self,healValue):
        self.hitpoint+=healValue
    
class MagicCharacter(Character):
    def __init__(self, strength, dexterity, constitution, intelligence, wisdom, charisma):
        super().__init__(strength, dexterity, constitution, intelligence, wisdom, charisma)
        mana= intelligence * 30 + 50

    def show_mana(self):
        print("mana",self.mana)
    
    def magicMissile(self):
        self.mana-=5
        return random.randint(5,10)

    def fireball(self):
        self.mana-=10
        return random.randint(10,20)

    def healMana(self,healValue):
        mana+=healValue
    



