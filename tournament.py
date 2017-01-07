"""vojtehovsky@gmail.com."""
from __future__ import division
import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    conn = connect()
    cursor = conn.cursor()
    query = "DELETE FROM matches"
    cursor.execute(query)
    conn.commit()
    conn.close()


def deletePlayers():
    """Remove all the player records from the database."""
    conn = connect()
    cursor = conn.cursor()
    query = "DELETE FROM players"
    cursor.execute(query)
    conn.commit()
    conn.close()


def countPlayers():
    """Return the number of players currently registered."""
    conn = connect()
    cursor = conn.cursor()
    query = "SELECT COUNT(id) AS num FROM players"
    cursor.execute(query)
    results = cursor.fetchone()
    conn.close()
    if results:
        return int(results[0])
    else:
        return 0


def registerPlayer(name):
    """Add a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    conn = connect()
    cursor = conn.cursor()
    query = "INSERT INTO players(name) VALUES (%(name)s)"
    cursor.execute(query, {'name': name})
    conn.commit()
    conn.close()


def playerStandings():
    """Return a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a
    player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    conn = connect()
    cursor = conn.cursor()
    query = "SELECT * FROM  win_total"
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


def reportMatch(winner, loser):
    """Record the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    conn = connect()
    cursor = conn.cursor()
    query = "INSERT INTO matches (winner, loser) VALUES (%(winner)s, %(loser)s)"
    cursor.execute(query, {'winner': winner, 'loser': loser})
    conn.commit()
    conn.close()


def swissPairings():
    """Return a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    players = playerStandings()
    result = []
    for index in range(len(players)//2):
        result.append((players[index*2][0],
                       players[index*2][1],
                       players[index*2 + 1][0],
                       players[index*2 + 1][1]))
    return result
