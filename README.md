# :computer: Logic of Programming and Algorithms :books:

This repo contains the assignments of my **Logic of Programming and Algorithms** subject on the University. Python was used as programming language, developed on Visual Studio Code IDE. Please find below the - freely translated by me - assignments.



**Exercise 1**

> Write a program that reads a fighter's name and weight and then returns the his/her category according to the table below (note the table was created for the sake of this exercise only and is not in accordance to any fighting confederation). The program output must be presented on the screen as the standard described below:
>
> > *Name: John MacDonald*
> >
> > *Weight (kg): 73.4*
> >
> > *The fighter John MacDonald weights 73.4kg and fits into the category Welterweight.*
>
> | Weight                                          | Category          |
> | ----------------------------------------------- | ----------------- |
> | Less than 65kg                                  | Bantamweight      |
> | More than or equals to 65kg and less than 72kg  | Featherweight     |
> | More than or equals to 72kg and less than 79kg  | Lightweight       |
> | More than or equals to 79kg and less than 86kg  | Welterweight      |
> | More than or equals to 86kg and less than 93kg  | Middleweight      |
> | More than or equals to 93kg and less than 100kg | Light Heavyweight |
> | More than or equals to 100kg                    | Heavyweight       |
>
> All the input (name and weight) must be read from the keyboard, being the fighter's name a *string* and the weight a *real number*. It is not necessary to store it on a data structure, just print it on the screen.
>
> Put your program on a loop and have it exited once a condition is met. This condition is up to you, for example to end the program once the word *exit* is typed in as name or a invalid weight, as *0*.



**Exercise 2**

> Write a program which gets as input an integer number of 5 digits in a defined range [from 10000 to 30000] representing codes of products being sold in a store. Create a function to validate the input making the user respect the defined range and the data type (integer).
>
> Create one more function to calculate and return a verifier digit using the calculus explained below. For example, for the product's code *21853*, which each digit is multiplied by a weight-value starting from 2 and increasing for each digit. All the results of these multiplications are summed, from the total summed the remainder of *Total / 7* is obtained as the verifier digit.
>
> | Digit        | 2    | 1    | 8    | 5    | 3    |                             |
> | ------------ | ---- | ---- | ---- | ---- | ---- | --------------------------- |
> | Weight-value | 2    | 3    | 4    | 5    | 6    |                             |
> | Result       | 4    | 3    | 32   | 25   | 18   | Sum of all the results = 82 |
> |              |      |      |      |      |      | Remainder of 82 / 7 = **5** |
>
> Return from this function the verifier digit calculated and print on the screen the product's code followed by its verifier digit separated by a dash, such as: *21853-5*.



**Exercise 3**

> Consider the following data structure: *Name + [N1, N2, N3, N4] + Status*, which must be stored in a dictionary.
>
> The *Name* represents a student's name and must be used as a key. *N1, N2, N3, N4* represent the exams scores of this student and must be placed in a list. In the end, the *Status* is nothing else than a *string* containing the word *Approved* or *Reproved*. Use a data structure of a dictionary with lists nested to solve this exercise.
>
> Write a program which reads the input of *n* students and print on the screen their names, scores and if they are approved or reproved. The approval criteria is the four scores arithmetic mean to be equals to or higher than 7.0. The *n* value is the quantity of students and is also an input from the user in the beginning of the program. Have a loop to read all the *n* students. The grades must be printed on the screen with one decimal digit of precision.



**Exercise 4**

> > ***Personal note:*** *I did not find this exercises' proposal much efficient but I made it accordingly to what was proposed.*
>
> Create a program which has three lists to read and store the name, age and the phone number of your contacts. Once an empty string is inserted as a name, the program interrupts the input reading.
>
> Print on the screen the contacts registered in alphabetical order, sorted by the contacts' names.
>
> After printing, store the contacts in other two dictionaries, using as criteria the age: under 18 years old people in one dictionary and all the others in another. Print on the screen both dictionaries gotten from this separation. Use as the dictionaries' keys: *name, age,* and *phone*.

