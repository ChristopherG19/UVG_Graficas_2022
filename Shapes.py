'''
    Universidad del Valle de Guatemala
    Gráficas por computadora
    Christopher García 20541
    2do. ciclo 2022
'''

from gl import *
from Colors import *

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
    
    

