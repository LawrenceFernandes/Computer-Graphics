#!/usr/bin/python
# -*- coding: utf-8 -*-

# File Name: tui.py
# Author: Lawrence Fernandes
# Copyright (C) 2016 Lawrence Fernandes

""" This module is the terminal user interface (TUI) of the app.
    It calls the other modules to draw the polygon requested by the user.
    The other modules must be located on the same directory.
"""
# Import Python modules
import os, sys
from time import gmtime, strftime

def menu():
    print('\nUsage: %s [-options]' % sys.argv[0])
    print('where the options are:')
    print('  -m    Draws the Polygon mesh (polyhedron with vertices, edges and faces).')
    print('  -f    Draws the Polyhedron without its faces.')

if __name__ == '__main__':
    print('\nStarting Interactive Geometry 1.0 at %s' % strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    print('(c) 2016 Lawrence Fernandes')
    option = ' '.join(sys.argv[1:])
    Done = False
    while not Done:
        if option=="-m":
            os.system("python cube_wfaces.py")
            break
            #print("Cube with face")
        elif option == '-f':
            os.system('python cube_faceless.py')
            break
            #print("Faceless cube")
        elif option == "Q":
            break
        else:
            print ("\nInvalid option! Please, try again.")
            menu()
            sys.exit(1)