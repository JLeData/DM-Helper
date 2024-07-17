# This is a program to assist DnD dungeon masters with their game.
# Current tools available in this build are:
    # Dice Rolling
    # Iniative Tracker
    # Note Tracker
    # Character Sheet Viewer

# Libraries
import time
import sys
import random
import os

# Disclaimer message
print("Disclaimer: This tool is developed for educational and practical purposes to assist Dungeon Masters in managing their Dungeons & Dragons games.")
print("It is not a substitute for professional advice or judgment. Use at your own discretion.")
print("I am not liable for any outcomes or consequences resulting from the use of this tool.")
print("")

# Specify the directory path to the desktop on Windows
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
folder_name = 'DnD Helper Data'
folder_path = os.path.join(desktop_path, folder_name)

# Ensure the folder exists
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Program stall
def press_enter():
    input("\nPress enter to continue: ")

# Loading effect
def loading_effect(duration=3):
    print("\nLoading", end="")
    for _ in range(duration):
        time.sleep(1)
        print(".", end="")
        sys.stdout.flush()
    print("")

# Create rolling effect
def rolling_effect(duration=3):
    print("\nRolling", end="")
    for _ in range(duration):
        time.sleep(1)
        print(".", end="")
        sys.stdout.flush()
    print("")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Dice rolling Functions

# Comments for 1 and 20 rolls
critical_fail_comment = [
    "You rolled a natural 1! Critical fail!",
]

# My critical fail comments
    #"Nice 1, lol.",
    #"RNG is not by your side today. Natural 1.",
    #"I am the 1, the 1! Critical fail!",
    #"Lmao gg no re, take that failed roll.",
    #"Skill issue tbh.",
    #"I bet you want to uninstall with this roll.",
    #"At least you can't roll a 0.",
    #"You are my special.",
    #"Taunt to get bodied, nice 1.",
    #"Will the DM end you with this roll? mayhaps.",
    #"Your action backfires spectacularly. Natural 1.",
    #"The dice said LMAO.",
    #"Jordan having a great time making these messages. Stop rolling 1s lul."

critical_success_comment = [
    "You rolled a natural 20! Critical Hit!",
]

# Critical success comments
    #"Sugoi!",
    #"Nah, I'd Win.",
    #"Pogu",
    #"Your action goes perfectly! Natural 20!",
    #"Nice roll, brother.",
    #"He's him.",
    #"You just might win this encounter, Nat 20!",
    #"A swing and a crit!"

# Dice roller
def roll_dice(dice_type, num_dice, modifier=0):
    print(f"Rolling {num_dice} d{dice_type}...")
    rolling_effect()

    original_results = [] # Store original rolls
    modified_results = [] # Store modified rolls
    
    for _ in range(num_dice): # Using _ as variable 
        roll_result = random.randint(1, dice_type) # Start roll at 1 and dice_type value 
        original_results.append(roll_result) # append roll to list
        modified_result = roll_result + modifier
        modified_results.append(modified_result)
        
        time.sleep(.5) # effect for rolling

        # Check for 1s and 20s with comments
        if dice_type == 20: # Check for if d20 is rolled
            if roll_result == 1:
                comment = random.choice(critical_fail_comment) # Retrieve a random comment from list above
                print(f"\n  Roll {_ + 1}: Original Roll: {roll_result}, \n  Roll with modifier: {modified_result} - {comment}")
            elif roll_result == 20:
                comment = random.choice(critical_success_comment)
                print(f"\n  Roll {_ + 1}: Original Roll: {roll_result}, \n  Roll with modifier: {modified_result} - {comment}")
            else:
                print(f"\n  Roll {_ + 1}: Original Roll: {roll_result}, \n  Roll with modifier: {modified_result}")
        else:
            print(f"\n  Roll {_ + 1}: Original Roll: {roll_result}, \n  Roll with modifier: {modified_result}") # d20 is not rolled
    
    total_result = sum(modified_results) # Adding together dice roll

    print(f"\n Total roll(with modifier): {[total_result]}")
    

