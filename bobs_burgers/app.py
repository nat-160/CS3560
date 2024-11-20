from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from sqlalchemy import ForeignKey, text
from flask_sqlalchemy import SQLAlchemy
from classes import *
from alchemy import Alchemy
from .order_operations import orders
from .account_operations import account
from Globals.input_validation import InputValidation
from datetime import datetime

app = Flask(__name__)
app.config['SESSION_COOKIE_PATH'] = '/'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://root:admin@localhost/restaurant"
app.secret_key = "secret key"

# REGSITER BLUEPRINTS HERE
app.register_blueprint(orders)
app.register_blueprint(account)

db = SQLAlchemy(app)


def get_db_connection():
  engine = db.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
  connection = engine.raw_connection()
  return connection


@app.route("/")
def home():
  try:
    if session['customer']:
      validUser = db.session.query(Customer).filter_by(customer_id=session['customer']).first()
      return render_template('welcome.html', user=validUser.customerName)
  except KeyError:
    print("session has not been created yet")
  try:
    session['errors']
  except KeyError:
    session['errors'] = []
  errors = session['errors']
  session.pop('errors')
  return render_template('sign-in.html', errors=errors)

@app.route("/setupDB")
def setup_DB():

  conn = get_db_connection()
  cur = conn.cursor()

  # execute a command: this creates a new table
  cur.execute('DROP TABLE IF EXISTS customer;')
  cur.execute('CREATE TABLE customer ('
              'customer_id SERIAL PRIMARY KEY,'
              'password varchar(128) DEFAULT NULL,'
              'customerName text,'
              'address text,'
              'phoneNumber VARCHAR,'
              'email text);')

  conn.commit()
  cur.close()
  conn.close()
  return render_template("sign-in.html")


@app.route('/welcome')
def index():
  books = db.session.query(Customer).filter_by(customer_id = 1).first().customerName
  print(books)
  return render_template('welcome.html', user=books)


if __name__ == '__main__':
  app.run(debug=True)
