import sys, re, os
import sqlite3 

def to_where(guess, result):
  if (len(guess) != 5):
    return "False"
  where = []
  pattern = []
  usepattern = False
  for (i,c) in enumerate(result):
    if(c == 'G'):
      pattern.append(guess[i])
      usepattern = True
    elif(c == 'Y'):
      where.append("word like '%%{}%%'".format(guess[i]))
      pattern.append("_")
    else:
      where.append("word not like '%%{}%%'".format(guess[i]))
      pattern.append("_")
  if usepattern:
    pattern = "".join(pattern)
    where.append("word like '{}'".format(pattern))
  return "({})".format(" and ".join(where))

def main(args):
  conn = sqlite3.connect("wordle.db")
  cur = conn.cursor()
  condition = "true"
  while True:
    wguess = input("Enter guess word: ")
    wresult = input("Enter result: ")
    condition = (condition + " and " + to_where(wguess, wresult))
    query = "select count(1) from answers where {}".format(condition)
    (matches,) = cur.execute(query).fetchone()
    print (query, " == ", matches)
    if (matches < 8):
      query = "select word from answers where {}".format(condition)
      answers = [w for w in cur.execute(query).fetchall()]
      if (matches == 1):
        print ("The answer is", answers[0])
        break


if __name__ == "__main__":
  main(sys.argv[1:])
# vim: tabstop=2 expandtab shiftwidth=2 softtabstop=2
