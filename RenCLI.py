import os
import time as tm
import random
import platform
cus = []
FP = 200

def refs(dela):
    dela = dela * (10 ** -3)
    tm.sleep(dela)
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
def chlist(x):
    if type(x) != list:
        cuser = x
        print('\033[93m'+'JustList:',cuser,type(x));exit()

def chnum(x):
    if type(x) != int:
        cuser = x
        print('\033[93m'+'JustInt:',cuser,type(x));exit()

def cuscol(lis,fp2=200):
    global cus
    global FP
    chlist(lis)
    if 'B' in lis or 'R' in lis or 'G' in lis or 'Y' in lis or 'D' in lis or 'C' in lis or 'W' in lis or '-' in lis or '_' in lis:
        cuser = lis
        print('\033[93m'+'Duplicate:',cuser)
    else:
        cus = lis
    chnum(fp2)
    FP = fp2
def color_char(char):
    if char == 'B':
        return '\u001b[34m' + '█'
    elif char == 'R':
       return '\u001b[31m' + '█'
    elif char == 'G':
        return '\u001b[32m' + '█'
    elif char == 'Y':
        return '\u001b[33m' + '█'
    elif char == 'D':
        return '\u001b[30m' + '█'
    elif char == 'C':
        return '\u001b[36m' + '█'
    elif char == 'W':
        return '\u001b[37m' + '█'
    elif char == '-':
        return '\n'
    elif char == '+':
        refs(FP)
        return ''
    elif char in cus:
        ind = cus.index(char)
        return cus[ind+1] + '█'
    else:
        return char

def colz(chars):
    return ''.join(color_char(c) for c in chars)

def random_noise(length, chars):
    chlist(chars)
    if len(chars)<2:
        print('\u001b[31mTwoInp:',chars);exit()
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