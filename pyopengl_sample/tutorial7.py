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

angle = 0.0
x_tmp = 0.0
y_tmp = 1.0
z_tmp = 0.0

def resize(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(30.0, w/h, 1.0, 100.0)
    glMatrixMode(GL_MODELVIEW)


def draw():
    global angle,x_tmp,y_tmp,z_tmp

    glClearColor(0.0, 0.0, 1.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()
    gluLookAt(3.0, 4.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    glRotated(angle, x_tmp, y_tmp, z_tmp)
    glBegin(GL_LINES)
    for i in range(0, 12):
        glVertex(vertex[edge[i][0]])
        glVertex(vertex[edge[i][1]])
    glEnd()

    glFlush()
    glutSwapBuffers()


def keyboard(key, x, y):
    global angle,x_tmp,y_tmp,z_tmp

    if key=='q':
        sys.exit()
    if key=='h':
        angle += 1.0
        glutPostRedisplay()
    if key=='x':
        x_tmp += 3.0
        glutPostRedisplay()
    if key=='y':
        y_tmp += 3.0
        glutPostRedisplay()
    if key=='z':
        z_tmp += 3.0
        glutPostRedisplay()

glutInit(sys.argv)
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(320, 320)
glutCreateWindow("PyOpenGL 8")
glutDisplayFunc(draw)
glutReshapeFunc(resize)
glutKeyboardFunc(keyboard)

glutMainLoop()
