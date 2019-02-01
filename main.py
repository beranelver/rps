"""Creating a user vs computer game of Rock, Paper, Scissors"""

from __future__ import division
from random import randint
from random import uniform
from time import sleep
import sys
import class_match
import class_statistics
import sqlite3

GREET_MSG = "Welcome to Rock, Paper, Scissors!"
WIN_MSG = "You win!"
TIE_MSG = "It's a tie!"
LOSE_MSG = "You lose!"


def slow_type(string):
    for char in string[::1]:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(uniform(0.2, 0.3))


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

    match = class_match.Match(length, 0, 0, 0)
    play_match(match)

    stats.add_match(match)

    if match.did_user_win():
        print "You won this match!"
    else:
        print "Aw, you lost this match"


stats = class_statistics.Statistics(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

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
        stats.print_overall_stats()

    again = raw_input("Would you like to play again? Y/N: ").upper()

    while again not in "YN" and len(again) != 1:
        again = raw_input("I didn't catch that. Please enter Y for yes or N for no: ").upper()

    if again == "N":
        print "Thanks for playing, %s. Here are your final statistics for today: " % name
        stats.print_stats()
        player_wants_to_continue = False
