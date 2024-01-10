# -*- coding: utf-8 -*-
from flask import Flask
from flask import jsonify
from src.errors_handling.msg_exception import msg_exception
from src.models.artist_controller import ArtistController


# Flask app instantiation
app = Flask(__name__)


@app.errorhandler(404)
def handle_not_found(e):
    return jsonify({"Error 404": f"{msg_exception(handle_not_found,e)}"}), 404

@app.errorhandler(500)
def handle_internal_server_error(e):
    return jsonify({"Error 500": f"{msg_exception(handle_internal_server_error,e)}"}), 500


if __name__ == "__main__":
    artist_controller = ArtistController()

    # Route configuration using the controller
    app.route("/artists")(artist_controller.list_artists)
    app.route("/artist/<code>", methods=["GET"])(artist_controller.get_artist)
    app.route("/artist", methods=["POST"])(artist_controller.add_artist)
    app.route("/artist/<code>", methods=["PUT"])(artist_controller.update_artist)
    app.route("/artist/<code>", methods=["DELETE"])(artist_controller.delete_artist)

    app.run()
