#!/usr/bin/python

from OpenGL.GL import *
from OpenGL.GLU import *
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

face = [
    [ 0, 1, 2, 3 ],
    [ 1, 5, 6, 2 ],
    [ 5, 4, 7, 6 ],
    [ 4, 0, 3, 7 ],
    [ 4, 5, 1, 0 ],
    [ 3, 2, 6, 7 ]]

normal = [
    [ 0.0, 0.0,-1.0 ],
    [ 1.0, 0.0, 0.0 ],
    [ 0.0, 0.0, 1.0 ],
    [-1.0, 0.0, 0.0 ],
    [ 0.0,-1.0, 0.0 ],
    [ 0.0, 1.0, 0.0 ]]

light0p = [ 0.0, 3.0, 5.0, 1.0 ]
light1p = [ 5.0, 3.0, 0.0, 1.0 ]
redColor = [ 1.0, 0.0, 0.0, 1.0 ]
greenColor = [ 0.0, 1.0, 0.0, 1.0 ]

angleX = 0.0
angleY = 0.0


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

    glLightfv(GL_LIGHT0, GL_POSITION, light0p)
    glLightfv(GL_LIGHT1, GL_POSITION, light1p)

    glRotated(angleX, 1.0, 0.0, 0.0)
    glRotated(angleY, 0.0, 1.0, 0.0)

    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, greenColor)

    glBegin(GL_QUADS)
    for j in range(0, 6):
        glNormal3dv(normal[j])
        for i in range(0, 4):
            glVertex(vertex[face[j][i]])
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
glutCreateWindow("PyOpenGL 12")

glutDisplayFunc(draw)
glutReshapeFunc(resize)
glutKeyboardFunc(keyboard)

glClearColor(0.0, 0.0, 1.0, 0.0)
glEnable(GL_DEPTH_TEST)
glEnable(GL_CULL_FACE)
glCullFace(GL_FRONT)

glEnable(GL_LIGHTING)
glEnable(GL_LIGHT0)
glEnable(GL_LIGHT1)
glLightfv(GL_LIGHT1, GL_DIFFUSE, redColor)
glLightfv(GL_LIGHT1, GL_SPECULAR, redColor)


glutMainLoop()
