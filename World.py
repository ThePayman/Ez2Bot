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

world = World()

def distance_between_positions(position_1,position_2):
    return (abs(position_1[0]-position_2[0]),abs(position_1[1]-position_2[1]))

def find_location_index(arg_list):
    location_name = ""
    for index in range(len(arg_list)):
        location_name+=arg_list[index]
        if(index != len(arg_list)-1):\
                 location_name+=" "
    index = next((i for i, location in enumerate(world.locations) if location.name.lower() == location_name.lower()))
    return(index)

