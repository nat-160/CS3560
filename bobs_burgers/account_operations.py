from flask import Blueprint, render_template, redirect, request, session, current_app, url_for
from flask_session import Session
from sqlalchemy import text
from Globals.db_connect import engine
from Globals.input_validation import InputValidation
from alchemy import Alchemy
from classes import Customer

sql = Alchemy(engine)
sess = sql.session

account = Blueprint('account_operations', __name__, static_folder='static', template_folder='templates')

@account.route("/new_account", methods=['POST'])
def create_new_account():
  errors = list()
  name = request.form['fname'] + " " + request.form['lname']
  email = request.form['email']
  phone = request.form['pNumber']
  psswd = request.form['password']
  rpsswd = request.form['rpassword']
  if(psswd != rpsswd):
    errors.append("Passwords do not match")
  # check if there's already an account that exists with that email
  email_query = sess.query(Customer).filter_by(email = email).all()
  if(len(email_query) > 0):
    errors.append("account already exists with this email")
  if (len(errors) > 0):
    return render_template('create-account.html', errors=errors)
  hashedPass = InputValidation.sha512_hash(psswd)
  cust = Customer(
    customerName = name, 
    email = email, 
    phoneNumber = phone, 
    password = hashedPass,
    address=None
  )
  sess.add(cust)
  sess.commit()
  session['errors'] = ["Account successfully created. Please log in"]
  return redirect('/')

@account.route("/logout")
def logout():
  try:
    # check if customer was logged in
    if session['customer']:
      session.pop('customer') # pop session customer id if logged in
      errors = ["Successfully logged out"]
      return render_template('sign-in.html', errors=errors)
  except KeyError:
    # there was no session id
    print("session does not exist")
    pass
  return render_template('sign-in.html')

@account.route("/create_account")
def create_account():
  return render_template('create-account.html')

@account.route("/edit_account")
def edit_account():
    try:
        session['customer']
    except KeyError:
        return redirect(url_for('home'))
    try:
        session['errors']
    except KeyError:
        session['errors'] = []
    errors = session['errors']
    session.pop('errors')
    user = sess.query(Customer).filter_by(customer_id = session['customer']).first()
    user_dict = {
        "name": user.customerName,
        "email": user.email,
        "phoneNumber": user.phoneNumber
    }
    return render_template('edit-account.html', user=user_dict, errors=errors)

@account.route("/send_account", methods=['POST'])
def send_account():
  session['errors'] = list()
  customer = sess.query(Customer).filter_by(customer_id = session['customer']).first()
  name = request.form['name']
  email = request.form['email']
  phoneNumber = request.form['pNumber']
  password = request.form['password']
  rpassword = request.form['rpassword']
  if(password != ""): # if password isn't blank; customer intends to update password
    hashedPass = InputValidation.sha512_hash(password)
    if (rpassword == password):
      # if the two passwords match
      if (hashedPass != customer.password): # update password if it isn't the same
        customer.password = InputValidation.sha512_hash(password)
    else:
      session['errors'].append("Passwords do not match!")
      return redirect(url_for('account_operations.edit_account'))
  if name != customer.customerName: # update name if updated
    customer.customerName = name
  if email != customer.email:
    # check if email already exists in system
    check_email = sess.query(Customer).filter_by(email = email).all()
    if len(check_email) > 0:
      session['errors'].append("An account already exists with this email")
      return redirect(url_for('account_operations.edit_account'))
    # if passed, then we can update the email
    customer.email = email
  if phoneNumber != customer.phoneNumber:
    customer.phoneNumber = phoneNumber
  sess.commit()
  return redirect(url_for('account_operations.view_account')) 
      

@account.route("/view_account")
def view_account():
  try:
    session['customer']
  except KeyError:
    return redirect(url_for('home'))
  user = sess.query(Customer).filter_by(customer_id = session['customer']).first()
  user_dict = {
    "name": user.customerName,
    "email": user.email,
    "phoneNumber": user.phoneNumber
  }
  return render_template("view-account.html", user=user_dict)

@account.route("/login", methods=['GET', 'POST'])
def login_confirm():
  if request.method == 'POST':
    email = request.form['email']
    password = request.form['password']
    hashedPass = InputValidation.sha512_hash(password)
    validUser = sess.query(Customer).filter_by(email=email, password=hashedPass).first()
    if validUser != None: 
      session['customer'] = validUser.customer_id
      return render_template('welcome.html', user=validUser.customerName)
    else:
      errors = ["Account information is incorrect!"]
      return render_template('sign-in.html', errors=errors)
  else:
    try:
      if session['customer']:
        validUser = sess.query(Customer).filter_by(customer_id=session['customer']).first()
        return render_template('welcome.html', user=validUser.customerName)
    except KeyError:
      print("session has not been created yet")
  return render_template('sign-in.html')

@account.route("/update_address", methods=["POST"])
def update_address():
  # this pertains to checkout
  db_user = sess.query(Customer).filter_by(customer_id = session['customer']).first()
  street_address = request.form['address']
  city = request.form['city']
  country = request.form['country']
  state = request.form['state']
  zip = request.form['zip']
  # 1234 E Streety McAddress Ln., City, State, ZIP
  formatted_address = street_address + ", " + city + ", " + state + ", " + country + " " + str(zip)
  db_user.address = formatted_address
  sess.commit()
  return redirect(url_for('order_operations.initiate_checkout'))
