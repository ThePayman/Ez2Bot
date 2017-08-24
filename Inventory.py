class Equips:
    def __init__(self,weapon=None,armor=None):
        self.equips = {"weapon":weapon,"armor":armor}
    def equip(item):
        try:
            self.equips[item.__class__.__name__.lower()] = item
        except:
            pass
