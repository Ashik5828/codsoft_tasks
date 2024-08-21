
import random


lowers = 'abcdefghijklmnopqrstuvwxyz'
uppers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '012345678'
symbols = '!@#$%^&*'

print('WELCOME TO THE PASSWORD GENERATOR ')
print('****Here you can generate your password****')

combination = lowers + uppers + numbers + symbols


length = int(input('Enter your length of the password :'))


password = ''.join(random.sample(combination, length))


print('Your password is :',password) 

