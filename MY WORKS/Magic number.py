import random
from colorama import init
from colorama import Fore, Back, Style
init()

print(Fore.RED)

random_number = random.randint(1, 5)
user_number = input('Угадай число от 1 до 5: ')

print(Fore.GREEN)

if random_number == int(user_number):
    print('Ты угадал!')
else: 
    print('Ты НЕ угадал!')
    print(f'Было загадано число: {random_number}')