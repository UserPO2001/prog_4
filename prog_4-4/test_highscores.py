from highscores import Highscores
import sqlite3

# test highscores
scores = Highscores()

# removes the table
# connection = sqlite3.connect('lingo.sqlite3')
# cursor = connection.cursor()
# cursor.execute("DROP TABLE highscores; ")
# connection.close()

# test adding of scores
scores.add_score("Peter", 100)