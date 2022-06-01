import os
from random import choice, randint

class Item:
    def __init__(self,y: int, x: int, value: int):
        self.y = y
        self.x = x
        self.value = value

def render():
    # fill array
    for y in range(4):
        for x in range(4):
            canvas[y][x] = 0
    for item in items:
        canvas[item.y][item.x] = item

    # print array
    width = 3
    for row in canvas:
        print('|', end='')
        for cell in row:
            if isinstance(cell, Item):
                print(cell.value , ' '*(width-len(str(cell.value))),'|', end='')
            else:
                print(' ' , ' '*(width-len(str(cell))), '|', end='')
        print()

def left():
    global score
    for y in range(4):
        for x in range(4):
            el = canvas[y][x]
            if isinstance(el, Item):
                if not x == 0:
                    if isinstance(canvas[y][x-1], int):
                        el.x -= 1
                        canvas[y][x] = 0
                    elif isinstance(canvas[y][x-1], Item):
                        if canvas[y][x-1].value == el.value:
                            canvas[y][x-1].value += el.value
                            score += 1
                            canvas[y][x] = 0
                            items.remove(el)

def right():
    for y in range(4):
        for x in reversed(range(4)):
            el = canvas[y][x]
            if isinstance(el, Item):
                if not x == 3:
                    if isinstance(canvas[y][x+1], int):
                        el.x += 1
                        canvas[y][x] = 0
                    elif isinstance(canvas[y][x+1], Item):
                        if canvas[y][x+1].value == el.value:
                            canvas[y][x+1].value += el.value
                            canvas[y][x] = 0
                            items.remove(el)

def up():
    for y in range(4):
        for x in range(4):
            el = canvas[y][x]
            if isinstance(el, Item):
                if not y == 0:
                    if isinstance(canvas[y-1][x], int):
                        el.y -= 1
                        canvas[y][x] = 0
                    elif isinstance(canvas[y-1][x], Item):
                        if canvas[y-1][x].value == el.value:
                            canvas[y-1][x].value += el.value
                            canvas[y][x] = 0
                            items.remove(el)

def down():
    for y in reversed(range(4)):
        for x in range(4):
            el = canvas[y][x]
            if isinstance(el, Item):
                if not y == 3:
                    if isinstance(canvas[y+1][x], int):
                        el.y += 1
                        canvas[y][x] = 0
                    elif isinstance(canvas[y+1][x], Item):
                        if canvas[y+1][x].value == el.value:
                            canvas[y+1][x].value += el.value
                            canvas[y][x] = 0
                            items.remove(el)

def fill(dir: str):
    free_pos = []
    if dir == 'left' or dir == 'right':
        if dir == 'left':
            x_coord = 3
        else:
            x_coord = 0
        for y in range(4):
            if isinstance(canvas[y][x_coord], int):
                free_pos.append(y)
        
        if not free_pos == []:
            coord = choice(free_pos)
            new_item = Item(coord, x_coord, 1)
            canvas[coord][x_coord] = new_item
            items.append(new_item)

    elif dir == 'up' or dir == 'down':
        if dir == 'down':
            y_coord = 0
        else:
            y_coord = 3
        for x in range(4):
            if isinstance(canvas[y_coord][x], int):
                free_pos.append(x)
        
        if not free_pos == []:
            coord = choice(free_pos)
            new_item = Item(y_coord, coord, 1)
            canvas[y_coord][coord] = new_item
            items.append(new_item)


if __name__ == '__main__':
    canvas = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
    items = []
    inp = ''
    score = 0
    first = Item(randint(0,3), randint(0,3), 1)
    items.append(first)

    while(inp != 'e' and score < 128): 
        loc_max = 0
        for item in items:
            if item.value > loc_max:
                loc_max = item.value
        score = loc_max
        os.system('cls')
        print()
        print('SCORE: ', score)
        print('_________________________')
        render()
        print('\nup: w down: s left: a right: d')
        inp = str(input('Command: '))

        if inp == 'a':
            left()
            fill('left')
        elif inp == 'd':
            right()
            fill('right')
        elif inp == 'w':
            up()
            fill('up')
        elif inp == 's':
            down()
            fill('down')
        elif inp == 'n': 
            if canvas[0][3] == 0:
                sec = Item(0,3,1)
                items.append(sec)

    print('SUCCES')
