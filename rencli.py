#RenCLI - ver1.4.8
# -*- coding: utf-8 -*- 
import os
import time as tm
import random
import sys
import platform

def d_list(list1,list2):
    return [[x + y for x, y in zip(row1, row2)] for row1, row2 in zip(list1, list2)] #SO IMPORTANT

cus = ['Ę',"\u001b[31m"]
FP = 200
backlog = ''
tex=''
bol = False
mand = True

def cuscol(lis=['Ę','\u001b[30;1m'],fp2=200,back='',text=['\u001b[30;1m',True],manr=True)  -> None:
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

def refs(dela) -> None:
    global mand
    dela = dela * (10 ** -3)
    tm.sleep(dela)
    if mand == False:
        sys.stdout.write("\033[2K\r")
    else:
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

def chn(x,typ) -> None:
    try:
        if type(x) != typ:
            cuser = x
            print('\033[93m'+'Just'+typ+':',cuser,type(x));exit()
    except:print('\u001b[31mBadInpTyp',x,typ)

def chpar(x):
    if ['ŀ','ę'] in x:
        print('\u001b[31mTwoInp:',x)
        exit()

def color_char(char,shadow=0) -> str:
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
        return '\r\n'
    elif char == 'ę':
        refs(FP)
        return '\r'
    elif char in cus:
        ind = cus.index(char)
        return cus[ind+1] + vj
    else:
        if backlog != '':
            return '\u001b[0m' + '\033[1m' + backlog + tex + char
        else:
            '\u001b[0m' + '\033[1m' + '\u001b[7m' + tex + char

def colz(chars,shadow=0,mand=False, lfix=False) -> str:
    check_list = []
    if lfix == True:
        for i in chars:
            if i != "ŀ":
                check_list.append(i)
            else:
                check_list=check_list[:-1];check_list.append(i)
        try:return ''.join(color_char(c,shadow) for c in check_list)
        except TypeError:print('\u001b[31mNanType:');exit(0)
    else:
        try:return ''.join(color_char(c,shadow) for c in chars)
        except TypeError:print('\u001b[31mNanType:');exit(0)

def ren_colz(local_, refs=False, shadow=0) -> str:
    data_temp_2 = ""
    for r in range(len(local_)):
        for i in local_[r]:
            data_temp_2 += color_char(str(i),shadow=shadow)
        data_temp_2 += "\n"
    if refs == True:
        data_temp_2 += color_char("ę")
        return data_temp_2
    else:
        return data_temp_2

#a lite final rend 
def move_2list(listin, ind, mod, spee=0, speel=1, emp=0, lback = [], final_rend=False):
  if mod == 1:
    for i in range(len(listin)):
      for ii in listin[i]:
        try:
          if ii == ind:
            if final_rend == True:
              loc = listin[i].index(ind)+1+spee
              listin[i].remove(ind)
              listin[i].insert(loc,ind)
              listin[i].pop(loc-1)
              for l in range(spee+1):
                listin[i].insert(loc-1,listin_back[i][loc-1-spee])
            else:
              if ii == ind:
                loc = listin[i].index(ind)+1+spee
                listin[i].remove(ind)
                listin[i].insert(loc,ind)
            i = 1
            if i == 1:
              i += 1
              continue
            elif i == 2:
              i = 0
        except:
            pass
  elif mod == 3:
    for i in range(len(listin)):
      for ii in listin[i]:
        try:
          if ii == ind:
            if final_rend == True:
              loc = listin[i].index(ind)-1-spee
              listin[i].remove(ind)
              listin[i].insert(loc,ind)
              listin[i].pop(loc+1)
              for l in range(spee+1):
                listin[i].insert(loc-1,listin_back[i][loc+1+spee])
            else:
              if ii == ind:
                loc = listin[i].index(ind)-1-spee
                listin[i].remove(ind)
                listin[i].insert(loc,ind)
            i = 1
            if i == 1:
              i += 1
              continue
            elif i == 2:
              i = 0
        except:
            pass
  elif mod == 4:
    for i in range(speel):
      temp_list = listin[-1]
      listin.pop(-1)
      listin.insert(0,temp_list)
  elif mod == 2:
    for i in range(speel):
      temp_list = listin[0]
      listin.pop(0)
      listin.append(temp_list)
  return listin

def random_noise(length, chars) -> str:
    chn(chars,list)
    chn(length,int)
    chpar(chars)
    if len(chars)<2:
        print('\u001b[31mTwoInp:',chars);exit()
    return colz(''.join(random.choice(chars) for _ in range(length)))

def prinx(image,sha=0,lfix=True) -> None:
    sys.stdout.write(colz(image,shadow=sha,lfix=lfix))

def prinx2(image,refs=True,sha=0):
    sys.stdout.write(ren_colz(image,refs=refs,shadow=sha))

def image2rencli(im,piXY,show=False) -> str:
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

def imgx(im,piXY,show=False) -> None:
    s=show
    sys.stdout.write(image2rencli(im,piXY,show=s))

#imgx('test.png',50, show=False)

def renweb(url,piXY,save=None,dr=False) -> None:
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

#renweb('https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/ThinkCentre_S50.jpg/800px-ThinkCentre_S50.jpg',100,save='Test',dr=True)
