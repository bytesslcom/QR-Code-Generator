from flask import Flask, request, render_template, g
import sqlite3

app = Flask(__name__)
DATABASE = 'database.db'

@app.route('/')
def home():
    return '<h2>QR Code App is Running</h2><p>Use a valid /view/&lt;entry_id&gt; URL to see data.</p>'
    
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db:
        db.close()

@app.route('/view/<entry_id>')
def view_entry(entry_id):
    cur = get_db().cursor()
    cur.execute("SELECT title, text, image_url FROM entries WHERE id=?", (entry_id,))
    row = cur.fetchone()
    if row:
        return render_template("view.html", title=row[0], text=row[1], image_url=row[2])
    return "Entry not found", 404

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
