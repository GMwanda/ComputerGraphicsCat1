import math

import cairo

# set surface
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()
OUTPUT_DIR = 'png_output/'

def drawRedRectangle():
    # draw the image
    ctx.rectangle(150, 100, 100, 240)
    ctx.set_source_rgb(1, 0, 0)
    ctx.fill()
    surface.write_to_png(OUTPUT_DIR+"RedRectangle.png")
def drawDifferentShapes():
    ctx.rectangle(100, 90, 20, 20)
    ctx.set_source_rgb(0, 1, 0)
    ctx.stroke()
    ctx.rectangle(300, 100, 100, 240)
    ctx.set_source_rgb(0, 0, 1)
    ctx.fill_preserve()
    surface.write_to_png(OUTPUT_DIR+"differentShapes.png")
def drawRomanTwo():
    ctx.rectangle(100, 90, 20, 240)
    ctx.set_source_rgb(0, 0, 0)
    ctx.fill()
    ctx.rectangle(130, 90, 20, 240)
    ctx.set_source_rgb(0, 0, 0)
    ctx.fill()
    ctx.rectangle(75, 60, 100, 20)
    ctx.set_source_rgb(0, 0, 0)
    ctx.fill()
    ctx.rectangle(75, 340, 100, 20)
    ctx.set_source_rgb(0, 0, 0)
    ctx.fill()
    surface.write_to_png(OUTPUT_DIR+"RomanTwo.png")
def juventusLogo():
    ctx.rectangle(100, 90, 20, 180)
    ctx.set_source_rgb(0, 0, 0)
    ctx.fill()
    ctx.arc(60, 270, 50, 0, 1.2)
    ctx.set_source_rgb(0,0,0)
    ctx.set_line_width(20)
    ctx.stroke()


    ctx.rectangle(150, 90, 20, 180)
    ctx.set_source_rgb(0, 0, 0)
    ctx.fill()
    ctx.arc(80, 270, 80, 0, 1.4)
    ctx.set_source_rgb(0, 0, 0)
    ctx.set_line_width(20)
    ctx.stroke()


    ctx.rectangle(50,90, 60, 20)
    ctx.set_source_rgb(0,0,0)
    ctx.fill()
    surface.write_to_png(OUTPUT_DIR+"JuventusLogo.png")
def drawALine():
    ctx.move_to(100, 100) # starting point of linne
    ctx.line_to(500, 300) # endinng point of linne
    ctx.set_source_rgb(0, 0, 0)
    ctx.set_line_width(10)
    ctx.stroke()
    surface.write_to_png(OUTPUT_DIR+"Line.png")
def drawParallelogram():
    ctx.move_to(150, 150)
    ctx.line_to(20, 300)
    ctx.line_to(500, 300)
    ctx.line_to(370, 150)
    ctx.line_to(147, 150)
    ctx.set_source_rgb(0, 0, 0)
    ctx.set_line_width(10)
    ctx.stroke()
    surface.write_to_png(OUTPUT_DIR+"Parallelogram.png")
def openPolygons():
    ctx.move_to(50, 200)
    ctx.line_to(100, 200)
    ctx.line_to(150, 250)
    ctx.line_to(250, 150)
    ctx.line_to(350, 250)
    ctx.line_to(450, 150)
    ctx.line_to(500, 200)
    ctx.line_to(550, 200)
    ctx.set_source_rgb(1, 0, 0)
    ctx.set_line_width(10)
    ctx.stroke()
    surface.write_to_png(OUTPUT_DIR+"OpenPolygon.png")
def drawArc():
    ctx.arc(300, 200, 50, 0 , 6.28)
    ctx.set_source_rgb(0, 0, 0)
    ctx.set_line_width(10)
    ctx.stroke()
    surface.write_to_png(OUTPUT_DIR+"Arc.png")
def bezierCurve():
    ctx.move_to(100, 200)
    ctx.curve_to(200, 100, 400, 300, 500, 200)
    ctx.set_source_rgb(0,0,0)
    ctx.set_line_width(10)
    ctx.stroke()
    surface.write_to_png(OUTPUT_DIR+"BezierCurve.png")
def lineCaps():
    ctx.set_source_rgb(0,0,0)
    ctx.set_line_width(20)
    # Butt cap
    ctx.move_to(100, 80)
    ctx.line_to(500, 80)
    ctx.set_line_cap(cairo.LINE_CAP_BUTT)
    ctx.stroke()
    # Square cap
    ctx.move_to(100, 200)
    ctx.line_to(500, 200)
    ctx.set_line_cap(cairo.LINE_CAP_SQUARE)
    ctx.stroke()
    # Round cap
    ctx.move_to(100, 320)
    ctx.line_to(500, 320)
    ctx.set_line_cap(cairo.LINE_CAP_ROUND)
    ctx.stroke()
    surface.write_to_png(OUTPUT_DIR+"LineCaps.png")
def lineJoins():
    ctx.set_line_width(20)
    ctx.set_source_rgb(0, 0, 0)
    # Miter join
    ctx.move_to(50, 100)
    ctx.line_to(100, 300)
    ctx.line_to(50, 300)
    ctx.set_line_join(cairo.LINE_JOIN_MITER)
    ctx.stroke()
    # Round Join
    ctx.move_to(240, 100)
    ctx.line_to(370, 300)
    ctx.line_to(240, 300)
    ctx.set_line_join(cairo.LINE_JOIN_ROUND)
    ctx.stroke()
    # Bevel join
    ctx.move_to(430, 100)
    ctx.line_to(560, 300)
    ctx.line_to(430, 300)
    ctx.set_line_join(cairo.LINE_JOIN_BEVEL)
    ctx.stroke()

    surface.write_to_png(OUTPUT_DIR+"lineJoins.png")
def dashedLines():
    ctx.set_source_rgb(0, 0, 0)
    ctx.set_line_width(5)

    ctx.move_to(100, 50)
    ctx.line_to(500,50)
    ctx.set_dash([20])
    ctx.stroke()

    ctx.move_to(100, 100)
    ctx.line_to(500, 100)
    ctx.set_dash([20, 10])
    ctx.stroke()

    ctx.move_to(100, 150)
    ctx.line_to(500, 150)
    ctx.set_dash([20, 5, 5, 5])
    ctx.stroke()

    ctx.move_to(100, 200)
    ctx.line_to(500, 200)
    ctx.set_dash([5,5,10])
    ctx.stroke()

    ctx.set_line_width(20)
    ctx.set_line_cap(cairo.LINE_CAP_ROUND)

    ctx.move_to(100, 250)
    ctx.line_to(500, 250)
    ctx.set_dash([10, 20])
    ctx.stroke()

    ctx.move_to(100, 300)
    ctx.line_to(500, 300)
    ctx.set_dash([0, 20])
    ctx.stroke()

    surface.write_to_png(OUTPUT_DIR+"dashedLines.png")

drawRomanTwo()