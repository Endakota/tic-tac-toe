import canvas as ctx
import time
import random

GAME_STATE = [None, None, None, None, None, None, None, None, None]

def draw_state(GAME_STATE):
    coords = ['58:58', '174:58', '290:58',
              '58:174', '174:174', '290:174', 
              '58:290', '174:290', '290:290']
    ctx.set_color('#808080')
    ctx.line_width(1)
    ctx.stroke_rect(0,0,350,350)
    ctx.stroke_rect(116,0,116,350)
    ctx.stroke_rect(0,116,350,116)

    for z, i in enumerate(coords):
        c = i.find(':')
        s = int(i[:c])
        j = int(i[(c+1):])
        ctx.line_width(4)
        if GAME_STATE[z]!=None:
            if GAME_STATE[z] == 'x':
                ctx.set_color('blue')
                ctx.radius_line(s-30,j+30,45,80)
                ctx.radius_line(s+30,j+30,-45,80)
            if GAME_STATE[z] == 'o':
                ctx.set_color('green')
                ctx.circle(s,j,30)
    
    ctx.draw()
    
def click(x,y):
    x//=116
    y//=116
    i=3*y+x
    
    if GAME_STATE[i] == None:
        GAME_STATE[i] = 'x'
        s = get_bot_move(GAME_STATE)
    
        if s:
            GAME_STATE[s] = "o"
            draw_state(GAME_STATE)
            print(get_winner(GAME_STATE))
        else:
            draw_state(GAME_STATE)
            print(get_winner(GAME_STATE))
            
def get_bot_move(GAME_STATE):
    a,b = [],0
    for i in GAME_STATE:
        if i == None:
            a.append(b)
        b+=1
    if a:
        return(random.choice(a))
a = [None,None]

def generate_coords():
    x = random.randint(0,350)
    y = random.randint(0,350)
    a[0] = x
    a[1] = y
    return a

def get_winner(arr):
    draw = True
    final_state = ''
    for i in range(3):
    #checking the row [0 1 2] [3 4 5] [6 7 8]
        if (arr[3*i] == arr[3*i+1] == arr[3*i+2]):
            if arr[3*i] == 'x':
                final_state = 'x_win'
                draw = False
            elif arr[3*i] == 'o':
                final_state = 'o_win'
                draw = False
            else:
                final_state = None
        #we need [0 3 6] [1 4 7] [2 5 8]
        #checking the columns [0 3 6] [1 4 7] [2 5 8]
        elif (arr[i] == arr[i+3] == arr[i+6]):
            if arr[i] == 'x':
                final_state = 'x_win'
                draw = False
            elif arr[i] == 'o':
                final_state = 'o_win'
                draw = False
            else:
                final_state = None
    # we need [0 4 8] [2 4 6]
    if arr[0] == arr[4] == arr[8]:
        if arr[0] == 'x':
            final_state = 'x_win'
            draw = False
        elif arr[0] == 'o':
            final_state = 'o_win'
            draw = False
        else:
            final_state = None
    if arr[2] == arr[4] == arr[6]:
        if arr[2] == 'x':
            final_state = 'x_win'
            draw = False
        elif arr[2] == 'o':
            final_state = 'o_win'
            draw = False
        else:
            final_state = None
    if None not in arr and draw == True:
        final_state = 'draw'
    return final_state
ctx.set_onclick(click)
draw_state(GAME_STATE)
ctx.listen()
