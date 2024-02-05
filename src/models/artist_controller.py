# -*- coding: utf-8 -*-
from flask import Flask
from flask import jsonify
from flask import request
from src.models.artist_repository import ArtistRepository
from flask import Flask, render_template

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

    def add_artist(self):
        """Manage the POST request to add  new artist

        Returns:
            json: confirmation 'insert' or exception
        """
        response = self.artist_repository.add_artist()
        return jsonify({"Response": response})

    def update_artist(self, code, jsonData):
        # Manage the PUT request to update the details an artist
        response = self.artist_repository.update_artist(code, jsonData)
        return response

    def delete_artist(self, code):
        # Manage the DELETE request to delete an artist
        response = self.artist_repository.delete_artist(code)
        
        return jsonify({"Response": response})
