import sys
import random


class Player:
    def __init__(self,name,characterType):
        self.name = name;

        if (characterType == "Ranger"):
            self.maxhealth = 90;
            self.health = self.maxhealth;
            self.attack = 7;
            self.gold = 0;
            self.flasks = 0;
            pass
        elif characterType == "Memester":
            self.maxhealth = 150;
            self.health = self.maxhealth;
            self.attack = 22;
            self.gold = 1;
            self.flasks = 0;
            pass
        elif characterType == "Friesen":
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
        
class Troll:
    def __init__(self,name):
        self.name = name;
        self.maxhealth = 100;
        self.health = self.maxhealth;
        self.attack = 7;
        self.goldgain = 10;
TrollG = Troll("Troll")

class AdeeshTheMirror:
    def __init__(self,name):
        self.name = name;
        self.maxhealth = 100;
        self.health = self.maxhealth;
        self.attack = 5;
        self.goldgain = 20;
AdeeshTheMirrorG = AdeeshTheMirror("AdeeshTheMirror")



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
        prefight()
    else:
        print("Are you stupid?")
        start1()
    start1()

def prefight():
    global enemy
    enemynum = random.randint(1,2)
    if enemynum == 1:
        enemy = AdeeshTheMirrorG
    else:
        enemy = Troll
    fight()

def fight():
<<<<<<< HEAD
    print(PlayerG.name + "versus" + enemyname)
    print(PlayerG.name + "HP:" + PlayerG.health + " Vs. " + enemy.name + "HP:" + enemy.health)
    print("Potions" + PlayerG.flasks)
=======
    print("%s VERSUS %s" % PlayerG.name, enemyname)
    print("%s's HP: %d/%d  %s's HP: %i/%i")(PlayerG.name, PlayerG.health, PlayerG.maxhealth, enemy.name, enemy.health, enemy.maxhealth)
    print("Potions %i\n"% PlayerG.flasks)
>>>>>>> origin/master
    print("1. Attack with fists")
    print("2. Drink flask")
    print("3. Walk out door, the mirror can't move after all")
    option = input(">> ")
    if option == "1":
        attack()
    elif option == "2":
        drinkflask()
    elif option == "3":
        walk()
    else:
        fight()
        
def attack():
    PlayerAttack = random.randint(PlayerG.attack / 2, PlayerG.attack)
    EnemyAttack = random.randint(enemy.attack / 2, enemy.attack)
    if PlayerAttack == PlayerG.attack/2:
        print ("You missed the mirror, wow that's hard to do")
<<<<<<< HEAD
        option = input
=======
    else:
        enemy.health -= PlayerAttack
        print ("You dealt %i damage!" %PlayerAttack)
    option = input(' ')
    if enemy.health <= 0:
        win()
    if EnemyAttack == enemy.attack/2:
        print ("The enemy attack missed!")
    else:
        print ("The enemy attack dealt %i damage" % EnemyAttack)
    option = input(' ')
    if PlayerG.health <= 0:
        die()
    else:   
        fight()
       
def drinkflask():
    if PlayerG.flasks = 0:
        print ("You have none!")
        option = input(' ')
        fight()
    else:
        PlayerG.health += 50
        if PlayerG.health > PlayerG.maxhealth:
            PlayerG.health = PlayerG.maxhealth
        print ("You drank a potion!")
    option = input(' ')
    fight()

def win():
    enemy.health = enemy.maxhealth
    print ("You have defeated the %s" % enemy.name)
    print ("There was %i gold found in the corpse % enemy.goldgain)
    option = input(' ')
    start1()

def dead():
    print ("You died! Finally! You're so stupid! AHAHAHA"_
    option = input(' ')
    
    
    
    
    
    
    
>>>>>>> origin/master
    
main()

<<<<<<< HEAD
=======
    main()
>>>>>>> origin/master
        
