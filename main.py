# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
lettersPart = []
numbersPart = []
symbolsPart = []
lettersLength = len(letters)
numbersLength = len(numbers)
symbolsLength = len(symbols)
passwordGenerated = []
passwordRandomised = []

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
totalSum = nr_letters + nr_symbols + nr_numbers

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

for number in range(0, totalSum):
    if number < nr_letters:
        passwordGenerated.insert(number, letters[random.randint(0, lettersLength - 1)])
    elif number >= nr_letters and number < (nr_letters + nr_symbols):
        passwordGenerated.insert(number, symbols[random.randint(0, symbolsLength - 1)])
    else:
        passwordGenerated.insert(number, numbers[random.randint(0, numbersLength - 1)])



for number in range(0, totalSum):
    randomNum = random.randint(0, len(passwordGenerated) - 1)
    passwordRandomised.insert(number, passwordGenerated[randomNum])
    passwordGenerated.pop(randomNum)


passwordRandomisedFinal = ""
for element in passwordRandomised:
    passwordRandomisedFinal += element

print(passwordRandomisedFinal)



















