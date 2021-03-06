"""Creating a user vs computer game of Rock, Paper, Scissors"""

from __future__ import division
from random import randint
from random import uniform
from time import sleep
import sys
import class_match
#import class_statistics
import class_statistics_storage
import class_statistics_fetch
#import class_session
import sqlite3

GREET_MSG = "Welcome to Rock, Paper, Scissors!"
WIN_MSG = "You win!"
TIE_MSG = "It's a tie!"
LOSE_MSG = "You lose!"


def slow_type(string):
    for char in string[::1]:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(uniform(0.05, 0.1))


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
        else:
            break
    return length


def play_match(match):
    while not match.check_match_is_won():
        print "ROUND %d" % (match.round_count + 1)

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
            match.increment_win_count()
        elif result == LOSE_MSG:
            match.increment_loss_count()
        elif result == TIE_MSG:
            match.increment_round_count()

        match.print_match_score()

        print "\n"


def play():
    length = choose_match_length()
    session_id = get_session_id()
    print "Session ID: %d" % session_id
    match = class_match.Match(session_id, 0, 0, 0, length)

    play_match(match)

    statistics_storage.write_stats(match)

    if match.did_user_win():
        print "You won this match!"
    else:
        print "Aw, you lost this match"


def create_tables():
    db = sqlite3.connect("rps_database.db")
    d = db.cursor()
    d.execute("CREATE TABLE IF NOT EXISTS matches (match_id INTEGER PRIMARY KEY AUTOINCREMENT, session_id INTEGER, "
              "round_count INTEGER, win_count INTEGER, loss_count INTEGER, length INTEGER)")
    d.execute("CREATE TABLE IF NOT EXISTS sessions (session_id INTEGER PRIMARY KEY AUTOINCREMENT, player_name TEXT, "
              "date_time TEXT)")
    db.commit()
    db.close()


def create_session(name):
    db = sqlite3.connect("rps_database.db")
    d = db.cursor()
    d.execute("INSERT INTO sessions (player_name, date_time) VALUES (?, datetime())", (name,))
    db.commit()
    db.close()


def get_session_id():
    db = sqlite3.connect("rps_database.db")
    d = db.cursor()
    d.execute("SELECT session_id FROM sessions ORDER BY date_time DESC LIMIT 1")
    session_id = d.fetchone()[0]
    db.close()
    return session_id

def print_statistics(stats):
    print "\n"
    print "-" * 49
    print " " * 9 + "-", "Total Rounds ", "-      Match length     - "
    print " " * 8, "-               -   1   -   3   -   5   - "
    print "-" * 49
    print "Played   -       %d     -   %d   -   %d   -   %d   - " % (stats.get("total_rounds"),
                                                                      stats.get("ml1_count"),
                                                                      stats.get("ml3_count"),
                                                                      stats.get("ml5_count"))
    print "Wins     -       %d      -   %d   -   %d   -   %d   -" % (stats.get("total_wins"),
                                                                      stats.get("ml1_wins"),
                                                                      stats.get("ml3_wins"),
                                                                      stats.get("ml5_wins"))
    print "Losses   -       %d      -   %d   -   %d   -   %d   - " % (stats.get("total_losses"),
                                                                      stats.get("ml1_losses"),
                                                                      stats.get("ml3_losses"),
                                                                      stats.get("ml5_losses"))
    print "Ties     -       %d      -------------------------" % stats.get("total_ties")
    print "Win %", "   -       %d      -   %d  -   %d  -   %d  -" % (stats.get("win_percent"),
                                                                      stats.get("ml1_win_percent"),
                                                                      stats.get("ml3_win_percent"),
                                                                      stats.get("ml5_win_percent"))

#------------stuff starts happening here-------------

statistics_storage = class_statistics_storage.StatisticsStorage()

statistics_fetch = class_statistics_fetch.StatisticsFetch()

create_tables()

print GREET_MSG
name = raw_input("What's your name? ").capitalize()
create_session(name)

print "Alright, %s, you know how it works, right? Rock beats scissors, scissors beat paper, paper beats rock. Let's" \
       " see if you've got what it takes to beat the computer!" % name
sleep(0)
print "\n"

player_wants_to_continue = True
while player_wants_to_continue:
    play()

    print_stats = raw_input("Show statistics for this session? Y/N: ").upper()
    if print_stats not in "YN" or len(print_stats) != 1:
        print "I'll take that as a no!"
    elif print_stats == "Y":
        print_statistics(statistics_fetch.get_session_stats(get_session_id()))

    again = raw_input("Would you like to play again? Y/N: ").upper()

    while again not in "YN" and len(again) != 1:
        again = raw_input("I didn't catch that. Please enter Y for yes or N for no: ").upper()

    if again == "N":
        print "Thanks for playing, %s. Here are your overall statistics:" % name
        print_statistics(statistics_fetch.get_overall_stats())
        player_wants_to_continue = False
