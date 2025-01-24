import random
#Dice Options created using list() and range()
diceOptions = list(range(1,7))

# Weapon list
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

print("Availabe weapons: ", ', '.join(weapons))

def getCombatStrength(prompt):
    while True:
        value = int(input(prompt))
        if 1<= value <= 6:
            return value    
        else:
            print("Invalid value. Please enter a number between 1 and 6.")
combatStrength = getCombatStrength("Enter a number between 1-6 for Player")
mCombatStrength = getCombatStrength("Enter a number between 1-6 for Monster")

for j in range(1, 21, 2):
    heroRoll = random.choice(diceOptions)
    monsterRoll = random.choice(diceOptions)

    heroWeapon = weapons[heroRoll - 1]
    monsterWeapon = weapons[monsterRoll - 1]

    heroTotal = combatStrength + heroRoll
    monsterTotal = mCombatStrength + monsterRoll

    print(f"\n Hero rolled {heroRoll}, Monster rolled {monsterRoll}")
    print(f"\n Hero Selected {heroWeapon}, Monster selected {monsterWeapon}")
    print(f"\n Hero total strength is {heroTotal}, Monster total strength is {monsterTotal}")
    if heroTotal > monsterTotal:
        print("Player wins!")
    elif heroTotal < monsterTotal:
        print("Monster wins!")
    else:
        print("It's a tie!")
    