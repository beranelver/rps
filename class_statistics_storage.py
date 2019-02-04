import sqlite3


class StatisticsStorage(object):
    def __innit__(self):
        pass


    def write_stats(self, match):
        db = sqlite3.connect("rps_database.db")
        d = db.cursor()
        d.execute("INSERT INTO matches (session_id, round_count, win_count, loss_count, length)"
                  "VALUES (?, ?, ?, ?, ?)", (match.session_id, match.round_no, match.match_user_score,
                                             match.match_comp_score, match.length))
        db.commit()
        db.close()

    def get_session_stats(self, session_id):
        total_rounds = self.get_total_rounds(session_id)




    def get_total_rounds(self, session_id):
        db = sqlite3.connect("rps_database.db")
        d = db.cursor()
        d.execute("SELECT SUM(round_count) FROM matches WHERE session_id = ?", (session_id,))
        total_rounds = int(d.fetchone()[0])
        db.close()
        return total_rounds


    def get_overall_stats(self):
        db = sqlite3.connect("rps_database.db")
        d = db.cursor()
        db.close()