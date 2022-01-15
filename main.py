import random

fighter_1_health = 100
fighter_2_health = 100
punch = 25
punch_chance = 3
kick = 45
kick_chance = 5
attack_damage = ""
roll = random.randint(1, 6)


def dice():
    global roll
    roll = 0
    roll += random.randint(1, 6)


def punch_fnt():
    global fighter_2_health
    if roll >= punch_chance:
        print("You punched for " + str(punch) + " damage!")
        fighter_2_health -= punch
    else:
        print("You missed!")


def kick_fnt():
    global fighter_2_health
    if roll >= kick_chance:
        print("You kicked for " + str(kick) + " damage!")
        fighter_2_health -= kick
    else:
        print("You missed!")


def punch_defence():
    global fighter_1_health
    dice()
    if roll >= punch_chance:
        print("They punched you!")
        fighter_1_health -= punch
        print("Your health is now " + str(fighter_1_health))
    else:
        print("They tried to punch you but missed!")


def kick_defence():
    global fighter_1_health
    dice()
    if roll >= kick_chance:
        print("They kicked you!")
        fighter_1_health -= kick
        print("Your health is now " + str(fighter_1_health))
    else:
        print("They tried to kick you but missed!")


def attack():
    global attack_damage
    attack_damage = input("Punch or Kick?").title().strip()
    dice()
    if not(attack_damage == "Punch" or "Kick"):
        print("try again")
        attack()
    else:
        if attack_damage == "Punch":
            punch_fnt()
        if attack_damage == "Kick":
            kick_fnt()


def defend():
    dice()
    if roll >= 5:
        kick_defence()
    else:
        punch_defence()


while fighter_2_health > 0 or fighter_1_health > 0:
    attack()
    print("They have " + str(fighter_2_health) + " health left")
    defend()

print("Game Over!")
