from flask import Flask, render_template, redirect, url_for, request,session
import os, json,random,time,math
trailer_list=[]
folder_path = 'static/trailers'
for filename in os.listdir(folder_path):
    if os.path.isfile(os.path.join(folder_path, filename)):
        trailer_list.append(filename)
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
def user_i(username):
    users=data("users.json")
    for i in range(len(users)):
        dict=users[i]
        if dict.get("username")==username:
            return i
        else:
            if i==len(users)-1:
                return None
def password_matches(password):
    users=data("users.json")
    for i in range(len(users)):
        dict=users[i]
        if dict.get("password")==password:
            return True
        else:
            if i==len(users)-1:
                return False
app.secret_key="!!!DonQuixoteDeLaMancha!!!"
@app.route("/",methods=["GET","POST"])
def index():
    session.pop("trailer",None)
    if session.get("trailers")==None:
        session["trailer"]=random.sample(trailer_list, k=5)
    if session.get("account")==None:
        session["account"]="guest"
    if request.method=="POST":
        if request.form.get("btn")=="ez":
            trailers=random.sample(trailer_list,k=5)
            session["guess_num"]=0
            session["trailers"]=trailers
            session["game_state"]="start"
            session["time"]=20
            session["start_time"]=time.time()
        elif request.form.get("btn")=="med":
            trailers=random.sample(trailer_list,k=5)
            session["guess_num"]=0
            session["trailers"]=trailers
            session["game_state"]="start"
            session["time"]=15
            session["start_time"]=time.time()
        elif request.form.get("btn")=="hard":
            trailers=random.sample(trailer_list,k=5)
            session["guess_num"]=0
            session["trailers"]=trailers
            session["game_state"]="start"
            session["time"]=10
            session["start_time"]=time.time()
        elif request.form.get("btn")=="guess":
            session["users_guess"]=request.form.get("guess")
            if session["users_guess"]==session["trailers"]:
                session["is_correct"]=True
                end=time.time()
                t=end-session["start_time"]
                if t>=60:
                    while t>=60:
                        m=math.floor(t/60)
                        if len(str(m))==1:
                            m=str("0"+str(m))
                else:
                    m="00"
                s=math.floor(t)
                if len(str(s))==1:
                    s=str("0"+str(s))
                ms=round(t*1000)
                if len(str(ms))>3:
                    ms=ms/10**len(str(ms))
                    ms=round(ms*1000)
                session["guess_time"]=f"{m}:{s}:{ms}" 
                if session.get("account")!="guest":
                    time_ms=int(m)*60+int(s)*1000+ms
                    all_data=data("users.json")
                    i=user_i(session["account"])
                    if all_data[i]["time"]==0:
                        all_data[i]["time"]=time_ms
                        with open("users.json",'w',encoding="UTF-8") as f:
                            json.dump(all_data,f,indent=4,ensure_ascii=False)
                    else:
                        if all_data[i]["time"]>time_ms:
                            all_data[i]["time"]=time_ms
                            with open("users.json",'w',encoding="UTF-8") as f:
                                json.dump(all_data,f,indent=4,ensure_ascii=False)
                else:
                    session["wrong_guess"]=True
        elif request.form.get("btn")=="close":
            session.pop("guess_time",None)
            session["is_correct"]=False
        return redirect(url_for("index"))
    t=session.get("time",15)
    ordered_data=sorted(data("users.json"),key=lambda x: x["time"],reverse=False)
    return render_template("index.html",data=ordered_data,
                           trailer=f"static/trailers/{session.get("trailers")[0]}#t=0,{t}",
                           trailer_list=trailer_list)
@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        user=request.form.get("username")
        password=request.form.get("password")
        if user_exists(user):
            if password_matches(password):
                session["account"]=user
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
                "username":user,
                "password":request.form.get("password"),
                "time": 0
            }
            all_data=data("users.json")
            all_data.append(new_data)
            with open("users.json",'w',encoding="utf-8") as f:
                json.dump(all_data,f,indent=4,ensure_ascii=False)
            session["account"]=user
            return redirect(url_for("index"))
        else:
            session["error"]="This username is taken"
    return render_template("sign_up.html")
if __name__=="__main__":
    app.run(debug=True)