from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "playzarmy_secret_key"

# Admin login details
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "playzarmy123"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session["admin"] = True
            return redirect(url_for("admin"))
        else:
            error = "❌ Wrong Username or Password"

    return render_template("login.html", error=error)

@app.route("/admin")
def admin():
    if not session.get("admin"):
        return redirect(url_for("login"))
    return render_template("admin.html")

@app.route("/logout")
def logout():
    session.pop("admin", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