# Roll again function
def re_roll():
    print("\n would you like to do more rolls?(y/n)")
    confirm = input("> ").strip().lower()

    while confirm not in ['y','n']:
        print("\nInvalid entry, Please try again: ")
        confirm = input("> ").strip().lower()
    
    if confirm == 'y':
        dice_rolling_menu()
    elif confirm == 'n':
        print("\nReturning to main menu.")
        press_enter()

# Function to handle dice rolling menu
def dice_rolling_menu():
    print("\nDice Rolling Menu:\n")
    print("1. Roll d4")
    print("2. Roll d6")
    print("3. Roll d8")
    print("4. Roll d10")
    print("5. Roll d12")
    print("6. Roll d20")
    print("7. Roll d100")
    print("8. Back to Main Menu")
    
    choice = input("\nEnter your choice: ").strip()
    
    if choice == "8":
        return  # Return to main menu
    
    while choice not in ['1', '2', '3', '4', '5', '6', '7']:
        choice = input("\nInvalid choice. Please enter a number from 1 to 7: ").strip()
        
    num_dice = int(input("\nEnter the number of dice to roll: ").strip()) 
    modifier = int(input("Enter the modifier (optional, 0 if none): ").strip())
    
    if choice == '1':
        dice_type = 4
    elif choice == '2':
        dice_type = 6
    elif choice == '3':
        dice_type = 8
    elif choice == '4':
        dice_type = 10
    elif choice == '5':
        dice_type = 12
    elif choice == '6':
        dice_type = 20
    elif choice == '7':
        dice_type = 100
    
    roll_dice(dice_type, num_dice, modifier) # retrieve inputted data and add into dice roller function
    re_roll() # reloop until chosen not to

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Initiative tracker functions

# Initiative tracker data
initiative_tracker = []

# Function to get the initiative tracker file path
def get_initiative_tracker_file_path():
    return os.path.join(folder_path, 'initiative_tracker.txt')

# Function to save initiative tracker data
def save_initiative_tracker():
    try:
        with open(get_initiative_tracker_file_path(), 'w') as file: # open file in writing mode using the return folder path and initiative tracker.txt, with block closes file
            for character in initiative_tracker: # loop initiative tracker list
                file.write(f"{character[0]}, {character[1]}\n") # store in tuple for later use
    except Exception as e:
        print(f"\nAn error occurred saving the tracker: {str(e)}")

# Function to load initiative tracker data
def load_initiative_tracker():
    try:
        with open(get_initiative_tracker_file_path(), 'r') as file:
            for line in file:
                character, initiative = line.strip().split(',')
                initiative_tracker.append((character.strip(), int(initiative.strip())))
    except FileNotFoundError:
        print("No previous initiative tracker found. Starting a new one.")

# Function to display initiative tracker ordered by initiative (highest to lowest)
def view_current_battle():
    if not initiative_tracker: # Check if initiative tracker has data
        print("\nNo characters in the initiative tracker.")
    else:
        initiative_tracker.sort(key=lambda x: x[1], reverse=True) # select initiative to be sorted via lambda in the [1] position
        print("\nCurrent Battle Order:\n")
        for index, character in enumerate(initiative_tracker, start=1): # assign index to each character
            print(f"{index}. {character[0]} - Initiative: {character[1]}")

# Function to add a character to the initiative tracker
def add_char_initative():
    character = input("\nEnter character name: ").strip()
    initiative = int(input("Enter initiative score: "))
    initiative_tracker.append((character, initiative))
    print(f"\n{character} added to the battle with initiative {initiative}.")
    save_initiative_tracker()
    add_more()

# add more characters
def add_more():
    print("\nWould you like add another character?(y/n)")
    confirm = input("> ").strip().lower()

    while confirm not in ['y','n']:
        print("\nInvalid entry, Please try again: ")
        confirm = input("> ").strip().lower()
    
    if confirm == 'y':
        add_char_initative()
    elif confirm == 'n':
        print("\nReturning to tracker menu.")
        press_enter()

# Function to delete a character from the initiative tracker
def delete_character():
    view_current_battle()
    try:
        if initiative_tracker:
            idx = int(input("\nEnter the index of the character to delete: ")) - 1
            if 0 <= idx < len(initiative_tracker):
                deleted_character = initiative_tracker.pop(idx) # use pop to remove the index within initiative tracker
                loading_effect()
                print(f"\n{deleted_character[0]} has been removed from the battle.")
                save_initiative_tracker()
            else:
                print("\nInvalid index. No character deleted.")
        else:
            print("\nNo characters to delete.")
            press_enter()
    except Exception as e:
        print(f"\nAn error occurred while deleting a character: {str(e)}")

