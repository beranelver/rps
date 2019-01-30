"""Creating a user vs computer game of Rock, Paper, Scissors"""

from __future__ import division
from random import randint
from random import uniform
from time import sleep
import sys


GREET_MSG = "Welcome to Rock, Paper, Scissors!"
WIN_MSG = "You win!"
TIE_MSG = "It's a tie!"
LOSE_MSG = "You lose!"


def slow_type(string):
    for char in string[::1]:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(uniform(0.2, 0.3))


class Match(object):
    def __init__(self, length, round_no, match_user_score, match_comp_score):
        self.length = length
        self.round_no = round_no
        self.match_user_score = match_user_score
        self.match_comp_score = match_comp_score

    def increment_round_no(self):
        self.round_no += 1

    def increment_match_user_score(self):
        self.match_user_score += 1
        self.round_no += 1

    def increment_match_comp_score(self):
        self.match_comp_score += 1
        self.round_no += 1

    def print_match_score(self):
        print "%s" % name, self.match_user_score, ":", self.match_comp_score, "Computer"

    def reset_match_stats(self):
        self.round_no = 0
        self.match_user_score = 0
        self.match_comp_score = 0

    def check_match_is_won(self):
        if self.length == 1:
            if self.match_user_score == 1 or self.match_comp_score == 1:
                return True

        elif self.length == 3:
            if self.match_user_score == 2 or self.match_comp_score == 2:
                return True

        elif self.length == 5:
            if self.match_user_score == 3 or self.match_comp_score == 3:
                return True

        else:
            return False

    def did_user_win(self):
        if self.match_user_score > self.match_comp_score:
            return True
        else:
            return False


class Statistics(object):
    def __init__(self, game_no, user_score, comp_score, tie_score, win_ratio, ml1_played, ml1_wins, ml3_played,
                 ml3_wins, ml5_played, ml5_wins, ml1_ratio, ml3_ratio, ml5_ratio):
        self.game_no = game_no
        self.user_score = user_score
        self.comp_score = comp_score
        self.tie_score = tie_score
        self.win_ratio = win_ratio
        self.ml1_played = ml1_played
        self.ml1_wins = ml1_wins
        self.ml3_played = ml3_played
        self.ml3_wins = ml3_wins
        self.ml5_played = ml5_played
        self.ml5_wins = ml5_wins
        self.ml1_ratio = ml1_ratio
        self.ml3_ratio = ml3_ratio
        self.ml5_ratio = ml5_ratio

    def increment_game_no(self):
        self.game_no += 1

    def increment_user_win(self):
        self.user_score += 1

    def increment_comp_win(self):
        self.comp_score += 1

    def increment_tie(self):
        self.tie_score += 1

    def get_ratio(self):
        if self.user_score == 0:
            self.win_ratio = 0
        elif self.user_score > 0 and self.comp_score == 0 and self.tie_score == 0:
            self.win_ratio = 100
        else:
            self.win_ratio = (self.user_score / self.game_no) * 100

    def print_win_line(self):
        if self.win_ratio == 100:
            print "Win %", "   -       %d    -   %d   -   %d   -   %d   -" % (self.win_ratio, self.ml1_ratio,
                                                                              self.ml3_ratio, self.ml5_ratio)
        elif self.win_ratio == 0:
            print "Win %", "   -       %d      -   %d   -   %d   -   %d   -" % (self.win_ratio, self.ml1_ratio,
                                                                                self.ml3_ratio, self.ml5_ratio)
        else:
            print "Win %", "   -       %d     -   %d   -   %d   -   %d   -" % (self.win_ratio, self.ml1_ratio,
                                                                               self.ml3_ratio, self.ml5_ratio)

    def print_stats(self):
        stats.get_ratio()
        print "\n"
        print "-" * 49
        print " %s" % name + "'s Statistics"
        print " " * 9 + "-", "Total Rounds", "-      Match length     - "
        print " " * 8, "-              -   1   -   3   -   5   - "
        print "-" * 49
        print "Played   -       %d      -   %d   -   %d   -   %d   - " % (self.game_no, self.ml1_played,
                                                                          self.ml3_played, self.ml5_played)
        print "Wins     -       %d      -   %d   -   %d   -   %d   -" % (self.user_score, self.ml1_wins, self.ml3_wins,
                                                                         self.ml5_wins)
        print "Losses   -       %d      -   %d   -   %d   -   %d   - " % (self.comp_score,
                                                                          (self.ml1_played - self.ml1_wins),
                                                                          (self.ml3_played - self.ml3_wins),
                                                                          (self.ml5_played - self.ml5_wins))
        print "Ties     -       %d      -------------------------" % self.tie_score
        self.print_win_line()

    def increment_ml1_played(self):
        self.ml1_played += 1

    def increment_ml1_wins(self):
        self.ml1_wins += 1
        self.ml1_played += 1

    def increment_ml3_played(self):
        self.ml3_played += 1

    def increment_ml3_wins(self):
        self.ml3_wins += 1
        self.ml3_played += 1

    def increment_ml5_played(self):
        self.ml5_played += 1

    def increment_ml5_wins(self):
        self.ml5_wins += 1
        self.ml5_played += 1

    def get_ml1_ratio(self):
        if self.ml1_wins == 0:
            self.ml1_ratio = " "
        elif self.ml1_wins > 0 and self.ml1_played == 0:
            self.ml1_ratio = 100
        else:
            self.ml1_ratio = (self.ml1_wins / self.ml1_played) * 100

    def get_ml3_ratio(self):
        if self.ml3_wins == 0:
            self.ml3_ratio = " "
        elif self.ml3_wins > 0 and self.ml1_played == 0:
            self.ml3_ratio = 100
        else:
            self.ml3_ratio = (self.ml3_wins / self.ml3_played) * 100

    def get_ml5_ratio(self):
        if self.ml5_wins == 0:
            self.ml5_ratio = " "
        elif self.ml5_wins > 0 and self.ml1_played == 0:
            self.ml5_ratio = 100
        else:
            self.ml5_ratio = (self.ml5_wins / self.ml5_played) * 100

    def add_match(self, match):
        for _ in range(match.round_no):
            self.increment_game_no()

        for _ in range(match.match_user_score):
            self.increment_user_win()

        for _ in range(match.match_comp_score):
            self.increment_comp_win()

        for _ in range(match.round_no - match.match_user_score - match.match_comp_score):
            self.increment_tie()

        if match.length == 1:
            if match.did_user_win() is True:
                self.increment_ml1_wins()
            else:
                self.increment_ml1_played()

        elif match.length == 3:
            if match.did_user_win() is True:
                self.increment_ml3_wins()
            else:
                self.increment_ml3_played()

        elif match.length == 5:
            if match.did_user_win() is True:
                self.increment_ml5_wins()
            else:
                self.increment_ml5_played()


