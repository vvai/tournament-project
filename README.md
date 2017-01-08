# tournament udacity project

## Description
This project represents a Python module that uses the PostgreSQL database to keep track of players and matches in a game tournament.

## Whats included?
Tournament project
- `tournament.sql` - sets up a tournament database schema with tables
- `tournament.py` - contains methods to connect, read, add, delete players and matches
- `tournament_test.py` - contains sctipts to test the methods implemented in `tournament.py` file

## How to setup environment?

1. To run this project you should have python 3 and PostgreSQL installed in your computer. Or you can use VM: just clone [this](http://github.com/udacity/fullstack-nanodegree-vm) repository and replace files in tornament folder.

2. Install `psycopg2` python package:

    `pip install psycopg2`

3. Run `tournament.sql` script and create database:

    `psql -f tournament.sql`

## How to execute tests?

Run tests script:

    python tournament_test.py

And that is all! You should see that tests passed well.
