from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# executing the instructions from our localhost "chinook" db
db = create_engine("postgresql:///chinook")

meta = MetaData(db)

# create variable for "Artist" table
artist_table = Table(
    "artist", meta,
    Column("artistId", Integer, primary_key=True),
    Column("name", String)
)

# create variable for "Album" table
album_table = Table(
    "album", meta,
    Column("albumId", Integer, primary_key=True),
    Column("title", String),
    Column("artistId", Integer, ForeignKey("artist_table.ArtistId"))
)

# create variable for "Track" table
track_table = Table(
    "track", meta,
    Column("trackId", Integer, primary_key=True),
    Column("name", String),
    Column("albumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("mediaTypeId", Integer, primary_key=False),
    Column("genreId", Integer, primary_key=False),
    Column("composer", String),
    Column("milliseconds", Integer),
    Column("bytes", Integer),
    Column("unitPrice", Float)
)


# making the connection
with db.connect() as connection:
    #Query 1 - select all records from the "artist" table
    select_query = artist_table.select()

    # Query 2 - select only the "Name" column from the "Artist" table
    # select_query = artist_table.select().with_only_columns([artist_table.c.Name])

    # Query 3 - select only 'Queen' from the "Artist" table
    # select_query = artist_table.select().where(artist_table.c.Name == "Queen")

    # Query 4 - select only by 'ArtistId' #51 from the "Artist" table
    # select_query = artist_table.select().where(artist_table.c.ArtistId == 51)

    # Query 5 - select only the albums with 'ArtistId' #51 on the "Album" table
    # select_query = album_table.select().where(album_table.c.ArtistId == 51)

    # Query 6 - select all tracks where the composer is 'Queen' from the "Track" table
    #select_query = track_table.select().where(track_table.c.Composer == "Queen")

    results = connection.execute(select_query)
    for result in results:
        print(result)