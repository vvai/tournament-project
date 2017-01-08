-- Table definitions fplaor the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament

DROP TABLE IF EXISTS players;
CREATE TABLE players ( id SERIAL PRIMARY KEY,
                       name TEXT);

DROP TABLE IF EXISTS matches;
CREATE TABLE matches ( id SERIAL PRIMARY KEY,
                       winner INTEGER REFERENCES players(id),
                       loser INTEGER REFERENCES players (id));

DROP VIEW IF EXISTS win_total;
CREATE VIEW win_total AS
SELECT n1.id,
       n1.name,
       coalesce(n2.count, 0) AS wins,
       n1.count AS matches
FROM
 (SELECT players.id,
         players.name,
         count(matches.winner)
  FROM players
  LEFT JOIN matches ON players.id=matches.winner
  OR players.id=matches.loser
  GROUP BY players.id) n1
LEFT JOIN
 (SELECT players.id,
         players.name,
         count(*)
  FROM players,
       matches
  WHERE matches.winner=players.id
  GROUP BY players.id) n2 ON (n1.id=n2.id)
ORDER BY wins DESC;
