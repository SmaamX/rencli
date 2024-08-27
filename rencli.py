#RenCLI - ver1.4.8
# -*- coding: utf-8 -*- 
import os
import time as tm
import random
import sys
import platform

def d_list(list1,list2) -> list:
    return [[x + y for x, y in zip(row1, row2)] for row1, row2 in zip(list1, list2)] #SO IMPORTANT

class check_vi():
  def check_r(test_list, test_list_back, rate, wall, isisnt, r=1) -> bool:
    if isisnt == True:
      return move_2list(test_list, 1, 1, found_ind=True) <= len(test_list[0]) and (test_list_back[move_2list(test_list, rate, 2, found_ind='y')][move_2list(test_list, rate, 3, found_ind=True)+r] == wall) if move_2list(test_list, rate, 3, found_ind=True) != len(test_list_back[0])-1 else False
    elif isisnt == False:
      return move_2list(test_list, 1, 1, found_ind=True) <= len(test_list[0]) and (test_list_back[move_2list(test_list, rate, 2, found_ind='y')][move_2list(test_list, rate, 3, found_ind=True)+r] != wall) if move_2list(test_list, rate, 3, found_ind=True) != len(test_list_back[0])-1 else False

  def check_l(test_list, test_list_back, rate, wall, isisnt, r=1) -> bool:
    if isisnt == True:
      return test_list_back[move_2list(test_list, rate, 2, found_ind='y')][move_2list(test_list, rate, 3, found_ind=True)-r] == wall if move_2list(test_list, rate, 1, found_ind=True) != 0 else False
    elif isisnt == False:
      return move_2list(test_list, 1, 3, found_ind=True) >= 1 and (test_list_back[move_2list(test_list, rate, 2, found_ind='y')][move_2list(test_list, rate, 3, found_ind=True)-r] != wall) if move_2list(test_list, rate, 1, found_ind=True) != 0 else False

  def check_u(test_list, test_list_back, rate, wall, isisnt, r=1) -> bool:
    if isisnt == True:
      return test_list_back[move_2list(test_list, rate, 2, found_ind='y')-r][move_2list(test_list, rate, 3, found_ind=True)] == wall
    elif isisnt == False:
      return move_2list(test_list, 1, 2, found_ind='y')-1 >= 0 and test_list_back[move_2list(test_list, rate, 2, found_ind='y')-r][move_2list(test_list, rate, 3, found_ind=True)] != wall

  def check_d(test_list, test_list_back, rate, wall, isisnt, r=1) -> bool:
    if isisnt == True:
      return test_list_back[move_2list(test_list, rate, 2, found_ind='y')+r][move_2list(test_list, rate, 3, found_ind=True)] == wall if move_2list(test_list, rate, 4, found_ind='y') != len(test_list)-1 else False
    elif isisnt == False:
      return move_2list(test_list, 1, 4, found_ind='y') <= len(test_list[0])-2 and (test_list_back[move_2list(test_list, rate, 2, found_ind='y')+r][move_2list(test_list, rate, 3, found_ind=True)] != wall) if move_2list(test_list, rate, 4, found_ind='y') != len(test_list)-1 else False

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
def move_2list(listin, ind, mod, spee=0, speel=1, lback = [], final_rend=False, found_ind=False) -> list:
  if mod == 1:
    for i in range(len(listin)):
      for ii in listin[i]:
        try:
          if ii == ind:
            if found_ind == "debug":
              return listin[i].index(ind)
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
                try:
                  if found_ind == True:
                    return listin[i].index(ind)
                except IndexError:
                    return -1
                listin[i].remove(ind)
                listin[i].insert(loc,ind)
            if len(listin)//2 == 0:
              i = -len(listin[ii])-2
            else:
              i = -len(listin[ii])-3
            if i == -len(listin[ii])-2:
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
            if found_ind == "debug":
              return listin[i].index(ind)
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
                try:
                  if found_ind == True:
                    return listin[i].index(ind)
                except IndexError:
                    return -1
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
    if found_ind == "y":
      for i in range(len(listin)):
        for ii in listin[i]:
          try:
            if ii == ind:
              try:
                return listin.index(listin[i])
              except:
                return listin.index(listin[i]-1)
          except:pass
    for i in range(speel):
      temp_list = listin[-1]
      listin.pop(-1)
      listin.insert(0,temp_list)
  elif mod == 2:
    if found_ind == "y":
      for i in range(len(listin)):
        for ii in listin[i]:
          try:
            if ii == ind:
              try:
                return listin.index(listin[i])
              except:
                return listin.index(listin[i]-1)
          except:pass
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
