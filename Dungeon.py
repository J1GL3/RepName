# Dictionary of Player Stats
hero_stats = {
    "name":"hero", # key : value (name -> key) : (hero -> value)
    "Strength" : 7,
    "Health" : 100.0,
    }


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

IsPlaying = True

#asks Player for their name
hero_stats["name"] = input ("what is ypour name?\n")

#Display player stats
player_stats()

#actions player can make
while (IsPlaying):


    action = input("\nSelect Action: Attack, Move & Flee\n").lower()

    print (f"Player Action:{action}")

    if (action == "flee"):
        IsPlaying = quit()

    elif (action == "move"):
        player_move()
    elif (action == "attack"):
        player_attack()
    else:
        print (f"{action} is an invalid action")
        

    print ("End of Loop")
    #hi
    

