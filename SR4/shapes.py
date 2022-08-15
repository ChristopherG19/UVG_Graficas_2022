'''
    Universidad del Valle de Guatemala
    Gráficas por computadora
    Christopher García 20541
    2do. ciclo 2022
'''

from gl import *
from colors import *
from vectors import *

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
    #--> Forma extensa: 
    sizeP = len(puntos)
    count = 0
    while (count != sizeP):
        if (count == sizeP-1):
            x0 = puntos[sizeP-1][0]
            y0 = puntos[sizeP-1][1]
            x1 = puntos[0][0]
            y1 = puntos[0][1]
            A = V2(x0,y0)
            B = V2(x1,y1)
            r.line(A, B, BLACK) 
        elif (count < sizeP-1):
            x0 = puntos[count][0]
            y0 = puntos[count][1]
            x1 = puntos[count+1][0]
            y1 = puntos[count+1][1]
            A = V2(x0,y0)
            B = V2(x1,y1)
            r.line(A, B, BLACK) 
        count += 1
    
def Center(puntos):
    centro = (0,0)
    x = 0
    y = 0
    for punto in range(0, len(puntos)):
        x += puntos[punto][0]
        y += puntos[punto][1]
    x = round(x/len(puntos))
    y = round(y/len(puntos))
    centro = (x,y)
    return centro
    
def InsidePoligon(x, y, puntos, sizeP):
    PuntoDentro = False
    x0, y0 = puntos[0]
    for i in range(sizeP+1):
        x1, y1 = puntos[i % sizeP]
        if (y > min(y0, y1)):
            if (y <= max(y0, y1)):
                if (x <= max(x0, x1)):
                    if (y0 is not y1):
                        xDentro = (y-y0)*(x1-x0)/(y1-y0)+x0    
                    if (x0 == x1 or x <= xDentro):
                        PuntoDentro = not PuntoDentro
        x0, y0 = x1, y1
    return PuntoDentro
    
def FillPoligons(r, puntos, colorp):
    sizeP = len(puntos)
    for x in range(r.width):
        for y in range(r.height):
            if(InsidePoligon(x,y,puntos,sizeP)):
                r.glpoint(x, y, colorp or WHITE)

def boundingB(*vertices):
    coords = [ (vertex.x, vertex.y) for vertex in vertices ]
    
    xmin = 999999
    xmax = -999999
    ymin = 999999
    ymax = -999999
    
    for (x,y) in coords:
        if (x < xmin):
            xmin = x
        if (x > xmax):
            xmax = x
        if (y < ymin):
            ymin = y
        if (y > ymax):
            ymax = y

    return V3(xmin, ymin), V3(xmax, ymax)

def barycentric(A, B, C, P):
    cx, cy, cz = cross(
        V3(B.x - A.x, C.x - A.x, A.x - P.x),
        V3(B.y - A.y, C.y - A.y, A.y - P.y)
    )
    if (abs(cz) < 1):
        return (-1, -1, -1)
    u = cx/cz
    v = cy/cz
    w = 1 - (u + v)
    return (w, v, u)
    
def transform(vertex, scale, translate):
    return V3(
        (vertex[0] * scale[0]) + translate[0],
        (vertex[1] * scale[1]) + translate[1],
        (vertex[2] * scale[2]) + translate[2]
    )

def triangule(r, A, B, C):
    
    # Acolor = (255, 0, 0)
    # Bcolor = (0, 255, 0)
    # Ccolor = (0, 0, 255)
    
    L = V3(0, 0, 1)
    N = (B - A) * (C - A)
    i = N.norm() @ L.norm()
    
    if (i < 0):
        return
    
    gris = round(255 * i)

    r.current_color = color2(gris, gris, gris)
    
    Bmin, Bmax = boundingB(A,B,C)
    Bmin.round()
    Bmax.round()
    
    for x in range(Bmin.x, Bmax.x + 1):
        for y in range(Bmin.y, Bmax.y + 1):
            w, v, u = barycentric(A, B, C, V3(x, y))        
            if (w < 0 or v < 0 or u < 0):
                continue
            
            z = A.z * w + B.z * v + C.z * u
            
            if (r.zBuffer[x][y] < z): 
                r.zBuffer[x][y] = z
                r.glpoint(y, x)

            
          
            
            
            