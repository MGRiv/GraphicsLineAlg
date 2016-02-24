from display import *
from draw import *
import math

screen = new_screen()
color = [ 0, 0, 0 ]
color2 = [ 0, 0, 0 ]
color3 = [ 0, 0, 0 ]
color4 = [ 0, 0, 0 ]

angle = 0
diff = math.pi / 7500
cdiff = 255 / 7500.0
temp = 0.0

while(angle <= math.pi):
    draw_line(screen,XRES / 2,0,int((XRES / 2) - ((XRES / 2) * math.cos(angle))),int((YRES / 2) * math.sin(angle)),color)
    draw_line(screen,0,YRES / 2,int((XRES / 2) * math.sin(angle)),int((YRES / 2) + ((YRES / 2) * math.cos(angle))),color2)
    draw_line(screen,XRES / 2,YRES,int((XRES / 2) + ((XRES / 2) * math.cos(angle))),int(YRES - ((YRES / 2) * math.sin(angle))),color3)
    draw_line(screen,XRES,YRES / 2,int(XRES - ((XRES / 2) * math.sin(angle))),int((YRES / 2) - ((YRES / 2) * math.cos(angle))),color4)

    draw_line(screen,XRES / 2,YRES / 2,int(XRES - ((XRES / 2) * math.sin(angle))),int((YRES / 2) - ((YRES / 2) * math.cos(angle))),color4)
    draw_line(screen,XRES / 2,YRES / 2,int((XRES / 2) + ((XRES / 2) * math.cos(angle))),int(YRES - ((YRES / 2) * math.sin(angle))),color3)
    draw_line(screen,XRES / 2,YRES / 2,int((XRES / 2) * math.sin(angle)),int((YRES / 2) + ((YRES / 2) * math.cos(angle))),color2)
    draw_line(screen,XRES / 2,YRES / 2,int((XRES / 2) - ((XRES / 2) * math.cos(angle))),int((YRES / 2) * math.sin(angle)),color)
    angle += diff
    temp += cdiff
    color[RED] = color2[GREEN] = color3[BLUE] = color4[RED] = color4[GREEN] = color4[BLUE] = int(temp)


display(screen)
