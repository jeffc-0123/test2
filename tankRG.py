import math

C = 9.8 * math.pow(10,-6)
G = 1
H = 9000
R = 8000
ti = input('Input thickness: ')
t = int(ti)
E = 203000
B = 1.285/(math.pow(R*t,0.5))
#print('B:',B)

w1 = (C * G * H * math.pow(R,2))
w2 = (E * t)

L = 0
while L < 9001:
    e = math.exp(-(B * L))
    cos = math.cos(B * L)
    w3 = (1 - e * cos - (L / H))

    #print('e:',e)
    #print('cos:', cos)

    #print('e*cos:', e * cos)

    W = w1 / w2 * w3

    #print('w1:(',w1,')')
    #print('w2:(',w2,')')
    #print('w3:(',w3,')')
    print('L:',L)
    print('answer:',W)
    print('')
    L += 1500
