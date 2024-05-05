--create database
--examine wire frames

--table 
-->Songs
    columns
        id
        title 
        artist
        rating,created_at,updated_at

        --Queries 2nd page in wireframe fav

        --pull all songs from db
        -- create a song
        --delete a song
        --get one song
        --update song
        --song by rating
        --get song by artist (search )
        --get songs search and top songs

        requirements
        # Wireframe activity
# create a database and all queries

What we need:

#    New DB
        table - songs 
            - column - id, title, artist, rating, created_at, updated_at

# Queries
- pull all songs from database
- add song
- get individual songs
- delete a song
- update a song
- get song by rating (top songs)
- get song by artist (search)


One Table - songs
Query 1: 
Create 4 songs: 
 - fill out the info as best you can
 - include created_at and updated_at

Query 2:
List all songs

Query 3: 
Ability to delete individual songs
 - Delete a song

 Query 4: 
 Search for songs by artist
 - display all songs by Ed Sheeran

 Query 5:
 Create 10 more songs

 Query 6:
 Search for songs by partial artist name (searching for "ed" should pull songs by artist containing 'ed')
 - display all songs by artist containing 'ra'
 select * from songs where artist like "%s%"

Bonus Query 1:
Display the top 10 songs in order of rating (highest to lowest)

Bonus Query 2:
Display the top songs in order of rating (highest to lowest) and ignore songs by Ed Sheeran

USER BONUS:
Add a users table (user should have id, name, created_at, updated_at)
==>SELECT * FROM songs order by rating DESC limit 10 
Create a 1 : Many relationship (one user many song) - to be sure to use a non-identifying relationship. Synchronize your model

Bonus Query 3:
Add 3 users

Bonus Query 4:
Adding users to existing songs (each user should have at least 1 song)

Bonus Query 5:
Get all songs by user 3

M:M BONUS:
add a like relationship
m:m users to songs

Bonus Query 6:
Like 3 songs with user 1, then display all songs liked by user 1