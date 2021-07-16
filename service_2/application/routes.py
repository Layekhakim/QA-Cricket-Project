from application import app
from flask import request, Response
import random

@app.route("/player", methods=["GET"])
def get_player():
    players = ["Stokes", "Shakib", "Smith"]
    return Response(str(random.choice(players)), mimetype='text/plain')

