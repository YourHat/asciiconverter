from PIL import Image
import PIL
import numpy as np


#im = Image.open('u.jpg')
#pix = im.load()
#hight, width = im.size
#im = im.convert('L')
#pix2 = im.load()
#numimage = []
#for i in range(width):
#    numn = []
#    for j in range(hight):
#        ans = pix2[j,i]//6
#        if ans == 0:
#            ss = '0'
#        elif ans == 1:
#            ss = '1'
#        elif ans == 2:
#            ss = '2'
#        elif ans == 3:
#            ss = '3'
#        elif ans == 4:
#            ss = '4'
#        elif ans == 5:
#            ss = '5'
#        elif ans == 6:
#            ss = '6'
#        elif ans == 7:
#            ss = '7'
#        elif ans == 8:
#            ss = '8'
#        elif ans == 9:
#            ss = '9'
#        elif ans == 10:
#            ss = '10'
#        elif ans == 11:
#            ss = '11'
#        elif ans == 12:
#            ss = '12'
#        elif ans == 13:
#            ss = '13'
#        elif ans == 14:
#            ss = '14'
#        elif ans == 15:
#            ss = '15'
#        elif ans == 16:
#            ss = '16'
#        elif ans == 17:
#            ss = '17'
#        elif ans == 18:
#            ss = '18'
#        elif ans == 19:
#            ss = '19'
#        elif ans == 20:
#            ss = '20'
#        elif ans == 21:
#            ss = '21'
#        elif ans == 22:
#            ss = '22'
#        elif ans == 23:
#            ss = '23'
#        elif ans == 24:
#            ss = '24'
#        elif ans == 25:
#            ss = '25'
#        elif ans == 26:
#            ss = '26'
#        elif ans == 27:
#            ss = '27'
#        elif ans == 28:
#            ss = '28'
#        elif ans == 29:
#            ss = '29'
#        elif ans == 30:
#            ss = '30'
#        elif ans == 31:
#            ss = '31'
#        elif ans == 32:
#            ss = '32'
#        elif ans == 33:
#            ss = '33'
#        elif ans == 34:
#            ss = '34'
#        elif ans == 35:
#            ss = '35'
#        elif ans == 36:
#            ss = '36'
#        elif ans == 37:
#            ss = '37'
#        elif ans == 38:
#            ss = '38'
#        elif ans == 39:
#            ss = '39'
#        elif ans == 40:
#            ss = '40'
#        elif ans == 41:
#            ss = '41'
#        elif ans == 42:
#            ss = '42'
#        numn.append(ss+'.jpg')
#    numimage.append(numn)
#list_img = []
#new_im = Image.new('RGB', (20*hight,20*width),(250,250,250))
#l = 0
#for i in numimage:
#    k = 0
#    for j in i:
#        new_im.paste(Image.open(j),(k,l))
#        k += 20
#    l +=20
#new_im.save('p.jpg')

######################################################

for r in range(1):
    im = Image.open('u'+str(r+99)+'.jpg')
    pix = im.load()
    hight, width = im.size
    im = im.convert('L')
    pix2 = im.load()
    numimage = []
    for i in range(width):
        numn = []
        for j in range(hight):
            ans = pix2[j,i]//6
            if ans == 0:
                ss = '0'
            elif ans == 1:
                ss = '1'
            elif ans == 2:
                ss = '2'
            elif ans == 3:
                ss = '3'
            elif ans == 4:
                ss = '4'
            elif ans == 5:
                ss = '5'
            elif ans == 6:
                ss = '6'
            elif ans == 7:
                ss = '7'
            elif ans == 8:
                ss = '8'
            elif ans == 9:
                ss = '9'
            elif ans == 10:
                ss = '10'
            elif ans == 11:
                ss = '11'
            elif ans == 12:
                ss = '12'
            elif ans == 13:
                ss = '13'
            elif ans == 14:
                ss = '14'
            elif ans == 15:
                ss = '15'
            elif ans == 16:
                ss = '16'
            elif ans == 17:
                ss = '17'
            elif ans == 18:
                ss = '18'
            elif ans == 19:
                ss = '19'
            elif ans == 20:
                ss = '20'
            elif ans == 21:
                ss = '21'
            elif ans == 22:
                ss = '22'
            elif ans == 23:
                ss = '23'
            elif ans == 24:
                ss = '24'
            elif ans == 25:
                ss = '25'
            elif ans == 26:
                ss = '26'
            elif ans == 27:
                ss = '27'
            elif ans == 28:
                ss = '28'
            elif ans == 29:
                ss = '29'
            elif ans == 30:
                ss = '30'
            elif ans == 31:
                ss = '31'
            elif ans == 32:
                ss = '32'
            elif ans == 33:
                ss = '33'
            elif ans == 34:
                ss = '34'
            elif ans == 35:
                ss = '35'
            elif ans == 36:
                ss = '36'
            elif ans == 37:
                ss = '37'
            elif ans == 38:
                ss = '38'
            elif ans == 39:
                ss = '39'
            elif ans == 40:
                ss = '40'
            elif ans == 41:
                ss = '41'
            elif ans == 42:
                ss = '42'
            numn.append(ss+'.jpg')
        numimage.append(numn)
    list_img = []
    new_im = Image.new('RGB', (20*hight,20*width),(250,250,250))
    l = 0
    for i in numimage:
        k = 0
        for j in i:
            new_im.paste(Image.open(j),(k,l))
            k += 20
        l +=20
    new_im.save('p'+str(r+99)+'.jpg')
    print('p'+str(r)+'.jpg is saved.')
