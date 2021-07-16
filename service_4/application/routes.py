from application import app 
from flask import request, Response

@app.route("/runs", methods=["POST"])
def runs():
    player = request.json["player"]
    team = request.json["team"]
    
    
    if player == "Flintoff":
        message="century scored"
    elif player == "Smith":
        if team == "Pakistan":
            message="out for a duck"
        else:
            message="half a century"
    elif player == "Stokes":
        if team == "South Africa" or team == "Bangladesh":
            message="century scored"
        else:
            message="out for a duck"
    elif player == "Shakib":
        if team == "England":
            message="double hundred"
        else:
            message="out for a duck"       
    return Response(message, mimetype='text/plain')