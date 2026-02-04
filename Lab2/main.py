from flask import Flask
from flask import render_template, request, jsonify
from utils import *

app = Flask(__name__)

# Route principale avec GET
@app.route("/", methods=["GET"])
def accueil():
    Titre = "HOROSCOPE"
    return render_template("accueil.html", titre=Titre)


# Horoscope route - handles AJAX POST request
from flask import jsonify

@app.route("/horoscope", methods=["POST"])
def horoscope():
    prenom_raw = request.form.get("prenom")
    nom_raw = request.form.get("nom")
    date_raw = request.form.get("date")

    # Validation "paramètre manquant"
    if not prenom_raw:
        return jsonify(error="parametre manquant : prenom"), 400
    elif not nom_raw:
        return jsonify(error="parametre manquant : nom"), 400
    elif not date_raw:
        return jsonify(error="parametre manquant : date"), 400
    
    prenom = validate_content(prenom_raw)
    nom = validate_content(nom_raw)
    date = validate_date(date_raw)  # doit retourner "date invalide" si invalide (voir point 2)

    sign = get_zodiac_sign(date)
    data = HOROSCOPES.get(sign, {})
    horoscope_text = data.get("text", "Horoscope non disponible")
    image = data.get("image", "")

    return jsonify(
        prenom=prenom,
        nom=nom,
        date=date,
        sign=sign,
        image=image,
        text=horoscope_text
    )


# Gestion des erreurs 404
@app.errorhandler(404)
def page_not_found(error):
    p = request.path
    if len(p) > 2000:
        p = p[:2000] + "…"
    return render_template("erreur404.html", path=p), 404


if __name__ == "__main__":
    app.run(debug=True, port=8000, ssl_context='adhoc')
