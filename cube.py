#!/usr/bin/python
# -*- coding: utf-8 -*-

# File Name: cube.py
# Author: Lawrence Fernandes
# Copyright (C) 2016 Lawrence Fernandes

""" This module draws a cube with its faces (polygon mesh) or without them.
    The cube is rotated on the screen. It can be done automatically or by the user,
    deppending on the arguments the program takes.
"""
#Import Python module
import sys
# Import OpenGL modules
try:
    from OpenGL.GLUT import *
    from OpenGL.GLU import *
    from OpenGL.GL import *
except:
    print ("OpenGL wrapper for Python not found.")

#Input validation
option = ' '.join(sys.argv[1:])
if option not in ("-f", "-m", "-f -c", "-m -c"):
    print ("\nInvalid option! Please, try again.")
    sys.exit(1)

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

#Define the edges connecting the vertices
edges = (
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

def cube_faceless():
    """This function creates a faceless cube."""
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glColor3fv(colors[vertex])
            glVertex3fv(vertices[vertex])
    glEnd()

def cube_wfaces():
    """This function creates a cube with colored faces."""
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
    for edge in edges:
        for vertice in edge:
            glVertex3fv(vertices[vertice])
    glEnd()

def display():
    """This function call the OpenGL functions to display something"""
    # Clear the color and depth buffers
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    # ... render stuff in here ...
    # It will go to an off-screen frame buffer.
    glRotatef(2,1,3,0)
    # Selecting the function to draw the cube
    if option=="-f":
        cube_faceless()
    else:
        cube_wfaces()
    glutSwapBuffers()

def timer(i):
    """This function creates a timer to automatically rotate the cube."""
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

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
# Create a double-buffer RGBA window.   (Single-buffering is possible.
# So is creating an index-mode window.)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
# Create a window, setting its size and title
glutInitWindowSize(800,600)
glutCreateWindow("Cube")
# Set the display callback.  You can set other callbacks for keyboard and
# mouse events.
glutDisplayFunc(display)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-10)
glRotatef(0,0,0,0)
# Switching the rotation options
if option=="-f -c" or option=="-m -c":
    # The callback function for keyboard controls
    glutSpecialFunc(keyboard)
else:
    # The callback function for the timer
    glutTimerFunc(50,timer,1)
# Run the GLUT main loop until the user closes the window.
glutMainLoop()
