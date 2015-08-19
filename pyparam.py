import sys, os
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import *

def init():
    glClearColor(1.0,1.0,1.0,1.0)
    gluOrtho2D(-2.0,2.0,-2.0,2.0)

def plotparam():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,0.0,0.0)
    glPointSize(3.0)

    glBegin(GL_LINES)
    glVertex2f(-2.0,0.0)
    glVertex2f(2.0,0.0)
    glVertex2f(0.0,-2.0)
    glVertex2f(0.0,2.0)

    glEnd()

    glBegin(GL_POINTS)

    for t in arange(0.0,6.28,0.001):
        x=sin(t)
        y=cos(t)
        glVertex2f(x,y)
        glColor3f(1.0,0.0,0.0)
    glEnd()

    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowPosition(50,50)
    glutInitWindowSize(500,500)
    glutCreateWindow("Cicle")
    glutDisplayFunc(plotparam)
    init()
    glutMainLoop()

main()