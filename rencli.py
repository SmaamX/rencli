import os
import time as tm
import random
import sys
import platform

cus = ['T',"\u001b[31m"]
backlog = ''
FP = 200

backlog=''
tex=''
bol=False
mand = True
def cuscol(lis=['T','\u001b[30;1m'],fp2=200,back='',text=['\u001b[30;1m',True],manr=True):
    global mand
    global cus
    global FP
    global backlog
    global tex
    global bol
    chn(manr, bool)
    mand = manr
    chpar(text)
    chn(text[0], str)
    tex = text[0]
    chn(text[1], bool)
    chn(back, str)
    backlog = back
    chn(lis,list)
    if 'B' in lis or 'R' in lis or 'G' in lis or 'Y' in lis or 'D' in lis or 'C' in lis or 'W' in lis or '-' in lis or '_' in lis:
        cuser = lis
        print('\033[93m'+'Duplicate:',cuser)
    else:
        cus = lis
    chn(fp2,int)
    FP = fp2

def refs(dela):
    global mand
    dela = dela * (10 ** -3)
    tm.sleep(dela)
    if mand == False:
        sys.stdout.flush()
    else:
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')
def chn(x,typ):
    try:
        if type(x) != typ:
            cuser = x
            print('\033[93m'+'Just'+typ+':',cuser,type(x));exit()
    except:print('\u001b[31mBadInpTyp',x,typ)

def chpar(x):
    if '-' in x or '+' in x:
        print('\u001b[31mTwoInp:',x)
        exit()

def color_char(char):
    global backlog
    if char == 'B':
        backlog = '\u001b[44m'
        return '\u001b[0m'+'\u001b[44m'+'\u001b[34m' + '█'
    elif char == 'R':
        backlog = '\u001b[41m'
        return '\u001b[0m'+'\u001b[41m'+'\u001b[31m' + '█'
    elif char == 'G':
        backlog = '\u001b[42m'
        return '\u001b[0m'+'\u001b[42m'+'\u001b[32m' + '█'
    elif char == 'Y':
        backlog = '\u001b[43m'
        return '\u001b[0m'+'\u001b[43m'+'\u001b[33m' + '█'
    elif char == 'D':
        backlog = '\u001b[40m'
        return '\u001b[0m'+'\u001b[40m'+'\u001b[30m' + '█'
    elif char == 'C':
        backlog = '\u001b[46m'
        return '\u001b[0m'+'\u001b[46m'+'\u001b[36m' + '█'
    elif char == 'W':
        backlog = '\u001b[47m'
        return '\u001b[0m'+'\u001b[47m'+'\u001b[37m' + '█'
    elif char == '-':
        return '\n'
    elif char == '+':
        refs(FP)
        return ''
    elif char in cus:
        ind = cus.index(char)
        return cus[ind+1] + '█'
    else:
        if backlog != '':
            return '\u001b[0m' + '\033[1m' + backlog + tex + char
        else:
            '\u001b[0m' + '\033[1m' + '\u001b[7m' + tex + char

def colz(chars,mand=False):
    return ''.join(color_char(c) for c in chars)

def random_noise(length, chars):
    chn(chars,list)
    chn(length,int)
    chpar(chars)
    if len(chars)<2:
        print('\u001b[31mTwoInp:',chars);exit()
    return colz(''.join(random.choice(chars) for _ in range(length)))

def prinx(image):
    sys.stdout.write(colz(image))

def image2rencli(im,piXY,show=False):
    try:import matplotlib.pyplot as plt
    except:print('\033[93mpip install matplotlib');exit()
    try:from PIL import Image
    except:print('\033[93mpip install Image');exit()
    try:import cv2
    except:print('\033[93mpip install cv2');exit()
    try:import numpy as np
    except:print('\033[93mpip install numpy');exit()
    chn(im, str)
    try:data = np.array(Image.open(im))
    except:
        print('\033[93mBadAD:',im)
        exit()
    data = cv2.resize(data, (piXY, piXY))
    image = ''
    for i in range(piXY):
        for j in range(piXY):
            rgb = data[i,j]
            r = rgb[0]
            g = rgb[1] 
            b = rgb[2]
            image += f'\033[38;2;{int(r)};{int(g)};{int(b)}m' + '█'
        image += '\n'
    if show == True:
        print(data.shape)
        plt.imshow(data)
        plt.show()
    return image
def imgx(im,piXY,show=False):
    s=show
    print(image2rencli(im,piXY,show=s))

#imgx('test.png',100, show=False)