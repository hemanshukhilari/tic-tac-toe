import math
import os
game=[' ',' ',' ',' ',' ',' ',' ',' ',' ']

player=True
def board(map):
        print("\n\n\n\n\n\n\n\n\t\t\t\t\t\t    |    |   ")
        print("\t\t\t\t\t\t",map[0]," |",map[1]," |",map[2],)
        print("\t\t\t\t\t\t````|````|````")
        print("\t\t\t\t\t\t",map[3]," |",map[4]," |",map[5],)
        print("\t\t\t\t\t\t````|````|````")
        print("\t\t\t\t\t\t",map[6]," |",map[7]," |",map[8],)


def update(val):
     os.system('cls')
     global player
     if player:
         game[val-1]='x'
     else:
         game[val-1]='o'
     player=not player
     board(game)
     #check game status
     #clear the screen
     
     #
  

def inputs():
    global player
    global game
    
    while(game_status(game)==0):
        print("Player1:") if player==True else print("Player2:")
        coordinate=int(input())
        
        if(coordinate>=1 and coordinate<=9 and game[coordinate-1]==' '):
            update(coordinate)
        else:
            print("WRONG COORDINATE ENTERED\nTry again:")
            inputs()
    input()


def game_status(game):
    #horizontal check
        for row in range(3):
            if game[int(math.ceil(row*3.5)):int(math.ceil((row+1)*3.5))]==['x','x','x']:  
                print("PLAYER1 WINS")
                return 1
            elif game[int(math.ceil(row*3.5)):int(math.ceil((row+1)*3.5))]==['o','o','o']:   
                print("PLAYER2 WINS")
                return -1
    #vertical check
        for col in range(3):
            if game[0+col]==game[1*3+col]==game[2*3+col]=='x':
                print("PLAYER1 WINS")
                return 1
            elif game[0+col]==game[1*3+col]==game[2*3+col]=='o':
                print("PLAYER2 WINS")
                return -1
    #diagonal check
        
        if (game[0]==game[4]==game[8]=='x' or game[6]==game[4]==game[2]=='x'):
            print("PLAYER1 WINS")
            return 1
        elif(game[0]==game[4]==game[8]=='o' or game[6]==game[4]==game[2]=='o'):
            print("PLAYER2 WINS")    
            return -1
        else:
            return 0
###############################################################################################


       
os.system('cls')
board(game)
print("ENTER NUMBER BETWEEN 1-9  TO MARK THE CELL\n")

inputs()
