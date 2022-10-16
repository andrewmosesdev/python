import inquirer
# using inquirer and hardcoding the possible actions saves us from a lot of validation and possible issues

RCE_options = {
    "movement": {
        "West": "Mausoleum Lookout"
    },
    }
ML_options = {
    "movement": {
        "East": "Ringed City Entrance", 
        "North": "Dragon Bridge"
    },
    "item_available": "Soul of a Crestfallen Knight" 
}
DB_options = {
    "movement": {
        "North": "Earthen Peak Ruins",
        "South": "Mausoleum Lookout",
        "East": "Shared Grave",
        "West": "The Tower"
    }, 
    "item_available": 'Iron Dragonslayer Set'
}
EPR_options = {
    "movement": {
        "South": "Dragon Bridge",
        "East": "Church of Filianore"
    },
    "item_available": 'Dragonhead Shield'
}
CoF_options = {
    "movement": {
        "West": "Earthen Peak Ruins"
    },
    "item_available": 'Moonlight Greatsword'
}
TT_options = {
    "movement": {
        "East": "Dragon Bridge"
    },
    "item_available": 'Havel\'s Ring'
}
SG_options = {
    "movement": {
        "West": "Dragon Bridge",
        "North": "Darkeater Midir"
    },
    "item_available": 'Titanite Chunk'
}
DM_options = {
    "items_needed": 6
}

room_dict = {
    "Ringed City Entrance": RCE_options,
    "Mausoleum Lookout": ML_options,
    "Dragon Bridge": DB_options,
    "The Tower": TT_options,
    "Earthen Peak Ruins": EPR_options,
    "Church of Filianore": CoF_options,
    "Shared Grave": SG_options,
    "Darkeater Midir": DM_options
}
inventory = []

def printItems(inventory_array):
    for item in inventory_array:
        print(item)

# we'll handle this recursively, it's cleaner, more efficient, and only requires one while loop
def main(current_position, game_active):
    
    if current_position == 'Darkeater Midir' and len(inventory) != 6:
        print('Game over! You challenged Darkeater Midir without all necessary items.')
        exit()
    elif current_position == 'Darkeater Midir' and len(inventory) ==6:
        print('You collected all necessary items and defeated Darkeater Midir! You win!')
        exit()
    
    while game_active == True:
        options_object = room_dict.get(current_position, 'Ringed City Entrance')
        user_options = []

        if 'movement' in options_object:
            user_options.append("Move to a different area")
        if 'item_available' in options_object:
            user_options.append("Pick up item")
        user_options.append("Quit")

        string_inventory = '\n '.join(map(str, inventory))
        
        print(f'You are in {current_position}.')
        print(f'Your current inventory consists of: \n {string_inventory if len(inventory) > 0 else "No items"}')
        entered_new_area_question = [
            inquirer.List('response', message=f'What would you like to do?', choices=user_options)
        ]
        
        user_choice = inquirer.prompt(entered_new_area_question)
        
        if user_choice['response'] == 'Move to a different area':
            direction_options = options_object['movement']
            choose_direction_question = [
                inquirer.List('response', message=f'Which direction would you like to go?', choices=direction_options)
            ]
            direction_choice = inquirer.prompt(choose_direction_question)
            position = room_dict.get(current_position, {}).get('movement', {}).get(direction_choice['response'], 'Ringed City Entrance')
            
            main(position, True)
        
        elif user_choice['response'] == 'Pick up item':
            item = room_dict.get(current_position, {})['item_available']
            inventory.append(item)
            print(f'Picked up {item}!')
            print(f'You now have {len(inventory)}/6 required items to challenge Darkeater Midir!')
            del room_dict[current_position]['item_available']
        else:
            exit()

    
main('Ringed City Entrance', True)