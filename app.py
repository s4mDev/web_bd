import requests
from flask import Flask, render_template, request
import psycopg2
app = Flask(__name__)
conn = psycopg2.connect(database="service_db",
                        user="koorub",
                        password="",
                        host="localhost",
                        port="5432")
cursor = conn.cursor()


@app.route('/login/', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    cursor.execute("SELECT * FROM service.users1 WHERE login=%s AND password=%s", (str(username), str(password)))
    records = list(cursor.fetchall())

    return render_template('account.html', full_name=records[0][1])


@app.route('/login/', methods=['GET'])
def index():
    return render_template('login.html')



if __name__ == '__main__':
    app.run()


