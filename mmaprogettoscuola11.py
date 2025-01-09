import random

class Fighter:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, opponent, attack_type):
        if attack_type == opponent.defense_type:
            return 0  
        else:
            damage = random.randint(10, 20)
            opponent.health -= damage
            return damage

    def defend(self, defense_type):
        self.defense_type = defense_type

def fight(user_fighter, opponent_fighter, user_control):
    if user_fighter.name == "Jon Jones" and opponent_fighter.name == "Dana White":
        print(f"{user_fighter.name} and {opponent_fighter.name} decide to kiss instead of fighting!")
        return True

    print(f"Fight between {user_fighter.name} and {opponent_fighter.name}!")
    while user_fighter.health > 0 and opponent_fighter.health > 0:
        if user_control:
            
            attack_type = input(f"Choose your attack type (high/low/takedown): ").strip().lower()
            if attack_type == "takedown":
                if random.randint(1, 4) == 1:
                    user_fighter.health -= 50
                    print("Takedown attempt failed! You lost 50 health.")
                else:
                    print("Takedown successful! The fight is now on the ground.")
                    if random.randint(1, 2) == 1:
                        print("You won the fight on the ground!")
                        return True
                    else:
                        print("You failed to win on the ground. The fight continues standing.")
            else:
                opponent_defense = random.choice(["high", "low"])
                opponent_fighter.defend(opponent_defense)
                damage = user_fighter.attack(opponent_fighter, attack_type)
                print(f"{user_fighter.name} attacks {opponent_fighter.name} for {damage} damage. {opponent_fighter.name} defended {opponent_defense}. {opponent_fighter.name} health: {opponent_fighter.health}")
                if opponent_fighter.health <= 0:
                    print(r"""
 __  ______  __  __  _      _______  __                         
 \ \/ / __ \/ / / / | | /| / /  _/ |/ /
  \  / /_/ / /_/ /  | |/ |/ _/ //    / 
  /_/\____/\____/   |__/|__/___/_/|_/  
                                       
                                                                                                                                      \$$
    """)
                    return True

           
            user_defense = input(f"Choose your defense type (high/low): ").strip().lower()
            user_fighter.defend(user_defense)
            attack_type = random.choice(["high", "low"])
            damage = opponent_fighter.attack(user_fighter, attack_type)
            print(f"{opponent_fighter.name} attacks {user_fighter.name} for {damage} damage. {opponent_fighter.name} attacked {attack_type}. {user_fighter.name} health: {user_fighter.health}")
            if user_fighter.health <= 0:
                print(r"""
__  ______  __  __   __    ____  _____ ______
\ \/ / __ \/ / / /  / /   / __ \/ ___// ____/
 \  / / / / / / /  / /   / / / /\__ \/ __/   
 / / /_/ / /_/ /  / /___/ /_/ /___/ / /___   
/_/\____/\____/  /_____/\____//____/_____/   
                                             
                                                                                                                                   \$$
    """)
                return False
        else:
            
            attack_type = random.choice(["high", "low", "takedown"])
            if attack_type == "takedown":
                if random.randint(1, 4) == 1:
                    user_fighter.health -= 50
                    print("Takedown attempt failed! You lost 50 health.")
                else:
                    print("Takedown successful! The fight is now on the ground.")
                    if random.randint(1, 2) == 1:
                        print("You won the fight on the ground!")
                        return True
                    else:
                        print("You failed to win on the ground. The fight continues standing.")
            else:
                opponent_defense = random.choice(["high", "low"])
                opponent_fighter.defend(opponent_defense)
                damage = user_fighter.attack(opponent_fighter, attack_type)
                print(f"{user_fighter.name} attacks {opponent_fighter.name} for {damage} damage. {opponent_fighter.name} defended {opponent_defense}. {opponent_fighter.name} health: {opponent_fighter.health}")
                if opponent_fighter.health <= 0:
                    print(f"{opponent_fighter.name} is knocked out! {user_fighter.name} wins!")
                    return True

            user_defense = random.choice(["high", "low"])
            user_fighter.defend(user_defense)
            attack_type = random.choice(["high", "low"])
            damage = opponent_fighter.attack(user_fighter, attack_type)
            print(f"{opponent_fighter.name} attacks {user_fighter.name} for {damage} damage. {opponent_fighter.name} attacked {attack_type}. {user_fighter.name} health: {user_fighter.health}")
            if user_fighter.health <= 0:
                print(f"{user_fighter.name} is knocked out! {opponent_fighter.name} wins!")
                return False

