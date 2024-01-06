# -*- coding: utf-8 -*-
from flask import Flask
from flask import jsonify
from flask import request


class ArtistRepository:
    def __init__(self, connectionDB) -> None:
        self.connectionDB = connectionDB

    def list_artists(self):
        # Logic to get list artists from the database
        try:
            with self.connectionDB.connection.cursor() as cursor:
                sql = "SELECT * FROM artist_table"
                cursor.execute(sql)
                dataGotListArtists = cursor.fetchall()
                artistsList = []

                for row in dataGotListArtists:
                    artist = {
                        "artist_key": row[0],
                        "artist_aka": row[1],
                        "artist_name": row[2],
                        "artist_dateborn": row[3],
                        "artist_deathdate": row[4],
                        "artist_country": row[5],
                    }
                    artistsList.append(artist)
                # Returns artist data in 'json' format
                return artistsList
        except Exception as ex:
            return f"Exception Error: {ex}"

    def get_artist(self, code):
        # logic to get the details the an artist from the database
        try:
            with self.connectionDB.connection.cursor() as cursor:
                sql = "SELECT * FROM artist_table WHERE artist_key = (%s)"
                cursor.execute(sql, (code,))
                dataGotArtist = cursor.fetchone()

                if dataGotArtist != None:
                    artist = {
                        "artist_key": dataGotArtist[0],
                        "artist_aka": dataGotArtist[1],
                        "artist_name": dataGotArtist[2],
                        "artist_dateborn": dataGotArtist[3],
                        "artist_deathdate": dataGotArtist[4],
                        "artist_country": dataGotArtist[5],
                    }
                    # Returns artist data in 'json' format
                    return artist

        except Exception as ex:
            return f"Exception Error: {ex}"

    def add_artist(self):
        # Logic to add a new artist in the database
        try:
            with self.connectionDB.connection.cursor() as cursor:
                sql = """INSERT INTO hip_hop_database.artist_table
                (artist_aka,
                artist_name,
                artist_dateborn,
                artist_deathdate,
                artist_country)
                VALUES (%s, %s, %s, %s, %s)"""
                value = (
                    request.json["artist_aka"],
                    request.json["artist_name"],
                    request.json["artist_dateborn"],
                    request.json["artist_deathdate"],
                    request.json["artist_country"],
                )
                cursor.execute(sql, value)
                self.connectionDB.connection.commit()

                return "Artist added"
        except Exception as ex:
            return f"Exception Error: {ex}"

    def update_artist(self, code):
        # Logic to update the details an artist in the database
        try:
            with self.connectionDB.connection.cursor() as cursor:
                sql = (
                    "UPDATE artist_table SET artist_aka = (%s) WHERE artist_key = (%s)"
                )
                value = (request.json["artist_aka"], (code,))
                cursor.execute(sql, value)
                self.connectionDB.connection.commit()
                return "Artist updated"
        except Exception as ex:
            return f"Exception Error: {ex}"

    def delete_artist(self, code):
        # Logic to delete an artist the database
        try:
            with self.connectionDB.connection.cursor() as cursor:
                sql = "DELETE FROM artist_table  WHERE artist_key = (%s)"
                value = (code,)
                cursor.execute(sql, value)
                self.connectionDB.connection.commit()
                return "Artist deleted"
        except Exception as ex:
            return f"Exception Error: {ex}"


class ArtistController:
    def __init__(self, artist_repository):
        self.artist_repository = artist_repository

    # Methods for handling requests HTTP (GET, POST, PUT, DELETE)
    def list_artists(self):
        # Manage the GET request to get the list of artists
        response = self.artist_repository.list_artists()
        return jsonify({"Artists": response})

    def get_artist(self, code):
        # Manage the  GET request to get  details of the artist
        response = self.artist_repository.get_artist(code)
        if response:
            return jsonify({"Artist": response})
        else:
            return jsonify({"Response": "Artist not found"})

    def add_artist(self):
        # manage the POST request to add  new artist
        data = request.json
        response = self.artist_repository.add_artist()
        return jsonify({"Response": response})

    def update_artist(self, code):
        # Manage the PUT request to update the details an artist
        response = self.artist_repository.update_artist(code)
        return jsonify({"Response": response})

    def delete_artist(self, code):
        # Manage the DELETE request to delete an artist
        response = self.artist_repository.delete_artist(code)
        return jsonify({"Response": response})
