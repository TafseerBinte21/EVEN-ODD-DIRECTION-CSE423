
import pygame
import sys
from math import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import time


def DrawLine(x1, y1, x2, y2, zone):
    dx = x2 - x1
    dy = y2 - y1
    d = 2 * dy - dx
    incE = 2 * dy
    incNE = 2 * (dy - dx)
    y = y1

    for x in range(x1, x2 + 1):
        if d > 0:
            d = d + incNE
            y = y + 1

        else:
            d = d + incE

        if zone == 0:
            glBegin(GL_POINTS)
            glPointSize(3)
            glVertex2f(x, y)
            glEnd()

        else:
            (x_new, y_new) = ConvertFromZoneZero(x, y, zone)
            glPointSize(3)
            glBegin(GL_POINTS)
            glVertex2f(x_new, y_new)
            glEnd()


def FindZone(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    if abs(dx) > abs(dy):
        if dx > 0 and dy > 0:
            zone = 0

        elif dx <= 0 and dy >= 0:
            zone = 3

        elif dx <= 0 and dy <= 0:
            zone = 4

        elif dx >= 0 and dy <= 0:
            zone = 7

    else:
        if dx >= 0 and dy >= 0:
            zone = 1

        elif dx <= 0 and dy >= 0:
            zone = 2

        elif dx <= 0 and dy <= 0:
            zone = 5

        elif dx >= 0 and dy <= 0:
            zone = 6
    return zone


def ConvertToZoneZero(x1, y1, x2, y2, zone):
    if zone == 0:
        w = x1
        x = y1
        y = x2
        z = y2

    elif zone == 1:
        w = y1
        x = x1
        y = y2
        z = x2

    elif zone == 2:
        w = y1
        x = -x1
        y = y2
        z = -x2

    elif zone == 3:
        w = -x1
        x = y1
        y = -x2
        z = y2

    elif zone == 4:
        w = -x1
        x = -y1
        y = -x2
        z = -y2
    elif zone == 5:
        w = -y1
        x = -x1
        y = -y2
        z = -x2

    elif zone == 6:
        w = -y1
        x = x1
        y = -y2
        z = x2

    elif zone == 7:
        w = x1
        x = -y1
        y = x2
        z = -y2
    # return w
    # return x
    # return y
    # return z
    return w, x, y, z


def Mid_Point(x1, y1, x2, y2):
    zone = FindZone(x1, y1, x2, y2)

    if zone == 0:
        DrawLine(x1, y1, x2, y2, zone)

    else:
        w, x, y, z = ConvertToZoneZero(x1, y1, x2, y2, zone)
        DrawLine(w, x, y, z, zone)


def ConvertFromZoneZero(x1, y1, zone):
    if zone == 0:
        w = x1
        x = y1

    elif zone == 1:
        w = y1
        x = x1

    elif zone == 2:
        w = -y1
        x = x1

    elif zone == 3:
        w = -x1
        x = y1

    elif zone == 4:
        w = -x1
        x = -y1

    elif zone == 5:
        w = -y1
        x = -x1

    elif zone == 6:
        w = -y1
        x = x1

    elif zone == 7:
        w = x1
        x = -y1

    return w, x


def init():
    glViewport(0, 0, 480, 480)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 480, 0.0, 480, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glColor3f(0.2, 0.6, 1)


def watchScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    init()

    Mid_Point(240, 175, 240, 327)

    Mid_Point(260, 325, 360, 325)
    Mid_Point(260, 250, 360, 250)
    Mid_Point(260, 175, 360, 175)
    Mid_Point(260, 250, 260, 325)
    Mid_Point(360, 175, 360, 250)

    # glutSwapBuffers()


def drawPoints(x, y):
    glPointSize(2.0)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def midPointCircle(X, Y, r):
    x = 0
    y = r
    d = 1 - r

    while x <= y:
        x += 1
        if d > 0:
            y = y - 1
            d = d + 2 * (x - y) + 5
        else:
            d = d + 2 * x + 3

        drawPoints(X + x, Y + y)
        drawPoints(X + y, Y + x)
        drawPoints(X + y, Y - x)
        drawPoints(X - x, Y + y)
        drawPoints(X - x, Y - y)
        drawPoints(X - y, Y - x)
        drawPoints(X - y, Y + x)
        drawPoints(X + x, Y - y)


def drawCircles(X, Y, r):
    midPointCircle(X, Y, r)
    midPointCircle(X + (r / 2), Y, r / 2)
    midPointCircle(X - (r / 2), Y, r / 2)
    midPointCircle(X, Y + (r / 2), r / 2)
    midPointCircle(X, Y - (r / 2), r / 2)
    midPointCircle(X + r / 2 * (math.sqrt(2) / 2), Y + r / 2 * (math.sqrt(2) / 2), r / 2)
    midPointCircle(X - r / 2 * (math.sqrt(2) / 2), Y + r / 2 * (math.sqrt(2) / 2), r / 2)
    midPointCircle(X - r / 2 * (math.sqrt(2) / 2), Y - r / 2 * (math.sqrt(2) / 2), r / 2)
    midPointCircle(X + r / 2 * (math.sqrt(2) / 2), Y - r / 2 * (math.sqrt(2) / 2), r / 2)


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()

    glClearColor(0,0.8,0.7,0)
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(5, 150, 00)


    # Even digit

    Mid_Point(240, 175+300, 240, 200+300)
    Mid_Point(240, 199+300, 255, 199+300)
    Mid_Point(240, 175+300, 255, 175+300)
    Mid_Point(240, 186+300, 255, 186+300)

    #circle
    drawCircles(100, 200, 50)
    drawCircles(200,115,50)
    drawCircles(300,115,50)
    drawCircles(400,200,50)
    drawCircles(100, 300, 50)
    drawCircles(200, 375, 50)
    drawCircles(300, 375, 50)
    drawCircles(400, 300, 50)

    drawCircles(250, 250, 50)
    midPointCircle(250, 250, 150)


    glutSwapBuffers()

def showScreen2():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glClearColor(0, 0.8, 0.7, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(250, 250, 2500)

    # odd digit

    Mid_Point(240, 175 + 300, 240, 200 + 300)
    Mid_Point(240, 199 + 300, 255, 199 + 300)
    Mid_Point(240, 175 + 300, 255, 175 + 300)
    Mid_Point(255, 175 + 300, 255, 200 + 300)


    # circle

    drawCircles(150, 150, 50)
    drawCircles(250, 100, 50)
    drawCircles(350, 150, 50)

    drawCircles(100, 250, 50)
    drawCircles(400, 250, 50)

    drawCircles(150, 350, 50)
    drawCircles(250, 400, 50)
    drawCircles(350, 350, 50)
    drawCircles(250, 250, 50)
    midPointCircle(250, 250, 150)
    glutSwapBuffers()


num=int(input("Enter a number: "))
if num%2==0:
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(550, 550)
    glutInitWindowPosition(0, 0)
    wind = glutCreateWindow(b"THE NUMBER IS EVEN")
    glutDisplayFunc(showScreen)
    glutMainLoop()
else:
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(550, 550)
    glutInitWindowPosition(0, 0)
    wind = glutCreateWindow(b"THE NUMBER IS ODD")
    glutDisplayFunc(showScreen2)
    glutMainLoop()




















