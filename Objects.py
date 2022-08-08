'''
    Universidad del Valle de Guatemala
    Gráficas por computadora
    Christopher García 20541
    2do. ciclo 2022
'''

class Obj(object):
    def __init__(self, filename):
        with open(filename) as f:
            self.lines = f.read().splitlines()
            
        self.vertices = []
        self.caras = []
        
        for line in self.lines:
            
            if not line:
                continue
            
            prefix, value = line.split(' ', 1)
            
            if (prefix == 'v'):
                self.vertices.append(
                    list(
                        map(float, value.split(' '))
                    )
                )
            
            elif (prefix == 'f'):
                self.caras.append([
                    list(map(int, face.split('//')))
                        for face in value.split(' ')
                ])
