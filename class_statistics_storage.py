import sqlite3


class StatisticsStorage(object):
    def __innit__(self):
        pass

    def write_stats(self, match):
        db = sqlite3.connect("rps_database.db")
        d = db.cursor()
        d.execute("INSERT INTO matches (session_id, round_count, win_count, loss_count, length)"
                  "VALUES (?, ?, ?, ?, ?)", (match.session_id, match.round_count, match.win_count,
                                             match.loss_count, match.length))
        db.commit()
        db.close()

    def get_stats(self):
        db = sqlite3.connect("rps_database.db")
        d = db.cursor()
        d.execute("SELECT * FROM matches")
        db.close()



"""from philipp:
this class- stupid - only write and get raw data for future use in some way
new class - statistics - reuse original perhaps - clever but limited - add the 17 functions that will 
be used for output

match class i have
stats class i have
should potentially have a session class too which holds session information
so it is cascading down, at the moment i am skipping the session step, going straight from match to stats"""