# tournament udacity project

This project represents a Python module that uses the PostgreSQL database to keep track of players and matches in a game tournament.

To run this project you should have python 3 and PostgreSQL installed in your computer. Or you can use VM: just clone [this](http://github.com/udacity/fullstack-nanodegree-vm) repository and replace files in tornament folder.

You should have `tournament` database created. Open `psql` from console and write:

    CREATE DATABASE tournament;

Also you should have `psycopg2` python package installed:

    pip install psycopg2

And that is all! Run command below and you will see that tests passed well:

    python tournament_test.py
