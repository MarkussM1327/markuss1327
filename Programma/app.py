from flask import Flask, render_template, redirect, url_for, request, session
import os
import json
import random
import time

trailer_list = []
base_dir = os.path.dirname(os.path.abspath(__file__))
folder_path = os.path.join(base_dir, 'static', 'trailers')
for filename in os.listdir(folder_path):
    if os.path.isfile(os.path.join(folder_path, filename)):
        trailer_list.append(filename)
app = Flask(__name__)
def data(file_name):
    # Load data from a JSON file, creating an empty list if the file doesn't exist.

    if not os.path.exists(file_name):
        with open(file_name, 'w', encoding="utf-8") as f:
            json.dump([], f, indent=4, ensure_ascii=False)
    with open(file_name, 'r', encoding="utf-8") as f:
        return json.load(f)
def user_exists(username):
    # Check if a user exists in the users.json file.

    users = data("users.json")
    for i in range(len(users)):
        user_dict = users[i]
        if user_dict.get("username") == username:
            return True
        else:
            if i == len(users) - 1:
                return False
def user_i(username):
    # Get the index of a user in the users.json file.

    users = data("users.json")
    for i in range(len(users)):
        user_dict = users[i]
        if user_dict.get("username") == username:
            return i
        else:
            if i == len(users) - 1:
                return None
def password_matches(password):
    # Check if the given password matches any user's password in users.json.

    users = data("users.json")
    for i in range(len(users)):
        user_dict = users[i]
        if user_dict.get("password") == password:
            return True
        else:
            if i == len(users) - 1:
                return False
app.secret_key = "!!!DonQuixoteDeLaMancha!!!"
@app.route("/", methods=["GET", "POST"])
def index():
    # Main route for the game. Handles game logic, difficulty selection, guessing, and scoring.
    session.pop("login_error", None)
    session.pop("signup_error", None)
    if session.get("trailers") is None:
        session["trailers"] = random.sample(trailer_list, k=5)
    if session.get("users_guess") is None:
        session["users_guess"] = []
    if request.method == "POST":
        # Handle difficulty selection and game start
        if request.form.get("btn") == "ez":
            session["start_time"] = time.time()
            trailers = random.sample(trailer_list, k=5)
            session["trailers"] = trailers
            session.pop("correct", None)
            session.pop("penalty", None)
            session["new_best"] = False
            session["show_results"] = False
            session["users_guess"].clear()
            session["guess_num"] = 0
            session["game_state"] = "start"
            session["time"] = 20
            session["start_time"] = time.time()
        elif request.form.get("btn") == "med":
            session["start_time"] = time.time()
            trailers = random.sample(trailer_list, k=5)
            session["trailers"] = trailers
            session["trailers"] = trailers
            session.pop("correct", None)
            session.pop("penalty", None)
            session["new_best"] = False
            session["show_results"] = False
            session["users_guess"].clear()
            session["guess_num"] = 0
            session["game_state"] = "start"
            session["time"] = 15
            session["start_time"] = time.time()
        elif request.form.get("btn") == "hard":
            session["start_time"] = time.time()
            trailers = random.sample(trailer_list, k=5)
            session["trailers"] = trailers
            session["trailers"] = trailers
            session.pop("correct", None)
            session.pop("penalty", None)
            session["new_best"] = False
            session["show_results"] = False
            session["users_guess"].clear()
            session["guess_num"] = 0
            session["game_state"] = "start"
            session["time"] = 10
        elif request.form.get("btn") == "guess":
            # Process user's guess
            session["users_guess"].append(request.form.get("guess"))
            session["guess_num"] += 1
            if session["guess_num"] == 5:
                # Calculate score after all guesses
                end=time.time()
                session["guess_num"]=0
                correct=0
                penalty_sec=0
                for trailer,guess in zip(session["trailers"], session["users_guess"]):
                    if trailer.replace(".mp4","")==guess:
                        correct+=1
                # Penalty based on number of correct guesses
                if correct==0:
                    penalty_sec=75
                elif correct==1:
                    penalty_sec=50
                elif correct==2:
                    penalty_sec=30
                elif correct == 3:
                    penalty_sec = 15
                elif correct == 4:
                    penalty_sec = 5
                else:
                    penalty_sec = 0
                session["show_results"] = True
                session["correct"] = correct
                session["penalty"] = penalty_sec
                # Calculate total time with penalty
                t = (end - session["start_time"]) + penalty_sec
                total_ms = int(round(t * 1000))
                m = total_ms // 60000
                s = (total_ms % 60000) // 1000
                ms = total_ms % 1000
                m = f"{m:02d}"
                s = f"{s:02d}"
                ms = f"{ms:03d}"
                session["guess_time"] = f"{m}:{s}:{ms}"
                # Update user best time if logged in
                if session.get("account", "Guest") != "Guest":
                    time_ms = int(m) * 60000 + int(s) * 1000 + int(ms)
                    all_data = data("users.json")
                    i = user_i(session["account"])
                    if all_data[i]["time"] == 0:
                        all_data[i]["time"] = time_ms
                        with open("users.json", 'w', encoding="UTF-8") as f:
                            json.dump(all_data, f, indent=4, ensure_ascii=False)
                    else:
                        if all_data[i]["time"] > time_ms:
                            session["new_best"] = True
                            all_data[i]["time"] = time_ms
                            with open("users.json", 'w', encoding="UTF-8") as f:
                                json.dump(all_data, f, indent=4, ensure_ascii=False)
                session.pop("game_state", None)
            return redirect(url_for("index"))
        elif request.form.get("btn") == "logout":
            session.pop("show_results", None)
            session.pop("account", None)
        elif request.form.get("btn") == "close_modal":
            session.pop("show_results", None)
        return redirect(url_for("index"))
    t = session.get("time", 15)
    ordered_data = sorted(data("users.json"), key=lambda x: x["time"], reverse=False)
    ordered_data = [user for user in ordered_data if user.get("time", 0) != 0]
    return render_template("index.html", data=ordered_data,
                           trailer=f"static/trailers/{session.get('trailers', random.sample(trailer_list, k=5))[session.get('guess_num', 0)]}#t=0,{t}",
                           trailer_list=trailer_list)
@app.route("/login", methods=["GET", "POST"])
def login():
    # Handle user login. Validates username and password, sets session if successful.

    session.pop("signup_error", None)
    if request.method == "POST":
        user = request.form.get("username")
        password = request.form.get("password")
        if user_exists(user):
            if password_matches(password):
                session["account"] = user
                session.pop("login_error", None)
                return redirect(url_for("index"))
            else:
                session["login_error"] = "Wrong password"
        else:
            session["login_error"] = "You're logging in an account that doesn't exist"
    return render_template("login.html")
@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    # Handle user sign up. Creates new user if username is available.

    session.pop("login_error", None)
    if request.method == "POST":
        user = request.form.get("username")
        if not user_exists(user):
            new_data = {
                "username": user,
                "password": request.form.get("password"),
                "time": 0
            }
            all_data = data("users.json")
            all_data.append(new_data)
            with open("users.json", 'w', encoding="utf-8") as f:
                json.dump(all_data, f, indent=4, ensure_ascii=False)
            session["account"] = user
            session.pop("signup_error", None)
            return redirect(url_for("index"))
        else:
            session["signup_error"] = "This username is taken"
    return render_template("sign_up.html")
if __name__ == "__main__":
    # Run the Flask app in debug mode
    app.run()