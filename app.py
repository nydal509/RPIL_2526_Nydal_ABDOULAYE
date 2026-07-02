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

    if request.method == "POST":
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

            if matiere in matieres_mentor:
                score = 50

                if abs(mentor["disponibilite"] - heure) <= 1:
                    score += 30

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
        mentors=mentors_compatibles
    )


if __name__ == "__main__":
    app.run(debug=True)