#!/usr/bin/python
# -*- coding: utf-8 -*-

# File Name: cube_wfaces.py
# Author: Lawrence Fernandes
# Copyright (C) 2016 Lawrence Fernandes

""" This module draws a cube with its faces (polygon mesh).
    Controls: UP - rotate up
        DOWN - rotate down
        LEFT - rotate left
        RIGHT - rotate right
"""
# Import OpenGL modules
try:
    from OpenGL.GLUT import *
    from OpenGL.GLU import *
    from OpenGL.GL import *
except:
    print ("OpenGL wrapper for Python not found.")

#Define the location (x,y,z) of each vertex
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

#Define the lines connecting the vertices
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

#Define the faces of the cube
faces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
    )

#Define the colors used for the faces of the cube
colors = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )

def Cube():
    """This function creates the cube."""
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
    """This function call the OpenGL functions to display something"""
    # Clear the color and depth buffers
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    Cube()
    # Copy the off-screen buffer to the screen.
    glutSwapBuffers()

def keyboard(key, x, y):
    """This function creates keyboard controls."""
    rotate_y = 0.0
    rotate_x = 0.0
    scale = 2.0
    # Rotate cube according to keys pressed
    if key == GLUT_KEY_RIGHT:
        rotate_y += 10
    if key == GLUT_KEY_LEFT:
        rotate_y -= 10
    if key == GLUT_KEY_UP:
        rotate_x += 10
    if key == GLUT_KEY_DOWN:
        rotate_x -= 10
    glutPostRedisplay()

# MAIN
glutInit(sys.argv)
# Create a double-buffer RGBA window.
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
# Create a window, setting its size and title
glutInitWindowSize(800,600)
glutCreateWindow("Cube")
# Set the display callback.
glutDisplayFunc(display)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-10)
glRotatef(0,0,0,0)
# The callback function for keyboard controls
glutSpecialFunc(keyboard)
# Run the GLUT main loop until the user closes the window.
glutMainLoop()
