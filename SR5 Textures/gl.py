'''
    Universidad del Valle de Guatemala
    Gráficas por computadora
    Christopher García 20541
    2do. ciclo 2022
'''
from colors import *
from vectors import *
import struct

def char(c):
    # 1 bytes
    return struct.pack('=c', c.encode('ascii'))
    
def word(w):
    # 2 bytes
    return struct.pack('=h', w)
    
def dword(d):
    # 4 bytes
    return struct.pack('=l', d)

class Render(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.InX = 0
        self.InY = 0
        self.current_color = RED
        self.VP_Color = RED
        self.background_Color = BLACK
        self.texture = None
        self.glViewPort(0,0, self.width, self.height)
        self.glClear()

    def write(self, filename):
        f = open(filename, 'bw')
    
        #pixel header
        f.write(char('B'))
        f.write(char('M'))
        f.write(dword(14 + 40 + self.width * self.height * 3))
        f.write(word(0))
        f.write(word(0))
        f.write(dword(14 + 40))
        
        #info header
        f.write(dword(40))
        f.write(dword(self.width))
        f.write(dword(self.height))
        f.write(word(1))
        f.write(word(24))
        f.write(dword(0))
        f.write(dword(self.width * self.height * 3))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        
        #pixel data
        for x in range(self.width):
            for y in range(self.height):
                f.write(self.framebuffer[x][y])
                
        f.close()
        
    def glpoint(self, x, y, colorp=None):
        xComp = (x >= 0 & x < self.width)
        yComp = (y >= 0 & y < self.height)
        
        if(xComp & yComp):
            self.framebuffer[x][y] = colorp or self.current_color
        
    #Funciones

    #Inicializar framebuffer con un tamaño
    def glCreateWindow(self, width, height):
        self.width = width
        self.height = height
        self.glClear()

    #Area de la imagen sobre la que se dibujara
    def glViewPort(self, x, y, width, height):
        self.InX = x
        self.InY = y
        self.ViewPW = width
        self.ViewPH = height

    #Llenar mapa de bits de un color
    def glClear(self):
        self.framebuffer = [
            [self.background_Color for x in range(self.width)]
            for y in range(self.height)
        ]
        
        self.zBuffer = [
            [-9999 for x in range(self.width)]
            for y in range(self.height)
        ]
        
    def glViewPortFM(self, colorp = None):
        ExtremoA = self.InX + self.ViewPW
        ExtremoB = self.InY + self.ViewPH
        
        for a in range(self.InX, ExtremoA):
            for b in range(self.InY, ExtremoB):
                self.glpoint(a,b,colorp or WHITE)

    #Cambiar color glClear
    def glClearColor(self, r, g, b):
        NewColor = color(r, g, b)
        self.background_Color = NewColor
        self.glClear()
        
    #Cambiar color punto en la pantalla
    def glVertex(self, x, y, colorp=None):
        xComp = (x > 1 or x < -1)
        yComp = (y > 1 or y < -1)
         
        if (xComp or yComp):
            print('Fuera de rango')
        else:
            if (x == 1):
                x -= 0.0001
            elif (x == -1):
                x += 0.0001   
            elif (y == 1):
                y -= 0.0001
            elif (y == -1):
                y += 0.0001 
            
            x2 = (x + 1) * round(self.ViewPW/2) + self.InX
            y2 = (y + 1) *round(self.ViewPH/2) + self.InY

            self.glpoint(round(x2), round(y2), colorp or self.VP_Color)

    #Cambiar color glVertex
    def glColor(self, r, g, b):
        self.VP_Color = color(r, g, b)
        
    def glLine(self, x0, y0, x1, y1, colorp=None):
        
        xComp = (x0 > 1 or x0 < -1 or x1 > 1 or x1 < -1)
        yComp = (y0 > 1 or y0 < -1 or y1 > 1 or y1 < -1)
        
        if (xComp or yComp):
            print('Fuera de rango')
            
        else:
            x0 = (x0 + 1) * round(self.ViewPW/2) + self.InX
            y0 = (y0 + 1) *round(self.ViewPH/2) + self.InY
            x1 = (x1 + 1) * round(self.ViewPW/2) + self.InX
            y1 = (y1 + 1) *round(self.ViewPH/2) + self.InY
        
        dy = abs(y1 - y0)
        dx = abs(x1 - x0)
        
        limEm = dy > dx
        
        if (limEm):
            x0, y0 = y0, x0
            x1, y1 = y1, x1
            
        if (x0 > x1):
            x0, x1 = x1, x0
            y0, y1 = y1, y0
            
        dy = abs(y1 - y0)
        dx = abs(x1 - x0)
            
        count = 0
        lim = round(dx)
        y = round(y0)
        
        for x in range (round(x0), round(x1)+1):
            
            if limEm:
                self.glpoint(round(y),round(x), colorp)
            else: 
                self.glpoint(round(x),round(y), colorp) 
            
            count += dy * 2
            if (count >= lim): 
                if (y0 < y1):
                    y += 1
                else:
                    y -= 1
                lim += dx * 2   
                
    def line(self, A, B, colorp=None):
        
        x0 = round(A.x)
        y0 = round(A.y)
        x1 = round(B.x)
        y1 = round(B.y)
        
        if ((x0 == x1) and (y0 == y1)):
            self.glpoint(x0, y0,colorp)
            return
        
        dy = abs(y1 - y0)
        dx = abs(x1 - x0)
        
        limEm = dy > dx
        
        if (limEm):
            x0, y0 = y0, x0
            x1, y1 = y1, x1
            
        if (x0 > x1):
            x0, x1 = x1, x0
            y0, y1 = y1, y0
            
        dy = abs(y1 - y0)
        dx = abs(x1 - x0)
            
        count = 0
        lim = dx
        y = y0
        
        for x in range (x0, x1+1):
            if limEm:
                self.glpoint(x, y, colorp)
            else: 
                self.glpoint(y, x, colorp) 
            
            count += dy * 2
            if (count >= lim): 
                if (y0 < y1):
                    y += 1
                else:
                    y -= 1
                lim += dx * 2 

    #Escribir imagen 
    def glFinish(self):
        self.write('a.bmp')
        
#Iniciar objeto interno
def glinit():
    return Render(1024, 1024)

