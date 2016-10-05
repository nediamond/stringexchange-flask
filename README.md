# stringexchange-flask

Stringexchange-flask is a Flask-based implementation of the string exchange project.

It accepts string submissions at the root url, then directs the user to /display upon submission, where a previously submitted string is displayed. The user can then choose to "Wipe this string from existence." or "Leave it for posterity!".

To Run:
(pip install -r requirements.txt)
(cd /.../stringexchange-flask)
export FLASK_APP=flask_app.py (Windows: set FLASK_APP=flask_app.py)
flask run
