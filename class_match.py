class Match(object):
    def __init__(self, session_id, round_no, match_user_score, match_comp_score, length):
        self.session_id = session_id
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
        print "You", self.match_user_score, ":", self.match_comp_score, "Computer"

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