from flask import request
from src.database.db_connect import create_db_connection
from src.database.db_connect import close_db_connection
from src.errors_handling.msg_exception import msg_exception

class ArtistRepository:

    def list_artists(self):
        """Logic to get list artists from the database

        Returns:
            Dictionary: artists data got
        """
        try:
            db_connection = create_db_connection()
            if db_connection:
                with db_connection.cursor() as cursor:
                    sql = "SELECT * FROM artist_table"
                    cursor.execute(sql)
                    
                    data_got = cursor.fetchall()
                    artists_list = []

                    for row in data_got:
                        # Dictionary with data got  for return
                        artist = {
                            "artist_key": row[0],
                            "artist_aka": row[1],
                            "artist_name": row[2],
                            "artist_dateborn": row[3],
                            "artist_deathdate": row[4],
                            "artist_country": row[5],
                        }
                        artists_list.append(artist)
                # Returns artists data in 'json' format | List of dictionaries
                return artists_list
        except Exception as ex:
            return msg_exception(self.list_artists, ex)
        finally:
            close_db_connection(db_connection)
            
    def get_artist(self, code):
        """Logic to get the details the an artist from the database

        Args:
            code (str): artist_aka of artist

        Returns:
            Dictionary: artist data got
        """
        try:
            db_connection = create_db_connection()
            if db_connection:
                with db_connection.cursor() as cursor:
                    sql = "SELECT * FROM artist_table WHERE artist_aka = (%s)"
                    cursor.execute(sql, (code,))
                    data_got = cursor.fetchone()

                    if data_got != None:
                        artist = {
                            "artist_key": data_got[0],
                            "artist_aka": data_got[1],
                            "artist_name": data_got[2],
                            "artist_dateborn": data_got[3],
                            "artist_deathdate": data_got[4],
                            "artist_country": data_got[5],
                        }
                        # Returns artist data in 'json' format | Dictionary
                        return artist

        except Exception as ex:
            return msg_exception(self.get_artist, ex)
        finally:
            close_db_connection(db_connection)

    def add_artist(self, data_artist):
        """Logic to add a new artist in the database
        
        Returns: confirmation 'INSERT' or exception
        """
        try:
            db_connection = create_db_connection()
            if db_connection:
                with db_connection.cursor() as cursor:
                    sql = """INSERT artist_table
                    (artist_aka,
                    artist_name,
                    artist_dateborn,
                    artist_deathdate,
                    artist_country)
                    VALUES (%s, %s, %s, %s, %s)"""

                    artist_dateborn = data_artist["artist_dateborn"]
                    if artist_dateborn ==  "":
                        artist_dateborn = None
                    artist_deathdate = data_artist["artist_deathdate"]
                    if artist_deathdate ==  "":
                        artist_deathdate = None
                    value = (
                        # 'artist key' is added when data is inserted into the database
                        data_artist["artist_aka"].lower(),
                        data_artist["artist_name"].lower(),
                        artist_dateborn,
                        artist_deathdate,
                        data_artist["artist_country"].lower(),
                    )
                    cursor.execute(sql, value)
                    db_connection.commit()
                    return "Artist added"
        except Exception as ex:
            return msg_exception(self.add_artist, ex)
        finally:
            close_db_connection(db_connection)

    def update_artist(self, code, jsonData):
        """Logic to update the details an artist in the database

        Args:
            code (int): Primary key of artist

        Returns:
            Returns: confirmation 'UPDATE' or exception
        """
        artist_aka = jsonData["artist_aka"].lower()
        artist_name = jsonData["artist_name"].lower()
        artist_dateborn = jsonData["artist_dateborn"]
        artist_deathdate = jsonData["artist_deathdate"]
        artist_country = jsonData["artist_country"].lower()

        
        if artist_dateborn == "":
            artist_dateborn = None
            
        if artist_deathdate == "":
            artist_deathdate = None
        
        try:
            db_connection = create_db_connection()
            if db_connection:
                with db_connection.cursor() as cursor:
                    sql = """UPDATE artist_table SET artist_aka = (%s),
                                    artist_name = (%s),
                                    artist_dateborn = (%s),
                                    artist_deathdate = (%s),
                                    artist_country = (%s)
                                    WHERE artist_key = (%s)"""
                    value = (artist_aka, artist_name, artist_dateborn, artist_deathdate, artist_country, code)
                    cursor.execute(sql, value)
                    db_connection.commit()
                    return "Artist updated"
        except Exception as ex:
            return msg_exception(self.update_artist, ex)
        finally:
            close_db_connection(db_connection)

    def delete_artist(self, code):
        # Logic to delete an artist the database
        try:
            db_connection = create_db_connection()
            if db_connection:
                with db_connection.cursor() as cursor:
                    sql = "DELETE FROM artist_table WHERE artist_key = (%s)"
                    value = (code,)
                    cursor.execute(sql, value)
                    db_connection.commit()
                    return "Artist deleted"
        except Exception as ex:
            return msg_exception(self.delete_artist, ex)
        finally:
            close_db_connection(db_connection)
