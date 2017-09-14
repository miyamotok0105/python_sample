#!/usr/bin/python

from OpenGL.GL import *
from OpenGL.GLUT import *


def draw():
    glClearColor(0.0, 0.5, 0.5, 0.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glBegin(GL_TRIANGLES)
    glVertex(-1, -1)
    glVertex(1, -1)
    glVertex(0, 1)
    glEnd()

    glFlush()
    glutSwapBuffers()


def resize(w, h):
    glViewport(0, 0, w, h)


def mouse(button, state, x, y):
    if button == GLUT_LEFT_BUTTON:
        print "left button",
    elif button == GLUT_MIDDLE_BUTTON:
        print "middle button",
    elif button == GLUT_RIGHT_BUTTON:
        print "right button",
    else:
        print "unknown button:", button,

    if state == GLUT_DOWN:
        print "down mouse button",
    elif state == GLUT_UP:
        print "up mouse button",
    else:
        print "unknown state:", state,

    print(x, y)


def motion(x, y):
    print "drag:", x, y


glutInit(sys.argv)
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(320, 240)
glutCreateWindow("PyOpenGL 4")
glutReshapeFunc(resize)
glutDisplayFunc(draw)
glutMouseFunc(mouse)
glutMotionFunc(motion)

glutMainLoop()
