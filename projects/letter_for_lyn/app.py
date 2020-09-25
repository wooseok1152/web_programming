from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)


@app.route('/')
def home():

    return render_template("index.html")

@app.route("/login_process", methods = ["POST"])
def login_process():

    code = request.form["code"]
    if code == "lynlyn":

        return redirect(url_for("letter"))
    
    else:

        return redirect(url_for("home"))

@app.route("/letter")
def letter():

    return render_template("letter.html")


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

    
