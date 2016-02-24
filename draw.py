from display import *

def draw_line( screen, x0, y0, x1, y1, color ):
    if(x0 > x1):
        draw_line(screen,x1,y1,x0,y0,color)
    else:
        a = y1 - y0
        b = x0 - x1
        if(a > 0):
            if(a > (b*-1)):
                #2nd
                d = a + 2*b
                a *= 2
                b *= 2
                while(y0 <= y1):
                    plot(screen,color,x0,y0)
                    if(d < 0):
                        x0 += 1
                        d += a
                    y0 += 1
                    d += b
            else:
                #1st
                d = b + 2*a
                a *= 2
                b *= 2
                while(x0 <= x1):
                    plot(screen,color,x0,y0)
                    if(d > 0):
                        y0 += 1
                        d += b
                    x0 += 1
                    d += a
        else:
            if((a*-1) > (b*-1)):
                #7th
                d = a - 2*b
                a *= 2
                b *= 2
                while(y0 >= y1):
                    plot(screen,color,x0,y0)
                    if(d > 0):
                        x0 += 1
                        d += a
                    y0 -= 1
                    d -= b
            else:
                #8th
                d = 2*a - b
                a *= 2
                b *= 2
                while(x0 <= x1):
                    plot(screen,color,x0,y0)
                    if(d < 0):
                        y0 -= 1
                        d -= b
                    x0 += 1
                    d += a
