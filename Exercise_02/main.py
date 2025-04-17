from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import contextlib

app = Flask(__name__)

# Tietokantayhteyden hallinta context-managerilla
@contextlib.contextmanager
def connect():
    conn = sqlite3.connect('users.sqlite')
    yield conn
    conn.close()

# Alustetaan tietokanta, jos taulu puuttuu
def initialize_database():
    with connect() as con:
        cur = con.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS departments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        ''')
        con.commit()

# Haetaan kaikki osastot tietokannasta
def _get_departments(conn):
    cur = conn.cursor()
    cur.execute('SELECT * FROM departments')
    rows = cur.fetchall()
    return [{'id': row[0], 'name': row[1]} for row in rows]

# -------------------------------------------------------------------------------------------------------------

# Näytetään lista osastoista
@app.route('/departments', methods=['GET'])
def get_departments():
    with connect() as con:
        departments = _get_departments(con)

        # lisää tähän puuttuvat osat, jotta saat osastot listattua html-sivulle
        return render_template('departments/index.html', departments=departments)

# -------------------------------------------------------------------------------------------------------------

# käyttäjien lisäyksen formin koodi
@app.route('/departments/new', methods=['GET'])
def new_department():
    with connect() as con:
        # lisää tähän puuttuva koodi, jotta formin lähettäminen selaimelle onnistuu
        return render_template('departments/new.html', error=None)

# koodi joka lisää rivin tietokantaan
@app.route('/departments/new', methods=['POST'])
def add_department():
    # HUOM!!!!! Muista, että _body-muuttujassa olevat avaimet vastaavat HTML-formin name-attribuutteja
    _body = request.form
    with connect() as con:
        try:
            cur = con.cursor()
            cur.execute('INSERT INTO departments (name) VALUES (?)',
                        # eli jotta 'name'-avain löytyy _bodysta, HTML-formissa osaston lisäysformilla p
                        # pitää osaston nimen tekstikentän name-attribuutti olla arvoltaan name
                        (_body.get('name'), ))
            con.commit()
            # kun osasto on lisätty tietokantaan, ohjataan selain takaisin osastojen listauksen sivulle
            # lisää puuttuva koodi tähän
            return redirect(url_for('get_departments'))  # Palataan listaukseen

        except Exception as e:
            con.rollback()
            # jos tulee virhe, haetaan departmentit uudelleen ja näytetään lisäksi virhe käyttäjälle
            # lisää puuttuvat koodit tähän
            return render_template('departments/new.html', error=str(e))

# -------------------------------------------------------------------------------------------------------------

# Käsitellään osaston poisto
@app.route('/departments/delete', methods=['POST'])
def delete_department():
    _body = request.form
    with connect() as con:
        try:
            dep_id = int(_body.get('department_id'))
            cur = con.cursor()
            cur.execute('DELETE FROM departments WHERE id = ?', (dep_id,))
            con.commit()
        except:
            con.rollback()
    return redirect(url_for('get_departments'))

# -------------------------------------------------------------------------------------------------------------

# Sovellus käynnistetään tästä
if __name__ == '__main__':
    initialize_database()  # Alustaa tietokannan: luo departments-taulun, jos sitä ei vielä ole
    app.run(port=5001, debug=True)  # Käynnistää Flask-sovelluksen paikallisessa palvelimessa portissa 5001 debug-tilassa

