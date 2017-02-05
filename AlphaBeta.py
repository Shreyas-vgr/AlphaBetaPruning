import copy
map = { 1: 'a',
        2 :'b',
        3 :'c',
        4 :'d',
        5 :'e',
        6 :'f',
        7 :'g',
        8 :'h',
        float('inf')  : "Infinity",
        float('-inf') : "-Infinity"
        }

logs = []
flag = 1

def Evaluate(state,current,opponent):
    c_eval = 0
    o_eval = 0
    for i,row in enumerate(state):
        for j,col in enumerate(row):
            if col == current:
                c_eval += eval[i][j]
            elif col == opponent:
                o_eval += eval[i][j]
    return (c_eval - o_eval)

def onBoard(i,j):
    return i >= 0 and i <=7 and j >=0 and j<=7


def Valid(state, startx, starty):
    if not onBoard(startx,starty) and state[startx][starty] != '*':
        return False
    temp = state[startx][starty]
    state[startx][starty] = current
    flips = []
    for X,Y in [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]:
        i = startx
        j = starty
        i += X
        j += Y
        if onBoard(i,j) and state[i][j] == opponent:
            i += X
            j += Y
            if not onBoard(i,j):
                continue
            while state[i][j] == opponent and not onBoard(i,j):
                i += X
                j += Y
            if not onBoard(i,j):
                continue
            if state[i][j] == current:
                while True:
                    i -= X
                    j -= Y
                    if i == startx and j == starty:
                        break
                    flips.append([i,j])

    state[startx][starty] = temp
    if len(flips) == 0:
        return False
    return flips

def ValidMoves(state):
    valid_moves = []
    for i in xrange(8):
        for j in xrange(8):
            if Valid(state,i,j):
                valid_moves.append([i,j])
    return valid_moves

def check(state,character):
    count = 0
    for i in xrange(8):
        for j in xrange(8):
            if state[i][j] == character:
                count = count +1
    if count == 0:
         return True
    return False

def Terminal(state,depth):
    if depth == d:
        return True
    return False


def display(param,d,val,a,b):
    if a == float('inf') or a == float('-inf'):
        a = map[a]
    if b == float('inf') or b == float('-inf'):
        b = map[b]
    if val == float('inf') or val == float('-inf'):
        val = map[val]
    if param == "root" or d == 0:
        first = "root"
    elif param == "pass":
        first = "pass"
    else:
        first = param
    print first, d, val, a, b
    logs.append("%s,%d,%s,%s,%s\n" % (first,d,str(val),str(a),str(b)))


#print ValidMoves(state)
def AlphaBeta(state):
    val = Max(state, float('-inf'), float('inf'), 0 , "root")

def Max(state, a , b , depth , param):
    global pass_val,flag
    val = float('-inf')

    if Terminal(state,depth):
        val = Evaluate(state,'X','O')
        display(param, depth, val, a, b)
        return val
    if pass_val != 2:
        display(param, depth, val, a, b)

    actions = ValidMoves(state)
    if not actions:
        if pass_val < 2:
            pass_val = pass_val + 1
            if depth == 0 and flag:
                for l in state:
                    output.write("".join(l)+"\n")
                flag = 0
            val = max(val,Min(state, a , b, depth +1,"pass"))
            if val >= b:
                display(param, depth, val, a, b)
                return val
            a = max(a,val)
        elif pass_val == 2:
            val = Evaluate(state,'X','O')
            display(param, depth, val, a, b)
            return val
        else:
            pass_val = 0
        display(param, depth, val, a, b)
        return val
    for i in actions:
        #print map[i[1]+1],i[0]+1,depth,val,a,b
        board = copy.deepcopy(state)
        board[i[0]][i[1]] = current
        flips = Valid(board,i[0],i[1])
        for x,y in flips:
            board[x][y] = current
        if depth == 0 and flag:
            for l in board:
                output.write("".join(l)+"\n")
            flag = 0
        param = str(map[i[1]+1])+str(i[0]+1)
        val = max(val,Min(board, a, b ,depth+1,param))
        if val >= b:
            display(param, depth, val, a, b)
            return val
        a = max(a,val)
    display(param, depth, val, a, b)
    return val

def Min(state, a , b , depth,param):

    global pass_val
    val = float('inf')
    if Terminal(state,depth):
        val = Evaluate(state,'X','O')
        display(param, depth, val, a, b)
        return val
    if pass_val != 2:
        display(param, depth, val, a, b)

    actions = ValidMoves(state)
    if not actions:
        if pass_val < 2:
            pass_val = pass_val + 1
            val = min(val,Max(state, a , b, depth +1,"pass"))
            if val <= a:
                display(param, depth, val, a, b)
                return val
            b = min(b, val)
        elif pass_val == 2:
            val = Evaluate(state,'O','X')
            display(param, depth, val, a, b)
            return val
        else:
            pass_val = 0
        display(param, depth, val, a, b)
        return val

    for i in actions:
        board = copy.deepcopy(state)
        board[i[0]][i[1]] = current
        flips = Valid(board,i[0],i[1])
        for x,y in flips:
            board[x][y] = current
        param = str(map[i[1] + 1]) + str(i[0]+1)
        val = min(val, Max(state, a, b, depth + 1))
        if val <= a:
            display(param, depth, val, a, b)
            return val
        b = min(b,val)
    display(param, depth, val, a, b)
    return val



input = open('input3.txt','r')
output = open('shreyas3.txt','w')

current = input.readline().strip()
if current == 'X':
    opponent = 'O'
else:
    opponent = 'X'

d =  int(input.readline().strip())
state = []

for line in input.readlines():
    state.append(list(line.strip()))

node = 'root'
alpha = float('inf')
beta = float('-inf')
pass_val = 0

positions = []

eval = [ [ 99, -8 , 8, 6, 6 , 8, -8, 99],
         [ -8, -24 , -4, -3, -3 , -4, -24, -8],
         [ 8, -4 , 7, 4, 4 , 7, -4, 8],
         [ 6, -3 , 4, 0, 0 , 4, -3, 6],
         [ 6, -3 , 4, 0, 0 , 4, -3, 6],
         [ 8, -4 , 7, 4, 4 , 7, -4, 8],
         [ -8, -4 , 7, 4, 4 , 7, -4, 8],
         [  -8, -24 , -4, -3, -3 , -4, -24, -8],
         [  99, -8 , 8, 6, 6 , 8, -8, 99 ]
        ]

AlphaBeta(state)
output.write("Node,Depth,Value,Alpha,Beta\n")
for i in logs:
    output.write(i)
