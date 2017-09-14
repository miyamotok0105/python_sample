#!/usr/bin/python

from OpenGL.GL import *
from OpenGL.GLUT import *


def resize(w, h):
    glViewport(30, 50, w/2, h/2)

def draw():
    glClearColor(0.0, 1.0, 0.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glBegin(GL_TRIANGLES)
    glVertex(-1, -1)
    glVertex(1, -1)
    glVertex(0, 1)
    glEnd()

    glBegin(GL_LINES)
    glVertex(-1, -1)
    glVertex(1, -1)
    glVertex(1, -1)
    glVertex(1, 1)
    glVertex(1, 1)
    glVertex(-1, 1)
    glVertex(-1, 1)
    glVertex(-1, -1)
    glEnd()

    glFlush()
    glutSwapBuffers()


glutInit(sys.argv)
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(320, 240)
glutCreateWindow("PyOpenGL 3")
glutReshapeFunc(resize)
glutDisplayFunc(draw)

glutMainLoop()
