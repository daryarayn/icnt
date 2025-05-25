import psycopg2
import os

from flask import Flask, render_template, redirect, url_for, flash, request, jsonify
from dotenv import load_dotenv

load_dotenv()

connection = {
	'dbname': os.getenv('DB_NAME'),
	'user': os.getenv('DB_USER'),
	'password': os.getenv('DB_PASSWORD'),
	'host': os.getenv('DB_HOST'),
	'port': os.getenv('DB_PORT')
}

app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = '170dcfee-6d7c-416f-a2b5-25788465f54a'


def get_teachers():
	conn = psycopg2.connect(**connection)
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM teachers")
	teachers = cursor.fetchall()
	conn.close()
	return teachers


def get_news():
	conn = psycopg2.connect(**connection)
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM news")
	news = cursor.fetchall()
	conn.close()
	return news

@app.route('/')
def home():
	return redirect(url_for('info'))


@app.route('/info')
def info():
	return render_template('info.html')


@app.route('/teachers')
def teachers():
	teachers = get_teachers()
	return render_template('teachers.html', teachers=teachers)


@app.route('/news')
def news():
	news = get_news()
	return render_template('news.html', news=news)


@app.route('/contacts')
def contacts():
	return render_template('contacts.html')


if __name__ == '__main__':
	app.run(debug=True, port=5000)
