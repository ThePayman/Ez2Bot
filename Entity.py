import DataBase as Database
import Inventory
import Items
import World
#Constitution,Strength,Defense,Intelligence
players = []
enemies = []
class Entity:
    def __init__(self,max_hp,strength):
        self.id = Database.find_next_id_db("Users")
        self.type = self.__class__.__name__
        self.equips = Inventory.Equips(Items.Weapon(1))
        if( not max_hp):
            self.max_hp = self.calculate_max_hp()
        else:
            self.max_hp = max_hp
        self.hp = self.max_hp
        if( not strength):
            self.strength = Database.select("entity_base","strength","WHERE type='"+self.__class__.__name__+"'")[0][0]
        else:
            self.strength = strength
    def calculate_max_hp(self):
        """ Returns the max hp for an entity based on it's current stats"""
        #This function is missing the implementation of the item system
        self.max_hp_constant = Database.select("entity_base","max_hp_constant","WHERE type='"+self.__class__.__name__+"'")
        for i in self.max_hp_constant:
            return(i[0])
#enemy entities inside a player entity
class Enemy:
    def __init__(self,attached_player):
        self.attached_player = attached_player
class Zombie(Entity,Enemy):
    def __init__(self,attached_player,max_hp = None,strength = None):
        Enemy.__init__(self,attached_player)
        Entity.__init__(self,max_hp,strength)
        
class Player(Entity):
    def __init__(self,player_id,player_name):
        Entity.__init__(self,10,10)
        self.player_id = player_id
        self.player_name = player_name
        self.available_commands = ["search","fight","travel"]
        self.status = "Idle"
        self.position = (1,1)
        self.locations = World.world.locations
    def action(self,action,args = None):
        if(action == "fight"):
            return self.fight()
        if(action == "search"):
            return self.search()
        if(action == "travel"):
            return self.travel(args)
    def fight(self):
        enemy_list_player = [enemy for enemy in enemies if enemy.attached_player == self.player_id]
        if(len(enemy_list_player)!=0):
            self.available_commands = ["attack","run","use item"]
            return ("You choose to fight the monsters")
        else:
            return ("There are no enemies to fight ##This should not happen in a real version")
        
    def search(self):
        enemyE = Zombie(self.player_id)
        enemies.append(enemyE)
        enemy_list_player = [enemy for enemy in enemies if enemy.attached_player == self.player_id]
        enemy = enemy_list_player[0]
        return(enemy.equips.equips["weapon"].name)
    
    def travel(self,arg_list = None):
        if(not arg_list):
            message = "Available Locations:"
            i = 1
            for location in self.locations:
                #Needs some polish, distance calculation based on 2 vectores and city behavior 
                distancelocation = World.distance_between_positions(self.position,location.position)
                message += "\n "+str(i)+" - "+ location.name + " distance - "+str(distancelocation)
                if(distancelocation[0]==0 and distancelocation[1] ==0):
                    message +=" - Current Location"
                if(location.__class__.__name__ == "City"):
                    for build in location.buildings:
                        message += (" \n  > "+build.name)
                i+=1
            return message
        else:
            target_location = arg_list[0]
            try:
                target_location = int(target_location)-1
            except:
                target_location = World.find_location_index(arg_list)
            if(len(self.locations)>int(target_location)):
                if(self.position != self.locations[int(target_location)].position):
                    self.position = self.locations[int(target_location)].position
                    return("You travel to "+self.locations[int(target_location)].name)
                else:
                    return("You already are at this location")
            else:
                return("ERROR: The selected location doesnt exist")
def player_exists(player_id):
    player = Database.select("players","*","WHERE id='"+player_id+"'")
    if(player):
        players.append(Player(player_id,"player_name"))
        return True
    else:
        create_player()
        print("creating char")
        return False

def create_player():
    pass
