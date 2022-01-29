import sqlite3

from wordle_data import valid_words, answer_words 

with  sqlite3.connect('wordle.db') as conn:
    cur = conn.cursor()
    cur.execute("""
    create table answers (word primary key)
    """)
    cur.execute("""
    create table words (word primary key)
    """)
    cur.executemany("insert into answers values(?)", [(w,) for w in answer_words])
    cur.executemany("insert into words values(?)", [(w,) for w in valid_words])



