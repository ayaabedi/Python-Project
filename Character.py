class Character:
    
    # constructor
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power


    def attack (self, enemy):
        enemy.health = enemy.health - self.power
        if (enemy.health < 0 ):
            enemy.health = 0

        print (self.name , "attacked 🗡️ ", enemy.name)
        print (enemy.name, " has {} health left".format(enemy.health))
        print("")

    def isAlive(self):
        if (self.health > 0):
            return True
        else:
            return False
