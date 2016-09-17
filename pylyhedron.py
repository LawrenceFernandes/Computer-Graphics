#!/usr/bin/python
# -*- coding: utf-8 -*-
# File Name: tui.py
#
# Author: Lawrence Fernandes
# Copyright (C) 2016 Lawrence Fernandes
#
""" This module is the terminal user interface (TUI) of the app.
    It calls the other modules to draw the polyhedron requested by the user.
    The other modules must be located on the same directory.
"""
# Import Python modules
import os, sys
from time import gmtime, strftime

def menu():
    """ This function creates an options menu."""
    print('\nUsage: %s [-option] [-option]' % sys.argv[0])
    print('where the options must be separeted by a space and are the following:')
    print('  -m    Draws the polygon mesh (polyhedron with vertices, edges and faces).')
    print('  -f    Draws the polyhedron without its faces, just vertices and edges.')
    print('  -c    Grants the user keyboard control over the rotation of the polyhedron.')

def main():
    """ This is the main function of the module."""
    print('\nStarting pylyhedron 1.0 at %s' % strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    print('(c) 2016 Lawrence Fernandes')
    option = ' '.join(sys.argv[1:])
    Done = False
    while not Done:
        if option=="-c":
            print ("\nInvalid usage! Needs to specify the type of drawing.")
            menu()
            break
        elif option not in {'-m','-f','-f -c','-m -c','-c -f','-c -m'}:
            print ("\nInvalid option! Please, try again.")
            menu()
            break
        else:
            os.system("python cube.py " + option)
            break

# Standard boilerplate to call the main function to begin the program.
if __name__ == '__main__':
    main()
