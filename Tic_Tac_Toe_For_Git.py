import random

class Tic_Tac_Toe:
    def __init__(self):
        self.board = []
        self.player = 0
        self.turn = 0
        self.bad = 0
    def b_creation(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)
    def b_print(self):
        for i in self.board:
            print(i)
    def s_player(self):
        game.b_print()
        toss = input("Click 1 for Toss : ")
        self.turn = 0
        if toss == "1":
            self.player = random.randint(0, 1)
            while True:
                if self.player == 1:
                    p = "O"
                    if self.turn == 9:
                        print("No one wins")
                        self.board.clear()
                        game.s_player()
                    n = int(input("Enter A number between [1-9] : "))
                    game.board_move(n, p)
                    print("The value of Turn : ",self.turn)
                    if self.turn <= 9:
                        if (game.c_f_r() == True or game.c_s_r() == True or game.c_t_r() == True or game.c_f_col() == True or game.c_s_col() == True or game.c_t_col() == True or game.c_cro_bs() == True or game.c_cro_fs() == True):
                            print("Human Wins")
                            self.board.clear()
                            game.b_creation()
                            break
                    else:
                        print("No one wins")
                        self.board.clear()
                        game.b_creation()
                        break
                    self.player = 0
                    if self.turn == 9:
                        print("No one wins")
                        self.board.clear()
                        game.s_player()
                    print("\nComputer Move")
                else:
                    c = "X"
                    if self.turn == 9:
                        print("No one wins")
                        self.board.clear()
                        game.s_player()
                    n = random.randint(1, 9)
                    game.board_move(n, c)
                    print("The value of Turn : ",self.turn)
                    if self.turn <= 9:
                        if (game.c_f_r() == True or game.c_s_r() == True or game.c_t_r() == True or game.c_f_col() == True or game.c_s_col() == True or game.c_t_col() == True or game.c_cro_bs() == True or game.c_cro_fs() == True):
                            print("Computer Wins")
                            self.board.clear()
                            game.b_creation()
                            break
                    else:
                        print("No one wins")
                        self.board.clear()
                        game.b_creation()
                        break

                    self.player = 1
                    if self.turn == 9:
                        print("No one wins")
                        self.board.clear()
                        game.s_player()
                    print("\nHuman Move")
    def c_f_r(self):
        if (self.board[0][0] == self.board[0][1] == self.board[0][2]) and (self.board[0][0] != '-' and self.board[0][1] != '-' and  self.board[0][2] != '-'):
            return True
    def c_s_r(self):
        if (self.board[1][0] == self.board[1][1] == self.board[1][2]) and (self.board[1][0] != '-' and  self.board[1][1] != '-' and self.board[1][2] != '-'):
            return True
    def c_t_r(self):
        if (self.board[2][0] == self.board[2][1] == self.board[2][2]) and (self.board[2][0] != '-' and self.board[2][1] != '-' and self.board[2][2] != '-'):
            return True
    def c_f_col(self):
        if (self.board[0][0] == self.board[1][0] == self.board[2][0]) and (self.board[0][0] != '-' and self.board[1][0] != '-' and self.board[2][0] != '-'):
            return True
    def c_s_col(self):
        if (self.board[0][1] == self.board[1][1] == self.board[2][1]) and (self.board[0][1] != '-' and self.board[1][1] != '-' and self.board[2][1] != '-'):
            return True
    def c_t_col(self):
        if (self.board[0][2] == self.board[1][2] == self.board[2][2]) and (self.board[0][2] != '-' and self.board[1][2] != '-' and self.board[2][2] != '-'):
            return True
    def c_cro_bs(self):
        if (self.board[0][0] == self.board[1][1] == self.board[2][2]) and (self.board[0][0] != '-' and self.board[1][1] != '-' and self.board[2][2] != '-'):
            return True    
    def c_cro_fs(self):
        if (self.board[0][2] == self.board[1][1] == self.board[2][0]) and (self.board[0][2] != '-' and self.board[1][1] != '-' and self.board[2][0] != '-'):
            return True        
    def board_move(self, n, p):
        if n > 9 and n < 1:
            print("Bad move")
        else:
            if n >= 1 and n <= 3:
                if self.board[0][n-1] == '-':
                    self.board[0][n-1] = p
                    self.turn = self.turn+1
                    game.b_print()
                else:
                    self.turn = self.turn
                    if self.turn == 9:
                        print("No one wins")
                        self.board.clear()
                        game.s_player()
                    print("Bad Move")
            elif n >= 4 and n <= 6:
                if n == 4:
                    if self.board[1][0] == '-':
                        self.board[1][0] = p
                        self.turn = self.turn+1
                        game.b_print()
                    else:
                        self.turn = self.turn
                        if self.turn == 9:
                            print("No one wins")
                            self.board.clear()
                            game.s_player()
                        print("Bad Move")
                elif n == 5: 
                    if self.board[1][1] == '-':
                        self.board[1][1] = p
                        self.turn = self.turn+1
                        game.b_print()
                    else:
                        self.turn = self.turn
                        if self.turn == 9:
                            print("No one wins")
                            self.board.clear()
                            game.s_player()
                        print("Bad Move")
                elif n == 6:
                    if self.board[1][2] == '-':
                        self.board[1][2] = p
                        self.turn = self.turn+1
                        game.b_print()
                    else:
                        self.turn = self.turn
                        if self.turn == 9:
                            print("No one wins")
                            self.board.clear()
                            game.s_player()
                        print("Bad Move")
            elif n >= 7 and n <= 9:
                if n == 7:
                    if self.board[2][0] == '-':
                        self.board[2][0] = p
                        self.turn = self.turn+1
                        game.b_print()
                    else:
                        self.turn = self.turn
                        if self.turn == 9:
                            print("No one wins")
                            self.board.clear()
                            game.s_player()
                        print("Bad Move")
                elif n == 8: 
                    if self.board[2][1] == '-':
                        self.board[2][1] = p
                        self.turn = self.turn+1
                        game.b_print()
                    else:
                        self.turn = self.turn
                        if self.turn == 9:
                            print("No one wins")
                            self.board.clear()
                            game.s_player()
                        print("Bad Move")
                elif n == 9:
                    if self.board[2][2] == '-':
                        self.board[2][2] = p
                        self.turn = self.turn+1
                        game.b_print()
                    else:
                        self.turn = self.turn
                        if self.turn == 9:
                            print("No one wins")
                            self.board.clear()
                            game.s_player()
                        print("Bad Move")
game = Tic_Tac_Toe()
game.b_creation()
while True:
    game_play = input("Welcome AI Tic Tac Toe\n[S] Start [Q] Quit Enter : ")
    if game_play.upper() == "S":
        game.s_player()
    elif game_play.upper() == "Q":
        print("Thank You!")
        break
