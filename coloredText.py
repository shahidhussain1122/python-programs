import colorama
from colorama import Fore, Back, Style

colorama.init()  # Initialize colorama
print(Fore.RED + 'some red text')

color = input('Enter a color: ')
match color:
    case 'red':
        print(Fore.RED + Back.BLUE+ 'some red text')
    case 'blue':
        print(Fore.BLUE + 'some blue text')
    case 'green':
        print(Fore.GREEN + 'some green text')
    case 'yellow':
        print(Fore.YELLOW + 'some yellow text')