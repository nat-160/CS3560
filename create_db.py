from datetime import datetime
from sqlalchemy import create_engine, text
from alchemy import Alchemy
from classes import Customer, Employee, Menu, MenuEntry, MenuItem, OrderItem, Orders

# connect to MySQL
alchemy = Alchemy()
engine = alchemy.engine

# delete existing tables just in case (order matters)
with engine.connect() as connection:
    connection.execute(text('DROP TABLE IF EXISTS orderitem'))
    connection.execute(text('DROP TABLE IF EXISTS orders'))
    connection.execute(text('DROP TABLE IF EXISTS menuentry'))
    connection.execute(text('DROP TABLE IF EXISTS menuitem'))
    connection.execute(text('DROP TABLE IF EXISTS menu'))
    connection.execute(text('DROP TABLE IF EXISTS employee'))
    connection.execute(text('DROP TABLE IF EXISTS customer'))

#create empty tables
alchemy.metadata.create_all(engine)

# grab the session
session = alchemy.session

# add some mock data
session.add(Customer("1234","john","123 first ave", "123-456-7890", "john@aol.com"))
session.add(Employee("cashier","jane","active"))
session.add(Employee("manager","jay","active"))
session.add(Menu("default","default","default"))
session.add(Menu("Breakfast","0400","1000"))
session.add(Menu("Lunch","1000","1600"))
session.add(MenuItem("Big Burger", "5.00", "Not affiliated with McD", "~/projpics/bigburger.jpg", "food"))
session.add(MenuItem("Whupper", "4.00", "Not affiliated with BK", "~/projpics/Whupper.jpg", "food"))
session.commit()
session.add(MenuEntry(1,1,"enabled"))
session.add(MenuEntry(2,2,"enabled"))
session.commit()
session.add(Orders(1, "date", "modNote", "0", "$5.00"))
session.commit()
session.add(OrderItem(1, 1, "No pickles"))
session.commit()

# print some of the new data
for c in session.query(Customer).all():
    print(c.customer_id, c.customerName, c.phoneNumber)
for e in session.query(Employee).all():
    print(e.employeeID,e.employeeName,e.employeeStatus,e.position)
for m in session.query(Menu).all():
    print(m.menuID, m.menuName, m.startTime, m.endTime)
for i in session.query(MenuItem).all():
    print(i.itemID, i.name, i.category, i.menuDescription)
for e in session.query(MenuEntry).all():
    print(e.entryID,e.itemID,e.menuID)
for o in session.query(Orders).all():
    print(o.orderID, o.amount)
for i in session.query(OrderItem).all():
    print(i.orderItemID, i.orderID, i.itemID)
