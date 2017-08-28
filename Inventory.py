class Equips:
    def __init__(self,attached_inventory=None,weapon=None,armor=None):
        self.equips = {"weapon":weapon,"armor":armor}
        self.attached_inventory = attached_inventory
    def equip(self,item):
        current_equip = self.equips[item.__class__.__name__.lower()]
        try: 
            self.equips[item.__class__.__name__.lower()] = item
        except:
            return False       
            
        if(self.attached_inventory):
            if(self.attached_inventory.add_item(current_equip)):
                 print("attached")
                 return True
            else:
                return False
        else:
            return True
        
class Inventory:
    def __init__(self,slots):
        self.inventory = []
        self.slots = slots
        for i in range(slots):
            self.inventory.append(None)
    def add_item(self,item):
        try:
            index = self.inventory.index(None)      
            self.inventory[index] = item
            return True
        except:            
            return False
    def remove_item(self,index):
        if(index in range(self.slots)):
            item = self.inventory[index]
            self.inventory[index] = None
            return item
        else:
            return False



