import DataBase as Database
import json
class Item:
    def __init__(self,id):
        self.id = id

class Weapon(Item):
    def __init__(self,id,name= None,price = None,damage = None,strenght_multiplier = None):
        Item.__init__(self,id)
        item_database = Database.select("weapons","*","WHERE id = '"+str(self.id)+"'")[0]
        if not name:
            self.name = item_database[2]
        else:
            self.name = name

        if not price:
            self.price = item_database[3]
        else:
            self.price = price

        
        if not damage:
            self.damage = item_database[4]
        else:
            self.damage = damage
            
        if not strenght_multiplier:
            self.strength_multiplier = item_database[5]
        else:
            self.strength_multiplier = strength_multiplier

def insert_weapon(item):
    querry = "INSERT INTO weapons (type,name,price,damage,strength_multiplier) VALUES ('melee','"+str(item.name)+"',"+str(item.price)+","+str(item.damage)+","+str(item.strength_multiplier)+")"
    print(querry)
    Database.insert(querry)
#item = Weapon(1 ,name=None,price=None,damage = 5)
#print(item.damage)
#insert_weapon(item)
            
