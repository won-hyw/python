class TictactoeGameEngine:

    def __init__(self):
        self.SIZE = 3
        self.board = list('.' * self.SIZE * self.SIZE)
        # ['.', '.', '.'/ '.', '.', '.'/ '.', '.', '.']
        # [0,1,2/3,4,5/6,7,8]
        self.turn = 'X'

    def show_board(self):
        print(self.board)

    def set(self, row, col):
        pass

    def set_winner(self):
        for x in range(len(self.board)):
            for y in self.board:
                if x % 3 == 1:
                    if y[x] == y[x+1] == y[x+2] == self.turn:
                        print('승리입니다')




        # - 3줄
        # | 3줄
        # \ 3줄
        # / 3줄

        # return self.turn
        # 비기는 조건 : 다 채워졌을 때, 위에 것에 해당 안됬을 때. self.board에 '.'이 없는 상태
        return 'd' # draw

    def change_turn(self):
        # self.turn 'X'면 'O', 'O'면 'X'로 바꾸자


if __name__ == '__main__':
    game_engine = TictactoeGameEngine()
    game_engine.show_board()
    game_engine.set(3, 2)
    game_engine.show_board()
    game_engine.set(3, 1)
    game_engine.set(3, 3)
    print(game_engine.set_winner())
    game_engine.change_turn()
    print(game_engine.turn)