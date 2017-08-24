import DataBase as Database
import Inventory
import Items
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
        self.available_commands = ["search","fight"]
        self.status = "Idle"
    def action(self,action):
        if(action == "fight"):
            return self.fight()
        if(action == "search"):
            return self.search()
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
