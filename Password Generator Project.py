#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+',':',';','<','=','>','?','@','|','_','/','{','}','[',']','^','~']
    

print("\nWelcome to the Integral Password Generator!\n")
nr_letters= int(input("How many letters would you like in your password? "))
nr_symbols = int(input("How many alphanumeric symbols would you like? "))
nr_numbers = int(input("How many numbers would you like? "))

combined=""
answer=""

for letter in range(nr_letters):
    combined+=random.choice(letters)
for alpha in range(nr_symbols):
    combined+=random.choice(symbols)
for number in range(nr_numbers):
    combined+=random.choice(numbers)

#creating a new list
new_list=list(combined)

#shuffling
random.shuffle(new_list)

#storing characters in new variable
for n in range(len(new_list)):
    answer+=new_list[n]
    
print(f"Your generated password is: {answer}")
