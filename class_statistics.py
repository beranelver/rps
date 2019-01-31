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
        self.get_ratio()
        print "\n"
        print "-" * 49
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
        print "-" * 49

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