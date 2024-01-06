# -*- coding: utf-8 -*-
from flask import Flask
from flask import jsonify
from flask import request
from flask_mysqldb import MySQL

from config import config
from src.models.artist_controller import ArtistController
from src.models.artist_controller import ArtistRepository


# Flask app instantiation
app = Flask(__name__)


@app.errorhandler(404)
def handle_not_found(e):
    return jsonify({"error": "Not Found"}), 404


if __name__ == "__main__":
    connectionDB = MySQL(app)
    artist_repository = ArtistRepository(connectionDB)
    artist_controller = ArtistController(artist_repository)

    # Route configuration using the controller
    app.route("/artists")(artist_controller.list_artists)
    app.route("/artist/<code>", methods=["GET"])(artist_controller.get_artist)
    app.route("/artist", methods=["POST"])(artist_controller.add_artist)
    app.route("/artist/<code>", methods=["PUT"])(artist_controller.update_artist)
    app.route("/artist/<code>", methods=["DELETE"])(artist_controller.delete_artist)

    app.config.from_object(config["development"])
    app.run()
