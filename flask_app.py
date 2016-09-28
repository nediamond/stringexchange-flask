from flask import Flask, render_template, session, request, redirect, url_for
from random import choice
import MySQLdb


app = Flask(__name__)
app.secret_key = "flippyfloppy"

@app.route('/')
def prompt():
    return render_template('text_submit.html')

@app.route('/submit', methods=['POST'])
def submit():
    session['submission'] = request.form['text_input']
    return redirect(url_for('display'))


@app.route('/display')
def display():
    if 'submission' in session:
        dal = DAL()
        rand_entry = dal.get_random_entry()
        session['result_id'] = rand_entry[0]
        dal.add_entry(session.pop('submission'))
        return render_template('text_display.html', text=rand_entry[1])
    else:
        return "You gotta submit a string to read one!"

@app.route('/decision', methods=['POST'])
def decision():
    if 'result_id' in session:
        result_id = session.pop('result_id')
        if request.form['submit'] == 'Wipe this string from existence.':
          dal = DAL()
          dal.remove_entry(result_id)

    return redirect(url_for('prompt'))

class DAL:
    def __init__(self):
        self.db = MySQLdb.connect(
            host='nediamond.mysql.pythonanywhere-services.com',
            user='nediamond',
            passwd='cheezits',
            db='nediamond$default',
            )

    def get_random_entry(self):
        cursor = self.db.cursor()
        cursor.execute('SELECT * FROM shared_strings')
        result = cursor.fetchall()
        return choice(result)

    def add_entry(self, entry):
        cursor = self.db.cursor()
        # Plz no injection thanks
        cursor.execute('INSERT INTO shared_strings (string) VALUES (%s)',(entry,))
        cursor.execute('INSERT INTO shared_strings_ro (string) VALUES (%s)',(entry,))
        self.db.commit()
        return

    def remove_entry(self, id):
        cursor = self.db.cursor()
        cursor.execute('DELETE FROM shared_strings WHERE id='+str(id))
        self.db.commit()
        return


