class Solution:
    def win(self, board: List[str], player)-> bool:
        for i in range(3):
            if(board[i][0]==player and player== board[i][2] and board[i][1] == player):
                return True
            if(board[0][i]==player and board[1][i]== player and board[2][i] == player):
                return True
        if(board[0][0]==player and board[1][1]== player and board[2][2]==player):
            return True
        if(board[2][0]==player and board[1][1]== player and board[0][2]==player):
            return True
        return False
    
    def validTicTacToe(self, board: List[str]) -> bool:
        x = "X"
        o = "O"
        xCount = 0
        oCount = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == x:
                    xCount +=1
                elif board[i][j]==o:
                    oCount+=1
        if oCount> xCount or xCount-1>oCount:
            return False
        if self.win(board,"X") and xCount-1 != oCount: return False
        if self.win(board,"O") and xCount!= oCount: return False
        return True