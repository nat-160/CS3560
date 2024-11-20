from flask import Blueprint, render_template, redirect, request, session, url_for
from sqlalchemy import text, literal_column
from Globals.db_connect import engine
from classes import Orders, OrderItem, Menu, MenuItem, Customer
from alchemy import Alchemy
from datetime import datetime
import time

sql = Alchemy(engine)
sess = sql.session

orders = Blueprint('order_operations', __name__, static_folder='static', template_folder='templates')

@orders.route("/orders")
def view_orders():
  # this is irrelevant; only the admin should be able to view all orders
  return redirect("/search_order")
  return render_template("orders.html",
                         orders=fetch_orders(),
                         order_items=fetch_items())


# ROUTES RELATING TO CART
@orders.route("/add_to_order", methods=["POST"])
def add_to_order():
  try:
    session['cart']
  except KeyError:
    session['cart'] = list()
  session['cart'] = session['cart'] # make sure session is up to date
  if 'itemID' not in request.form:
    return "error"
  else:
    itemID = request.form.get('itemID')
  if 'specialInstruction' in request.form:
    specialInstruction = request.form.get('specialInstruction')
    if specialInstruction == "":
      specialInstruction = None
  else:
    specialInstruction = None
  requestedItem = OrderItem(itemID=itemID, specialInstruction=specialInstruction)
  session['cart'].append(orderitem_to_dict(requestedItem, (len(session['cart'])+1)))
  return redirect("/view_cart")

@orders.route("/view_cart")
def view_cart():
  cart_info = {"total": 0.00}
  item_list = list()
  try:
    print(session['cart'])
  except KeyError:
    session['cart'] = list()
  for item in session['cart']:
    item_entry = sess.query(MenuItem).filter_by(itemID = item.get('itemID')).first()
    item_dict = {
      "item-name": item_entry.name,
      "description": item_entry.menuDescription,
      "price": item_entry.price,
      "image": item_entry.image,
      "specialInstruction": item.get('specialInstruction'),
      "cartItemID": item.get('cartItemID')
    }
    item_list.append(item_dict)
    cart_info.update({"total": cart_info.get('total') + item_dict.get('price')})


  return render_template("view-cart.html",
                         cart_items=item_list,
                         cart_info=cart_info)

@orders.route("/remove_from_cart", methods=["GET"])
def remove_from_cart():
    try:
        session['cart'] = session['cart']
        id = request.args.get('id')
        item_to_destroy = next(filter(lambda d: d.get("cartItemID") == int(id), session['cart']), None)
        session['cart'].remove(item_to_destroy)
    except KeyError:
        pass
    return redirect("/view_cart")

@orders.route("/clear_cart")
def clear_cart():
  try:
    session.pop('cart')
  except KeyError:
    pass
  return redirect("/view_cart")

# ROUTES RELATING TO ORDERS
@orders.route("/send_checkout", methods=['POST'])
def send_checkout_info():
  billing_info = {
    'first-name': request.form['fname'],
    'last-name': request.form['lname'],
    'email': request.form['email'],
    'address': request.form['address'],
    'country': request.form['country'],
    'state': request.form['state'],
    'zip': request.form['zip']
  }
  payment_info = {
    'name-on-card': request.form['ncard'],
    'cc-number': request.form['cc-number'],
    'cc-expiration': request.form['cc-expiration'],
    'cc-ccv': request.form['cc-ccv'],
  }
  return render_template('welcome.html', user=None)

@orders.route("/set_address")
def set_address():
   return render_template('set-address.html')

@orders.route("/initiate_checkout")
def initiate_checkout():
  sess.commit()
  db_user = sess.query(Customer).filter_by(customer_id = session['customer']).first()
  if not db_user.address:
     # billing address is not set
     return redirect(url_for('order_operations.set_address'))
  else:
     # billing address is set
     address = db_user.address
     return render_template('confirm-address.html', address=address)

@orders.route("/payment_checkout")
def payment_checkout():
   return render_template('payment-info.html')

@orders.route("/confirm_checkout")
def confirm_checkout():
  return render_template('confirm-checkout.html', order=None)

@orders.route("/place_order", methods=["POST"])
def place_order():
    try:
        session['cart']
        session['customer']
    except KeyError:
       # something went wrong
       return redirect("/view_cart")
    session['cart'] = session['cart']
    if len(session['cart']) == 0:
       # there's no items in the cart
       return redirect("/view_cart")
    
    # passed the checks, we can insert the order
    new_order = Orders(customerID = session['customer'],
                      orderDate = sess.query(text("NOW()")),
                      modNote = None,
                      orderstatus = 0,
                      amount=0)
    sess.add(new_order)
    sess.commit()
    order_id = new_order.orderID
    order_total = 0.0
    # now we handle the items in the cart!
    for item in session['cart']:
       new_item = OrderItem(
          itemID = item['itemID'],
          orderID = order_id,
          specialInstruction = item['specialInstruction']
       )
       sess.add(new_item)
       sess.commit()
       order_total += sess.query(MenuItem).filter_by(itemID = item['itemID']).first().price
    session.pop('cart')
    new_order.amount = order_total
    sess.commit()
    return redirect("/view_order?id=" + str(order_id))

