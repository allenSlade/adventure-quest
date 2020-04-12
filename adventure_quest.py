import time
import random
items = []


def print_pause(message):
    print(message)
    time.sleep(2)


def intro():
    wizard = random.choice(["Wizard", "Guardian", "Elder"])
    print_pause("Your kingdom has fallen into darkness "
                "and only you can save it.\n")
    print_pause("You have been sent on a quest to transport the Stone of Ohr "
                "through the mountain to deliver it to the " + wizard + ".")
    print_pause("Only then will darkness leave the kingdom.")
    print_pause("Before you depart, "
                "you must pick a weapon to take on your quest.\n")
    print_pause("Will you take the Cloak of Deception "
                "or the Hammer of Gabar?\n")
    selection = input("Enter 1 for the Cloak of Deception.\n"
                      "Enter 2 for the Hammer of Gabar\n")
    if selection == '1':
        items.append("Cloak of Deception")
        print_pause("You have chosen the Cloak of Deception.\n")
        passageways()
    elif selection == '2':
        items.append("Hammer of Gabar")
        print_pause("You have chosen the Hammer of Gabar.\n")
        passageways()
    else:
        print_pause("Please enter 1 or 2.\n")


def passageways():
    print_pause("You travel tirelessly across the plains and valleys.")
    print_pause("You have reached the mountain caverns "
                "and entered its dark tunnels.")
    print_pause("You come to a split in the passageway.")
    print_pause("You must go right or left. Which way will you go?\n")
    selection = input("Enter 1 for right\n"
                      "Enter 2 for left\n")
    if selection == '1':
        right_passageway()
    elif selection == '2':
        left_passageway()
    else:
        print_pause("Please enter 1 or 2.\n")


def right_passageway():
    watercraft = random.choice(["rowboat", "pontoon", "raft"])
    aerial = random.choice(["frayed rope-bridge", "rickety old bridge"])
    print_pause("You walk down the right passageway and encounter a river.")
    print_pause("There is a " + aerial + " that is barely standing "
                "and a " + watercraft + " on the river bank.")
    print_pause("You must use one to cross the river. "
                "Which one will you choose?\n")
    selection = input("Enter 1 for the watercraft\n"
                      "Enter 2 for the bridge\n")
    if selection == '1':
        print_pause("You chose the watercraft. "
                    "It's full of holes and you sink.\n")
        game_over()
        play_again()
    elif selection == '2':
        print_pause("You chose the bridge.\n"
                    "You cross the river safely "
                    "and find yourself back at the start of your journey.\n")
        passageways()
    else:
        print_pause("Please enter 1 or 2.\n")


def left_passageway():
    serpent = random.choice(["python", "cobra"])
    print_pause("You walk down the left passageway "
                "and encounter a " + serpent + ".")
    print_pause("He has keen eyesight and moves swiftly to attack you.")
    if "Cloak of Deception" in items:
        selection = input("Enter 1 to use the Cloak of Deception\n"
                          "Enter 2 to run away\n")
        if selection == '1':
            print_pause("You put on the Cloak of Deception and disappear "
                        "into the darkness of the cavern.")
            print_pause("The python cannot find you "
                        "and you pass safely through the mountain "
                        "to deliver the Stone of Ohr.\n")
            print_pause("You saved the kingdon!")
            play_again()
        elif selection == '2':
            print_pause("You run away and your quest is forfeit.")
            game_over()
            play_again()
        else:
            print_pause("Please enter 1 or 2.\n")
    elif "Hammer of Gabar" in items:
        selection = input("Enter 1 to use the Hammer of Gabar to fight\n"
                          "Enter 2 to run away\n")
        if selection == '1':
            print_pause("You pull out the Hammer of Gabar, "
                        "but the python is too quick and he defeats you.")
            game_over()
            play_again()
        elif selection == '2':
            print_pause("You run away and your quest is forfeit.")
            game_over()
            play_again()
        else:
            print_pause("Please enter 1 or 2.\n")


def game_over():
    print_pause("GAME OVER")


def play_again():
    selection = input("Would you like to play again? (y/n)\n").lower()
    if 'y' in selection:
        intro()
    elif 'n' in selection:
        print_pause("Thanks for playing. Goodbye!")
    else:
        print_pause("Please enter y/n\n")


def play_game():
    intro()


play_game()
