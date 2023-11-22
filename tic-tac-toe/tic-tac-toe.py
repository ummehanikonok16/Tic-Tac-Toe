class Game:
    def __init__(self):
        self.initialize_game()

    def initialize_game(self):
        print("Board=")
        self.cur_state = []
        for j in range(3):
            temp = input().split(" ")
            self.cur_state.append(temp)
        # print(self.cur_state)
        turn = input("Player =")
        # for i in range(0, 3):
        #     for j in range(0, 3):
        #         print('{} '.format(self.cur_state[i][j]), end=" ")
        #     print()
        # print()

        if turn == 'Max':
            self.player = 'X'
        else:
            self.player = 'O'

    def valid(self, ax, ay):
        if ax < 0 or ax > 2 or ay < 0 or ay > 2:
            return False
        elif self.cur_state[ax][ay] != '_':
            return False
        else:
            return True

    def win(self):
        for i in range(0, 3):
            if (self.cur_state[0][i] != '_' and
                    self.cur_state[0][i] == self.cur_state[1][i] and
                    self.cur_state[1][i] == self.cur_state[2][i]):
                return self.cur_state[0][i]

        for i in range(0, 3):
            if self.cur_state[i] == ['X', 'X', 'X']:
                return 'X'
            elif self.cur_state[i] == ['O', 'O', 'O']:
                return 'O'

        if (self.cur_state[0][0] != '_' and
                self.cur_state[0][0] == self.cur_state[1][1] and
                self.cur_state[0][0] == self.cur_state[2][2]):
            return self.cur_state[0][0]

        if (self.cur_state[0][2] != '_' and
                self.cur_state[0][2] == self.cur_state[1][1] and
                self.cur_state[0][2] == self.cur_state[2][0]):
            return self.cur_state[0][2]

        for i in range(0, 3):
            for j in range(0, 3):
                if self.cur_state[i][j] == '_':
                    return None

        return '_'

    def max(self):
        max_val = -2

        ax = None
        ay = None

        winner = self.win()

        if winner == 'X':
            return -1, 0, 0
        elif winner == 'O':
            return 1, 0, 0
        elif winner == '_':
            return 0, 0, 0

        for i in range(0, 3):
            for j in range(0, 3):
                if self.cur_state[i][j] == '_':
                    self.cur_state[i][j] = 'O'
                    (m, min_i, min_j) = self.min()
                    if m > max_val:
                        max_val = m
                        ax = i
                        ay = j
                    self.cur_state[i][j] = '_'
        return max_val, ax, ay

    def min(self):
        min_val = 2

        qx = None
        qy = None

        winner = self.win()

        if winner == 'X':
            return (-1, 0, 0)
        elif winner == 'O':
            return (1, 0, 0)
        elif winner == '_':
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if self.cur_state[i][j] == '_':
                    self.cur_state[i][j] = 'X'
                    (m, max_i, max_j) = self.max()
                    if m < min_val:
                        min_val = m
                        qx = i
                        qy = j
                    self.cur_state[i][j] = '_'

        return (min_val, qx, qy)

    def play(self):
        while True:
            for i in range(0, 3):
                for j in range(0, 3):
                    print('{} '.format(self.cur_state[i][j]), end=" ")
                print()
            print()

            self.winner = self.win()

            if self.winner != None:
                if self.winner == 'X':
                    print('Winner is Max')
                elif self.winner == 'O':
                    print('Winner is Min')
                elif self.winner == '_':
                    print("Draw")
                return

            if self.player == 'X':
                while True:
                    ax = int(input('X-axis: '))
                    ay = int(input('Y-axis: '))

                    if self.valid(ax, ay):
                        self.cur_state[ax][ay] = 'X'
                        self.player = 'O'
                        break
                    else:
                        print('invalid move!')

            else:
                if self.winner == 'X':
                    break
                else:
                    (m, ax, ay) = self.max()
                    self.cur_state[ax][ay] = 'O'
                    self.player = 'X'


if __name__ == "__main__":
    g = Game()
    g.play()

# _ _ _
# _ _ _
# _ _ _

# X _ _
# _ O X
# O _ _

# X _ X
# _ O _
# O _ _
