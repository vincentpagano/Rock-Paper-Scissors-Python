import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    moves = ['rock', 'paper', 'scissors']

    def __init__(self):
        self.my_move = self.moves
        self.their_move = random.choice(self.moves)

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class RandomPlayer(Player):
    def move(self):
        return random.choice(self.moves)


class ReflectPlayer(Player):
    def move(self):
        return self.their_move


class CyclePlayer(Player):
    def move(self):
        if self.my_move == self.moves[0]:
            return self.moves[1]
        elif self.my_move == self.moves[1]:
            return self.moves[2]
        else:
            return self.moves[0]


class HumanPlayer(Player):
    def move(self):
        while True:
            move_human = input("Rock, paper, scissors? > ")
            if move_human.lower() in self.moves:
                return move_human.lower()
            elif move_human.lower() == 'exit':
                exit()


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score_p1 = 0
        self.score_p2 = 0

    def beats(self, one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))

    def rounds(self):
        while True:
            self.number_rounds = input(
                "How many rounds do you want want play? > ")
            if self.number_rounds.isdigit():
                return self.number_rounds
            elif self.number_rounds.lower() == 'exit':
                exit()

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        if self.beats(move1, move2):
            self.score_p1 += 1
            winner = '*** Player ONE Wins! ***'
        elif move1 == move2:
            self.score_p1 = self.score_p1
            self.score_p2 = self.score_p2
            winner = '*** TIE ***'
        else:
            self.score_p2 += 1
            winner = '*** Player TWO Wins! ***'
        print(
            f"> You played : {move1}"
            f"\n> Opponent played : {move2}"
            f"\n{winner}"
            f"\nScore: Player one ( {self.score_p1} ),"
            f"Player two ( {self.score_p2} )"
        )
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print(
            ">>>> Game start! <<<<"
            "\n(The game will ask you the number of rounds and your move."
            "\n If you want to exit the game, please enter \'exit\')"
        )
        self.rounds()
        for round in range(int(self.number_rounds)):
            print(f"\nRound {round + 1} --")
            self.play_round()
        if self.score_p1 == self.score_p2:
            print(
                f"\n*** The game ended in a TIE! ***"
                f"\nScore: Player one ( {self.score_p1} ),"
                f"Player two ( {self.score_p2} )"
            )
        elif self.score_p1 > self.score_p2:
            print(
                f"\n*** Player ONE has won! ***"
                f"\nScore: Player one ( {self.score_p1} )*,"
                f"Player two ( {self.score_p2} )"
            )
        else:
            print(
                f"\n*** Player TWO has won! ***"
                f"\nScore: Player one ( {self.score_p1} ),"
                f"Player two ( {self.score_p2} )*"
            )


if __name__ == '__main__':
    game = Game(HumanPlayer(), random.choice(
        [RandomPlayer(), ReflectPlayer(), CyclePlayer()]))
    game.play_game()
