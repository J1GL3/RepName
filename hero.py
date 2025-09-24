


class Hero ():
    def __init__(self):
        self.max_health = 100.0
       
        self.stats = {
            "name" : "hero",
            "strength": 7,
            "health": 100.0,        
        }
       
       self.iventory = {"sword", "health potion", "rope"}
    
    def print_stats(self):
       print("Your stats are: ")
       for key,value in self.stats.items():
          print(f"{key} : {value}")

    def set_name(self, name):
        self.stats["name"] = name
        self.print_stats()

    def move ():
    pass

    def attack ():
    pass

    def heal(self):

        if (self.inventory.count("health potion")<=0):
            print (f"You dont have any {item_name}")

        print (f"You've used a {item_name} you've restored {health_potion_strength} health")
        if (self.stats["health"] >= self.max_health):
            print ("you've reached max health")
            self.stats["health"] = se

        pass

    def take_damage(self, damage):
        self.stats["health"] = self.stats["health"] - damage
        print (f"your health is now {self.stats["health"]}")
        pass

    def use_item():
        pass







player = Hero()

print (f"Here are your hero stats {player.stats}")
player.print_stats()