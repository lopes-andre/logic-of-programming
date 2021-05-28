# EXERCISE DEVELOPED ON IDE: Visual Studio Code v1.55.2

# Declaring the lists
names = []
phones = []
ages = []
# Declaring the dicts
contacts = {}
contactsYounger = {}
contactsOlder = {}

print("\n#### ADD NEW CONTACTS (empty contact to exit) ###")
while True:  # Loop to add new contacts until an empty string is inserted
    name = input("\nContact's name: ")  # Saves the name into the object 'name'

    if name == "":
        break  # Breaks the loop if the contact's name string is empty

    elif name in names:  # Check if the name already exists
        print("This contact already exists!")
        continue

    names.append(name)  # Adds name to the names[] list

    # Gets the phone number and saves into the phones[] list
    phone = input(f"{name}\'s phone: ")
    phones.append(phone)

    # Loop to validate the age as greater than zero and an integer
    while True:
        try:
            age = int(input(f"{name}\'s age: "))
            if age > 0:
                break
            continue
        except:
            continue
    ages.append(age)  # Adds age to the ages[] list

# Loop iterating thru the names and add the names as keys of the
# contacts{} dict and adding a list as value having the phone number
# and the age of each contact
for i in range(len(names)):
    contacts[names[i]] = [phones[i], ages[i]]

# Prints the header of the full contacts list
title = "### FULL CONTACTS LIST ###"
menu = ["NAME", "PHONE", "AGE"]
print(f"\n{title:^59}")
print(f"{menu[0]:^28} | {menu[1]:^18} | {menu[2]:^7}\n"+("-"*59))

# Loop to get the name and data from the contacts.items() sorted and printing it out
for name, data in sorted(contacts.items()):

    print(f"{name:^28} | {data[0]:^18} | {data[1]:^7}")

    # Condition to check if the contact is older than 18 years old
    # Add the contact to the contactsOlder{} if older than 18yo
    # or to the contactsYounger{} dict if younger than 18yo
    if(data[1] >= 18):
        contactsOlder[name] = [data[0], data[1]]

    else:
        contactsYounger[name] = [data[0], data[1]]

contacts.clear()  # Eliminates the original dict

# Prints out the header for the contacts list for older than 18yo
title = "### CONTACTS LIST OLDER THAN 18 ###"
print(f"\n{title:^59}")
print(f"{menu[0]:^28} | {menu[1]:^18} | {menu[2]:^7}\n"+("-"*59))
# Loop to get name and data from the sorted contactsOlder.items()
# and printing it out formated
for name, data in sorted(contactsOlder.items()):
    print(f"{name:^28} | {data[0]:^18} | {data[1]:^7}")

# Prints out the header for the contacts list for younger than 18yo
title = "### CONTACTS LIST YOUNGER THAN 18 ###"
print(f"\n{title:^59}")
print(f"{menu[0]:^28} | {menu[1]:^18} | {menu[2]:^7}\n"+("-"*59))
# Loop to get name and data from the sorted contactsYounger.items()
# and printing it out formated
for name, data in sorted(contactsYounger.items()):
    print(f"{name:^28} | {data[0]:^18} | {data[1]:^7}")

print()