# New battle (delete current one)
def start_new_battle():
    initiative_tracker.clear() # clear initiative tracker
    loading_effect()
    save_initiative_tracker() 
    print("\nInitiative tracker has been cleared. Ready for new battle.")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Campaign notes functions

# Campaign notes data
campaign_notes = []

# Function to get the campaign notes file path
def get_campaign_notes_file_path():
    return os.path.join(folder_path, 'campaign_notes.txt')

# Function to save campaign notes data
def save_campaign_notes():
    try:
        with open(get_campaign_notes_file_path(), 'w') as file:
            for note in campaign_notes:
                file.write(f"{note}\n")
    except Exception as e:
        print(f"\nAn error occurred saving the campaign notes: {str(e)}")

# Function to load campaign notes data
def load_campaign_notes():
    try:
        with open(get_campaign_notes_file_path(), 'r') as file:
            for line in file:
                campaign_notes.append(line.strip())
    except FileNotFoundError:
        print("No previous campaign notes found. Starting new notes.")

# Function to display campaign notes
def view_campaign_notes():
    if not campaign_notes:
        print("\nNo campaign notes available.")
    else:
        print("\nCampaign Notes:\n")
        for index, note in enumerate(campaign_notes, start=1):
            print(f"{index}. {note}")

# Function to add a note to the campaign notes
def add_note():
    note = input("\nEnter the campaign note: ").strip()
    campaign_notes.append(note)
    print(f"\nNote added: {note}")
    save_campaign_notes()
    add_more_notes()

# Function to prompt for adding more notes
def add_more_notes():
    print("\nWould you like to add another note? (y/n)")
    confirm = input("> ").strip().lower()

    while confirm not in ['y', 'n']:
        print("\nInvalid entry, please try again: ")
        confirm = input("> ").strip().lower()
    
    if confirm == 'y':
        add_note()
    elif confirm == 'n':
        print("\nReturning to main menu.")
        press_enter()

# Function to delete a note from the campaign notes
def delete_note():
    view_campaign_notes()
    try:
        index = int(input("\nEnter the index of the note to delete: "))
        if 1 <= index <= len(campaign_notes):
            note = campaign_notes.pop(index - 1)
            print(f"\nNote deleted: {note}")
            save_campaign_notes()
        else:
            print("\nInvalid index. Please try again.")
    except Exception as e:
        print(f"\nAn error occurred deleting campaign notes: {str(e)}")

# Function to clear all notes from the campaign notes
def clear_campaign_notes():
    print("\nAre you sure you want to clear all campaign notes? (y/n)")
    confirm = input("> ").strip().lower()
    if confirm == 'y':
        loading_effect()
        campaign_notes.clear()
        save_campaign_notes()
        print("\nCampaign notes cleared.")
    else:
        print("\nClearing campaign notes canceled.")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Character sheet functions


# Global variable for storing characters
characters = []

# Function to get the character data file path
def get_characters_file_path():
    folder_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'D&D Helper Data') # create file path to folder
    os.makedirs(folder_path, exist_ok=True)  # Ensure folder exists
    return os.path.join(folder_path, 'characters.txt')

def save_characters():
    try:
        with open(get_characters_file_path(), 'w') as file:
            for character in characters:
                file.write(f"{character['player_name']},{character['name']},{character['race']},"
                           f"{character['class']},{character['level']},"
                           f"{';'.join(character['languages']) if character['languages'] else ''},"
                           f"{character['stats']['STR']},{character['stats']['DEX']},{character['stats']['CON']},"
                           f"{character['stats']['INT']},{character['stats']['WIS']},{character['stats']['CHA']},"
                           f"{character['armor_class']},{character['speed']},{character['health']},"
                           f"{character['dark_vision']}\n")
        print("\nCharacter data saved successfully.")
    except Exception as e:
        print(f"\nAn error occurred saving character data: {str(e)}")


