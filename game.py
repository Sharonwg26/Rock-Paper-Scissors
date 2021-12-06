class Game:
    def __init__(self, id):
        self.p1Went = False
        self.p2Went = False
        self.ready = False
        self.id = id
        self.moves = [None, None]
        self.wins = [0,0]
        self.ties = 0

    def get_player_move(self, p):
        print("get_player_move：",p,self.moves[p])
        return self.moves[p]

    def play(self, player, move):
        self.moves[player] = move
        if player == 0:
            self.p1Went = True
            print("self.moves[player1]:",self.moves[player])
        else:
            self.p2Went = True
            print("self.moves[player2]:",self.moves[player])

    def connected(self):
        print("ready:",self.ready)
        return self.ready

    def bothWent(self):
        print("bothWent:",self.p1Went ,"\t", self.p2Went)
        return self.p1Went and self.p2Went

    def winner(self):
        p1 = self.moves[0]
        p2 = self.moves[1]
        print("winner:",p1 ,"\t", p2)   
        
        winner = -1
        if p1 == "R" and p2 == "S":
            winner = 0
        elif p1 == "S" and p2 == "R":
            winner = 1
        elif p1 == "P" and p2 == "R":
            winner = 0
        elif p1 == "R" and p2 == "P":
            winner = 1
        elif p1 == "S" and p2 == "P":
            winner = 0
        elif p1 == "P" and p2 == "S":
            winner = 1

        return winner

    def resetWent(self):
        self.p1Went = False
        self.p2Went = False