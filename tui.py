#!/usr/bin/python
# -*- coding: utf-8 -*-

# File Name: tui.py
# Author: Lawrence Fernandes
# Copyright (C) 2016 Lawrence Fernandes

""" This module is the terminal user interface (TUI) of the app.
    It calls the other modules to draw the polyhedron requested by the user.
    The other modules must be located on the same directory.
"""
# Import Python modules
import os, sys
from time import gmtime, strftime

def menu():
    print('\nUsage: %s [-options]' % sys.argv[0])
    print('where the options are:')
    print('  -m    Draws the polygon mesh (polyhedron with vertices, edges and faces).')
    print('  -f    Draws the polyhedron without its faces, just vertices and edges.')
    print('  -c    Grants the user keyboard control over the rotation of the polyhedron.')

if __name__ == '__main__':
    print('\nStarting pylyhedron 1.0 at %s' % strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    print('(c) 2016 Lawrence Fernandes')
    option = ' '.join(sys.argv[1:])
    Done = False
    while not Done:
        if option=="-m":
            os.system("python cube.py -m")
            break
        elif option == '-m -c':
            os.system('python cube.py -m -c')
            break
        elif option == '-f':
            os.system('python cube.py -f')
            break
        elif option == '-f -c':
            os.system('python cube.py -f -c')
            break    
        elif option == "Q":
            break
        else:
            print ("\nInvalid option! Please, try again.")
            menu()
            sys.exit(1)
