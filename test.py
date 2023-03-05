import turtle

# start: shape start position
# sideLen: the length of the side of the shape
# sideCount: how many sides for the shape
def drawRegularShape(start, sideLen, sideCount, color = 'purple'):
  t = turtle.Turtle()
  t.speed(8)
  t.color(color)
  t.penup()
  t.goto(start)
  t.pendown()
  turnAngle = 180 - (sideCount - 2) * 180 / sideCount
  for i in range(sideCount):
    t.forward(sideLen)
    t.right(turnAngle)

def drawRegularTriangle(start, sideLen):
  drawRegularShape(start, sideLen, 3)
  return 3
  
def drawSquare(start, sideLen):
  drawRegularShape(start, sideLen, 4)
  return 4
 
ret = drawSquare((0, 0), 100)
print(ret)
drawRegularTriangle((-100, 100), 100)
#drawRegularTriangle((0, 0), 120)

turtle.done()