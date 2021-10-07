import ai

class Game:
    def __init__(self):
        self.board = [0,0,0,0,0,0,0,0,0]
        self.ai = ai.AI()

    #check if board is full
    def isFull(self):
        for i in self.board:
            if i == 0:
                return False
        return True

    #check if cell is occupied
    def cellIsOccupied(self, cell):
        if self.board[cell] != 0:
            return True
        return False

    #update the board
    def updateBoard(self, cell):
        self.board[cell] = 1
        

    #number to sign
    def numberToSign(self, number):
        if number == 0:
            return " "
        elif number == 1:
            return "X"
        else:
            return "O"

    #check for win
    def checkWin(self, board, sign):
        if board[0] == sign and board[1] == sign and board[2] == sign:
            return True
        if board[3] == sign and board[4] == sign and board[5] == sign:
            return True
        if board[6] == sign and board[7] == sign and board[8] == sign:
            return True
        if board[0] == sign and board[3] == sign and board[6] == sign:
            return True 
        if board[1] == sign and board[4] == sign and board[7] == sign:
            return True
        if board[2] == sign and board[5] == sign and board[8] == sign:
            return True
        if board[0] == sign and board[4] == sign and board[8] == sign:
            return True
        if board[2] == sign and board[4] == sign and board[6] == sign:
            return True 


   #print board
    def printBoard(self):
        print(self.numberToSign(self.board[0]) + " | " + self.numberToSign(self.board[1]) + " | " + self.numberToSign(self.board[2]))
        print(self.numberToSign(self.board[3]) + " | " + self.numberToSign(self.board[4]) + " | " + self.numberToSign(self.board[5]))
        print(self.numberToSign(self.board[6]) + " | " + self.numberToSign(self.board[7]) + " | " + self.numberToSign(self.board[8]))

    #start gameloop
    def start(self):
        while not self.isFull():
            self.printBoard()
            
            #player set sign to board
            try:
                cell = int(input("set sign to board (1-9): ")) -1
            except ValueError:
                print("only numbers between 1 and 9")
                continue
            
            if not self.cellIsOccupied(cell):
                self.updateBoard(cell)
            else:
                print("cell is occupied")
                continue
            
            #check if player win (player-sign = 1)
            if self.checkWin(self.board, 1):
                print("player won")
                self.printBoard()
                break
            
            #ai logic
            self.ai.checkPossiblePositions(self.board)

            self.ai.makeTurn(self.board)

            #check if ai win (ai-sign = -1)
            if self.checkWin(self.board, -1):
                print("computer won")
                self.printBoard
                break     
    
