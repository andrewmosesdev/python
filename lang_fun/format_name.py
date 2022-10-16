user_name = input("Please enter your name (ex: Andrew James Moses): ")
name_list = user_name.split()

if len(name_list) == 2:
    first_name = name_list[0].capitalize()
    
    first_initial = first_name[0:1]
    
    last_name = name_list[1].capitalize()
    
    formatted_name = f'{last_name}, {first_initial}.'
    print(formatted_name)
elif len(name_list) == 3:
    first_name = name_list[0].capitalize()
    first_initial = first_name[0:1]
    
    middle_name = name_list[1].capitalize()
    middle_initial = middle_name[0:1]

    last_name = name_list[2].capitalize()
    
    formatted_name = f'{last_name}, {first_initial}.{middle_initial}.'
    print(formatted_name)