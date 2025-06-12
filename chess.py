def parse_fen(fen):
 
    fen_pieces, to_move, castling_rights, ep, hm, fm = fen.split(" ")
    pieces = [[]]
    for char in fen:
        if char.isdigit():
            pieces[-1].extend(["."] * int(char))
        elif char == "/":
            pieces.append([])
        else:
            pieces[-1].append(char)
    
    return pieces


def generate_moves(board):
    print(board)
    raise NotImplementedError("This function is not implemented yet.")


def apply_move(board, move):
    raise NotImplementedError("This function is not implemented yet.")


def grid_printer(data):
   #data is [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
        #  ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
        #  ['.', '.', '.', '.', '.', '.', '.', '.'],
        #  ['.', '.', '.', '.', '.', '.', '.', '.'],
        #  ['.', '.', '.', '.', '.', '.', '.', '.'],
        #  ['.', '.', '.', '.', '.', 'N', '.', '.'],
        #  ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
        #  ['R', 'N', 'B', 'Q', 'K', 'B', '.', 'R', ' ', 'w', ' ', 'K', 'Q', 'k', 'q', ' ', '-', ' ', ' ', '.']]
   
    print("-"*8*4)         #this print the ----------- on the top and below our grid
    for row in range(8):    #this for loop is used to iterate through the data as it is
        print("|",end="")   # i'm printing the border wall before i run a for loop which i will use for the list within data
        for col in range(8):
            print(data[row][col],end=" | ") #print would my default print what ever is given and would jump to a new line in 
                                        #the end argument i'm placing line so we see every time it prints value automatically adds a | for us
        print("")
        print("-"*8*4)
        
def view(data):
   
    
    for row in range(8):
        for col in range(8):
            print((row,col),end="")
        print("\n")
            


        
    

def view1(data):
    print("-"*8)
    arr = (data.split(" ")[0]).split("/")
    for row in arr:
        if row=="8":
            print(""*8)
        else:
            print(row)
        
    print("-"*8)

board =parse_fen( "rnbqkbnr/pppppppp/8/8/8/5N2/PPPPPPPP/RNBQKB1R b KQkq - 1 1"  )
#lowwer is black
#upper is white
def generate_moves2(board):
    turn=board[-1][-12]
   
    moves=[]
    for row in range(8):
        for column in range(8):
            if turn == "b":
                if board[row][column]=="k":
                    king=(row,column)
                if board[row][column].islower():

                    func = identify_pc(board[row][column])
                    pc_moves=func(row,column)
                    moves.append({board[row][column]:pc_moves})

            if turn =="w":
                if board[row][column].isupper():
                    func = identify_pc(board[row][column])
                    if func(row,column):
                        moves.append({board[row][column]:(row,column)})
    return moves

                
def identify_pc(chr):
    if chr.lower() =="p":
        return pawn
    elif chr.lower() == "r":
        return rook
    if chr.lower() =="b":
        return bishop
    elif chr.lower() == "k":
        return king
    if chr.lower() =="q":
        return queen
    elif chr.lower() == "k":
        return king


def rook(row,col):
    pass

def pawn(row,col):
    enem

def bishop(row,col):
    pass

def knight(row,col):
    direc = [(2,1),(1,2),(2,-1),(-1,2),(-2,1),(1,-2),(-2,-1),(-1,-2)]
    moves=[]
    for x,y in direc:
        if not is_confilct(x,y) and is_legal(row,col,row+x,col+y):
            moves.append((row+x,col+y))
    return moves






def queen(row,col):
    return rook(row,col)+bishop(row,col)
    

def king(row,col):
    direc=[(1,1),(1,-1),(-1,-1),(-1,1),(1,0),(-1,0),(0,-1),(0,1)]
    moves=[]
    for x,y in direc:
        if not is_confilct(x,y) and is_legal(row,col,row+x,col+y):
            moves.append((row+x,col+y))




def is_confilct(row,col):
    try:
        return board[row][col]
    except IndexError:
        return True;
    

def is_legal(row,col,n_row,n_col):
    return True




#grid(board)
print(generate_moves2(board))