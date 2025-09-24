# Dictionary of Player Stats
hero_stats = {
    "name":"hero", # key : value (name -> key) : (hero -> value)
    "Strength" : 7,
    "health" : 100.0,
    }
hero_max_health = 100.0

#inventory
health_potion_strength = 5
hero_iventory = ("sword", "health potion", "rope")

#Flee, Game Over
def quit ():
    print ("You Chose to Flee")
    print ("Game Over")
    return False

#Lists Player Stats
def player_stats ():
    for key, value in hero_stats.items():
        print(f"{key} : {value}" ) 

def player_move ():
    pass

def player_attack ():
    pass

def player_heal(item_name):
     
    if (hero_iventory.count("health potion") <=0):
        print(f"You dont have any {item_name}")
        return

    print (f"You've used {item_name} you've restored {health_potion_strength} health")
            hero_stats["health"] = hero_stats["health"] + health_potion_strength

    if (hero_stats{"health"}>= hero_max_health):
        print ("You;ve reach max health")
        hero_stats{"health"} = hero_max_health


    print (f"your health is now {hero_stats['health']}")
    hero_iventory.remove("health potion")
    print(f"your inventory is now {hero_iventory}")

def use_item():
    item_name = input(f"What item do you want to use?{hero_iventory}\n").lower()
    print (f"The item you want to use is {item_name}")

    match item_name:
        case "health potion":
            player_heal(item_name)
        case "rope":
            pass
        case "sword":
            pass
        case _:
            print (f"{item_name} is not in your inventory")
            


#temporary function
def damage_player():
    hero_stats["health"] -= 10
    print (f"your health is now {hero_stats["health"]}")

IsPlaying = True

#asks Player for their name
hero_stats["name"] = input ("what is ypour name?\n")

#Display player stats
player_stats()

#actions player can make
while (IsPlaying):


    action = input("\nSelect Action: Attack, Use, Move & Flee\n").lower()
    print (f"Player Action:{action}")

    if (action == "flee"):
        IsPlaying = quit()

    elif (action == "move"):
        player_move()
    elif (action == "attack"):
        #player_attack()
        damage_player()
    elif (action == "use"):
        use_item()
    else:
        print (f"{action} is an invalid action")



        

    print ("End of Loop")

    

