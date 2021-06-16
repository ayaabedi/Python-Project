from Character import Character
import time 
players = []
enemies = []
currentLvl = 1

def startGame():
    print("")
    print("Welcome to Hero vs. Zombie 🗡️ 🗡️  ")
    print("**************************")
    print("")
    # create and add players
    hero = Character("Hero", 50, 10)
    players.append(hero)     # index 0
    zombie = Character("Zombie", 20, 15)
    enemies.append(zombie)   # index 0
    print("Level {}, Kill all enemies".format(currentLvl))
    battle()

# this method is called when all enemies are dead in each lvl
def increaseLvl():
    global currentLvl
    print("Level complete, moving to the next level")
    currentLvl = currentLvl+1
    print("Level {}, Kill all enemies".format(currentLvl))
    i = 1
    while i <= currentLvl:
        zombie = Character("Zombie {}".format(i), 20, 15)
        enemies.append(zombie)
        i += 1
    
def battle():
    time.sleep(1)
    global currentLvl
    user_input = ("1")
    if (len(enemies) > 0 and players[0].isAlive()):
        print("")
        print ("Your turn")
        print("***********")
        print("1. Attack 🗡️ ")
        print("2. Flee")
        user_input = input()
    if (user_input == "1"):
        if(players[0].isAlive()):
            
            if len(enemies) > 0 : 
                players[0].attack(enemies[0])
                if enemies [0].isAlive():
                    enemies[0].attack(players[0])
                    battle()
                else:
                    print(enemies[0].name, "is dead")
                    enemies.remove(enemies[0])
                    if (len(enemies) == 0):
                        keepPlaying()
                    else:
                        battle()
            else:
                increaseLvl()
                if (currentLvl < 4):
                    battle()
        else:
            print("GAME OVER ☠️")

    elif (user_input == "2"):
        print(" You are a coward")

    else:
        print("Invalid input")
        battle()

def keepPlaying():
    print("Do you want to continue?")
    print("*************************")
    print("Y")
    print("N")
    keep_playing= input()
    if (keep_playing == "Y"):
        battle()
    elif (keep_playing == "N"):
        print("Leaving game")
    else:
        print("Invalid input")
        keepPlaying()










    