def get_winner(user, comp):
    if user == comp:
        return TIE_MSG
    elif (user == " Rock" and comp == " Scissors") or (user == " Scissors" and comp == " Paper" or
                                                       (user == " Paper" and comp == " Rock")):
        return WIN_MSG
    else:
        return LOSE_MSG


def get_word(guess):
    if guess == "R" or guess == 1:
        return " Rock"
    elif guess == "P" or guess == 2:
        return " Paper"
    elif guess == "S" or guess == 3:
        return " Scissors"


def choose_match_length():
    valid_lengths = [1, 3, 5]

    while True:
        try:
            length = int(raw_input("Would you like to play the best of [1], [3] or [5] games? "))
        except ValueError:
            print "I'm not sure I understand..."
            continue
        if length not in valid_lengths:
            print "That's not an option!"
            continue
        else:
            break
    return length


def play_match(match):
    while not match.check_match_is_won():
        print "ROUND %d" % (match.round_no + 1)

        user_guess = raw_input("Guess [R]ock, [P]aper or [S]cissors: ").upper()
        while user_guess not in "RPS" or len(user_guess) != 1:
            user_guess = raw_input("I didn't catch that. Please enter R for rock, P for paper or S for "
                                   "scissors: ").upper()

        comp_guess = randint(1, 3)
        user_final = get_word(user_guess)
        comp_final = get_word(comp_guess)

        print "Your guess =" + user_final
        sleep(1)
        print "Computer guess =",
        slow_type(comp_final)

        print "\n"
        sleep(0)

        result = get_winner(user_final, comp_final)
        print result

        sleep(0)

        if result == WIN_MSG:
            match.increment_match_user_score()
        elif result == LOSE_MSG:
            match.increment_match_comp_score()
        elif result == TIE_MSG:
            match.increment_round_no()

        match.print_match_score()

        print "\n"


def play():
    length = choose_match_length()

    match = Match(length, 0, 0, 0)
    play_match(match)

    stats.add_match(match)

    if match.did_user_win():
        print "You won this match!"
    else:
        print "Aw, you lost this match"

stats = Statistics(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

"""------------stuff starts displaying from here-------------"""

print GREET_MSG
name = raw_input("What's your name? ").capitalize()
print "Alright, %s, you know how it works, right? Rock beats scissors, scissors beat paper, paper beats rock. Let's" \
       " see if you've got what it takes to beat the computer!" % name
sleep(0)
print "\n"

player_wants_to_continue = True
while player_wants_to_continue:
    play()

    print_stats = raw_input("Show statistics for [T]his session, [O]verall or [N]ot at all? ").upper()
    if print_stats not in "TON" or len(print_stats) != 1:
        print "I'll take that as a no!"
    elif print_stats == "T":
        stats.print_stats()
    elif print_stats == "O":
        print "I'm not clever enough to do that yet. Come back next week!"

    again = raw_input("Would you like to play again? Y/N: ").upper()

    while again not in "YN" and len(again) != 1:
        again = raw_input("I didn't catch that. Please enter Y for yes or N for no: ").upper()

    if again == "N":
        print "Thanks for playing, %s. Here are your final statistics for today: " % name
        stats.print_stats()
        player_wants_to_continue = False