@orders.route("/search_order")
def search_order():
    try:
      session['errors']
    except KeyError:
      session['errors'] = list()
    errors = session['errors']
    session.pop('errors')
    return render_template('/search-order.html', errors=errors)

@orders.route("/view_order", methods=["GET"])
def view_order():
    session['errors'] = list()
    if not request.args.get('id'):
        session['errors'].append("No order specified")
        return redirect("/search_order")
    order_id = request.args.get('id')
    db_order = sess.execute(text("SELECT * FROM full_order_details WHERE orderID = " + order_id)).first()
    if not db_order:
       session['errors'].append("Order does not exist")
       return redirect("/search_order")
    order_info = {
      "orderID": db_order.orderID,
      "orderstatus": db_order.orderstatus,
      "orderDate": db_order.orderDate,
      "amount": db_order.amount,
      "customerName": db_order.customerName,
      "phoneNumber": db_order.phoneNumber,
      "email": db_order.email,
      "modNote": db_order.modNote
  }

    return render_template("view-order.html",
                            order_items=fetch_order_items(order_id),
                            order=order_info)

# ROUTES RELATING TO MENU
@orders.route("/menu")
def menu():
  sess.commit()
  # get list of menus
  list_menus = list()
  menu_query = sess.execute(text("SELECT * FROM menu ORDER BY endTime"))
  for menu in menu_query.all():
    menu_dict = {
      'menuID': menu.MenuID,
      'menuName': menu.menuName,
      'startTime': int(str(menu.startTime).replace(":","")),
      'endTime': int(str(menu.endTime).replace(":","")),
      'startTimeRaw': menu.startTime,
      'endTimeRaw': menu.endTime
    }
    list_menus.append(menu_dict)
  # get list of menu items
  list_items = list()
  item_query = sess.execute(text("SELECT * FROM menu_entry_details"))
  for item in item_query.all():
    item_dict = {
      'itemID': item.itemID,
      'menuID': item.menuid,
      'name': item.name,
      'menuDescription': item.menuDescription,
      'price': item.price,
      'image': item.image,
      'category': item.category,
      'state': item.state
    }
    list_items.append(item_dict)
  current_time = int(datetime.now().strftime('%H%M'))
  return render_template("menu.html", menus=list_menus, items=list_items, time=current_time)



# METHODS GO HERE

def orderitem_to_dict(OrderItem, cartItemID = None):
  dict = {
    "itemID": OrderItem.itemID,
    "specialInstruction": OrderItem.specialInstruction,
    "cartItemID": cartItemID
  }
  return dict

def fetch_orders(): # these need to be set IN THE RENDER CALL; if we append to a pre-existing array it will be cached and duplicate data on refresh
    list_orders = list()
    result = sess.execute(text("SELECT * FROM full_order_details ORDER BY orderDate ASC"))
    for order in result.all():
        order_entry = {
            'order-id': order.orderID,
            'status': order.orderstatus,
            'name': order.customerName,
            'phoneNumber': order.phoneNumber,
            'amount': order.amount,
            'date': order.orderDate,
            'instructions': order.modNote
        }
        list_orders.append(order_entry)
    sess.commit() # we do this so that the list actually updates on refresh; flask is annoying
    return list_orders # return a list of dictionaries

def fetch_order_items(id):
    list_items = list()
    result = sess.execute(text("SELECT * FROM order_item_details WHERE orderID = " + id + " ORDER BY (price) DESC"))
    for item in result.all():
        item_entry = {
            'order-id': item.orderID,
            'item-id': item.itemID,
            'orderItemID': item.orderItemID,
            'name': item.name,
            'price': item.price,
            'specialInstruction': item.specialInstruction
        }
        list_items.append(item_entry)
    sess.commit()
    return list_items

def fetch_items():
    list_items = list()
    result = sess.execute(text("SELECT * FROM order_item_details ORDER BY (price) DESC"))
    for item in result.all():
        item_entry = {
            'order-id': item.orderID,
            'item-id': item.itemID,
            'orderItemID': item.orderItemID,
            'name': item.name,
            'price': item.price,
            'specialInstruction': item.specialInstruction
        }
        list_items.append(item_entry)
    sess.commit()
    return list_items