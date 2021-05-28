# EXERCISE DEVELOPED ON IDE: Visual Studio Code v1.55.2

def getInt(phrase, min, max):
    """Function gets three parameters and validates the input number inside the pre-defined range
    Parameter 1: phrase to be printed on the screen;
    Parameter 2: minimum value of the range which the number must be in;
    Parameter 3: maximum value of the range which the number must be in."""

    while True:  # Inifite loop to get a valid value
        try:
            # Gets the input from the keyboard and trys to convert to an integer
            a = int(input(phrase))
        except:
            # In case of an error, print the alert and restart the loop
            print("Insert a valid number!")
            continue
        else:
            if (a > min) and (a < max):  # Checks if the number is within the specific range
                break
            elif a == 0:  # Closes the program if the user types in 0
                quit()
            else:
                # Prints an alert if the number is out of the range
                print(f"Insert a number between {min} and {max}!")
                continue
    return a


# Programa principal
print("### PRODUCTS VERIFIER DIGIT GENERATOR ###")
while True:
    cod = getInt("\nInsert the product's code (0 to exit): ", 10000, 30000)
    digit = str(cod)  # Converts the code to a string
    digit = map(int, digit)  # Maps each digit of the string to an int
    digit = list(digit)  # Converts it to a list

    j = 2  # Object "weight" starting in 2 and being iterated
    for i in range(len(digit)):  # Loop to multiply each digit for its weight
        digit[i] *= j
        j += 1
    digit = sum(digit)  # Sums all the values of the list
    digit %= 7  # Calculates the remainder of the division by 7

    print(f"\nProduct's code with verifier digit: {cod}-{digit}.")
