#RenCLI - ver1.4.7
# -*- coding: utf-8 -*- 
import os
import time as tm
import random
import sys
import platform

cus = ['Ę',"\u001b[31m"]
FP = 200
backlog=''
tex=''
bol=False
mand = True

def cuscol(lis=['Ę','\u001b[30;1m'],fp2=200,back='',text=['\u001b[30;1m',True],manr=True):
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
    if ['§','¦','¶','Ą','º','¸','Į','ŀ','ę'] in lis:
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
        sys.stdout.write("\033[2K")
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

def color_char(char,shadow=0):
    global backlog
    if shadow == 0: vj = '█'
    elif shadow == 1: vj = '▓'
    elif shadow == 2: vj = '▒'
    elif shadow == 3: vj = '░'
    elif shadow == str(shadow): vj = shadow
    else:print('\u001b[31mBadShadowConf:',shadow);exit()
    if char == '§':
        backlog = '\u001b[44m'
        return '\u001b[0m'+('\u001b[44m' if shadow == 0 else '')+'\u001b[34m' + vj + '\u001b[0m'
    elif char == '¦':
        backlog = '\u001b[41m'
        return '\u001b[0m'+('\u001b[41m' if shadow == 0 else '')+'\u001b[31m' + vj + '\u001b[0m'
    elif char == '¶':
        backlog = '\u001b[42m'
        return '\u001b[0m'+('\u001b[42m' if shadow == 0 else '')+'\u001b[32m' + vj + '\u001b[0m'
    elif char == 'Ą':
        backlog = '\u001b[43m'
        return '\u001b[0m'+('\u001b[43m' if shadow == 0 else '')+'\u001b[33m' + vj + '\u001b[0m'
    elif char == 'º':
        backlog = '\u001b[40m'
        return '\u001b[0m'+('\u001b[40m' if shadow == 0 else '')+'\u001b[30m' + vj + '\u001b[0m'
    elif char == '¸':
        backlog = '\u001b[46m'
        return '\u001b[0m'+('\u001b[46m' if shadow == 0 else '')+'\u001b[36m' + vj + '\u001b[0m'
    elif char == 'Į':
        backlog = '\u001b[47m'
        return '\u001b[0m'+('\u001b[47m' if shadow == 0 else '')+'\u001b[37m' + vj + '\u001b[0m'
    elif char == 'ŀ':
        return '\n'
    elif char == 'ę':
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

def colz(chars,shadow=0,mand=False):
    try:return ''.join(color_char(c,shadow) for c in chars)
    else TypeError:print('\u001b[31mNanType:')

def random_noise(length, chars):
    chn(chars,list)
    chn(length,int)
    chpar(chars)
    if len(chars)<2:
        print('\u001b[31mTwoInp:',chars);exit()
    return colz(''.join(random.choice(chars) for _ in range(length)))

def prinx(image,sha=0):
    sys.stdout.write(colz(image,shadow=sha))

def image2rencli(im,piXY,show=False):
    fl = False
    try:import matplotlib.pyplot as plt
    except:print('\033[93mpip install matplotlib');fl=True
    try:from PIL import Image
    except:print('\033[93mpip install Image');fl=True
    try:import cv2
    except:print('\033[93mpip install opencv-python');fl=True
    try:import numpy as np
    except:print('\033[93mpip install numpy');fl=True
    if fl == True:exit()
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
            try:r = rgb[0]
            except:r = 0
            try:g = rgb[1]
            except:g = 0
            try:b = rgb[2]
            except:b = 0
            image += f'\033[38;2;{int(r)};{int(g)};{int(b)}m' + '█'
        image += '\n'
    if show == True:
        print(data.shape)
        plt.imshow(data)
        plt.show()
    return image

def imgx(im,piXY,show=False):
    s=show
    sys.stdout.write(image2rencli(im,piXY,show=s))

#imgx('test.png',50, show=False)

def renweb(url,piXY,save=None,dr=False):
    ft=False
    try:import requests
    except:print('\033[93mpip install requests');ft=True
    from random import randint
    try:from PIL import Image
    except:print('\033[93mpip install pillow');ft=True
    from io import BytesIO
    if ft==True:exit()
    try:r = requests.get(url)
    except:print('\033[93mConnection_problem',url);exit()
    if save != None: fname = save+'.png'
    if save == None:rname=str(randint(1000,900000));fname='out'+rname+'.png'
    img = Image.open(BytesIO(r.content))
    if os.path.isfile(fname) == False:
        if save == None:img.save(fname)
        else:img.save()
    else:print('\033[93mReTN:', fname)
    if dr==False:image2rencli(fname,piXY)
    elif dr==True:imgx(fname, piXY)
    else:image2rencli(fname,piXY)

#Beta
def vidx(vpath, fps, reso):
  try:import matplotlib.pyplot as plt
  except:print('\033[93mpip install matplotlib');fl=True
  try:from PIL import Image
  except:print('\033[93mpip install Image');fl=True
  try:import cv2
  except:print('\033[93mpip install opencv-python');fl=True
  try:import numpy as np
  except:print('\033[93mpip install numpy');fl=True
  if fl == True:exit()
  cap = cv2.VideoCapture(vpath)
  for i in range(fps):
    ret, frame = cap.read()
    if not ret:
        break
    imgx(frame, reso)
    cv2.waitKey(1)
  cap.release()
  cv2.destroyAllWindows()

#renweb('https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/ThinkCentre_S50.jpg/800px-ThinkCentre_S50.jpg',100,save='Test',dr=True)
