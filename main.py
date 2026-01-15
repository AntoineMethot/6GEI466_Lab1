from flask import Flask,send_from_directory

app = Flask(__name__)

# Route principale
@app.route("/")
def accueil():
    return send_from_directory("static", "accueil.html")

# Retourne la page correspondante dans static
@app.route("/static/<name>")
def static_html(name):
    filename = f"{name}.html"
    return send_from_directory("static", filename)

# Gestion des erreurs 404
@app.errorhandler(404)
def page_not_found(error):
    return send_from_directory("static", "erreur404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)
