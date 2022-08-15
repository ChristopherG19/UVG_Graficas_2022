'''
    Universidad del Valle de Guatemala
    Gráficas por computadora
    Christopher García 20541
    2do. ciclo 2022
'''

from objects3d import Obj
from gl import *
from colors import *
from shapes import *

width = 100
height = 100
veri = True
r = glinit()
r.glClear()
r.glFinish()

VP_Active = False

while(veri):
    try:        
        print('\n\t\tMenu')
        print('1) Opciones manuales')
        print('2) Puntos')
        print('3) House')
        print('4) Poligonos')
        print('5) 3D Flat Shading')
        print('6) 3D Texturas')
        print('20) Salir y escribir la imagen\n')
                
        op = int(input('Opcion: '))
        
        if (op == 1):
            
            veri2 = True
            while(veri2):
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
                    print('10) Salir\n')
                    
                    op1 = int(input('Opcion: '))
                    
                    if (op1 == 1):
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
                    
                    elif (op1 == 2):
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
                        VP_Active = True
                        r.glFinish()
                        
                    elif (op1 == 3):
                        #Pasar un color en esta función para cambiar el fondo del VP
                        r.glViewPortFM()
                        r.glFinish() 
                        
                    elif (op1 == 4):
                        r.glClear()
                        r.glFinish()
                        
                    elif (op1 == 5):
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
                        
                    elif (op1 == 6):
                        print('Ejercicios de muestra')
                        print('Coordenadas (-1,-1), (0,0), (1,1)')
                        r.glVertex(1, 1)
                        r.glVertex(0, 0)
                        r.glVertex(-1, -1)
                        r.glFinish()
                        
                    elif (op1 == 7):
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
                    
                    elif (op1 == 8):
                        print('Los valores permitidos estan entre -1 y 1')
                        try:
                            ver = True 
                            while(ver):
                                x = float(input('Valor de x: '))
                                y = float(input('Valor de y: '))
                                
                                xComp = (x > 1 or x < -1)
                                yComp = (y > 1 or y < -1)
                                
                                if (xComp or yComp):
                                    print('Error, solo se permiten valores entre -1 y 1')
                                else:
                                    print('Colocando punto...')
                                    r.glVertex(x, y)
                                    r.glFinish()
                                    ver = False
                        except Exception as E:
                            print(E)
                            print('Error, valor(es) invalido(s)')
                    
                    elif (op1 == 9):
                        print('Los valores permitidos estan entre -1 y 1')
                        try:
                            ver = True 
                            while(ver):
                                x0 = float(input('Valor de x0: '))
                                y0 = float(input('Valor de y0: '))
                                x1 = float(input('Valor de x1: '))
                                y1 = float(input('Valor de y1: '))
                                
                                xComp = (x0 > 1 or x0 < -1 or x1 > 1 or x1 < -1)
                                yComp = (y0 > 1 or y0 < -1 or y1 > 1 or y1 < -1)
                                
                                if (xComp or yComp):
                                    print('Error, solo se permiten valores entre -1 y 1')
                                else:
                                    print('Creando linea...')
                                    r.glLine(x0, y0, x1, y1, RED)
                                    r.glFinish()
                                    ver = False
                        except Exception as E:
                            print(E)
                            print('Error, valor(es) invalido(s)')
                    elif (op1 == 10):
                        r.glFinish()
                        veri2 = False
                except:
                    print('Error, ingreso invalido')
            
        elif (op == 2):
            width = 512
            height = 512
            r.glCreateWindow(width, height)
            r.glViewPort(int(width/4), int(height/4), int(width/2), int(height/2))
            r.glClearColor(0.4, 0.5, 0.4)
            r.glClear()
            r.glViewPortFM(color(1, 1, 1))
            r.glVertex(1, 1, color(0, 0, 0))
            r.glVertex(0, 0, color(0, 0, 0))
            r.glVertex(-1, -1, color(0, 0, 0))
            r.glFinish()
          
        elif (op == 3):
            if(VP_Active == False):
                r.glCreateWindow(512,512)
                r.glViewPort(128,128,256,256)
                r.glViewPortFM()
                house(r)
                r.glFinish()
            else:
                house(r)
                r.glFinish()
                
        elif (op == 4):
            
            r.glCreateWindow(1024,1024)
            r.glClear()
            
            pol1 = [(165, 380), (185, 360), (180, 330), (207, 345), (233, 330), 
                    (230, 360), (250, 380), (220, 385), (205, 410), (193, 383)]

            pol2 = [(321, 335), (288, 286), (339, 251), (374, 302)]

            pol3 = [(377, 249), (411, 197), (436, 249)]

            pol4 = [(413, 177), (448, 159), (502, 88), (553, 53), (535, 36), (676, 37),
                    (660, 52), (750, 145), (761, 179), (672, 192), (659, 214), (615, 214),
                    (632, 230), (580, 230), (597, 215), (552, 214), (517, 144), (466, 180)]

            pol5 = [(682, 175), (708, 120), (735, 148), (739, 170)]
            
            r.glCreateWindow(1024,1024)
            DrawPoligons(r, pol1)
            DrawPoligons(r, pol2)
            DrawPoligons(r, pol3)
            DrawPoligons(r, pol4)
            DrawPoligons(r, pol5)
            FillPoligons(r, pol1, GREEN)
            FillPoligons(r, pol2, BLUE)
            FillPoligons(r, pol3, YELLOW)
            FillPoligons(r, pol4, RED)
            FillPoligons(r, pol5, r.background_Color)
 
            r.glFinish()
            
        elif (op == 5):  
            r.glCreateWindow(1000,1000)  
                        
            cube = Obj('./Shine.obj')
                
            s = (200,200,500)
            tf = (512,512,0)
            
            for face in cube.caras:
                
                if (len(face) == 4):
                    f1 = face[0][0] - 1
                    f2 = face[1][0] - 1
                    f3 = face[2][0] - 1
                    f4 = face[3][0] - 1
                    
                    v1 = transform(cube.vertices[f1], s, tf)
                    v2 = transform(cube.vertices[f2], s, tf)
                    v3 = transform(cube.vertices[f3], s, tf)
                    v4 = transform(cube.vertices[f4], s, tf)

                    triangule(r, v1, v2, v3)
                    triangule(r, v1, v3, v4)
                    
            
                if (len(face) == 3):
                    f1 = face[0][0] - 1
                    f2 = face[1][0] - 1
                    f3 = face[2][0] - 1
                    
                    v1 = transform(cube.vertices[f1], s, tf)
                    v2 = transform(cube.vertices[f2], s, tf)
                    v3 = transform(cube.vertices[f3], s, tf)
                
                    triangule(r, v1, v2, v3)
            
            r.glFinish()
            
        elif (op == 6):
            r.glCreateWindow(200, 200)
            r.current_color = color(0, 0.8, 0.8)
                
            s = (400, 400, 500)
            tf = (512, 500, 0)
            
            triangule(r, V3(10,70), V3(50,160), V3(70,80))
            triangule(r, V3(180,50), V3(150,1), V3(70,180))
            triangule(r, V3(180,150), V3(120,160), V3(130,180))
            
            r.glFinish()
    
        elif (op == 20):
            r.glFinish()
            veri = False
        
    except Exception as e:
        print(e)
        print('Error, ingreso invalido')
