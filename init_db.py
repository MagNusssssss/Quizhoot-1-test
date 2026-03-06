import sqlite3

# Verbindung herstellen (erzeugt die Datei database.db)
connection = sqlite3.connect('sql.quiz.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

connection.commit()
connection.close()
print("Datenbank erfolgreich initialisiert!")