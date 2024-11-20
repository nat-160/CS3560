class Customer:
    def __init__(self, password,customerName,address,phoneNumber,email,customer_id=None):
        self.password,self.customerName,self.address,self.phoneNumber,self.email=password,customerName,address,phoneNumber,email
        self.customer_id=customer_id
class Employee:
    def __init__(self,position,employeeName,employeeStatus,employeeID=None):
        self.position,self.employeeName,self.employeeStatus=position,employeeName,employeeStatus
        self.employeeID=employeeID
class Menu:
    def __init__(self,menuName,startTime,endTime,menuID=None):
        self.menuName,self.startTime,self.endTime=menuName,startTime,endTime
        self.menuID=menuID
class MenuEntry:
    def __init__(self,menuID,itemID,state):
        self.menuID,self.itemID,self.state=menuID,itemID,state
class MenuItem:
    def __init__(self,name,price,menuDescription,image,category,itemID=None):
        self.name,self.price,self.menuDescription,self.image,self.category=name,price,menuDescription,image,category
        self.itemID=itemID
class OrderItem:
    def __init__(self,itemID,orderID=None,specialInstruction=None,orderItemID=None):
        self.itemID,self.orderID,self.specialInstruction=itemID,orderID,specialInstruction
        self.orderItemID=orderItemID
class Orders:
    def __init__(self,customerID,orderDate,modNote,orderstatus,amount,orderID=None):
        self.customerID,self.orderDate,self.modNote,self.orderstatus,self.amount=customerID,orderDate,modNote,orderstatus,amount
        self.orderID=orderID
