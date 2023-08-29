from colordo import prinx
from colordo import refs
from time import sleep
def sscree():
    print('Config122 loading')
    sleep(0.2)
    print('Config122 loading')
    sleep(0.2)
    print('Config122 loading')
    sleep(0.2)
    print('Config122 loading')
    sleep(0.2)
    print('Config122 loading')
    sleep(0.2)
    print('Config122 loading')
    sleep(0.2)
    print('Config122 loading')
    sleep(0.2)
    print('Config122 loading')
    sleep(0.2)
    print('Config122 loading')
    sleep(0.2)
    print('Config122 loading')
    refs(300)
    y = 20
    y1 = 20
    y2 = 18
    y3 = 16
    y4 = 16
    y5 = 18
    y6 = 20
    y7 = 20

    x = 10
    x1 = 9
    x2 = 10
    x3 = 11
    x4 = 11
    x5 = 10
    x6 = 9
    x7 = 10

    for xp in range(1,18):
        prinx('D' * 40)
        prinx('D' * x + 'W' * 10 + 'D' * y)
        prinx('D' * x1 + 'W' * 11 + 'D' * y1)
        prinx('D' * x2 + 'W' * 12 + 'D' * y2)
        prinx('D' * x3 + 'W' * 13 + 'D' * y3)
        prinx('D' * x4 + 'W' * 13 + 'D' * y4)
        prinx('D' * x5 + 'W' * 12 + 'D' * y5)
        prinx('D' * x6 + 'W' * 11 + 'D' * y6)
        prinx('D' * x7 + 'W' * 10 + 'D' * y7)
        prinx('D' * 40)
        refs(100)
        y = y - 1
        x = x + 1
        y1 = y1 - 1
        x1 = x1 + 1
        y2 = y2 - 1
        x2 = x2 + 1
        y3 = y3 - 1
        x3 = x3 + 1
        y4 = y4 - 1
        x4 = x4 + 1
        y5 = y5 - 1
        x5 = x5 + 1
        y6 = y6 - 1
        x6 = x6 + 1
        y7 = y7 - 1
        x7 = x7 + 1
    prinx('D' * 40)
    prinx('D' * 10 + 'W' * 10 + 'D' * 20)
    prinx('D' * 10 + 'W' * 10 + 'D' * 20)
    prinx('D' * 10 + 'W' * 10 + 'D' * 20)
    prinx('D' * 10 + 'W' * 10 + 'D' * 20)
    prinx('D' * 10 + 'W' * 10 + 'D' * 20)
    prinx('D' * 10 + 'W' * 10 + 'D' * 20)
    prinx('D' * 10 + 'W' * 10 + 'D' * 20)
    prinx('D' * 10 + 'W' * 10 + 'D' * 20)
    prinx('D' * 40)
    refs(500)
    prinx('D' * 40)
    prinx('D' * 20 + 'W' * 10 + 'D' * 10)
    prinx('D' * 20 + 'W' * 10 + 'D' * 10)
    prinx('D' * 20 + 'W' * 10 + 'D' * 10)
    prinx('D' * 20 + 'W' * 10 + 'D' * 10)
    prinx('D' * 20 + 'W' * 10 + 'D' * 10)
    prinx('D' * 20 + 'W' * 10 + 'D' * 10)
    prinx('D' * 20 + 'W' * 10 + 'D' * 10)
    prinx('D' * 20 + 'W' * 10 + 'D' * 10)
    prinx('D' * 40)
    refs(500)
    prinx('D' * 40)
    prinx('D' * 10 + 'W' * 10 + 'D' * 20)
    prinx('D' * 10 + 'W' * 10 + 'D' * 20)
    prinx('D' * 10 + 'W' * 10 + 'D' * 20)
    prinx('D' * 10 + 'W' * 10 + 'D' * 20)
    prinx('D' * 10 + 'W' * 10 + 'D' * 20)
    prinx('D' * 10 + 'W' * 10 + 'D' * 20)
    prinx('D' * 10 + 'W' * 10 + 'D' * 20)
    prinx('D' * 10 + 'W' * 10 + 'D' * 20)
    prinx('D' * 40)

    x11 = 10
    x12 = 10
    f = 10

    for v in range(1,9):
        f = f - 1
        x11 = x11 - 1
        x12 = x12 + 1
        prinx('D' * 40)
        prinx('D' * x12 + 'W' * x11 + 'D' * 20)
        prinx('D' * x12 + 'W' * x11 + 'D' * 20)
        prinx('D' * x12 + 'W' * x11 + 'D' * 20)
        prinx('D' * x12 + 'W' * x11 + 'D' * 20)
        prinx('D' * x12 + 'W' * x11 + 'D' * 20)
        prinx('D' * x12 + 'W' * x11 + 'D' * 20)
        prinx('D' * x12 + 'W' * x11 + 'D' * 20)
        prinx('D' * x12 + 'W' * x11 + 'D' * 20)
        prinx('D' * 40)
        if f > 2:
            refs(500)
    refs(100)
    prinx('D' * 40)
    prinx('D' * 18 + 'R' * 2 + 'D' * 20)
    prinx('D' * 18 + 'R' * 2 + 'D' * 20)
    prinx('D' * 15 + 'R' * 5 + 'R' * 4 + 'D' * 15)
    prinx('D' * 18 + 'R' * 2 + 'D' * 20)
    prinx('D' * 18 + 'R' * 2 + 'D' * 20)
    prinx('D' * 18 + 'R' * 2 + 'D' * 20)
    prinx('D' * 18 + 'R' * 2 + 'D' * 20)
    prinx('D' * 18 + 'R' * 2 + 'D' * 20)
    prinx('D' * 40)
sscree()
