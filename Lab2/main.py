from flask import Flask
from flask import render_template, request, abort
import re

app = Flask(__name__)

# Route principale avec GET and POST
@app.route("/", methods=["GET", "POST"])
def accueil():
    titre = "Page d’accueil"

    if request.method == "POST":
        prenom = validate_content(request.form.get("prenom", ""))
        nom = validate_content(request.form.get("nom", ""))
        date = validate_date(request.form.get("date", ""))
        return render_template("accueil.html", titre=titre, soumis=True, prenom=prenom, nom=nom, date=date)

    return render_template("accueil.html", titre=titre, soumis=False)

# Gestion des erreurs 404
@app.errorhandler(404)
def page_not_found(error):
    p = request.path
    if len(p) > 2000:
        p = p[:2000] + "…"
    return render_template("erreur404.html", path=p), 404


def validate_content(s: str) -> str:
    # Remove whitespace
    s = (s or "").strip()
    # Max 50 char limit
    if not (1 <= len(s) <= 50):
        abort(400, "Invalid length")
    # Accept only letters and what would be in a name
    if not re.fullmatch(r"[A-Za-zÀ-ÖØ-öø-ÿ '\-]+", s):
        abort(400, "Invalid characters")
    return s

def validate_date(s: str) -> str:
    # Remove whitespace
    s = (s or "").strip()
    # Accept date format MM/DD/YYYY from jQuery datepicker
    if not re.fullmatch(r"\d{2}/\d{2}/\d{4}", s):
        abort(400, "Invalid date format")
    return s

if __name__ == "__main__":
    app.run(debug=True, port=8000)
