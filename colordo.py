import os
import time as tm
import random
import platform

try:
    import colorama as cl
except ModuleNotFoundError:
    print('pip install colorama')
    exit()
    
def c(man):
    plist=man;rv=[];out2=''
    for manz in man:
        if manz == 'B': rv.append(cl.Fore.BLUE + '█')
        if manz == 'R': rv.append(cl.Fore.RED + '█')
        if manz == 'G': rv.append(cl.Fore.GREEN + '█')
        if manz == 'Y': rv.append(cl.Fore.YELLOW + '█')
        if manz == 'BL': rv.append(cl.Fore.BLACK + '█')
        if manz == 'C': rv.append(cl.Fore.CYAN + '█')
        if manz == 'W': rv.append(cl.Fore.WHITE + '█')
    for x in rv:
        out2=out2+str(x)
    return(out2)

def cd(inp):
    inputr = []
    for x in inp:
        inputr.append(x)
    return c(inputr)

def sp():return '\n'

def ref(dela):
    tm.sleep(int(dela)*(10**-3))
    if platform.system() == 'Windows':os.system('cls')
    else:os.system('clear')

def noise(rang,r):
    lplist = []
    for y in range(1,rang):
        rand = random.choice(r);lplist.append(rand)
    return cd(lplist)

if __name__ == '__main__':
    rl = ['BL','W']
    rl2 = ['B','R','G','Y','BL','C','W']
    while True:
        try:
            ref('20')
            print(' '+noise(45,rl),sp(),noise(45,rl),sp(),noise(45,rl),sp(),noise(45,rl),sp(),noise(45,rl),sp(),noise(45,rl),sp(),noise(45,rl),sp(),noise(45,rl),sp(),noise(45,rl),sp(),noise(45,rl),sp(),noise(45,rl))
            ref('30')
            print(' '+cd('B'*44),sp(),cd('B'*44),sp()
                    ,cd('B'*22)+noise(23,rl2),sp()
                    ,cd('B'*21)+noise(24,rl2),sp()
                    ,cd('B'*20)+noise(25,rl2),sp()
                    ,cd('B'*19)+noise(4,rl2)+cd('B'*22),sp()
                    ,cd('B'*18)+noise(5,rl2)+cd('B'*22),sp()
                    ,cd('B'*17)+noise(6,rl2)+cd('B'*22),sp()
                    ,cd('B'*16)+noise(7,rl2)+cd('B'*22),sp()
                    ,cd('B'*15)+noise(8,rl2)+cd('B'*22),sp()
                    ,cd('B'*14)+noise(9,rl2)+cd('B'*22),sp())
            ref('200')
        except:KeyboardInterrupt;print(cl.Fore.RED + 'FExit');exit()