# Function to load character data
def load_characters():
    global characters # Define character in global scope
    characters = []  # Initiate empty list for characters
    try:
        with open(get_characters_file_path(), 'r') as file:
            for line in file:
                data = line.strip().split(',') # strip and split line of text
                if len(data) >= 15:  # Ensure all fields are present
                    languages = data[5].split(';') if data[5] else []  # Split languages if multiple
                    new_character = {
                        'player_name': data[0],
                        'name': data[1],
                        'race': data[2],
                        'class': data[3],
                        'level': data[4],
                        'languages': languages,
                        'stats': {
                            'STR': int(data[6]),
                            'DEX': int(data[7]),
                            'CON': int(data[8]),
                            'INT': int(data[9]),
                            'WIS': int(data[10]),
                            'CHA': int(data[11])
                        },
                        'armor_class': int(data[12]),
                        'speed': int(data[13]),
                        'health': int(data[14]),
                        'dark_vision': data[15]
                    }
                    characters.append(new_character)
            print("\nCharacter data loaded successfully.")
    except FileNotFoundError:
        print("No previous character data found. Starting with an empty character list.")
    except Exception as e:
        print(f"\nAn error occurred loading character data: {str(e)}")

# Function to display character sheet
def display_character_sheet(character):
    loading_effect()
    print("  _______________________________________________________________")
    print(" |                                                               |")
    print(" |                      Character Sheet                          |")
    print(" |_______________________________________________________________|")
    print(f" Player Name: {character['player_name']}") 
    print(f"    Character Name: {character['name']}") 
    print(f"    Class: {character['class']}")
    print(f"    Level: {character['level']}")
    print(f"    Race: {character.get('race', '')}")
    print("  _______________________________________________________________")
    print(" |                                                               |")
    print(" |                          Stats                                |")
    print(" |_______________________________________________________________|")
    print("")
    print(f" STR: {character['stats']['STR']:>3} | DEX: {character['stats']['DEX']:>3} | CON: {character['stats']['CON']:>3} | " # use :<(number) as spaces within the value
          f" INT: {character['stats']['INT']:>3} | WIS: {character['stats']['WIS']:>3} | CHA: {character['stats']['CHA']:>3}")
    print("  _______________________________________________________________")
    print(f"    Armor Class: {character['armor_class']}") 
    print(f"    Speed: {character['speed']}")
    print(f"    Health: {character['health']}")
    print(f"    Languages: {', '.join(character.get('languages', []))}")
    print(f"    Dark Vision: {character['dark_vision']}")
    print(" ________________________________________________________________")
    press_enter()

# Function to add a new character
def add_character():
    print("\nAdding a new character:")
    try:
        player_name = input("Enter Player Name: ").strip()
        name = input("Enter Character Name: ").strip()
        race = input("Enter Race: ").strip()
        class_name = input("Enter Class: ").strip()
        level = input("Enter Level: ").strip()
        languages = []
        
        while True: # add more languages
            language = input("Enter a Language (press Enter to finish): ").strip()
            if not language:
                break
            languages.append(language)

        str_stat = int(input("Enter Strength (STR): "))
        dex_stat = int(input("Enter Dexterity (DEX): "))
        con_stat = int(input("Enter Constitution (CON): "))
        int_stat = int(input("Enter Intelligence (INT): "))
        wis_stat = int(input("Enter Wisdom (WIS): "))
        cha_stat = int(input("Enter Charisma (CHA): "))
        armor_class = int(input("Enter Armor Class: "))
        speed = int(input("Enter Speed (feet per round): "))
        health = int(input("Enter Health: "))
        dark_vision = input("Does the character have Dark Vision? (yes/no): ").strip().lower() == "yes"

        new_character = {
            'name': name,
            'class': class_name,
            'level': level,
            'player_name': player_name,
            'race': race,
            'languages': languages,
            'stats': {
                'STR': str_stat,
                'DEX': dex_stat,
                'CON': con_stat,
                'INT': int_stat,
                'WIS': wis_stat,
                'CHA': cha_stat
            },
            'armor_class': armor_class,
            'speed': speed,
            'health': health,
            'dark_vision': "yes" if dark_vision else "no"
        }

        characters.append(new_character)
        save_characters()
        loading_effect()
        print(f"\nCharacter '{name}' added successfully!")
    
    except ValueError as ve:
        print(f"\nInvalid input: {ve}. Please enter valid numbers for attributes.")
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")

