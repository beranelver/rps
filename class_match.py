class Match(object):
    def __init__(self, session_id, round_count, win_count, loss_count, length):
        self.session_id = session_id
        self.length = length
        self.round_count = round_count
        self.win_count = win_count
        self.loss_count = loss_count

    def increment_round_count(self):
        self.round_count += 1

    def increment_win_count(self):
        self.win_count += 1
        self.round_count += 1

    def increment_loss_count(self):
        self.loss_count += 1
        self.round_count += 1

    def print_match_score(self):
        print "You", self.win_count, ":", self.loss_count, "Computer"

    def check_match_is_won(self):
        if self.length == 1:
            if self.win_count == 1 or self.loss_count == 1:
                return True

        elif self.length == 3:
            if self.win_count == 2 or self.loss_count == 2:
                return True

        elif self.length == 5:
            if self.win_count == 3 or self.loss_count == 3:
                return True

        else:
            return False

    def did_user_win(self):
        if self.win_count > self.loss_count:
            return True
        else:
            return False
