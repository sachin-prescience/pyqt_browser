from flask import Flask, render_template,request
from controllers.api_Controller_1 import resp
from controllers.login_Controller import isLogin

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login",methods=['GET'])
def login():
    params=request.args
    u_name=params.get('username')
    p_name=params.get('password')
    login = isLogin(u_name,p_name)
    if login:
        return "Login Success"
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/table_1")
def table_page_1():
    return render_template("table_1.html",response=resp,headers=resp[0].keys())


if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.run(port="8080", host="0.0.0.0", debug=True)
