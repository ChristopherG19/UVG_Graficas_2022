'''
    Universidad del Valle de Guatemala
    Gráficas por computadora
    Christopher García 20541
    2do. ciclo 2022
'''

from tkinter import Y
from gl import *
from Colors import *
from vector import *

#SR2
def house(r):
    #Base
    r.glLine(-0.5, 0.49, 0, 0.49, RED)
    r.glLine(-0.5, -0.5, -0.5, 0.49, RED)
    r.glLine(-0.3, -0.7, -0.5, -0.5, RED)
    r.glLine(0.19, -0.68, -0.305, -0.68, RED)
    r.glLine(-0.5, -0.5, 0, -0.5, RED)
    #Techo
    r.glLine(0.2, -0.7, 0, -0.5, BLUE)
    r.glLine(0, 0.499, 0, -0.5, BLUE)
    r.glLine(0.001, 0.499, 0.5, -0.001, BLUE)
    r.glLine(0, -0.5, 0.5, 0, BLUE)
    r.glLine(0.61, -0.2, 0.19, -0.68, BLUE)
    r.glLine(0.61, -0.2, 0.5, 0, BLUE)
    #Puerta
    r.glLine(-0.5, -0.1, -0.5, 0.1, GREEN)
    r.glLine(-0.5, -0.1, -0.25, -0.1, GREEN)
    r.glLine(-0.5, 0.1, -0.25, 0.1, GREEN)
    r.glLine(-0.25, -0.1, -0.25, 0.1, GREEN)
    
#LAB_01: Rellenar polígonos
pol1 = [(165, 380), (185, 360), (180, 330), (207, 345), (233, 330), 
        (230, 360), (250, 380), (220, 385), (205, 410), (193, 383)]
pol2 = [(321, 335), (288, 286), (339, 251), (374, 302)]
pol3 = [(377, 249), (411, 197), (436, 249)]
pol4 = [(413, 177), (448, 159), (502, 88), (553, 53), (535, 36), (676, 37),
        (660, 52), (750, 145), (761, 179), (672, 192), (659, 214), (615, 214),
        (632, 230), (580, 230), (597, 215), (552, 214), (517, 144), (466, 180)]
pol5 = [(682, 175), (708, 120), (735, 148), (739, 170)]

#Función para dibujar cualquier polígono
def DrawPoligons(r, puntos):
    last = puntos[-1]
    for p in puntos:
        r.line(*last, *p, WHITE)
        last = p
    
    ''' #--> Forma extensa: 
    sizeP = len(puntos)
    count = 0
    while (count != sizeP):
        if (count == sizeP-1):
            x0 = puntos[sizeP-1][0]
            y0 = puntos[sizeP-1][1]
            x1 = puntos[0][0]
            y1 = puntos[0][1]
            r.line(x0, y0, x1, y1, WHITE) 
        elif (count < sizeP-1):
            x0 = puntos[count][0]
            y0 = puntos[count][1]
            x1 = puntos[count+1][0]
            y1 = puntos[count+1][1]
            r.line(x0, y0, x1, y1, WHITE) 
        count += 1
    '''

def Center(puntos):
    centro = (0,0)
    x = 0
    y = 0
    for punto in range(0, len(puntos)):
        x += puntos[punto][0]
        y += puntos[punto][1]
    x = trunc(x/len(puntos))
    y = trunc(y/len(puntos))
    centro = (x,y)
    return centro

def FillPoligons(r, puntos):
    centro = Center(puntos)
    r.glpoint(trunc(centro[0]),trunc(centro[1]),WHITE)

    xPoints = []
    yPoints = []
    
    sizeP = len(puntos)
    coun = 0

    while (coun != sizeP):
        if (coun == sizeP-1):
            tempX = []
            tempY = []
            print(puntos[coun][0], puntos[coun][1], puntos[0][0], puntos[0][1]) 
            if (puntos[coun][0] > puntos[0][0]):
                for i in range(puntos[coun][0], puntos[0][0]-1, -1):
                    tempX.append(i)
                xPoints.append(tempX)
            else:
                for i in range(puntos[coun][0], puntos[0][0]+1):
                    tempX.append(i)
                xPoints.append(tempX)
                    
            if (puntos[coun][1] > puntos[0][1]):
                for i in range(puntos[coun][1], puntos[0][1]-1, -1):
                    tempY.append(i)
                yPoints.append(tempY)
            else:
                for i in range(puntos[coun][1], puntos[0][1]+1):
                    tempY.append(i)
                yPoints.append(tempY)
            
        else:
            tempX = []
            tempY = []
            print(puntos[coun][0], puntos[coun][1], puntos[coun+1][0], puntos[coun+1][1])
            if (puntos[coun][0] > puntos[coun+1][0]):
                for i in range(puntos[coun][0], puntos[coun+1][0]-1, -1):
                    tempX.append(i)
                xPoints.append(tempX)
            else:
                for i in range(puntos[coun][0], puntos[coun+1][0]+1):
                    tempX.append(i)
                xPoints.append(tempX)
                    
            if (puntos[coun][1] > puntos[coun+1][1]):
                for i in range(puntos[coun][1], puntos[coun+1][1]-1, -1):
                    tempY.append(i)
                yPoints.append(tempY)
            else:
                for i in range(puntos[coun][1], puntos[coun+1][1]+1):
                    tempY.append(i)
                yPoints.append(tempY)
        
        coun +=1

    '''print(len(xPoints))
    print(len(yPoints))
    print()
    print(xPoints)
    print()
    print(yPoints)
    print()'''

    for i in range(len(xPoints)):
        xTemp = 0
        yTemp = 0
    
        for j in range(len(xPoints[i])):
            xTemp = xPoints[i][j]
            #print("Intento: ",i, "X(",j,"): ",xTemp)
            
        for k in range(len(yPoints[i])):
            yTemp = yPoints[i][k]
            #print("Intento: ",i, "Y(",k,"): ",yTemp)
            
        r.line(trunc(centro[0]),trunc(centro[1]), xTemp, yTemp, WHITE)
    

    