# Password Generator using Python3

# Use this to generate a strong pass for your Account
import random

print('Generate a 12 Digit Strong Password with this Password Generator\n')

password_list = []

Capital_Letters = [cap for cap in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
Small_Letters = [sml for sml in 'abcdefghijklmnopqrstuvwxyz']
Numbers = [num for num in range(11)]
Symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')']


Combined = Capital_Letters + Small_Letters + Numbers + Symbols

while len(password_list) != 12:
    p = random.choice(Combined)
    password_list.append(str(p))


print('Your 12 Digit Strong Password is ')
print(''. join(password_list))


