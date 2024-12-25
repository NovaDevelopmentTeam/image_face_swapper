from flask import Flask, render_template, redirect, url_for, request, session, jsonify

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Dummy-Datenbank für Benutzer
USERS = {"testuser": "password123"}

@app.route("/")
def home():
    return render_template("landing.html", logged_in="user" in session)

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    if username in USERS and USERS[username] == password:
        session["user"] = username
        return jsonify({"success": True})
    return jsonify({"success": False, "message": "Falscher Benutzername oder Passwort."})

@app.route("/register", methods=["POST"])
def register():
    username = request.form.get("username")
    password = request.form.get("password")
    if username in USERS:
        return jsonify({"success": False, "message": "Benutzer existiert bereits."})
    USERS[username] = password
    session["user"] = username
    return jsonify({"success": True})

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("home"))

@app.route("/face-swap")
def face_swap():
    if "user" not in session:
        return jsonify({"error": "Nicht autorisiert"}), 401
    return jsonify({"message": "Face-Swap erfolgreich!"})

if __name__ == "__main__":
    app.run(debug=True)
