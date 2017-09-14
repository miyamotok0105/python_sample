#!/usr/bin/python

import struct
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


vertex = [
    [ -1.0, 0.0, 1.0 ],
    [ 1.0, 0.0, 1.0 ],
    [ 1.0, 0.0, -1.0 ],
    [ -1.0, 0.0, -1.0 ]]

face = [
    [ 0, 1, 2, 3 ]]

uvcoord = [
    [0.0, 0.0],
    [1.0, 0.0],
    [1.0, 1.0],
    [0.0, 1.0]]

angleX = 0.0
angleY = 0.0

def maketex():
    w = 32
    h = 32
    n = 2
    data = ''
    for x in range(w):
        for y in range(h):
            xx = x % (w/n) < w/(n*2)
            yy = y % (h/n) < h/(n*2)
            if xx ^ yy:
                data += struct.pack('BBB', 255, 0, 0)
            else:
                data += struct.pack('BBB', 0, 255, 0)
    tex = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, tex)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, w, h, 0, GL_RGB, GL_UNSIGNED_BYTE, data)


def resize(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(30.0, w/h, 1.0, 100.0)
    glMatrixMode(GL_MODELVIEW)


def draw():
    global angleX, angleY

    glClearColor(0.0, 0.0, 1.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()
    gluLookAt(3.0, 4.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    glRotated(angleX, 1.0, 0.0, 0.0);
    glRotated(angleY, 0.0, 1.0, 0.0);

    glEnable(GL_TEXTURE_2D)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    glBegin(GL_QUADS)
    for j in range(len(face)):
        for i in range(4):
            n = face[j][i]
            glTexCoord2f(uvcoord[n][0], uvcoord[n][1])
            glVertex(vertex[n])
    glEnd()

    glFlush()
    glutSwapBuffers()


def keyboard(key, x, y):
    global angleX, angleY
    if key=='q':
        sys.exit()
    elif key=='h':
        angleY += 1.0
        glutPostRedisplay()
    elif key=='j':
        angleX += 1.0
        glutPostRedisplay()

glutInit(sys.argv)
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(320, 320)
glutCreateWindow("PyOpenGL 15")
glutDisplayFunc(draw)
glutReshapeFunc(resize)
glutKeyboardFunc(keyboard)

glClearColor(0.0, 0.0, 1.0, 0.0)
glEnable(GL_DEPTH_TEST)
glEnable(GL_CULL_FACE)
glCullFace(GL_BACK)

maketex()

glutMainLoop()
