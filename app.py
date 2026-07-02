from flask import Flask

app = Flask(__name__)

@app.route('/')
def accueil():
    return "Projet Recherche de Mentor"

if __name__ == '__main__':
    app.run(debug=True)
