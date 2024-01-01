# -*- coding: utf-8 -*-
from flask import Flask
from flask import jsonify
from flask import request
from flask_mysqldb import MySQL

from config import config


class App:
    def __init__(self) -> None:
        # Flask app instantiation
        self.app = Flask(__name__)

        # Mysql database connecion
        self.connectionDB = MySQL(self.app)

        # Configuration of routes
        self.routes()

    def routes(self):
        @self.app.route("/artist")
        def listArtist():
            try:
                cursor = self.connectionDB.connection.cursor()
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
                return jsonify({"Artists": artistsList})

            except Exception as ex:
                return jsonify({"Response": "Exception Error"})

        @self.app.route("/artist/<code>", methods=["GET"])
        def artistDetails(code):
            try:
                cursor = self.connectionDB.connection.cursor()
                sql = "SELECT * FROM artist_table WHERE artist_key = '{0}'".format(code)
                cursor.execute(sql)
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
                    return jsonify(
                        {
                            "Artist": artist,
                        }
                    )
                else:
                    return jsonify({"Response": "Artist not found"})

            except Exception as ex:
                return jsonify({"Response": "Exception Error"})

        @self.app.route("/artist", methods=["POST"])
        def registerArtist():
            try:
                cursor = self.connectionDB.connection.cursor()
                sql = """INSERT INTO hip_hop_database.artist_table (artist_aka, artist_name, artist_dateborn, artist_deathdate, artist_country) VALUES (%s, %s, %s, %s, %s)"""
                value = (
                    request.json["artist_aka"],
                    request.json["artist_name"],
                    request.json["artist_dateborn"],
                    request.json["artist_deathdate"],
                    request.json["artist_country"],
                )
                cursor.execute(sql, value)
                self.connectionDB.connection.commit()

                return jsonify({"Response": "Artist added"})
            except Exception as ex:
                return jsonify({"Response": "Exception Error"})

        @self.app.route("/artist/<code>", methods=["PUT"])
        def updateArtist(code):
            try:
                cursor = self.connectionDB.connection.cursor()
                sql = (
                    "UPDATE artist_table SET artist_aka = (%s) WHERE artist_key = (%s)"
                )
                value = (request.json["artist_aka"], code)
                cursor.execute(sql, value)
                self.connectionDB.connection.commit()
                return jsonify({"Response": "Artist updated"})
            except Exception as ex:
                return jsonify({"Response": "Exception Error"})

        @self.app.route("/artist/<code>", methods=["DELETE"])
        def deleteArtist(code):
            print(code)
            try:
                cursor = self.connectionDB.connection.cursor()
                sql = "DELETE FROM artist_table  WHERE artist_key = (%s)"
                value = (code,)
                cursor.execute(sql, value)
                self.connectionDB.connection.commit()
                return jsonify({"msg": "Artist deleted"})
            except Exception as ex:
                return jsonify({"Response": f"Exception Error: {ex}"})

        @self.app.errorhandler(404)
        def error404(error):
            return "pagina no encontrada 404", 404


if __name__ == "__main__":
    app = App()
    app.app.config.from_object(config["development"])
    app.app.run()
