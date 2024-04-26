# -*- coding: utf-8 -*-
from flask import jsonify
from src.models.artist_repository import ArtistRepository

class ArtistController:
    def __init__(self):
        """Methods for handling requests HTTP (GET, POST, PUT, DELETE)
        """
        self.artist_repository = ArtistRepository()

    def list_artists(self):
        """Manage the GET request to get the list of artists

        Returns:
            dicc: artists data got
        """
        # It is assumed that the "request.method" is "GET"
        response_got = self.artist_repository.list_artists()
        return response_got

    def get_artist(self, artist_name):
        """Manage the request to get  details of the artist

        Args:
            artist_name (str): "Aka" of artist, it server for key for the query
            Example: "SELECT * FROM artist_table WHERE artist_aka = artist_name"        

        Returns:
            Dictionary: artist data got
        """
        # "search" it is an attribute of the element "input" in "navbar.html or the artist name obtained event click in the table row
        # this receives the data necessary to make the request
        response = self.artist_repository.get_artist(artist_name)

        if not response == None:
            return response

    def add_artist(self, data_artist):
        """Manage the POST request to add  new artist

        Returns:
            json: confirmation 'insert' or exception
        """
        response = self.artist_repository.add_artist(data_artist)
    
        if response == "Artist added":
            return response
        else:
            return f"'{data_artist['artist_aka']}' already exists"

    def update_artist(self, code, jsonData):
        # Manage the PUT request to update the details an artist
        expected_response = "Artist updated"
        response = self.artist_repository.update_artist(code, jsonData)
        artist_aka = jsonData["artist_aka"]
        if response == expected_response:
            # response = f"'{artist_aka}': Aka Available"
            response = f"Artist update"
        else:
            response = f"'{artist_aka}': Already exist!"

        return response

    def delete_artist(self, code):
        # Manage the DELETE request to delete an artist
        response = self.artist_repository.delete_artist(code)
        
        return jsonify({"Response": response})
