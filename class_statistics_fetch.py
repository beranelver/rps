from __future__ import division
import sqlite3


class StatisticsFetch(object):
    def __innit__(self):
        pass

    def get_session_stats(self, session_id):
        session_stats = {}

        total_rounds = self.get_session_total_rounds(session_id)
        session_stats["total_rounds"] = total_rounds

        total_wins = self.get_session_total_wins(session_id)
        session_stats["total_wins"] = total_wins

        total_losses = self.get_session_total_losses(session_id)
        session_stats["total_losses"] = total_losses

        #total_ties = total_rounds - total_wins - total_losses
        #session_stats["total_ties"] = total_ties

        total_ties = self.get_session_total_ties(session_id)
        session_stats["total_ties"] = total_ties

        if total_wins == 0:
            win_percent = 0
        else:
            win_percent = (total_wins / total_rounds) * 100
            #win_percent = self.get_session_total_win_percent(session_id)
        session_stats["win_percent"] = win_percent

        ml1_count = self.get_session_ml_count(1, session_id)
        session_stats["ml1_count"] = ml1_count

        ml1_wins = self.get_session_ml_wins(1, session_id)
        session_stats["ml1_wins"] = ml1_wins

        ml1_losses = self.get_session_ml_losses(1, session_id)
        session_stats["ml1_losses"] = int(ml1_losses)

        if ml1_wins == 0:
            ml1_win_percent = 0
        else:
            ml1_win_percent = (ml1_wins / ml1_count) * 100
        session_stats["ml1_win_percent"] = ml1_win_percent

        ml3_count = self.get_session_ml_count(3, session_id)
        session_stats["ml3_count"] = ml3_count

        ml3_wins = self.get_session_ml_wins(3, session_id)
        session_stats["ml3_wins"] = ml3_wins

        ml3_losses = self.get_session_ml_losses(3, session_id)
        session_stats["ml3_losses"] = ml3_losses

        if ml3_wins == 0:
            ml3_win_percent = 0
        else:
            ml3_win_percent = (ml3_wins / ml3_count) * 100
        session_stats["ml3_win_percent"] = ml3_win_percent

        ml5_count = self.get_session_ml_count(5, session_id)
        session_stats["ml5_count"] = ml5_count

        ml5_wins = self.get_session_ml_wins(5, session_id)
        session_stats["ml5_wins"] = ml5_wins

        ml5_losses = self.get_session_ml_losses(5, session_id)
        session_stats["ml5_losses"] = ml5_losses

        if ml5_wins == 0:
            ml5_win_percent = 0
        else:
            ml5_win_percent = (ml5_wins / ml5_count) * 100
        session_stats["ml5_win_percent"] = ml5_win_percent

        return session_stats

    def get_session_total_rounds(self, session_id):
        db = sqlite3.connect("rps_database.db")
        d = db.cursor()
        d.execute("SELECT SUM(round_count) FROM matches WHERE session_id = ?", (session_id,))
        total_rounds = int(d.fetchone()[0])
        db.close()
        return total_rounds

    def get_session_total_wins(self, session_id):
        db = sqlite3.connect("rps_database.db")
        d = db.cursor()
        d.execute("SELECT SUM(win_count) FROM matches WHERE session_id = ?", (session_id,))
        total_wins = int(d.fetchone()[0])
        db.close()
        return total_wins

    def get_session_total_losses(self, session_id):
        db = sqlite3.connect("rps_database.db")
        d = db.cursor()
        d.execute("SELECT SUM(loss_count) FROM matches WHERE session_id = ?", (session_id,))
        total_losses = int(d.fetchone()[0])
        db.close()
        return total_losses

    def get_session_total_ties(self, session_id):
        db = sqlite3.connect("rps_database.db")
        d = db.cursor()
        d.execute("SELECT (SUM(round_count) - SUM(win_count) - SUM(loss_count)) FROM matches WHERE session_id = ?",
                  (session_id,))
        total_ties = int(d.fetchone()[0])
        db.close()
        return total_ties

    def get_session_total_win_percent(self, session_id):
        db = sqlite3.connect("rps_database.db")
        d = db.cursor()
        d.execute("SELECT COUNT((win_count / round_count) * 100) FROM matches WHERE session_id = ?",
                  (session_id,))
        total_win_percent = int(d.fetchone()[0])
        db.close()
        return total_win_percent

    def get_session_ml_count(self, match_length, session_id):
        db = sqlite3.connect("rps_database.db")
        d = db.cursor()
        d.execute("SELECT COUNT(length) FROM matches WHERE length = ? AND session_id = ?;",
                  (match_length, session_id,))
        ml_count = int(d.fetchone()[0])
        db.close()
        return ml_count

    def get_session_ml_wins(self, match_length, session_id):
        db = sqlite3.connect("rps_database.db")
        d = db.cursor()
        d.execute("SELECT COUNT(length) FROM matches WHERE length = ? AND win_count > loss_count AND session_id = ?",
                  (match_length, session_id,))
        ml_wins = int(d.fetchone()[0])
        db.close()
        return ml_wins

    def get_session_ml_losses(self, match_length, session_id):
        db = sqlite3.connect("rps_database.db")
        d = db.cursor()
        d.execute("SELECT COUNT(length) FROM matches WHERE length = ? AND win_count < loss_count AND session_id = ?",
                  (match_length, session_id,))
        ml_losses = int(d.fetchone()[0])
        db.close()
        return ml_losses

    def get_overall_stats(self):
        overall_stats = {}

        total_rounds = self.get_total_rounds()
        overall_stats["total_rounds"] = total_rounds

        total_wins = self.get_total_wins()
        overall_stats["total_wins"] = total_wins

        total_losses = self.get_total_losses()
        overall_stats["total_losses"] = total_losses

        # total_ties = total_rounds - total_wins - total_losses
        # overall_stats["total_ties"] = total_ties

        total_ties = self.get_total_ties()
        overall_stats["total_ties"] = total_ties

        if total_wins == 0:
            win_percent = 0
        else:
            win_percent = (total_wins / total_rounds) * 100
            # win_percent = self.get_session_total_win_percent()
        overall_stats["win_percent"] = win_percent

        ml1_count = self.get_ml_count(1)
        overall_stats["ml1_count"] = ml1_count

        ml1_wins = self.get_ml_wins(1)
        overall_stats["ml1_wins"] = ml1_wins

        ml1_losses = self.get_ml_losses(1)
        overall_stats["ml1_losses"] = int(ml1_losses)

        if ml1_wins == 0:
            ml1_win_percent = 0
        else:
            ml1_win_percent = (ml1_wins / ml1_count) * 100
        overall_stats["ml1_win_percent"] = ml1_win_percent

        ml3_count = self.get_ml_count(3)
        overall_stats["ml3_count"] = ml3_count

        ml3_wins = self.get_ml_wins(3)
        overall_stats["ml3_wins"] = ml3_wins

        ml3_losses = self.get_ml_losses(3)
        overall_stats["ml3_losses"] = ml3_losses

        if ml3_wins == 0:
            ml3_win_percent = 0
        else:
            ml3_win_percent = (ml3_wins / ml3_count) * 100
        overall_stats["ml3_win_percent"] = ml3_win_percent

        ml5_count = self.get_ml_count(5)
        overall_stats["ml5_count"] = ml5_count

        ml5_wins = self.get_ml_wins(5)
        overall_stats["ml5_wins"] = ml5_wins

        ml5_losses = self.get_ml_losses(5)
        overall_stats["ml5_losses"] = ml5_losses

        if ml5_wins == 0:
            ml5_win_percent = 0
        else:
            ml5_win_percent = (ml5_wins / ml5_count) * 100
        overall_stats["ml5_win_percent"] = ml5_win_percent

        return overall_stats

    def get_total_rounds(self):
        db = sqlite3.connect("rps_database.db")
        d = db.cursor()
        d.execute("SELECT SUM(round_count) FROM matches")
        total_rounds = int(d.fetchone()[0])
        db.close()
        return total_rounds

    def get_total_wins(self):
        db = sqlite3.connect("rps_database.db")
        d = db.cursor()
        d.execute("SELECT SUM(win_count) FROM matches")
        total_wins = int(d.fetchone()[0])
        db.close()
        return total_wins
    def get_total_losses(self):
        db = sqlite3.connect("rps_database.db")
        d = db.cursor()
        d.execute("SELECT SUM(loss_count) FROM matches")
        total_losses = int(d.fetchone()[0])
        db.close()
        return total_losses

    def get_total_ties(self):
        db = sqlite3.connect("rps_database.db")
        d = db.cursor()
        d.execute("SELECT (SUM(round_count) - SUM(win_count) - SUM(loss_count)) FROM matches")
        total_ties = int(d.fetchone()[0])
        db.close()
        return total_ties

    def get_total_win_percent(self):
        db = sqlite3.connect("rps_database.db")
        d = db.cursor()
        d.execute("SELECT COUNT((win_count / round_count) * 100) FROM matches")
        total_win_percent = int(d.fetchone()[0])
        db.close()
        return total_win_percent

    def get_ml_count(self, match_length):
        db = sqlite3.connect("rps_database.db")
        d = db.cursor()
        d.execute("SELECT COUNT(length) FROM matches WHERE length = ?", (match_length,))
        ml_count = int(d.fetchone()[0])
        db.close()
        return ml_count

    def get_ml_wins(self, match_length):
        db = sqlite3.connect("rps_database.db")
        d = db.cursor()
        d.execute("SELECT COUNT(length) FROM matches WHERE length = ? AND win_count > loss_count", (match_length,))
        ml_wins = int(d.fetchone()[0])
        db.close()
        return ml_wins

    def get_ml_losses(self, match_length):
        db = sqlite3.connect("rps_database.db")
        d = db.cursor()
        d.execute("SELECT COUNT(length) FROM matches WHERE length = ? AND win_count < loss_count", (match_length,))
        ml_losses = int(d.fetchone()[0])
        db.close()
        return ml_losses