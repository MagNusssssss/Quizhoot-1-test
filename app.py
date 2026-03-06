import sqlite3
from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)


# HAUPTSEITEN


@app.route('/')
def index():
    quizzes = load_quizzes()
    return render_template('home_de.html', quizzes=quizzes)


@app.route('/home_eng')
def homeeng():
    return render_template('home_eng.html')


@app.route('/home_span')
def homespan():
    return render_template('home_span.html')


@app.route('/projekte_de')
def projektede():
    return render_template('projekte_de.html')


@app.route('/projekte_eng')
def projekteeng():
    return render_template('projekte_eng.html')


@app.route('/projekte_span')
def projektespan():
    return render_template('projekte_span.html')


# QUIZ SEITEN


@app.route('/quiz_1_de')
def quiz1():
    return render_template('quiz_1_de.html')


@app.route('/quiz_1_eng')
def quiz1_eng():
    return render_template('quiz_1_eng.html')


@app.route('/quiz_1_span')
def quiz1_span():
    return render_template('quiz_1_span.html')



# ABOUT SEITEN


@app.route('/ueberuns')
def ueberuns():
    return render_template('ueberuns.html')


@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')


@app.route('/sobrenosotras')
def sobrenosotras():
    return render_template('sobrenosotras.html')



# LOGIN / REGISTRIEREN


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/registrieren')
def registrieren():
    return render_template('registrieren.html')


@app.route('/registrarse')
def registrarse():
    return render_template('registrarse.html')



# QUIZ TEST SEITEN


@app.route('/quiz1-1')
def quiz67():
    return render_template('quiz-test-1/quiz1-1.html')


@app.route('/falsch1')
def falsch1():
    return render_template('quiz-test-1/falsch1.html')


@app.route('/richtig1')
def richtig1():
    return render_template('quiz-test-1/richtig1.html')



# DATENBANK


def get_db_connection():
    conn = sqlite3.connect('sqlite_datenbank.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/anmelden', methods=['POST'])
def anmelden():

    conn = get_db_connection()

    items = conn.execute('SELECT * FROM benutzer').fetchall()

    conn.close()

    return render_template('anmelden.html', benutzer=items)



# QUIZ JSON SYSTEM


FILE = "quizzes.json"


if not os.path.exists(FILE):
    with open(FILE, "w") as f:
        json.dump({}, f)


def load_quizzes():
    try:
        with open(FILE) as f:
            return json.load(f)
    except:
        return {}


def save_quizzes(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)


# QUIZ ERSTELLEN


@app.route("/qui1_1_de_erstellen", methods=["GET", "POST"])
def create():

    if request.method == "POST":

        title = request.form["title"]
        question = request.form["question"]

        a = request.form["a"]
        b = request.form["b"]
        c = request.form["c"]

        correct = request.form["correct"]

        quizzes = load_quizzes()

        quizzes[title] = {
            "question": question,
            "a": a,
            "b": b,
            "c": c,
            "correct": correct
        }

        save_quizzes(quizzes)

        return redirect("/")

    return render_template("qui1_1_de_erstellen.html")


#Quiz spielen

@app.route("/quiz/<name>", methods=["GET", "POST"])
def play(name):

    quizzes = load_quizzes()

    if name not in quizzes:
        return "Quiz nicht gefunden"

    quiz = quizzes[name]

    result = None

    if request.method == "POST":

        user_answer = request.form.get("answer")

        if user_answer == quiz["correct"]:
            result = "Richtig!"
        else:
            result = "Falsch!"

    return render_template("play.html", quiz=quiz, name=name, result=result)



# SERVER START


if __name__ == '__main__':
    app.run(debug=True)