def tournament(user_fighter, fighters):
    opponents = list(fighters.values())
    opponents.remove(user_fighter)
    wins = 0

    while wins < 3:
        opponent_fighter = random.choice(opponents)
        opponents.remove(opponent_fighter)
        print(f"Round {wins + 1}: {user_fighter.name} vs {opponent_fighter.name}")
        if not fight(user_fighter, opponent_fighter, True):
            print(f"{user_fighter.name} is knocked out! You lose the tournament.")
            return False
        wins += 1
        user_fighter.health = 100 

    print(f"{user_fighter.name} wins the tournament!")
    return True

if __name__ == "__main__":
    lightweight_middleweight_fighters = {
        "islam makachev": Fighter("Islam Makachev", 100, 20),
        "dustin poirier": Fighter("Dustin Poirier", 100, 20),
        "khamzat chimaev": Fighter("Khamzat Chimaev", 100, 20),
        "sean strickland": Fighter("Sean Strickland", 100, 20)
    }

    heavyweight_fighters = {
        "jon jones": Fighter("Jon Jones", 100, 20),
        "ankalev": Fighter("Ankalev", 100, 20),
        "stipe miochic": Fighter("Stipe Miochic", 100, 20),
        "alex pereira": Fighter("Alex Pereira", 100, 20),
        "dana white": Fighter("Dana White", 100, 20)
    }

    wins = 0
    losses = 0

    while True:
        create_custom_fighter = input("Do you want to create a custom fighter? (yes/no): ").strip().lower() == "yes"
        if create_custom_fighter:
            custom_fighter_name = input("Enter the name of your custom fighter: ").strip()
            weight_class = input("Choose weight class for your custom fighter (lightweight/middleweight or heavyweight): ").strip().lower()
            if weight_class in ["lightweight", "middleweight"]:
                lightweight_middleweight_fighters[custom_fighter_name.lower()] = Fighter(custom_fighter_name, 100, 20)
            elif weight_class == "heavyweight":
                heavyweight_fighters[custom_fighter_name.lower()] = Fighter(custom_fighter_name, 100, 20)
            else:
                print("Invalid weight class selection.")
                continue

        weight_class = input("Choose weight class (lightweight/middleweight or heavyweight): ").strip().lower()
        if weight_class in ["lightweight", "middleweight"]:
            fighters = lightweight_middleweight_fighters
        elif weight_class == "heavyweight":
            fighters = heavyweight_fighters
        else:
            print("Invalid weight class selection.")
            continue

        mode = input("Do you want to play a single match or a tournament? (single/tournament): ").strip().lower()
        
        if mode == "single":
            user_control = input("Do you want to control the fighter? (yes/no): ").strip().lower() == "yes"
            if user_control:
                print("Available fighters: ", ", ".join(fighters.keys()))
                user_fighter_name = input("Choose your fighter: ").strip().lower()
                if user_fighter_name == "bruce lee":print("You have chosen the legendary Bruce Lee! Prepare for an epic fight!")
                opponent_fighter_name = input("Choose your opponent: ").strip().lower()
                user_fighter = fighters.get(user_fighter_name)
                opponent_fighter = fighters.get(opponent_fighter_name)
            else:
                user_fighter = random.choice(list(fighters.values()))
                opponent_fighter = random.choice(list(fighters.values()))
                

            if user_fighter and opponent_fighter:
                if fight(user_fighter, opponent_fighter, user_control):
                    wins += 1
                else:
                    losses += 1
            else:
                print("Invalid fighter selection.")
        elif mode == "tournament":
            print("Available fighters: ", ", ".join(fighters.keys()))
            user_fighter_name = input("Choose your fighter: ").strip().lower()
            user_fighter = fighters.get(user_fighter_name)
            if user_fighter:
                if tournament(user_fighter, fighters):
                    wins += 1
                else:
                    losses += 1
            else:
                print("Invalid fighter selection.")
        else:
            print("Invalid mode selection.")

        print(f"Statistics: {wins} wins, {losses} losses")
        continue_playing = input("Do you want to continue playing? (yes/no): ").strip().lower() == "yes"
        if not continue_playing:
            break