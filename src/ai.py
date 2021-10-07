class AI:
    def __init__(self):
        self.possiblePositions = [0,0,0,0,0,0,0,0,0]

    def checkPossiblePositions(self, board):
        j = 0
        
        for i in board:
            if i == 0:
                self.possiblePositions[j] = 1
            else:
                self.possiblePositions[j] = 0
            j = j + 1

    def makeTurn(self, board):
        for i in range(len(self.possiblePositions)):
            if self.possiblePositions[i] == 1:
                board[i] = -1
                break

