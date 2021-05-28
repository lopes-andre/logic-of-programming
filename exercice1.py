# EXERCISE DEVELOPED ON IDE: Visual Studio Code v1.55.2

while True: # Infinite loop which will be broken if the user types in "exit" (non case-sensitive)
    print("### FIGHTERS CATEGORY VERIFICATION ###\n(Type \"exit\" to close the program)")

    name = input("Name: ") # Gets from the keyboard the fighter's name

    if name.upper() == "EXIT": break # Closes the program if the user types in exit

    while True: # Loop the get a valid weight, greater than zero and a real number (float)
        try:
            weight = float(input("Weight: ")) # Gets the weight
            
            if weight > 0: # If the weight is greater than zero the loop is broken
                break
        
        except: # In case of any error inputing the weight, the loop runs again
            print("Insert a valid weight!")
            continue

    # Start of the conditions to check the fighter's category
    # multiple conditions are used
    if weight < 65: categ = "Bantamweight"

    elif weight > 65 and weight < 72: categ = "Featherweight"

    elif weight > 72 and weight < 79: categ = "Lightweight"

    elif weight > 79 and weight < 86: categ = "Welterweight"

    elif weight > 86 and weight < 93: categ = "Middleweight"

    elif weight > 93 and weight < 100: categ = "Light Heavyweight"

    else: categ = "Heavyweight"

    print(f"The fighter {name} weights {weight:.1f}kg and fits into the {categ} category.\n")

print("\nClosing the program...")