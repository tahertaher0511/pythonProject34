# Created by Taher Ismail. 15/10/2020 1:55 AM

import random
from os import path


class RockPaperScissors:
    allowed_input = ('help', 'rating', 'exit', 'rock', 'paper', 'scissors')
    allowed_game_input = ('rock', 'paper', 'scissors')
    winners_paris = {'rock': 'paper', 'paper': 'scissors', 'scissors': "rock"}
    score_path = 'rating.txt'
    POINTS_WINS = 100
    POINTS_DRAW = 50

    # The game files are created  in __init__
    def __init__(self):
        self.user_input = ''
        self.cpu_choice = ''
        self.exit = False
        self.user_name = ''
        # create files games now
        if not path.exists(self.score_path):
            open(self.score_path, 'w').close()

    def random_option_cpu(self):
        random.seed()
        self.cpu_choice = random.choice(self.allowed_game_input)

    def scores_to_list(self):
        score_sheet = open(self.score_path, 'r')
        current_scores = [x.strip('\n').split() for x in score_sheet]
        score_sheet.close()
        return current_scores

    def increased_user_score(self, score):
        # read the current scores
        scores = self.scores_to_list()
        # update the specific score file
        for x in scores:
            if x[0] == self.user_name:
                x[1] = str(int(x[1]) + score)
        # update the score file
        score_sheet = open(self.score_path, 'w')
        for x in scores:
            score_sheet.write(x[0] + " " + x[1] + "\n")
        score_sheet.close()
        # print(entry[0], entry[1], sep=" ", end="\n", file=score_sheet)# print(entry[0], entry[1], sep=" ",
        # end="\n", file=score_sheet)

    def announce_winner(self):
        # 1. draw
        if self.user_input == self.cpu_choice:
            print(f'This is a draw({self.cpu_choice})')
            self.increased_user_score(score=self.POINTS_DRAW)
        # cpu wins
        elif self.winners_paris[self.user_input] == self.cpu_choice:
            print(f'Sorry but computer choose {self.cpu_choice}')
        # 3. user wins
        elif self.winners_paris[self.cpu_choice] == self.user_input:
            print(f'Well done. CPU choose {self.cpu_choice} and failed')
            self.increased_user_score(score=self.POINTS_WINS)

    def is_game_input(self):
        return self.user_input in self.allowed_game_input

    def get_user_input(self):
        action = input()
        if action not in self.allowed_input:
            self.user_input = ''
            print('Please write (help) to see your options!')
        else:
            if action == 'exit':
                print('Bye!')
                self.user_input = ''
                self.exit = True
            elif action == 'help':
                self.user_input = ''
                print('write either (rock, paper, scssors) or (exit) or (rating)')
            elif action == 'rating':
                self.user_input = ''
                scores = self.scores_to_list()
                for x in scores:
                    if x[0] == self.user_name:
                        print('Your rating:', x[1])
            else:
                # all others cases are game input
                self.user_input = action

    # get_user_name is executed at the start of the game
    def register_new_user(self):
        score_sheet = open(self.score_path, 'a')
        score_sheet.write(self.user_name + " 0\n")
        score_sheet.close()

    def get_correct_user_name(self):
        self.user_name = input('Enter your name: ').replace(' ', '')
        print(f'Hello, {self.user_name}.')
        # add the user to the score sheet  if not already in the sheet
        if path.getsize(self.score_path) > 0:
            scores = self.scores_to_list()
            user_in_scores = False
            for x in scores:
                if x[0] == self.user_name:
                    user_in_scores = True
            if not user_in_scores:
                self.register_new_user()
        else:
            # in case there was no user at all, add the user right away
            self.register_new_user()

    def no_user_yet(self):
        return self.user_name == ''

    def game(self):
        while not self.exit:
            if self.no_user_yet():
                self.get_correct_user_name()
            else:
                self.get_user_input()
                if self.is_game_input():
                    self.random_option_cpu()
                    self.announce_winner()


rockpaperscissors = RockPaperScissors()
rockpaperscissors.game()
