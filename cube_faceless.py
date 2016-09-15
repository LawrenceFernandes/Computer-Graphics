#!/usr/bin/python
# -*- coding: utf-8 -*-

# File Name: cube_faceless.py
# Author: Lawrence Fernandes
# Copyright (C) 2016 Lawrence Fernandes

""" This module draws a cube without its faces.
"""
# Import OpenGL modules
try:
    from OpenGL.GLUT import *
    from OpenGL.GLU import *
    from OpenGL.GL import *
except:
    print ("OpenGL wrapper for Python not found.")

#Define the location (x,y,z) of each vertex
vertices= (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
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
    (5,7)
    )

#Define the colors used for the faces of the cube
colors = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )

def Cube():
	"""This function creates the cube."""
    glBegin(GL_LINES)
    for line in lines:
        for vertex in line:
            glColor3fv(colors[vertex])
            glVertex3fv(vertices[vertex])
    glEnd()

def display():
    """This function call the OpenGL functions to display something"""
    # Clear the color and depth buffers
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    # ... render stuff in here ...
    # It will go to an off-screen frame buffer.
    glRotatef(2,1,3,0)
    Cube()
     # Copy the off-screen buffer to the screen.
    glutSwapBuffers()

def timer(i):
	"""This function creates a timer to rotate the cube."""
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

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
glutTimerFunc(50,timer,1)
# Run the GLUT main loop until the user closes the window.
glutMainLoop()