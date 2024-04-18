# -*- coding: utf-8 -*-
import os
from flask import Flask, request, session
from flask import jsonify
from flask import Flask, render_template
from src.errors_handling.msg_exception import msg_exception
from src.models.artist_controller import ArtistController
from src.models.login_controller import LoginController

# Flask app instantiation
app = Flask(__name__)
# for flask session
app.secret_key = os.urandom(24)

artist_controller = ArtistController()
login_controller = LoginController()

@app.errorhandler(404)
def handle_not_found(e):
    error404 = jsonify({"Error 404": f"{msg_exception(handle_not_found,e)}"}), 404
    return render_template("not_found.html",error404 = error404)

@app.errorhandler(405)
def handle_not_found405(e):
    error405 = jsonify({"Error 405": f"{msg_exception(handle_internal_server_error,e)}"}), 405
    return render_template("not_found.html",error405 = error405)

@app.errorhandler(500)
def handle_internal_server_error(e):
    error500 = jsonify({"Error 500": f"{msg_exception(handle_internal_server_error,e)}"}), 500
    return render_template("not_found.html",error500 = error500)

@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')

# ---------------------------------------------------------------------------------------------
@app.route("/", methods=["GET", "POST"])
def list_artists_show():
    """
    It show a list with  all artist 

    Returns:
       template flask
    """
    # "requested_with" will get the header from the request
    requested_with = request.headers.get('X-Requested-With')
    response_got = artist_controller.list_artists()

    if request.method == "GET" :
        if requested_with == "popstate_event": # Value of header
            return render_template("table.html",response = response_got)
        else:
            return render_template("index.html",response = response_got)
    elif request.method == "POST":
        return render_template("table.html",response = response_got)
    
@app.route("/artist/<code>", methods=["GET"])
def artist_show(code):
    """
    Args:
        code (str): this content a argument passed by url. Ej "artist/artis_name"
        It is received in this format "artist_name", then it is replace "_" -> " "
        Resulting in "artist name" for make query at the database

    Returns:
       template flask
    """
    requested_with = request.headers.get('X-Requested-With')

    artist_name = code
    # This block will format the "artist name" a format requered
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
                return render_template("artist_table.html",response2 = response_got)
            else:
                return render_template("artist_not_found.html", artist_name = artist_name)

@app.route("/artist", methods=["POST"])
def artist_show2():
    if request.method == "POST":
        artist_name = request.get_json()
        artist_name = artist_name["search"]
        response_got = artist_controller.get_artist(artist_name)
        if not response_got == None:
            return render_template("table.html",response2 = response_got)
        else:
            return render_template("artist_not_found.html", artist_name = artist_name)

@app.route("/artist_update", methods=["PUT"])
def artist_update():
    """
    Returns:
        confirm data update
    """
    if request.method == "PUT":
        if request.is_json:
            artist_data = request.get_json()
            artist_key = artist_data["artist_key"]
            
            response_got = artist_controller.update_artist(artist_key, artist_data)
            return response_got
        
@app.route("/add_artist", methods=["GET", "POST"])
def add_artist():
    """Add a new artist
    """
    if session.get('user'):
        requested_with = request.headers.get('X-Requested-With')
    
        if request.method == "GET":
            if requested_with == "popstate_event":
                artist_name = str(request.args.keys())
                artist_name = artist_name.replace("dict_keys(['{", "")
                artist_name = artist_name.replace('"artistData":"', "")
                artist_name = artist_name.replace("'])", "")
                artist_name = artist_name.replace('"}', "")
                response_got = artist_controller.get_artist(artist_name)
                if response_got != None:
                    return f"'{artist_name}' already exists"
                else:
                    return f"'{artist_name}' available"
                
            else:
                return render_template("add_artist.html")
            

        elif request.method == "POST":
            new_artist_data = request.json["artistData"]
            response_got = artist_controller.add_artist(new_artist_data)
            return response_got
    else:
        return render_template("session_not_active.html")
    
@app.route("/login", methods=["GET"])
def login():
    return render_template("login.html")

@app.route("/login_verification", methods=["POST"])
def login_verification():
    """This function will verify if the username and password exist in the database

    Returns:
        template: Session activated or not
    """
    login_data = request.get_json()
    login_data = login_data["search"]

    login_data_user = login_data["user"]
    login_data_pass = login_data["pass"]

    #access_login return false or true
    access_login = login_controller.login_verify(login_data_user,login_data_pass)


    response_got = artist_controller.list_artists()
    print(access_login)
    if access_login == 1:
        session["user"] = login_data_user
        return render_template("index.html",response = response_got)
    else:
        return ""
    
@app.route("/logout", methods=["GET"])
def logout():
    response_got = artist_controller.list_artists()
    session.pop('user', None)
    return render_template("index.html",response = response_got)

    
if __name__ == "__main__":
    # Allows external connection in development
    app.run(host="0.0.0.0")