def parse_fen(fen):
    view(fen)
    fen_pieces, to_move, castling_rights, ep, hm, fm = fen.split(" ")
    pieces = [[]]
    for char in fen:
        if char.isdigit():
            pieces[-1].extend(["."] * int(char))
        elif char == "/":
            pieces.append([])
        else:
            pieces[-1].append(char)

    return ...


def generate_moves(board):
    raise NotImplementedError("This function is not implemented yet.")


def apply_move(board, move):
    raise NotImplementedError("This function is not implemented yet.")

def view(data):
    count=8
    print("-"*count)
    for row in range(count):
        for col in range(count):
            if row == 0:
                print("|",end="")
            


        
    print("-"*8)

def view1(data):
    print("-"*8)
    arr = (data.split(" ")[0]).split("/")
    for row in arr:
        if row=="8":
            print(""*8)
        else:
            print(row)
        
    print("-"*8)