DROP TABLE IF EXISTS Players;
DROP TABLE IF EXISTS Match;
DROP TABLE IF EXISTS Tournaments;
DROP TABLE IF EXISTS Score;
DROP TABLE IF EXISTS TournamentComments;
DROP TABLE IF EXISTS Comment;



CREATE TABLE Players (
  player_id INTEGER PRIMARY KEY,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
  rating INTEGER NOT NULL
);

CREATE TABLE Tournaments (
  tournament_id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  format TEXT NOT NULL,
  date_time TEXT
);


CREATE TABLE Match (
  winner_id INTEGER,
	loser_id INTEGER, 
  score_id INTEGER,
  tournament_id INTEGER, 
  PRIMARY KEY (winner_id, loser_id, score_id, tournament_id),
  FOREIGN KEY (winner_id) 
  REFERENCES Players (player_id) 
    ON DELETE CASCADE 
    ON UPDATE CASCADE 
  FOREIGN KEY (loser_id) 
  REFERENCES Players (player_id) 
    ON DELETE CASCADE 
    ON UPDATE CASCADE 
  FOREIGN KEY (score_id) 
  REFERENCES Score (score_id) 
    ON DELETE CASCADE 
    ON UPDATE CASCADE 
  FOREIGN KEY (tournament_id) 
  REFERENCES Tournaments(tournament_id) 
    ON DELETE CASCADE 
    ON UPDATE CASCADE 
);

CREATE TABLE Score (
  score_id INTEGER PRIMARY KEY,
	loser_score INTEGER NOT NULL,
	winner_score INTEGER NOT NULL 
);

CREATE TABLE TournamentComments (
  tournament_comments_id INTEGER PRIMARY KEY NOT NULL,
  tournament_id INTEGER NOT NULL,
  name TEXT NOT NULL,
  FOREIGN KEY (tournament_id) 
  REFERENCES Tournaments(tournament_id) 
    ON UPDATE CASCADE 
    ON DELETE CASCADE 
);

CREATE TABLE Comment (
  comment_id INTEGER PRIMARY KEY NOT NULL,
  tournament_comments_id INTEGER NOT NULL,
  text Text NOT NULL,
  date_time TEXT NOT NULL,
  FOREIGN KEY (tournament_comments_id) 
  REFERENCES TournamentComments(tournament_comments_id) 
    ON UPDATE CASCADE 
    ON DELETE CASCADE 
);

INSERT INTO Players (first_name, last_name, rating)
VALUES ("MR", "B", 2200), ("MR", "A", 2100);

INSERT INTO Tournaments(name, format, date_time)
VALUES ("2022", "Teams Event", datetime('now'));

INSERT INTO TournamentComments(tournament_id, name)
VALUES (1, 'Day 1');
INSERT INTO Comment(tournament_comments_id, text, date_time)
VALUES (1, "This is a comment", datetime('now')), (1, "BONKERS!!", datetime('now'));


pragma foreign_keys=on;
