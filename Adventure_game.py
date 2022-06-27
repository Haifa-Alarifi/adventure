import time
import random

enemy_creature = ['wicked fairie', 'pirate', 'troll', 'dragon']
enemy = random.choice(enemy_creature)


def print_pause(message_to_ptint):
    print(message_to_ptint)
    time.sleep(2)


def intro():
    print_pause("You find yourself standing in an open field,"
                "filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a " + enemy + " is somewhere "
                "around here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very "
                "effective) dagger.")
    field


def fight(item):
    if "sword" in item:
        print_pause("As the " + enemy + " moves to attack, you unsheath your "
                    "new sword.")
        print_pause("The Sword of Ogoroth shines brightly in your hand as you "
                    "brace yourself for the attack.")
        print_pause("But the " + enemy + " takes one look at your shiny new "
                    "toy and runs away!")
        print_pause("You have rid the town of the " + enemy + ". You are "
                    "victorious!")
    else:
        print_pause("You do your best...")
        print_pause("but your dagger is no match for the " + enemy + ".")
        print_pause("You have been defeated!")
        item.append("sword")
    play_again()


def cave(item):
    if "sword" in item:
        print_pause("You peer cautiously into the cave.")
        print_pause("You've been here before, and gotten all the good"
                    " stuff. It's just an empty cave now.")
        print_pause("You walk back out to the field.")
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and take the sword "
                    "with you.")
        print_pause("You walk back out to the field.")
        item.append("sword")
    field(item)


def field(item):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    choice = input("(Please enter 1 or 2.)")
    if choice == '1':
        house(item)
    elif choice == '2':
        cave(item)
    else:
        print_pause("(Please enter 1 or 2.)")
        field(item)


def house(item):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and out steps "
                "a " + enemy + ".")
    print_pause("Eep! This is the " + enemy + "'s house!")
    print_pause("The " + enemy + " attacks you!")

    if "sword" not in item:
        print_pause("You feel a bit under-prepared for this, what with "
                    "only having a tiny dagger.")

    choice2 = input("Would you like to (1) fight or (2) run away?")
    if choice2 == '1':
        fight(item)
    elif choice2 == '2':
        print_pause("You run back into the field. Luckily, you don't"
                    "seem to have been followed.")
        field(item)
    else:
        fight(item)


def play_again():
    play = input("Would you like to play again? (y/n)")
    if play == 'y':
        print_pause("Excellent! Restarting the game ...")
        play_game()
    elif play == 'n':
        print_pause("Thanks for playing! See you next time.")
    else:
        play_again()


def play_game():
    item = []
    intro()
    field(item)


play_game()
