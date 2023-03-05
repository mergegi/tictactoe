import turtle

MARGIN = 50
BOARD_WIDTH = 600
DIMENSION = 3
CELL_SIZE = BOARD_WIDTH / DIMENSION
DELTA = CELL_SIZE / 8

data = []
for i in range(DIMENSION):
    temp = []
    for j in range(DIMENSION):
        temp.append(0)
    data.append(temp)

cur_player = 'x' #current player

def checkAnyWin(ln):
    if sum(ln) == DIMENSION:
        return 'x'
    elif sum(ln) == -DIMENSION:
        return 'o'
    return ''

#check who is the winner
# returns: 
#  'x' - x win
#  'o' - o win
#  '-' - tie
#  '' unsettled
def checkWin():
    # check all cols
    for i in range(DIMENSION):
        ln = data[i]
        w = checkAnyWin(ln)
        if w != '': 
            return w 

    # check all rows
    for i in range(DIMENSION):
        ln = []
        for j in range(DIMENSION):
            ln.append(data[j][i])

        w = checkAnyWin(ln)
        if w != '':
            return w

    # check diagonal 1
    ln = []
    for i in range(DIMENSION):
        for j in range(DIMENSION):
            if i == j:
                ln.append(data[j][i])
        
    w = checkAnyWin(ln)
    if w != '':
        return w

    # check diagonal 2
    ln = []
    for i in range(DIMENSION):
        for j in range(DIMENSION):
            if i + j == DIMENSION - 1:
                ln.append(data[j][i])

    w = checkAnyWin(ln)
    if w != '':
        return w

    for i in range(DIMENSION):
        for j in range(DIMENSION):
            if data[i][j] == 0:
                return '' #unsettled
                
    return '-'

    return '' # unsettled

def drawXPiece(x, y, color = '#534B62'):
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.color(color)
    t.width(DELTA)

    t.penup()
    t.goto(x - CELL_SIZE / 2 + DELTA, y - CELL_SIZE / 2 + DELTA)
    t.pendown()
    t.goto(x + CELL_SIZE / 2 - DELTA, y + CELL_SIZE / 2 - DELTA)

    t.penup()
    t.goto(x + CELL_SIZE / 2 - DELTA, y - CELL_SIZE / 2 + DELTA)
    t.pendown()
    t.goto(x - CELL_SIZE / 2 + DELTA, y + CELL_SIZE / 2 - DELTA)

def drawOPiece(x, y): 
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.color('#A499B3')
    t.width(DELTA)
    t.penup()
    t.goto(x, y - CELL_SIZE / 2 + DELTA)
    t.pendown()
    t.circle(CELL_SIZE / 2 - DELTA)

def drawOPiece2(x, y):
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.width(DELTA)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color('purple')
    t.dot(CELL_SIZE - DELTA * 2)
    t.color('white')
    t.dot(CELL_SIZE - DELTA * 4)

def drawLine(x1, y1, x2, y2, color = 'purple'):
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.color(color)
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.goto(x2, y2)

def drawBoard():
    turtle.setup(BOARD_WIDTH + MARGIN * 2, BOARD_WIDTH + MARGIN * 2)
    startX = -BOARD_WIDTH / 2
    startY = -BOARD_WIDTH / 2

    # draw horizontal lines
    for i in range(DIMENSION + 1):
        x1 = startX
        y1 = startY + i * BOARD_WIDTH / DIMENSION
        x2 = startX	+ BOARD_WIDTH
        y2 = startY + i *BOARD_WIDTH / DIMENSION
        drawLine(x1, y1, x2, y2)

    # draw vertical lines
    for i in range(DIMENSION + 1):
        x1 = startX + i * BOARD_WIDTH / DIMENSION
        y1 = startY 
        x2 = startX + i * BOARD_WIDTH / DIMENSION
        y2 = startY + BOARD_WIDTH
        drawLine(x1, y1, x2, y2)

def dropXPiece(col, row): 
    x = -BOARD_WIDTH / 2 + col * CELL_SIZE + CELL_SIZE / 2
    y = -BOARD_WIDTH / 2 + row * CELL_SIZE + CELL_SIZE / 2
    drawXPiece(x, y)
    data[col][row] = 1

def dropOPiece(col, row):
    x = -BOARD_WIDTH / 2 + col * CELL_SIZE + CELL_SIZE / 2
    y = -BOARD_WIDTH / 2 + row * CELL_SIZE + CELL_SIZE / 2
    drawOPiece(x, y)
    data[col][row] = -1

def declareWin(w):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(-BOARD_WIDTH / 2, -BOARD_WIDTH / 2 - 50)
    statement = w + ' wins!'
    if w == 'x':
        t.color('#836590')
    elif w == 'o':
        t.color('#65586F')
    else:
        t.color('#38244A')
        statement = 'Tie! :|'
    t.write(w + ' wins! :)', font = ('Times New Roman', 50, 'normal'))

def reset():
    global data
    data = [[0 for i in range(DIMENSION)] for j in range(DIMENSION)]
    turtle.clearscreen()
    drawBoard()
    playGame()

def xy2colrow(x, y):
    startX = -BOARD_WIDTH / 2
    startY = -BOARD_WIDTH / 2
    col = int((x - startX) / CELL_SIZE)
    row = int((y - startY) / CELL_SIZE)
    return col, row

def handleClick(x,y):
    # if click is outside the board, ignore it
    if x < -BOARD_WIDTH / 2 or x > BOARD_WIDTH / 2 or y < -BOARD_WIDTH / 2 or y > BOARD_WIDTH / 2:
        return
    global cur_player

    #convert x, y to col, row
    col, row = xy2colrow(x, y)

    #if piece already exists, ignore it
    if data[col][row] != 0:
        return

    if cur_player == 'x':
        dropXPiece(col,row)
        cur_player = 'o'
    else:
        dropOPiece(col, row)
        cur_player = 'x'

    w = checkWin()
    if w == '': #unsettled
        return
    declareWin(w)
    answer = turtle.textinput('Play again?,', 'Do you want to play again? (y/n)')
    if answer == 'y':
        reset()

def playGame():
    sn = turtle.Screen()
    sn.onclick(handleClick)

drawBoard()
playGame()

turtle.done()