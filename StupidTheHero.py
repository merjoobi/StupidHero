import sys
import random

weapons = {"Great Sword": 40}

class Player:
    def __init__(self,name,characterType):
        self.name = name;

        if (characterType == "Ranger"):
            self.maxhealth = 90;
            self.health = self.maxhealth;
            self.attack = 7;
            self.gold = 0;
            self.flasks = 0;
            self.weap = ["Crappy Bow"]
            self.curweap = ["Crappy Bow"]
            pass
        elif characterType == "Memester":
            self.maxhealth = 150;
            self.health = self.maxhealth;
            self.attack = 22;
            self.gold = 1;
            self.flasks = 0;
            self.weap = ["Drumstick"]
            self.curweap = ["Drumstick"]
            pass
        elif characterType == "Friesen":
            self.maxhealth = 50;
            self.health = self.maxhealth;
            self.attack = 50;
            self.gold = 0;
            self.flasks = 0;
            self.weap = ["Keyboard Sword"]
            self.curweap = ["Keyboard Sword"]
            pass
        else:
            self.maxhealth = 100;
            self.health = self.maxhealth;
            self.attack = 10;
            self.gold = 0
            self.flasks = 0
            self.weap = ["Stick"]
            self.curweap = ["Stick"]
            pass
      
    @property
    def attack(self):
        attack = self.base_attack
        if self.curweap == "Crappy Bow":
            attack += 7
            
        if self.curweap == "Drumstick":
            attack += 8
            
        if self.curweap == "Keyboard Sword":
            attack += 10
            
        if self.curweap == "Stick":
            attack += 5
            
        return attack
        

class Enemy:
    def __init__(self,name):
        
        if (name == "AdeeshTheMirror"):
            self.name = "Adeesh The Mirror";
            self.maxhealth = 90;
            self.health = self.maxhealth;
            self.attack = 7;
            self.gold = 0;
            self.flasks = 0;
            pass
        elif name == "HomieG":
            self.name = "Homie G."
            self.maxhealth = 150;
            self.health = self.maxhealth;
            self.attack = 22;
            self.gold = 1;
            self.flasks = 0;
            pass
        elif name == "CrazyDude":
            self.name = "Crazy Dude"
            self.maxhealth = 50;
            self.health = self.maxhealth;
            self.attack = 50;
            self.gold = 0;
            self.flasks = 0;
            pass
        else:
            self.maxhealth = 100;
            self.health = self.maxhealth;
            self.attack = 10;
            self.gold = 0
            self.flasks = 0
            pass

def main():
    print("Hello traveler")
    print("Welcome to Stupid Hero - a game where the hero is stupid")
    print("Your friends made you retrieve a ball, but you appear to have gotten lost")
    print("There are two paths, east and west")
    print("In front of you lies a piece of paper")
    
    print("1. pick up")
    print("2. Walk east")
    print("3. Walk west, I wouldn't do this!")
    option = input(">> ")
    if option == "1":
        start()
    elif option == "2":
        pass
    elif option == "3":
        sys.exit()
    else:
        print("What are you doing?")
        main()
        
def start():
    print("You are teleported to a bedroom in a castle")
    print("A talking mirror asks:")
    print("What? How did you get in here? What's your name?")
    option = input(">> ")
    print("What are you, b/c im PC bro?")
    characterType = input(">> ")
    global PlayerG
    PlayerG = Player(option,characterType)      
    start1()
    
def start1():
    print("Well what are you doing here?" + PlayerG.name)
    print("Attack:" + str(PlayerG.attack))
    print("Health:" + str(PlayerG.health))
    print("Gold:" + str(PlayerG.gold))
    print("Flasks:" +str(PlayerG.flasks))
    print("1. I don't know, where the heck am I?")
    print("2. What are YOU doing here?")
    print("3. *Attack the Mirror*")
    option = input(">> ")
    if option == "1":
        print("You're in the high estate of King Patel")
        pass
    elif option == "2":
        print("...")
        pass
    elif option == "3":
        print("What, what are you doing? Punching me isn't going to help you!")
        global enemy
        enemy = Enemy("AdeeshTheMirror")
        fight(enemy)
    else:
        print("Are you stupid?")
        start1()


def fight(enemy):
    print(PlayerG.name + " HP: " + str(PlayerG.health) + " Vs. " + enemy.name + " HP: " + str(enemy.health))
    print("Potions: " + str(PlayerG.flasks))
    print("1. Attack with weapon")
    print("2. Drink flask")
    print("3. Run away")
    option = input(">> ")
    if option == "1":
        '''attack()'''
    elif option == "2":
        drinkflask()
    elif option == "3":
        walk()
    else:
        fight()
        
def attack():
    PlAttack = random.randint(PlayerG.attack / 2, PlayerG.attack)
    EnAttack = random.randint(enemy.attack / 2, enemy.attack)
    if PlAttack == PlayerG.attack / 2:
        print ("You missed the mirror, wow that's hard to do")
    else:
        enemy.health -= PlAttack
        print "You deal %i damage!" % PlAttack
        option = input(' ')
    if EnAttack == enemy.attack/2:
        print "The enemy missed hah!"
    else:
        print "The enemy deals %i damage!" % EnAttack
    option = input(' ')
    if PlayerG.health <= 0:
        dead()
    else:
        fight()
    
def drinkflask():
    if PlayerG.flasks = 0:
        print "You have none..."
        option = input(' ')
        fight()
    else:
        PlayerG.health += 69
        if PlayerG.health > PlayerG.maxhealth:
            PlayerG.health = PlayerG.maxhealth
        print "You take a swig of the flask!"
    option = input(' ')
    fight()
    
def win():
    
def die():
    
def store():
    
    
    
    
    
 main()

        
