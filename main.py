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

@app.route("/", methods=["GET"])
def list_artists_show():
    print(request.method)
    if request.method == "GET":
        response_got = artist_controller.list_artists()
        return render_template("index.html",response = response_got)


@app.route("/artist_ajax", methods=["POST"])
def name():
    if request.method == "POST":
        response_got = artist_controller.get_artist()
        if not response_got == None:
            return render_template("table.html",response2 = response_got)
        else:
            return render_template("artist_not_found.html")

if __name__ == "__main__":

    # Route configuration using the controller
    # app.route("/artists",methods=["GET","POST"])(artist_controller.list_artists)
    app.route("/api/artist", methods=["POST"])(artist_controller.get_artist)

    # app.route("/artist", methods=["POST"])(artist_controller.add_artist)
    
    # app.route("/artist/<code>", methods=["PUT"])(artist_controller.update_artist)
    # app.route("/artist/<code>", methods=["DELETE"])(artist_controller.delete_artist)

    app.run()
