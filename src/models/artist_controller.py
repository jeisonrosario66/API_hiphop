# -*- coding: utf-8 -*-
from flask import Flask
from flask import jsonify
from flask import request
from src.models.artist_repository import ArtistRepository

class ArtistController:
    def __init__(self):
        """Methods for handling requests HTTP (GET, POST, PUT, DELETE)
        """
        self.artist_repository = ArtistRepository()

    def list_artists(self):
        """Manage the GET request to get the list of artists

        Returns:
            json: artists data got
        """
        response_got = self.artist_repository.list_artists()
        return jsonify({"Artists": response_got})

    def get_artist(self, code):
        """Manage the  GET request to get  details of the artist

        Args:
            code (int): Primary key of artist

        Returns:
            Dictionary: artist data got
        """
        response = self.artist_repository.get_artist(code)
        if response:
            return jsonify({"Artist": response})
        else:
            return jsonify({"Response": "Artist not found"})

    def add_artist(self):
        """Manage the POST request to add  new artist

        Returns:
            json: confirmation 'insert' or exception
        """
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
