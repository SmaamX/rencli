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

def noise(rang):
    lplist = []
    rl = ['B', 'R', 'G', 'BL', 'Y', 'C', 'W']
    for y in range(1,rang):
        rand = random.choice(rl);lplist.append(rand)
    return cd(lplist)

if __name__ == '__main__':
    while True:
        try:
            ref('20')
            print(' '+noise(25),sp(),noise(25),sp(),noise(25),sp(),noise(25),sp(),noise(25),sp(),noise(25),sp(),noise(25))
        except:KeyboardInterrupt;print(cl.Fore.RED + 'FExit');exit()