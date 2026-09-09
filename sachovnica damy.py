import PIL
from PIL import Image, ImageDraw
chessboard = []
counter = 0

def create_Image():
    img = Image.new("RGB", (1600, 1600), "black")
    draw = ImageDraw.ImageDraw(img) 
    for x in range(0, 1601, 200):
        for y in range(0, 1601, 200):
            if (x+y) % 400 == 0:
                draw.rectangle([x, y, x+200, y+200], fill="white")
    img.save(f"riesenie{counter}.png")
    
def create_chessboard():
    global chessboard  
    #chessboard = [row] * 8 - toto nerob
    for i in range(8):
        row = [0] * 8
        chessboard.append(row)

def checkit(x, y):
    for i in range (0,8):  
        if chessboard[y][i] == 1:
            return False
        if chessboard[i][x] == 1:
            return False
    for i in range(0,8):
        for j in range(0,8):
            if j + i == x + y:
                if chessboard[i][j] == 1:
                    return False
            if j - i == x - y:
                if chessboard[i][j] == 1:
                    return False
    return True

def create_queens(n):
    global chessboard
    global counter
    if n == 8:
        counter += 1
        create_Image()
        print (chessboard)
        print ("-----------------------------------------------------------------------")
    else:
        for i in range (0,8):
            if checkit(i,n):
                chessboard[n][i] = 1
                create_queens(n+1)
                chessboard[n][i] = 0

create_chessboard()
create_queens(0)
print (f"Pocet rieseni: {counter}")