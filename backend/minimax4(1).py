from os import system
import time
from math import inf as infinity

board=["_", "_", "_",
       "_", "_", "_",
       "_", "_", "_"]

def printboard(board):
    print(" ",board[0],"|",board[1],"|",board[2]," ")
    print("--------------")
    print(" ",board[3],"|",board[4],"|",board[5]," ")
    print("--------------")
    print(" ",board[6],"|",board[7],"|",board[8]," ")

def evaluate(state):
    if winner(state,"0"):
        score=+1
    elif winner(state,"X"):
        score=-1
    else:
        score=0

    return score
def freespots(board):
    result=[]
    for i,j in enumerate(board):
        if j =="_":
            result.append(i)
    return result

def winner(state,player):
    win_state=[
        [state[0],state[1],state[2]],
        [state[3],state[4],state[5]],
        [state[6],state[7],state[8]],
        [state[0],state[3],state[6]],
        [state[1],state[4],state[7]],
        [state[2],state[5],state[8]],
        [state[0],state[4],state[8]],
        [state[2],state[4],state[6]],
    ]
    if [player,player,player] in win_state:
        return True
    else:
        return False

def gameover(state):
    return winner(state,"X") or winner(state,"O")

def minimax(board,level,player):
    if player =="O":
        best=[-1,-infinity]
    else:
        best=[-1,infinity]

    if level == 0 or gameover(board):
        score= evaluate(board)
        return[-1,score]
    for cell in freespots(board):
        board[cell] = player

        if player == "O":
            score = minimax(board,level - 1,"X")
        else:
            score = minimax(board,level - 1,"O")
        board[cell] = "_"
        score[0] = cell
        if player == "O":
            if best[1] < score[1]:
                best = score
        else:
            if best[1] > score[1]:
                best = score
    return best

def player(board):
    depth = len(freespots(board))
    if depth == 0 or gameover(board):
        return

    move = -1

    while move < 1 or move > 9:
        clean()
        print('player turn \n')
        printboard(board)
        move = int(input("Enter position between 1-9: "))

        if move <= 9 and move >= 1:
            if board[move-1] == "_":
                move -= 1
                board[move] = "X"
                printboard(board)
                return
            else:
                print("This position is not free :(")
                move = -1
                time.sleep(1)

        else:
            print("wrong move Not available :/")
            move = -1
def player2(board):
    depth = len(freespots(board))
    if depth == 0 or gameover(board):
        return

    move = -1

    while move < 1 or move > 9:
        clean()
        print('player2 turn \n')
        printboard(board)
        move = int(input("Enter position between 1-9: "))

        if move <= 9 and move >= 1:
            if board[move-1] == "_":
                move -= 1
                board[move] = "O"
                printboard(board)
                return
            else:
                print("This position is not free :(")
                move = -1
                time.sleep(1)

        else:
            print("wrong move Not available :/")
            move = -1
def clean():
    system('cls')

def CompMove(level):
    if level == 5:
        level = len(freespots(board))
    if level == 0 or gameover(board):
        return

    clean()

    print("AI turn \n")
    move=minimax(board,level,'O')
    board[move[0]] = 'O'
    printboard(board)
    time.sleep(1)

def main(board):
    print("opponent human or computer type h for human and c for computer \n")
    opp = input("Enter opponent h or c \n")
    if opp == "h":
        while len(freespots(board)) > 0 and not gameover(board):
            player(board)
            player2(board)

        if winner(board, "X"):
            print("Player won!")
            return 0
        elif winner(board, "O"):
            print("Player 2 won!")
            return 0
        else:
            print("Draw")
            return 0

    elif opp == "c":
        print("Choose level 1,2,3,4,5 (5-unlimited)")
        level = int(input("Enter level \n"))
        while len(freespots(board)) > 0 and not gameover(board):
            player(board)
            CompMove(level)

        if winner(board, "X"):
            print("Player won!")
            return 0
        elif winner(board, "O"):
            print("Computer won!")
            return 0
        else:
            print("Draw")
            return 0

if __name__ == "__main__":
    while True:
        main(board)
        board = ["_","_","_","_","_","_","_","_","_"]
        again = input("Wanna play again?[y/n]: ")
        if again == "n":
            break
