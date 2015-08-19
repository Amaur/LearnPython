import sys, os
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def init():
    glClearColor(0.0,0.0,0.0,1.0)
    gluOrtho2D(-1.0,1.0,-1.0,1.0)

def plotpoints():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)
    #glPointSize(5.0)
    glLineWidth(3.0)
    #glBegin(GL_POINTS)
    glBegin(GL_LINES)

    glVertex2f(0.0,0.0)
    glVertex2f(0.3,0.5)
    glEnd()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(100,100)
    glutCreateWindow("Plot point")
    glutDisplayFunc(plotpoints)
    init()

    glutMainLoop()

main()