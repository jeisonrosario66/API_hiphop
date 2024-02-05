# -*- coding: utf-8 -*-
from flask import Flask, request
from flask import jsonify
from flask import Flask, render_template
from src.errors_handling.msg_exception import msg_exception
from src.models.artist_controller import ArtistController

# Flask app instantiation
app = Flask(__name__)
artist_controller = ArtistController()


@app.errorhandler(404)
def handle_not_found(e):
    return jsonify({"Error 404": f"{msg_exception(handle_not_found,e)}"}), 404

@app.errorhandler(500)
def handle_internal_server_error(e):
    return jsonify({"Error 500": f"{msg_exception(handle_internal_server_error,e)}"}), 500

@app.errorhandler(405)
def handle_not_found405(e):
    return jsonify({"Error 405": f"{msg_exception(handle_internal_server_error,e)}"}), 405

# ---------------------------------------------------------------------------------------------
@app.route("/", methods=["GET", "POST"])
def list_artists_show():
    response_got = artist_controller.list_artists()
    if request.method == "GET":
        return render_template("index.html",response = response_got)
    if request.method == "POST":
        return render_template("table.html",response = response_got)
    
    
@app.route("/artist", methods=["POST"])
def artist_show():

    artist_name = request.form["search"]
    if request.method == "POST":
        response_got = artist_controller.get_artist(artist_name)
        if not response_got == None:
            return render_template("table.html",response2 = response_got)
        else:
            return render_template("artist_not_found.html")

@app.route("/artist_update", methods=["PUT"])
def artist_update():
    if request.method == "PUT":
        if request.is_json:
            artist_data = request.get_json()
            artist_key = artist_data["artist_key"]
            response_got = artist_controller.update_artist(artist_key, artist_data)
            return  "response_got"

if __name__ == "__main__":
    app.run()