# Function to delete a character by index
def delete_character():
    view_characters()
    if characters:
        index = int(input("\nEnter the index of the character to delete: ")) - 1
        if 0 <= index < len(characters):
            deleted_character = characters.pop(index)
            save_characters()
            print(f"\nCharacter '{deleted_character['name']}' deleted successfully!")
        else:
            print("\nInvalid index. Please try again.")
    else:
        print("\nNo characters to delete.")

# Function to view all characters
def view_characters():
    if not characters:
        print("\nNo characters available.")
    else:
        print("\nCharacters:")
        for index, character in enumerate(characters, start=1):
            print(f"{index}. {character['name']}")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Menu and submenus

# Initiatve tracker display
def initiative_tracker_display():
    print("\nInitiative Tracker Menu\n")
    print("1: View Current Battle")
    print("2: Add a Character")
    print("3: Delete a Character")
    print("4: Start New Battle")
    print("5: Main Menu")

# Inititive tracker menu
def initiative_tracker_menu():
    load_initiative_tracker()
    while True:
        initiative_tracker_display()
        choice = input("> ").strip().lower()

        if choice == '1':
            view_current_battle() # Display current battle
            press_enter()
        elif choice == '2':
            add_char_initative() # add character function
        elif choice == '3':
            delete_character() # delete character function
        elif choice == '4':
            start_new_battle() # delete old battle and create new
        elif choice == '5':
            print("\nReturning to main menu.")
            press_enter()
            break
        else:
            print("Invalid option: Please try again.")

# Campaign notes tracker display
def campaign_notes_display():
    print("\nCampaign Notes Menu\n")
    print("1: View Notes")
    print("2: Add New Note")
    print("3: Delete Note")
    print("4: Clear Notes")
    print("5: Main Menu")

# Campaign notes tracker menu
def campaign_notes_menu():
    load_campaign_notes()
    while True:
        campaign_notes_display()
        choice = input("> ").strip().lower()

        if choice == '1':
            view_campaign_notes()  # Call the function to display notes
            press_enter()
        elif choice == '2':
            add_note()  # add note
        elif choice == '3':
            delete_note()  # delete note
        elif choice == '4':
            clear_campaign_notes()  # clear file
        elif choice == '5':
            print("\nReturning to main menu.")
            press_enter()
            break
        else:
            print("Invalid option: Please try again.")

# Function to display character sheet menu
def character_sheet_viewer_menu():
    load_characters()

    while True:
        print("\nCharacter Sheet Viewer Menu:\n")
        print("1. View Characters")
        print("2. Add Character")
        print("3. Delete Character")
        print("4. Return to Main Menu")
        choice = input("> ").strip()

        if choice == '1':
            view_characters()
            if characters:
                index = int(input("\nEnter the index of the character to view (or 0 to cancel): ")) - 1 # List element starts at 0. requires -1 to correctly choose index
                if 0 <= index < len(characters):
                    display_character_sheet(characters[index])
                elif index == -1:
                    continue
                else:
                    print("\nInvalid index. Please try again.")
        elif choice == '2':
            add_character()
        elif choice == '3':
            delete_character()
        elif choice == '4':
            print("\nReturning to main menu.")
            break
        else:
            print("\nInvalid choice. Please try again.")

# Main menu display
def main_menu_display():
    print("\nDungeons and Dragons DM Helper\n")
    print("1: Dice Rolling")
    print("2: Initiative Tracker")
    print("3: Campaign Notes")
    print("4: Character Sheet Viewer")
    print("5: Exit")

# Main menu
def main_menu():
    
    while True:
        main_menu_display()
        choice = input("> ").strip().lower()
        
        if choice == "1":
            dice_rolling_menu()
        elif choice == "2":
            initiative_tracker_menu()
        elif choice == "3":
            campaign_notes_menu()      
        elif choice == "4":
            character_sheet_viewer_menu()
        elif choice == "5" or choice == "exit":
            print("\nExiting program. Goodbye!")
            press_enter()
            sys.exit()
        else:
            print("\nInvalid choice. Please try again.")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Main function
def main():
    main_menu()

if __name__ == "__main__":
    main()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
