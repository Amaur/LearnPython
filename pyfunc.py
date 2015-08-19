import sys, os
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import *

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-5.0, 5.0, -5.0, 5.0)

def plotfunc():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 0.0)
    glPointSize(3.0)
    glLineWidth(2.0)
    glBegin(GL_LINES)
    glVertex2f(-5.0,0.0)
    glVertex2f(5.0,0.0)
    glVertex2f(0.0,-5.0)
    glVertex2f(0.0,5.0)
    glEnd()
    glBegin(GL_POINTS)

    for x in arange(-5.0, 5.0, 0.1):
        y=x*x+1
        glVertex2f(x,y)
        glColor3f(1.0, 0.0, 0.0)
    glEnd()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowPosition(50,50)
    glutInitWindowSize(400,400)
    glutCreateWindow("func plotter")

    glutDisplayFunc(plotfunc)

    init()
    glutMainLoop()

main()