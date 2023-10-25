from flask import Flask, render_template, jsonify, request, session
from model import connect_to_db , db, User, Reservation
import crud
from datetime import datetime
import os


app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_KEY')


@app.route("/login")
def login():
    """Show login page."""
    
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def check_login():
    """ Checks user's email and password. Returns JSON, status error or success """
    email = request.get("email")
    password = request.get("password")
    if crud.check_user_login(email, password):
        return jsonify({"status": "success"})
    return jsonify({"status": "error"})


@app.route("/")
def homepage():
    """Show index page or login page if user not loged in."""

    user = session.get('user_id')
    print("Books user: ", session.get('user_id'))
    if user:
        return render_template("index.html")
    else:
        return render_template("login.html")