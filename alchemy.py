from sqlalchemy import Engine, ForeignKey, create_engine, MetaData, Table, Column, Integer, String, text
from sqlalchemy.orm import registry, sessionmaker, clear_mappers
from classes import Customer, Employee, Menu, MenuEntry, MenuItem, OrderItem, Orders
class Alchemy:
    def __init__(self, engine=None):
        if engine is None:
            # troubleshooting: should be mysql://[user]:[password]@localhost/[schema]
            engine = create_engine('mysql+mysqlconnector://root:admin@localhost/restaurant')
        meta = MetaData()
        # create tables (order matters)
        customer_table = Table(
            'Customer', meta,
            Column('customer_id', Integer, primary_key=True),
            Column('password', String(255)),
            Column('customerName', String(255)),
            Column('address', String(255)),
            Column('phoneNumber', String(255)),
            Column('email', String(255)),
        )
        employee_table = Table(
            'Employee', meta,
            Column('employeeID', Integer, primary_key=True),
            Column('position', String(255)),
            Column('employeeName', String(255)),
            Column('employeeStatus', String(255)),
        )
        menu_table = Table(
            'Menu', meta,
            Column('menuID', Integer, primary_key=True),
            Column('menuName', String(255)),
            Column('startTime', String(255)),
            Column('endTime', String(255)),
        )
        menuitem_table = Table(
            'MenuItem', meta,
            Column('itemID', Integer, primary_key=True),
            Column('name', String(255)),
            Column('price', String(255)),
            Column('menuDescription', String(255)),
            Column('image', String(255)),
            Column('category', String(255)),
        )
        menuentry_table = Table(
            'MenuEntry', meta,
            Column('menuID', ForeignKey(menu_table.key), primary_key=True),
            Column('itemID', ForeignKey(menuitem_table.key), primary_key=True),
            Column('state', String(255)),
        )
        orders_table = Table(
            'Orders', meta,
            Column('orderID', Integer, primary_key=True),
            Column('customerID', ForeignKey('Customer.customer_id')),
            Column('orderDate', String(255)),
            Column('modNote', String(255)),
            Column('orderstatus', String(255)),
            Column('amount', String(255)),
        )
        orderitem_table = Table(
            'OrderItem', meta,
            Column('orderItemID', Integer, primary_key=True),
            Column('orderID', ForeignKey(orders_table.key)),
            Column('specialInstruction', String(255)),
            Column('itemID', ForeignKey(menuitem_table.key)),
        )
        # clear mappers to prevent crash
        clear_mappers()
        # create a session and map the appropriate classes to it
        registry().map_imperatively(Customer, customer_table)
        registry().map_imperatively(Employee, employee_table)
        registry().map_imperatively(Menu, menu_table)
        registry().map_imperatively(MenuEntry, menuentry_table)
        registry().map_imperatively(MenuItem, menuitem_table)
        registry().map_imperatively(OrderItem, orderitem_table)
        registry().map_imperatively(Orders, orders_table)
        Session = sessionmaker(bind=engine)
        # bind some variables that we can use
        self.engine = engine
        self.session = Session()
        self.metadata = meta
        return
