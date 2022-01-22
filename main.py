import random
# This nested dictionary stores all the attacks, damages and chance to hit (out of six)
# this should allow me to call attacks based on user inputs, also add more attacks at will
atck_dict = dict(Punch      = {'Damage': 35, 'Chance': 2},
                 Kick       = {'Damage': 45, 'Chance': 4},
                 Uppercut   = {'Damage': 55, 'Chance': 5},
                 Headbutt   = {'Damage': 50, 'Chance': 5},
                 Taunt      = {'Damage': 10, 'Chance': 1})

# This is the most recently selected attack, must have '' around it to succesfully call the dictionary
attack = ""
roll = ""
player_health = 100
computer_health = 100

# This is a six sided dice roll based on import random at the top of the page
def dice(max):
    global roll
    roll = 0
    roll += random.randint(1,max)

# Counts the number of attacks in the dictionary and then randomly sets 'roll' to a number from 0 to that number
# minus one. (it has to be from zero to len -1 because python lists start at zero
def computer_attack_rand():
    global roll
    roll = 0
    roll += random.randint(0, (len(atck_dict.keys())-1))

def attack_try():
    try:
        attack()
    except:
        print("That isn't an attack, try again")
        attack_try()

# This is the fuction for when the player is attacking the computer
def attack():
    global computer_health
# This line asks the user to attack and assigns it to the attack variable (there is also some cleaning to
# make it match the dictionary better
    attack = input("Punch or Kick?").strip().capitalize().replace(' ', '_')
# This prints the dice roll and the chosen attack chance (might be deletable)
    print("Dice Roll:" + str(roll) + " you need "+ str(atck_dict[attack]['Chance']) + " or more to " + attack)

# This checks if the dice roll is greater than to or equal to attack chance, looked up from the dictionary
    if roll >= atck_dict[attack]['Chance']:
# This looks up the damage of the typed attack from the dictionary
        computer_health -= atck_dict[attack]['Damage']
# This checks if health is zero or lower it prints what just happened back to the user
# It's frustrating that this is a nested if statment, but because attack can't be a global variable
# for some reason I can't make it global without it breaking the function
        if computer_health <= 0:
            print("You knocked them out!")
        else:
            print("You " + attack + "ed for " + str(atck_dict[attack]['Damage']) + " damage and their health is now " + str(computer_health))
    else:
        print("You missed!")

def defence():
    global player_health
# Randomly picks an attack for the computer to attempt, all attacks are given equal weighting
    computer_attack_rand()
    attack = list(atck_dict.keys())[roll]
    dice(6)
    if roll >= atck_dict[attack]['Chance']:
        player_health -= atck_dict[attack]['Damage']
        if player_health <= 0:
            print("They knocked you out!")
        else:
            print("They " + attack + "ed you for " + str(atck_dict[attack]['Damage']) + " damage and your health is now " + str(player_health))
    else:
        print("They tried to " + attack + " you but missed!")

while computer_health >= 0:
    if player_health <= 0:
        break
    dice(6)
    attack_try()
    if computer_health <= 0:
        break
    defence()

print("Game Over!")
