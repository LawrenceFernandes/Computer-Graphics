# -*- coding: utf-8 -*-
#Author: Lawrence Fernandes
#This program creates and rotates a 3D cube using OpenGL

from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

vertices = (
    ( 1,-1,-1),
    ( 1, 1,-1),
    (-1, 1,-1),
    (-1,-1,-1),
    ( 1,-1, 1),
    ( 1, 1, 1),
    (-1,-1, 1),
    (-1, 1, 1),
    )

lines = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7),
    )

faces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
    )

colors = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )

def Cube():
    glBegin(GL_QUADS)
    i = 0
    for face in faces:
        glColor3fv(colors[i])
        for vertex in face:
            glColor3fv(colors[vertex])
            glVertex3fv(vertices[vertex])
        i = i+1
    glEnd()

    glColor3fv((0,0.5,0))
    glBegin(GL_LINES)
    for line in lines:
        for vertice in line:
            glVertex3fv(vertices[vertice])
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    Cube()
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

# MAIN
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)

glutInitWindowSize(800,600)
glutCreateWindow("Cube 3D")
glutDisplayFunc(display)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-10)
glRotatef(0,0,0,0)
glutTimerFunc(50,timer,1)
glutMainLoop()
