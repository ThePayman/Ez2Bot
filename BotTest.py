#-*-coding:utf8;-*-
#qpy:3
#qpy:console

#Entity
    #Player
    #Enemy
        #Zombie
        #Skeleton
        #...
    #NPC
#Items
    #Weapon
    #Armor
    #Boots
#Inventory
#Equips
#World
#Battle
#TextInterface
#Place
user_position = (0,1)
class World:
    def __init__(self):
        self.locations = [City(1,1,"City of Amber","Pay",[Blacksmith("smithy",None),Blacksmith("ez2smith",None),Castle("Castle")]),Location(3,2,"Forest")]
class Location:
    def __init__(self,x,y,name,enemies = None):
        self.position = (x,y)
        self.name = name
        self.actions = ["explore","travel"]
        self.enemies = enemies
class City(Location):
    def __init__(self,y,x,name,lord,buildings):
        Location.__init__(self,x,y,name)
        self.lord = lord
        self.buildings = buildings
        self.actions.append("enter")
class Building:
    def __init__(self,name):
        self.name = name
class Shop:
    def __init__(self,inventory):
        self.inventory = inventory
    def buy(product,user):
        pass
class Blacksmith(Building,Shop):
    def __init__(self,name,inventory):
        Building.__init__(self,name)
        Shop.__init__(self,inventory)
class Castle(Building):
    def __init__(self,name):
        Building.__init__(self,name)
world=World()
for location in world.locations:
    distancelocation = (abs(user_position[0]-location.position[0]),abs(user_position[1]-location.position[1]))
    print(location.name + " distance: "+str(distancelocation))
    if(location.__class__.__name__ == "City"):
        for build in location.buildings:
            print(" > "+build.name)