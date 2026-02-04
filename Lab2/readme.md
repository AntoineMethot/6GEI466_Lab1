# Laboratoire 2 6GEI466

Version Python: 3.12.6

## Description générale
Ce projet est un petit serveur web HTTP en **Python (Flask)** qui sert une page d’accueil contenant un formulaire.  
Lorsque l’utilisateur soumet le formulaire, un appel **AJAX (POST)** est effectué vers la route **`/horoscope`**.  
Le serveur valide les paramètres reçus, calcule le **signe du zodiaque** selon la date, puis retourne une réponse en **JSON** contenant :
- le prénom et le nom
- la date
- le signe du zodiaque
- le nom d’un fichier image associé
- un court texte d’horoscope

Le résultat est ensuite affiché dynamiquement sur la page via **manipulation du DOM** (jQuery).

---

## Démarrage du serveur
Le serveur peut être démarré localement en se plaçant dans le répertoire contenant le fichier `main.py` et en exécutant la commande : `python .\main.py` 
Il est également possible d’utiliser l’extension Python de Visual Studio Code.  
Dans tous les cas, un environnement virtuel doit être configuré et les dépendances doivent être installées à partir du fichier `requirements.txt` à l’aide de la commande : `pip install -r requirements.txt`

## Accès au serveur
Le serveur a été précisé à fonctionner sur le port 8000. Pour y acceder, dans le navigateur il faut inscrire https://localhost:8000 ou https://127.0.0.1:8000 puisque c'est https. Puisque l'application même a crée le certificat, le navigateur avertira que le certificat peut être dangereux.

## Structure des fichiers
project/
├─ main.py
├─ utils.py
├─ templates/
│  ├─ accueil.html
│  └─ erreur404.html
└─ static/
   ├─ js/
   │  ├─ ajax-form.js
   │  └─ datepicker.js
   └─ images/
      ├─ SIGNS.jpg
      ├─ ARIES.png
      ├─ TAURUS.png
      ├─ ...


## Sécurité

Avec la lib `pyopenssl`, il est possible de générer des certificats ssl et utiliser le protocole https. Puisque l'application même a crée le certificat, le navigateur avertira que le certificat peut être dangereux.

Par défaut, Jinja2 applique un échappement HTML automatique lors de l’affichage de variables à l’aide de la syntaxe `{{ }}`, ce qui constitue un premier niveau de protection contre les injections de code. L'ajout de `| e` dans `{{ }}` est redondant, mais démontre explicitement l'échappement HTML.

En complément, une fonction `validate_content()` a été implémentée afin de valider les données saisies dans le formulaire. Cette fonction vérifie notamment :
- la longueur des champs
- l’absence de caractères spéciaux non désirés

Un mécanisme similaire est utilisé pour l’affichage de la route invalide dans le gabarit de l’erreur 404.  
Cependant, cette validation est adaptée afin de permettre la présence de chiffres dans l’URL.  
Une vérification de la longueur est également effectuée afin d’éviter qu’une requête contenant un nombre excessif de caractères ne puisse nuire au serveur.