from flask import request, jsonify
from . import main

from socketio import Client

clientio = Client()

@main.route('/',methods=['GET','POST'])
def index():
    """ main form """
    return jsonify(hello = 'world')


@main.route('/connect',methods=['GET'])
def connect_socket():
    """connect to the server socket"""
    try:
        clientio.connect("http://localhost:4000")
        return "Socket client connected!", 200
    except Exception as e:
        return str(e), 500