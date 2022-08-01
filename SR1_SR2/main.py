'''
    Universidad del Valle de Guatemala
    Gráficas por computadora
    Christopher García 20541
    2do. ciclo 2022
'''

from gl import *
from Colors import *
from Shapes import *

width = 100
height = 100
veri = True
r = glinit()
#r.glCreateWindow(width,height)
r.glClear()
#r.line(13, 20, 80, 40, RED)
r.glFinish()

while(veri):
    try:        
        print('\n\t\tMenu')
        print('1) Especificar size ventana')
        print('2) ViewPort')
        print('3) ClearViewPort')
        print('4) Clear')
        print('5) Clear Color')
        print('6) Vertex ejemplo')
        print('7) Vertex Color')
        print('8) Crear punto (Vertex)')
        print('9) Crear linea')
        print('10) House')
        print('11) Salir y escribir la imagen\n')
                
        op = int(input('Opcion: '))
        
        if (op == 1):
            try:
                ver = True
                while (ver):
                    width = int(input('Ingrese ancho: '))
                    height = int(input('Ingrese alto: '))
                    
                    if (width < height or (width % 4 != 0) or width < 0 or height < 0):
                        print('Error, no es posible trabajar con estos datos')
                    else:
                        ver = False
            except:
                print('Error, Ingreso invalido')

            r.glCreateWindow(width,height)
            r.glFinish()
            
        elif (op == 2):
            print('Para crear el Viewport son necesarios los siguientes datos: ')
            print('1) coordenada x, y')
            print('2) ancho')
            print('3) alto\n')
            
            try:
                ver = True
                while (ver):
                    x = int(input('Ingrese x: '))
                    y = int(input('Ingrese y: '))
                    widthVP = int(input('Ingrese ancho: '))
                    heightVP = int(input('Ingrese alto: '))
                    
                    if (widthVP < heightVP or widthVP < 0 or heightVP < 0 or x < 0 or y < 0):
                        print('Error, no es posible trabajar con algun dato')
                        print('Intente nuevamente')
                    else:
                        ver = False
                    
            except:
                print('Error, Ingreso invalido')
            
            r.glViewPort(x,y,widthVP,heightVP)
            r.glViewPortFM()
            r.glFinish()
            
        elif (op == 3):
            #Pasar un color en esta función para cambiar el fondo del VP
            r.glViewPortFM()
            r.glFinish() 
            
        elif (op == 4):
            r.glClear()
            r.glFinish()
            
        elif (op == 5):
            print('Los valores permitidos para el color estan entre 0 y 1')
            try:
                ver = True
                while(ver):
                    rC = float(input('Valor de r: '))
                    g = float(input('Valor de g: '))
                    b = float(input('Valor de b: '))
                    
                    if ((0 > rC > 1) | (0 > g > 1) | (0 > b > 1)):
                        print('Error, solo se permiten valores entre 0 y 1')
                    else:
                        print('Cambiando color...')
                        r.glClearColor(rC,g,b)
                        r.glFinish()
                        ver = False
            except Exception as E:
                print(E)
                print('Error, valor(es) invalido(s)')
            
        elif (op == 6):
            print('Ejercicios de muestra')
            print('Coordenadas (-1,-1), (0,0), (1,1)')
            r.glVertex(1, 1)
            r.glVertex(0, 0)
            r.glVertex(-1, -1)
            r.glFinish()
            
        elif (op == 7):
            print('Los valores permitidos para el color estan entre 0 y 1')
            try:
                ver = True
                while(ver):
                    rC = float(input('Valor de r: '))
                    g = float(input('Valor de g: '))
                    b = float(input('Valor de b: '))
                    
                    if ((0 > rC > 1) | (0 > g > 1) | (0 > b > 1)):
                        print('Error, solo se permiten valores entre 0 y 1')
                    else:
                        print('Cambiando color...')
                        r.glColor(rC,g,b)
                        r.glFinish()
                        ver = False
            except:
                print('Error, valor(es) invalido(s)')
        
        elif (op == 8):
            print('Los valores permitidos estan entre -1 y 1')
            try:
                ver = True 
                while(ver):
                    x = float(input('Valor de x: '))
                    y = float(input('Valor de y: '))
                    
                    if((-1 > x > 1) or (-1 > y > 1)):
                        print('Error, solo se permiten valores entre -1 y 1')
                    else:
                        print('Colocando punto...')
                        r.glVertex(x, y)
                        r.glFinish()
                        ver = False
            except Exception as E:
                print(E)
                print('Error, valor(es) invalido(s)')
        
        elif (op == 9):
            print('Los valores permitidos estan entre -1 y 1')
            try:
                ver = True 
                while(ver):
                    x0 = float(input('Valor de x0: '))
                    y0 = float(input('Valor de y0: '))
                    x1 = float(input('Valor de x1: '))
                    y1 = float(input('Valor de y1: '))
                    
                    if((-1 > x0 > 1) or (-1 > y0 > 1) or (-1 > x1 > 1) or (-1 > y1 > 1)):
                        print('Error, solo se permiten valores entre -1 y 1')
                    else:
                        print('Creando linea...')
                        r.glLine(x0, y0, x1, y1, RED)
                        r.glFinish()
                        ver = False
            except Exception as E:
                print(E)
                print('Error, valor(es) invalido(s)')
            
        elif (op == 10):
            house(r)
            r.glFinish()
            
        elif (op == 11):
            r.glFinish()
            veri = False
        
    except Exception as e:
        print(e)
        print('Error, ingreso invalido')
