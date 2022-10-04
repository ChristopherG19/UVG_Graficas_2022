'''
    Universidad del Valle de Guatemala
    Gráficas por computadora
    Christopher García 20541
    2do. ciclo 2022
'''

import math
from gl import *
from shapes import * 
from colors import *
from vectors import *
from textures import *
from matrix import *

# center = (300, 300)

# points = [
#     (200, 200),
#     (400, 200),
#     (400, 400),
#     (200, 400),
# ]

# # scale_matrix = matrix([
# #     [3/2, 0],
# #     [0, 3/2]
# # ])
        
# a = math.pi/6

# # rotation_matrix = matrix([
# #     [cos(a), -sin(a), 0],
# #     [sin(a), cos(a), 0],
# #     [0, 0, 1]
# # ])

# # move_to_center_matrix = matrix([
# #     [1, 0, -center[0]],
# #     [0, 1, -center[1]],
# #     [0, 0, 1]
# # ])

# # scale_matrix = matrix([
# #     [1, 0, 0],
# #     [0, 1, 0],
# #     [0.003, 0, 1]
# # ])

# # move_from_center_matrix = matrix([
# #     [1, 0, center[0]],
# #     [0, 1, center[1]],
# #     [0, 0, 1]
# # ])

# move_to_center_matrix_2 = [
#     [1, 0, -center[0]],
#     [0, 1, -center[1]],
#     [0, 0, 1]
# ]

# scale_matrix_2 = [
#     [1, 0, 0],
#     [0, 1, 0],
#     [0.003, 0, 1]
# ]

# move_from_center_matrix_2 = [
#     [1, 0, center[0]],
#     [0, 1, center[1]],
#     [0, 0, 1]
# ]

# # transformed_matrix = move_from_center_matrix @ scale_matrix @ move_to_center_matrix
# temps = matrix_multiplication(scale_matrix_2, move_to_center_matrix_2)
# transformed_matrix_2 = matrix_multiplication(move_from_center_matrix_2, temps)

# temp_points = []
# transformed_points = []
# for p in points:
#     tp = matrix_multiplication(transformed_matrix_2, [p[0], p[1], 1])

#     t = []
#     for i in tp:
#         t.append(i[0])
    
#     temp_points.append(t)

# for tempP in temp_points:
#     tp2 = [
#         tempP[0]/tempP[2],
#         tempP[1]/tempP[2]
#     ]
#     transformed_points.append(V3(*tp2))

# transformed_points = []
# for p in points:
#     tp = transformed_matrix @ [
#         p[0], 
#         p[1], 
#         1
#     ]
#     print(tp)
#     tp = tp.tolist()[0]
#     tp2 = [
#         tp[0]/tp[2],
#         tp[1]/tp[2]
#     ]
    
#     transformed_points.append(V3(*tp2))

# print(transformed_points)

# r = Render(900, 900)

# # r.glpoint(400,400,GREEN)
# # r.glpoint(800,400,BLUE)
# # r.glpoint(800,800,RED)
# # r.glpoint(400,800,WHITE)

# prev_p = transformed_points[-1]
# for point in transformed_points:
#     r.line(prev_p, point, WHITE)
#     prev_p = point

# r.write("trans.bmp")

r = Render(1024,1024)  
                        
t = Texture('./helmet.bmp')
r.texture = t

cube = Obj('./helmet_clean.obj')

# ------------ Dutch Angle ------------------
# s = (30, 30, 60)
# tf = (512, 500, 0)
# rot = (0, 0.1, 0.35)

# load_model(r, t,'./helmet_clean.obj', tf, s, rot)
# r.write("Dutch_Angle.bmp")

# ------------ High Angle ------------------
# s = (30,30,30)
# tf = (512, 500, 0)
# rot = (2, 0, 0)

# load_model(r, t,'./helmet_clean.obj', tf, s, rot)
# r.write("High_Angle.bmp")

# ------------ Medium Angle ------------------
# s = (30,30,30)
# tf = (512, 500, 1)
# rot = (0, 0, 0)

# load_model(r, t,'./helmet_clean.obj', tf, s, rot)
# r.write("Medium_Angle.bmp")

# ------------ Low Angle ------------------
# s = (30,30,30)
# tf = (512, 500, 0)
# rot = (-0.6, 0, 0)

# load_model(r, t,'./helmet_clean.obj', tf, s, rot)
# r.write("Low_Angle.bmp")