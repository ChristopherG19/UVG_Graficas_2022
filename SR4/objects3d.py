'''
    Universidad del Valle de Guatemala
    Gráficas por computadora
    Christopher García 20541
    2do. ciclo 2022
'''
import re

class Obj(object):
    def __init__(self, filename):
        with open(filename) as f:
            self.lines = f.read().splitlines()
            
        self.vertices = []
        self.tvertices = []
        self.caras = []
        
        for line in self.lines:
            
            if not line:
                continue
            
            prefix, value = line.split(' ', 1)
            
            if (prefix == 'v'):
                temp = []
                list(map(lambda x: temp.append(float(x)) 
                        if (x != '') else False, value.split(' ')))
                self.vertices.append(temp)
            
            if (prefix == 'vt'):
                temp = []
                list(map(lambda x: temp.append(float(x)) 
                        if (x != '') else False, value.split(' ')))
                self.tvertices.append(temp)
            
            if (prefix == 'f'):
                self.caras.append([
                    list(map(int, re.split('/+',face))) for face in value.split(' ')
                ])


