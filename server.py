from flask import Flask, render_template, jsonify, request, session, redirect
from model import connect_to_db , db, User, Reservation
import crud
from datetime import datetime, time
import os
from dateutil import parser


app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_KEY')


@app.route("/login")
def login():
    """Show login page."""
    
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def check_login():
    """Checks user's email and password. Redirects to index page if credentials are correct."""

    email = request.form.get("email")
    password = request.form.get("password")
    if crud.check_user_login(email, password):
        session['user_id'] = email
        return redirect("/")
    return render_template("login.html", incorrect=True)


@app.route("/")
def homepage():
    """Show index page or login page if user not loged in."""

    user = session.get('user_id')
    print("User: ", user)
    if user:
        return render_template("index.html")
    else:
        return redirect("/login")
    

@app.route("/api/submit_form", methods=["POST"])
def check_date():
    """Checks user's input, date and time"""
    data = request.get_json()
    day = data.get("day")
    parsed_day = parser.parse(day)
    
    new_datetime = datetime.combine(parsed_day.date(), time(14,0))
    
    start_time = data.get("start")
    end_time = data.get("end")
    print(data)
    if start_time and end_time:
        time_list = crud.get_time(start_time, end_time)
        print(time_list)
      
    return jsonify({ "status": "success" })


if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True, host='127.0.0.1')