# EXERCISE DEVELOPED ON IDE: Visual Studio Code v1.55.2

grades = {}  # Creates an empty dictionary


def qtd_students():
    """Function to get from the user via keyboard the quantity
    of students to be stored. Ignores 0 and all the negative numbers
    and ignores any input that is not an integer."""
    while True:  # Infinite loop to validate the input of how many students to be stored
        try:
            qtd = int(input("Insert the quantity of students: "))
            if qtd >= 0:
                break
            print("Insert a valid quantity of students!")
            continue
        except:  # Restarts the loop if anything goes wrong
            print("Insert a valid quantity of students!")
    return qtd  # Returns the qtd of students


def getScore(phrase):
    """Function to get from the user via keyboard the score
    and validate it in terms of value (between 0 and 10) and also
    rejects any value that is not a float."""
    while True:  # Infinte loop until the score is valid
        try:
            score = float(input(phrase))
            if score >= 0 and score <= 10:
                break  # Score to be between 0.0 and 10.0
            print("Insert a valid score!")
            continue
        except:  # Restarts the loop if anything goes wrong
            print("Insert a valid score!")
            continue
    return score  # Returns the score value


# Main program
print("### STUDENTS SCORES INSERTION ###")
qtd = qtd_students()  # Gets the quantity of students to be stored


def average(n1, n2, n3, n4): return (n1 + n2 + n3 + n4) / \
    4  # Lambda function to calculate the arithmetic mean


# Declare the necessary objects
score = 0
studentAverage = 0
# The arithmetic means list is separated from the dictionary because the exercices dictates how the dictionary should be structured
means = []

for i in range(qtd):  # Loop to register the quantity of students inserted by the user
    name = input("\nStudent's name: ")
    grades[name] = []  # Creates a key in the dictionary with the student's name
    for j in range(1, 5):  # Loop to input the four grades of the student
        score = getScore(f"Student's score #{j}: ")
        # Adds each score to the list in the dict's value
        grades[name].append(score)

    studentAverage = average(*grades[name])
    if studentAverage >= 7:
        status = "Approved"
    else:
        status = "Reproved"

    means.append(studentAverage)
    grades[name].append(status)  # Adds the status to the list

title = ["Student's grades", "Score 1", "Score 2",
         "Score 3", "Score 4", "Mean", "Status"]
print(f"\n\n{title[0]:<27} {title[1]:<8} {title[2]:<8} {title[3]:<8} {title[4]:<8} {title[5]:<8} {title[6]:<8}")
print("-"*20)

i = 0  # Iterator for the index of the 'means[]' list
for name in grades:  # Loop to print on the screen the students' names
    print(f"{name:<28}", end="")  # Prints out the names formated
    for k in range(len(grades[name])-1):  # Loop to print ou the scores
        # Prints out all the stuent's scores
        print(f"{grades[name][k]:<9.1f}", end="")
    # Prints out the student's mean Imprime a média de cada aluno
    print(f"{means[i]:<9.1f}", end="")
    print(f"{grades[name][-1]}")  # Prints out the status
    print()
    i += 1
