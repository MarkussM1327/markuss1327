from flask import Flask, render_template, redirect, url_for, request,session
import os, json
app=Flask(__name__)
def data(file_name):
    if not os.path.exists(file_name):
        with open(file_name,'w',encoding="utf-8") as f:
            json.dump([],f,indent=4,ensure_ascii=False)
    with open(file_name,'r',encoding="utf-8") as f:
        return json.load(f)
def user_exists(username):
    users=data("users.json")
    for i in range(len(users)):
        dict=users[i]
        if dict.get("username")==username:
            return True
        else:
            if i==len(users)-1:
                return False
def password_matches(password):
    users=data("users.json")
    for i in range(len(users)):
        dict=users[i]
        if dict.get("password")==password:
            return True
        else:
            if i==len(users)-1:
                return False
app.secret_key="test"
@app.route("/",methods=["GET","POST"])
def index():
    if request.method=="POST":
        if request.form.get("diff")=="ez":
            session["game_state"]="start"
            session["time"]=20
        elif request.form.get("diff")=="med":
            session["game_state"]="start"
            session["time"]=15
        else:
            session["game_state"]="start"
            session["time"]=10
        return redirect(url_for("index"))
    time=session.get("time")
    if time is None:
        time=15
    return render_template("index.html",data=data("users.json"))
@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        if user_exists(request.form.get("username")):
            if password_matches(request.form.get("password")):
                session["account"]=request.form.get("username")
                session.pop("error",None)
                return redirect(url_for("index"))
            else:
                session["error"]="Wrong password"
        else:
            session["error"]="You're logging in an account that doesn't exist"
    return render_template("login.html")
@app.route("/sign_up",methods=["GET","POST"])
def sign_up():
    if request.method=="POST":
        user=request.form.get("username")
        if not user_exists(user):
            new_data={
                "username":request.form.get("username"),
                "password":request.form.get("password"),
                "time": 0
            }
            all_data=data("users.json")
            all_data.append(new_data)
            with open("users.json",'w',encoding="utf-8") as f:
                json.dump(all_data,f,indent=4,ensure_ascii=False)
            return redirect(url_for("index"))
        else:
            session["error"]="This username is taken"
    return render_template("sign_up.html")
if __name__=="__main__":
    app.run(debug=True)