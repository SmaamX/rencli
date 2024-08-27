from rencli import *
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
