#main.
lst=[0,0,0,0,0,0,0,0,0]
def board():
    count=0
    for i in range(3):
        for j in range(3):
            if lst[count]==0:
                print("__|",end="")
            else:
                print(lst[count]+"|",end="")
            count+=1
        print()

def swap_users():
    if globals()['user']=='X':
        globals()['user']='O'
    else:
        globals()['user']='X'

def win():
    if lst[0]=='X' and lst[1]=='X' and lst[2]=='X':
        board()
        globals()['game']=False
        print("Player X wins!")
    elif lst[3]=='X' and lst[4]=='X' and lst[5]=='X':
        board()
        globals()['game']=False
        print("Player X wins!")
    elif lst[6]=='X' and lst[7]=='X' and lst[8]=='X':
        board()
        globals()['game']=False
        print("Player X wins!")
    elif lst[0]=='X' and lst[3]=='X' and lst[6]=='X':
        board()
        globals()['game']=False
        print("Player X wins!")
    elif lst[1]=='X' and lst[4]=='X' and lst[7]=='X':
        board()
        globals()['game']=False
        print("Player X wins!")
    elif lst[2]=='X' and lst[5]=='X' and lst[8]=='X':
        board()
        globals()['game']=False
        print("Player X wins!")
    elif lst[0]=='X' and lst[4]=='X' and lst[8]=='X':
        board()
        globals()['game']=False
        print("Player X wins!")
    elif lst[2]=='X' and lst[4]=='X' and lst[6]=='X':
        board()
        globals()['game']=False
        print("Player X wins!")
    elif lst[0]=='O' and lst[1]=='O' and lst[2]=='O':
        board()
        globals()['game']=False
        print("Player O wins!")
    elif lst[3]=='O' and lst[4]=='O' and lst[5]=='O':
        board()
        globals()['game']=False
        print("Player O wins!")
    elif lst[6]=='O' and lst[7]=='O' and lst[8]=='O':
        board()
        globals()['game']=False
        print("Player O wins!")
    elif lst[0]=='O' and lst[3]=='O' and lst[6]=='O':
        board()
        globals()['game']=False
        print("Player O wins!")
    elif lst[1]=='O' and lst[4]=='O' and lst[7]=='O':
        board()
        globals()['game']=False
        print("Player O wins!")
    elif lst[2]=='O' and lst[5]=='O' and lst[8]=='O':
        board()
        globals()['game']=False
        print("Player O wins!")
    elif lst[0]=='O' and lst[4]=='O' and lst[8]=='O':
        board()
        globals()['game']=False
        print("Player O wins!")
    elif lst[2]=='O' and lst[4]=='O' and lst[6]=='0':
        board()
        globals()['game']=False
        print("Player O wins!")

def is_full():
    return all(cell != 0 for cell in lst)



game=True
user='X'

while game:
    board()
    n = int(input(f"Player {user}, enter your selection (1-9): "))
    if  1 <= n <= 9 and lst[n - 1] == 0:
        lst[n - 1] = user
        if win():
            board()
            print(f"Player {user} wins!")
            game = False
        elif is_full ==True:
            board()
            print("It's a tie!")
            game = False
        else:
            swap_users()
    else:
        print("Invalid move. Try again.")
print("---End---")