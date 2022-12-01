import sqlite3
import logging


def db_connect(with_connection = False):

  conn = sqlite3.connect('db.dev')
  cur = conn.cursor() 
  cur.execute('pragma foreign_keys = 1')

  if not with_connection:
    return cur

  return cur, conn


def format_tournament_comments(prev):
  cleaned = []
  for (id, name) in prev:
    cleaned.append(
      {
        'tournament_comments_id': id, 
        'name': name,
      },
    )
  return cleaned
def format_tournament_comment_feed(prev):
  cleaned = []
  for (id, text, date_time) in prev:
    cleaned.append(
      {
        'comment_id': id, 
        'text': text,
        'date_time': date_time,
      },
    )
  return cleaned


def fetch_tournament_comments(tournament_id):
  cur = db_connect()
  result = cur.execute(
    '''
    SELECT tournament_comments_id, name from TournamentComments where tournament_id = (?);
    ''',
  (tournament_id,))
  return format_tournament_comments(result.fetchall())

def create_tournament_comment(tournament_id, name):

  cur, conn = db_connect(True)

  cur.execute(
    '''
    INSERT INTO TournamentComments(tournament_id, name) VALUES(?, ?);
    ''',
  (tournament_id, name))

  conn.commit()

  return True 
def create_tournament_feed_comment(tournament_id, tournament_comment_id, text):
  cur, conn = db_connect(True)
  cur.execute(
    '''
    INSERT INTO Comment(tournament_comments_id, text, date_time)
    VALUES(?, ?, datetime("now"))
    ''',
    (tournament_comment_id, text)
  )
  conn.commit()
  return True

def fetch_tournament_comment_feed(tournament_comment_id):
  cur = db_connect()
  result = cur.execute(
    '''
    SELECT comment_id, text, date_time from Comment where tournament_comments_id = (?) ORDER BY date_time ASC;
    ''',
  (tournament_comment_id,))
  return format_tournament_comment_feed(result.fetchall())