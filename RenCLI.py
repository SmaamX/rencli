import os
import time as tm
import random
import platform
import colorama as cl
cus = []
def chlist(x):
    if type(x) != list:
        cuser = x
        print('\033[93m'+'JustList:',cuser);exit()
def cuscol(lis):
    global cus
    chlist(lis)
    if 'B' in lis or 'R' in lis or 'G' in lis or 'Y' in lis or 'D' in lis or 'C' in lis or 'W' in lis:
        cuser = lis
        print('\033[93m'+'Duplicate:',cuser)
    else:
        cus = lis
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
    elif char in cus:
        ind = cus.index(char)
        return cus[ind+1] + '█'
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

def block(col,col2,rv,ta):
    T=rv*2;S=0
    for r in range(rv*2):
        T = T-1
        S = S+1
        for x in range(ta):
            prinx('D'*rv+col2*T+col*S+'D'*rv)
        prinx('D'*80)
        refs(50)