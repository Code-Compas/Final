from flask import render_template,request,Flask
from flask import current_app as app
from application.models import *

b=dict()
b["in"]=False
a=0

@app.route("/",methods=["GET","POST"])
def f1():
    if request.method=="GET":
        return render_template("HomePage.html")
    
@app.route("/login.html",methods=["GET","POST"])
def f3():
    if request.method=="GET" and b["in"]==False:
        return render_template("login.html")
    elif request.method=="GET" and b["in"]:
        return render_template("Profile.html",a=b)
    else:
        a=dict(request.form)
        for i in a:
            b[i]=a[i]
        
        if "login" in a:
            return render_template("form.html",a=b)
        else:
            if "submit" in a:
                b["in"]=True
                return render_template("HomePage.html",a=b)
            return render_template("form.html",a=b)