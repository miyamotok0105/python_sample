#!/usr/bin/python

from OpenGL.GL import *
from OpenGL.GLUT import *


vertex = [
    [ 0.0, 0.0, 0.0 ],
    [ 1.0, 0.0, 0.0 ],
    [ 1.0, 1.0, 0.0 ],
    [ 0.0, 1.0, 0.0 ],
    [ 0.0, 0.0, 1.0 ],
    [ 1.0, 0.0, 1.0 ],
    [ 1.0, 1.0, 1.0 ],
    [ 0.0, 1.0, 1.0 ]]

edge = [
    [ 0, 1 ],
    [ 1, 2 ],
    [ 2, 3 ],
    [ 3, 0 ],
    [ 4, 5 ],
    [ 5, 6 ],
    [ 6, 7 ],
    [ 7, 4 ],
    [ 0, 4 ],
    [ 1, 5 ],
    [ 2, 6 ],
    [ 3, 7 ]]


def resize(w, h):
    glViewport(0, 0, w, h)
    glLoadIdentity()
    glOrtho(-2.0, 2.0, -2.0, 2.0, -2.0, 2.0)


def draw():
    glClearColor(0.0, 0.0, 1.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glBegin(GL_LINES)
    for i in range(0, 12):
        glVertex(vertex[edge[i][0]])
        glVertex(vertex[edge[i][1]])
    glEnd()

    glFlush()
    glutSwapBuffers()

glutInit(sys.argv)
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(320, 320)
glutCreateWindow("PyOpenGL 7")
glutDisplayFunc(draw)
glutReshapeFunc(resize)

glutMainLoop()
