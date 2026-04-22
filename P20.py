# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 10:02:22 2026

"""
# Lisa Kraatz

from turtle import *

def main():
    shape('arrow')
    speed(4)
    bgcolor('#ffd4e7')
    # Big Circle
    penup()
    pensize(4)
    setposition(0,-280)
    pencolor('#ded4ff')
    fillcolor('#efebff')
    begin_fill()
    pendown()
    speed(4)
    circle(300)
    end_fill()
    # Left Small Circle
    penup()
    setposition(-100,50)
    pencolor('#d4fff9')
    fillcolor('#ebfffc')
    begin_fill()
    pendown()
    circle(70)
    end_fill()
    # Left Small Circle
    penup()
    setposition(100,50)
    pencolor('#d4fff9')
    fillcolor('#ebfffc')
    begin_fill()
    pendown()
    circle(70)
    end_fill()
    # Line
    penup()
    setposition(-120,-80)
    pencolor('#fffed6')
    fillcolor('#ffffeb')
    begin_fill()
    pendown()
    forward(250)
    left(90)
    forward(30)
    left(90)
    forward(250)
    left(90)
    forward(30)
    end_fill()
    # Triangle
    penup()
    pencolor('#d6ffda')
    fillcolor('#ebffed')
    goto(-120,-110)
    begin_fill()
    pendown()
    goto(130,-110)
    goto(5,-200)  
    goto(-120,-110)
    end_fill()
    
    
    
    
    
    
main()