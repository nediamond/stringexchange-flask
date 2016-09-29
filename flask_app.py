from flask import Flask, render_template, session, request, redirect, url_for
from DAL import DAL

app = Flask(__name__)

# Arbitrary secret key to use Flask.session
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
