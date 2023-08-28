import os
import time as tm 
import random
import platform
try:
    import colorama as cl
except ModuleNotFoundError:
    print('pip install colorama')
    exit()
    
def color_char(char):
    if char == 'B':
        return cl.Fore.BLUE + '█' 
    elif char == 'R':
       return cl.Fore.RED + '█'
    elif char == 'G':
        return cl.Fore.GREEN + '█'
    elif char == 'Y':
        return cl.Fore.YELLOW + '█'
    elif char == 'D':
        return cl.Fore.BLACK + '█'
    elif char == 'C':
        return cl.Fore.CYAN + '█'
    elif char == 'W':
        return cl.Fore.WHITE + '█'
    else:
        return char 
        
def colz(chars):
    return ''.join(color_char(c) for c in chars)
    
def neli():
    print('\n')
    
def refs(dela):
    dela = dela * (10 ** -3)
    tm.sleep(dela)
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
        
def random_noise(length, chars):
    return colz(''.join(random.choice(chars) for _ in range(length)))
    
def prinx(image):
    print(colz(image))

def test():
    refs(100)

    image = 'B' * 44
    prinx(image)

    for x in range(1,19):
        image2 = 'B' * 22 + random_noise(22, ['D', 'R'])
        prinx(image2)

    image = 'B' * 44
    prinx(image)

    for x in range(1,19):
        image2 = 'B' * 22 + random_noise(22, ['D', 'Y'])
        prinx(image2)
