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
    # "requested_with" will get the header from the request
    requested_with = request.headers.get('X-Requested-With')
    response_got = artist_controller.list_artists()

    if request.method == "GET" :
        print("xx")
        if requested_with == "popstate_event": # Value of header
            return render_template("table.html",response = response_got)
        else:
            return render_template("index.html",response = response_got)
    elif request.method == "POST":
        return render_template("table.html",response = response_got)
    
@app.route("/artist/<code>", methods=["GET"])
def artist_show2(code):
    """_summary_

    Args:
        code (str): this content a argument passed by url. Ej "artist/artis_name"
        It is received in this format "artist_name", then it is replace "_" -> " "
        Resulting in "artist name" for make query at the database


    Returns:
       template flask
    """
    requested_with = request.headers.get('X-Requested-With')

    artist_name = code
    for i in code:
        if i == "_":
            artist_name = artist_name.replace("_", " ")

    response_got = artist_controller.get_artist(artist_name)

    if request.method == "GET":
        if requested_with == "popstate_event":
            # If the header "X-Requested-With" is equal "popstate_event"
            # Return only the template "table.html"
            return render_template("table.html",response2 = response_got)
            
        else:
            if not response_got == None:
                return render_template("artist_table.html",response3 = response_got)
            else:
                return render_template("artist_not_found.html")

@app.route("/artist", methods=["POST"])
def artist_show():
    if request.method == "POST":
        artist_name = request.form["search"]
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
