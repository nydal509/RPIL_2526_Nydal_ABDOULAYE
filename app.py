<<<<<<< HEAD
from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mone",
    database="projet_integrateur"
)
cursor = db.cursor()
cursor.execute("SHOW TABLES")
print(cursor.fetchall())
@app.route("/", methods=["GET", "POST"])
def index():

    mentors_compatibles = []
    recherche_effectuee = False

    if request.method == "POST":
        recherche_effectuee = True

        matiere = request.form["matiere"].strip().lower()
        heure = int(request.form["heure"])
        filiere = request.form["filiere"].strip().lower()

        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM mentors")
        mentors = cursor.fetchall()

        for mentor in mentors:
            matieres_mentor = [
                m.strip().lower()
                for m in mentor["matieres"].split(",")
            ]
            score=0
            if (
                matiere in matieres_mentor
                and abs(mentor["disponibilite"] - heure) <= 1
            ):
                score = 80

                if mentor["filiere"].lower() == filiere:
                    score += 20

                mentors_compatibles.append({
                    "nom": mentor["nom"],
                    "matiere_commune": matiere,
                    "disponibilite": mentor["disponibilite"],
                    "format_mentorat": mentor["format_mentorat"],
                    "score": score
                })
                

    mentors_compatibles.sort(
     key=lambda x: x["score"],
     reverse=True
        )

    return render_template(
        "index.html",
        mentors=mentors_compatibles,
        recherche_effectuee=recherche_effectuee
    )

if __name__ == "__main__":
    app.run(debug=True)
=======
from flask import Flask

app = Flask(__name__)

@app.route('/')
def accueil():
    return "Projet Recherche de Mentor"

if __name__ == '__main__':
    app.run(debug=True)
>>>>>>> f2e2a7861e631ac7c6aa7b63baa9f8c5863376fa
