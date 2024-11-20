#!/usr/bin/env python3
from datetime import datetime
import tkinter as tk
from tkinter import Tk, Frame, Label, Button, Entry, Menu, messagebox
from functools import partial
import sys
import os
from sqlalchemy import update
sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.dirname(
                os.path.realpath(
                    __file__)))))
from alchemy import Alchemy
from classes import Customer, Employee, MenuEntry, MenuItem, OrderItem, Orders
from classes import Menu as MenuClass

# globals
h1,h2 = "Arial 20 bold", "Arial 18 bold"
p,sub = "Arial 16", "Arial 14 italic"
code = "Courier 14"
root = Tk()
content = Frame(root)
alchemy = Alchemy()
debugMode = True

# call main at end of file, so all functions are defined
def main():
    # set up window
    init_window(root, "Restauraunt System - Login", side=tk.LEFT)
    # catch system exit
    root.protocol("WM_DELETE_WINDOW", prompt_exit)
    # create screen
    create_login()
    # start program
    root.mainloop()

def debug_print(*objs):
    if debugMode:
        print(objs)

def prompt_exit(event=None):
    debug_print("prompt_exit", event)
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        exit(0)

def init_window(window: Tk, title, popup=False, side=tk.RIGHT):
    window.option_add('*tearOff', tk.FALSE)
    window.grid_rowconfigure(1, weight=1)
    window.grid_columnconfigure(1, weight=1)
    window.title(title)
    window.bind("<Control-q>", lambda e: prompt_exit(e))
    menubar = Menu(window, font=code)
    if popup:
        def ex(e=None): debug_print(e); window.destroy()
        window.bind("<Escape>", ex)
        menubar.add_command(label="[esc] Close", command=window.destroy)
        window['menu'] = menubar
    w,h = window.winfo_screenwidth(),window.winfo_screenheight()
    if side==tk.LEFT:
        window.geometry("%dx%d+%d+%d" % (w/2, h, 0, 0))
    else:
        window.geometry("%dx%d+%d+%d" % (w/2, h, w/2, 0))
    return menubar

def create_login():
    global username_entry, pin_entry, b_color
    Label(content, font=h1, text="Employee Login").grid(row=0)
    # create input fields
    inputs = Frame(content)
    Label(inputs, font=p, text="Username:").grid(row=0, column=0, sticky="E")
    username_entry = Entry(inputs, font=code)
    username_entry.grid(row=0, column=1)
    Label(inputs, font=p, text="PIN:").grid(row=1, column=0, sticky="E")
    pin_entry = Entry(inputs, show="*", font=code)
    pin_entry.bind("<Return>", login)
    pin_entry.grid(row=1, column=1)
    # create buttons
    buttons = Frame(content)
    b = Button(buttons, font=h2, text="Log In", command=login)
    b.bind("<Return>", login)
    b.grid(row=0, column=0)
    q = Button(buttons, font=h2, text="Quit", command=prompt_exit)
    q.bind("<Return>", prompt_exit)
    q.grid(row=0, column=2)
    # add objects
    inputs.grid(row=1)
    buttons.grid(row=2)
    content.grid(row=1, column=1)
    # select default input
    username_entry.focus()

    # grab button color for later
    b_color = b['background']

    # autologin as admin when debugging
    if debugMode:
        username_entry.insert(0, "sudo")
        pin_entry.insert(0, "4321")
        b.focus()

def login(event=None):
    debug_print("login", event)
    # get employee names
    employee = alchemy.session.get(Employee,pin_entry.get())
    if employee is not None and username_entry.get() == employee.employeeName:
        if employee.position == "manager":
            create_system(isManager=True)
        else:
            create_system()
    elif debugMode:
        create_system(isManager=True)
    else: # Display error
        Label(content, font=sub, fg="red", text="Invalid username/PIN").grid(row=3)
        username_entry.focus()
        username_entry.selection_range(0, tk.END)

def logout(event=None):
    debug_print("logout", event)
    global content
    content.destroy()
    content = Frame(root)
    root['menu'] = ""
    create_login()

def create_system(isManager=False):
    global content, update_state
    content.destroy()
    content = Frame(root)
    root.title("Restaurant System - Employee View")
    create_menubar(isManager)
    Label(content, font=h1, text="Acknowledged Orders").grid(row=0)
    Label(content, font=h1, text="New Orders").grid(row=2)
    Label(content, font=h1, text="Completed Orders").grid(row=4)
    display_orders()
    content.grid(row=1, column=1)
    update_state = False


def create_menubar(isManager):
    menubar = Menu(root, font=code)
    manager = Menu(menubar, font=code)
    if(isManager):
        root.title("Restaurant System - Manager View")
        menubar.add_cascade(underline=0, menu=manager, label="Manager")
    manager.add_command(underline=5, command=create_menueditor, label="Edit Menus")
    manager.add_command(underline=5, command=create_itemeditor, label="Edit Items")
    menubar.add_command(underline=0, command=new_order, label="New Order")
    menubar.add_command(underline=0, command=updateorder_mode, label="Update Order")
    refresh = partial(create_system, isManager)
    menubar.add_command(underline=0, command=refresh, label="Refresh")
    menubar.add_command(underline=0, command=logout, label="Logout")
    root['menu'] = menubar

def display_orders():
    alchemy.session.commit()
    global ack_orders, new_orders, fin_orders
    orders = alchemy.session.query(Orders).all()
    ack_orders,new_orders,fin_orders = Frame(content),Frame(content),Frame(content)
    for order in orders:
        text = str(order.orderID)
        if int(order.orderstatus) == 0:
            Button(new_orders, font=h2, text=text, command=partial(view_order, order.orderID, 0)).pack(side=tk.LEFT)
        elif int(order.orderstatus) == 1:
            Button(ack_orders, font=h2, text=text, command=partial(view_order, order.orderID, 1)).pack(side=tk.LEFT)
        elif int(order.orderstatus) == 2:
            Button(fin_orders, font=h2, text=text, command=partial(view_order, order.orderID, 2)).pack(side=tk.LEFT)
    ack_orders.grid(row=1)
    new_orders.grid(row=3)
    fin_orders.grid(row=5)

def get_currentmenus():
    menus = list()
    for m in alchemy.session.query(MenuClass):
        if m.menuName=="default":
            menus.append(m)
        else:
            currentTime = int(datetime.now().strftime('%H%M'))
            startTime = int(str(m.startTime).replace(":",""))
            endTime = int(str(m.endTime).replace(":",""))
            if startTime < currentTime < endTime:
                menus.append(m)
            elif endTime < startTime:
                if endTime < currentTime or currentTime < startTime:
                    menus.append(m)
    return menus

def get_currentmenuitems():
    menuIDs = [m.menuID for m in get_currentmenus()]
    menuEntrys = [e for e in alchemy.session.query(MenuEntry) if e.menuID in menuIDs]
    itemIDs = [d.itemID for d in menuEntrys]
    menuItems = [i for i in alchemy.session.query(MenuItem) if i.itemID in itemIDs]
    return menuItems

def get_itemcount(orderID:int, itemID:int):
    order = [1 for o in alchemy.session.query(OrderItem) if o.orderID==orderID and o.itemID==itemID]
    return len(order)

def view_order(orderID:int, status:int):
    # todo: add customer name?
    debug_print("view_order", orderID, status)
    window = Tk()
    init_window(window, "Order Viewer", popup=True)
    popup = Frame(window)
    popup.grid(row=1, column=1)
    text = "Order: "+str(orderID)
    Label(popup, text=text, font=h1).pack()
    text = "Status: "+("new" if status==0 else "acknowledged" if status==1 else "completed")
    Label(popup, text=text, font=p).pack()
    text = "Menus: "+", ".join([x.menuName for x in get_currentmenus()])
    Label(popup, text=text, font=h2).pack()
    orderFrame = Frame(popup)
    items = [i for i in alchemy.session.query(OrderItem).all() if i.orderID==orderID]
    entries = list()
    for i in range(len(items)):
        row = Frame(orderFrame)
        text = alchemy.session.get(MenuItem, items[i].itemID).name
        Label(row, text=text, font=h2).pack(side=tk.LEFT)
        e = Entry(row, font=code)
        text = items[i].specialInstruction
        if text is not None:
            e.insert(0, text)
        e['state'] = tk.DISABLED
        e.pack(side=tk.LEFT)
        entries.append(e)
        row.pack()
    orderFrame.pack()
    noteFrame = Frame(popup)
    l = Label(noteFrame, font=h2, text="Note: ")
    l.grid(row=0,column=0)
    l = Label(noteFrame, font=code, text=alchemy.session.get(Orders,orderID).modNote)
    l.grid(row=0,column=1)
    noteFrame.pack()
    buttons = Frame(popup)
    text = "Start Order" if status==0 else "Finish Order" if status==1 else "Order Picked-Up"
    def update(): update_order(orderID, status); window.destroy()
    Button(buttons, text=text, font=h2, command=update).pack(side=tk.LEFT)
    def cancel():
        if messagebox.askokcancel("Confirm", "Are you sure?"):
            update_order(orderID, -1); window.destroy()
    cancelButton = Button(buttons, text="Cancel Order", font=h2, command=cancel)
    editButton = Button(buttons, text="Edit Order", font=h2)
    def edit():
        for e in entries:
            if isinstance(e, Entry):
                e['state'] = tk.NORMAL
        editButton['text'] = "Save Changes"
        editButton['command'] = save
    def save():
        for i in range(len(entries)):
            if isinstance(entries[i], Entry):
                entries[i]['state'] = tk.DISABLED
                items[i].specialInstruction = entries[i].get()
                print(i,entries[i].get())
        alchemy.session.commit()
        editButton['text'] = "Edit Order"
        editButton['command'] = edit
    editButton['command'], cancelButton['command'] = edit, cancel
    cancelButton.pack(side=tk.LEFT)
    editButton.pack(side=tk.LEFT)
    buttons.pack()

def new_order():
    debug_print("new_order")
    window = Tk()
    init_window(window, "Order Viewer", popup=True)
    popup = Frame(window)
    popup.grid(row=1,column=1)
    Label(popup, text="New Order", font=h1).pack()
    text = "Menus: "+", ".join([x.menuName for x in get_currentmenus()])
    Label(popup, text=text, font=h2).pack()
    menu, nums, numLabels = Frame(popup), list(), list()
    totalLabel = Label(popup, text="$0.00", font=code)
    menuItems = get_currentmenuitems()
    def calc_total():
        total = 0
        for i in range(len(menuItems)):
            #num items in order * price
            total += float(menuItems[i].price) * nums[i]
        return total
    for i in range(len(menuItems)):
        Label(menu, text=menuItems[i].name, font=h2).grid(row=0, column=i)
        nums.append(0)
        l = Label(menu, text=nums[i], font=code)
        l.grid(row=2, column=i)
        numLabels.append(l)
        def subtract(i):
            if nums[i]!=0:
                nums[i]-=1
                numLabels[i]['text'] = nums[i]
                totalLabel['text'] = "${:.2f}".format(calc_total())
        def addition(i):
            nums[i]+=1
            numLabels[i]['text'] = nums[i]
            totalLabel['text'] = "${:.2f}".format(calc_total())
        sub = partial(subtract, i)
        add = partial(addition, i)
        Button(menu, text="+", font=h2, command=add).grid(row=1, column=i)
        Button(menu, text="-", font=h2, command=sub).grid(row=3, column=i)
    menu.pack()
    Label(popup, text="Order Modifications", font=h2).pack()
    e = Entry(popup, font=code)
    e.pack()
    def create():
        debug_print(e.get())
        if totalLabel['text']!="$0.00":
            debug_print(e.get())
            o = Orders(1, datetime.now(), e.get(), "0", calc_total())
            alchemy.session.add(o)
            alchemy.session.commit()
            for i in range(len(menuItems)):
                for j in range(nums[i]):
                    alchemy.session.add(OrderItem(menuItems[i].itemID, o.orderID, str(j)))
            alchemy.session.commit()
            b = Button(new_orders, text=o.orderID, font=h2, command=partial(view_order, o.orderID, 0))
            b.pack(side=tk.LEFT)
            window.destroy()
        else:
            messagebox.showerror("Empty Order","Order is empty")
    Label(popup, text="Total", font=h2).pack()
    totalLabel.pack()
    Button(popup, text="Create", font=h2, command=create).pack()

def updateorder_mode(e=None):
    debug_print("update_order_mode", e)
    global update_state
    if update_state:
        update_order(-1, -1)
        root.unbind("<Escape>")
        return
    update_state = True
    root.bind("<Escape>",updateorder_mode)
    for b in new_orders.winfo_children():
        if isinstance(b, Button):
            b['background'] = "yellow"
            b['command'] = partial(update_order, b['text'], 0)
    for b in ack_orders.winfo_children():
        if isinstance(b, Button):
            b['background'] = "green"
            b['command'] = partial(update_order, b['text'], 1)
    for b in fin_orders.winfo_children():
        if isinstance(b, Button):
            b['background'] = "red"
            b['command'] = partial(update_order, b['text'], 2)

def update_order(orderID:int, status):
    # Status: 0 for new, 1 for acknowledged, 2 for completed, -1 for cancel
    debug_print("update_order", orderID, status)
    global update_state
    update_state = False
    for b in fin_orders.winfo_children():
        if isinstance(b, Button):
            b['background'] = b_color
            b['command'] = partial(view_order, b['text'], 2)
            if b['text'] == str(orderID):
                b.destroy()
    for b in ack_orders.winfo_children():
        if isinstance(b, Button):
            b['background'] = b_color
            b['command'] = partial(view_order, b['text'], 1)
            if b['text'] == str(orderID):
                if status == 1:
                    com = partial(view_order, orderID, 2)
                    Button(fin_orders, font=h2, text=orderID, command=com).pack(side=tk.LEFT)
                b.destroy()
    for b in new_orders.winfo_children():
        if isinstance(b, Button):
            b['background'] = b_color
            b['command'] = partial(view_order, b['text'], 0)
            if b['text'] == str(orderID):
                if status == 0:
                    com = partial(view_order, orderID, 1)
                    Button(ack_orders, font=h2, text=orderID, command=com).pack(side=tk.LEFT)
                b.destroy()
    if orderID!=-1:
        order = alchemy.session.get(Orders, orderID)
        order.orderstatus = str(int(status)+1) if status!=-1 else -1
        alchemy.session.commit()

def create_menueditor():
    debug_print("create_menueditor")
    window = Tk()
    popup = Frame(window)
    popup.grid(row=1,column=1)
    m = init_window(window, "Menu Editor", popup=True)
    m.add_command(label="New Menu", command=partial(edit_menu, -1), underline=0)
    def display():
        for c in popup.winfo_children():
            c.destroy()
        content = Frame(popup)
        Label(content, text="Menu Name", font=h1).grid(row=0, column=0)
        Label(content, text="| Start Time |", font=h1).grid(row=0, column=1)
        Label(content, text="End Time", font=h1).grid(row=0, column=2)
        alchemy.session.commit()
        menus = alchemy.session.query(MenuClass).all()
        for i in range(len(menus)):
            text,menuID = menus[i].menuName, menus[i].menuID
            b = Button(content, text=text, font=h2, command=partial(edit_menu, menuID))
            if text=="default":
                b['state'] = tk.DISABLED
            b.grid(row=i+1, column=0)
            startTime,endTime = menus[i].startTime,menus[i].endTime
            Label(content, text=startTime, font=code).grid(row=i+1, column=1)
            Label(content, text=endTime, font=code).grid(row=i+1, column=2)
        content.pack()
    m.add_command(label="Refresh", command=display, underline=0)
    display()

def edit_menu(menuID:int):
    debug_print("edit_menu", menuID)
    menu = MenuClass("", "", "") if menuID == -1 else alchemy.session.get(MenuClass, menuID)
    window = Tk()
    popup = Frame(window)
    popup.grid(row=1,column=1)
    init_window(window, "Menu Editor", popup=True, side=tk.LEFT)
    text = "New Menu" if menuID == -1 else "Edit Menu"
    Label(popup, text=text, font=h1).pack()
    grid = Frame(popup)
    Label(grid, text="menuName", font=h2).grid(row=0, column=0, sticky=tk.E)
    Label(grid, text="startTime", font=h2).grid(row=1, column=0, sticky=tk.E)
    Label(grid, text="endTime", font=h2).grid(row=2, column=0, sticky=tk.E)
    menuName = Entry(grid, font=code)
    startTime = Entry(grid, font=code)
    endTime = Entry(grid, font=code)
    menuName.insert(0, menu.menuName)
    startTime.insert(0, menu.startTime)
    endTime.insert(0, menu.endTime)
    menuName.grid(row=0, column=1)
    startTime.grid(row=1, column=1)
    endTime.grid(row=2, column=1)
    grid.pack()
    # SQL HERE!
    def save():
        menu.menuName = menuName.get()
        menu.startTime = startTime.get()
        menu.endTime = endTime.get()
        if menuID == -1:
            alchemy.session.add(menu)
        alchemy.session.commit()
        window.destroy()
    Button(popup, text="Save", font=h2, command=save).pack()

def create_itemeditor():
    debug_print("create_itemeditor")
    window = Tk()
    popup = Frame(window)
    popup.grid(row=1,column=1)
    m = init_window(window, "Item Editor", popup=True)
    m.add_command(label="New Item", command=partial(edit_item, -1), underline=0)
    def display():
        for c in popup.winfo_children():
            c.destroy()
        content = Frame(popup)
        Label(content, text="Item Name", font=h1).grid(row=0, column=0)
        Label(content, text="| Item Description |", font=h1).grid(row=0, column=1)
        Label(content, text="Item Price", font=h1).grid(row=0, column=2)
        alchemy.session.commit()
        items = alchemy.session.query(MenuItem).all()
        for i in range(len(items)):
            text,itemID = items[i].name, items[i].itemID
            Button(content, text=text, font=h2, command=partial(edit_item, itemID)).grid(row=i+1, column=0)
            text, price = items[i].menuDescription, items[i].price
            Label(content, text=text, font=p).grid(row=i+1, column=1)
            Label(content, text=price, font=code).grid(row=i+1, column=2)
        content.pack()
    m.add_command(label="Refresh", underline=0, command=display)
    display()

def edit_item(itemID:int):
    debug_print("edit_item", itemID)
    item = MenuItem("","","","","") if itemID==-1 else alchemy.session.get(MenuItem, itemID)
    window = Tk()
    popup = Frame(window)
    popup.grid(row=1,column=1)
    init_window(window, "Item Editor", popup=True, side=tk.LEFT)
    text = "New Item" if itemID == -1 else "Edit Item"
    Label(popup, text=text, font=h1).pack()
    grid = Frame(popup)
    Label(grid, text="name", font=h2).grid(row=0, column=0, sticky=tk.E)
    Label(grid, text="price", font=h2).grid(row=1, column=0, sticky=tk.E)
    Label(grid, text="menuDescription", font=h2).grid(row=2, column=0, sticky=tk.E)
    Label(grid, text="image", font=h2).grid(row=3, column=0, sticky=tk.E)
    Label(grid, text="category", font=h2).grid(row=4, column=0, sticky=tk.E)
    name = Entry(grid, font=code)
    price = Entry(grid, font=code)
    menuDescription = Entry(grid, font=code)
    image = Entry(grid, font=code)
    category = Entry(grid, font=code)
    name.insert(0, item.name)
    price.insert(0, item.price)
    menuDescription.insert(0, item.menuDescription)
    image.insert(0, item.image)
    category.insert(0, item.category)
    name.grid(row=0, column=1)
    price.grid(row=1, column=1)
    menuDescription.grid(row=2, column=1)
    image.grid(row=3, column=1)
    category.grid(row=4, column=1)
    grid.pack()
    if itemID != -1:
        menuButtons = Frame(popup)
        Label(menuButtons, text="In Menus:", font=h2).pack(side=tk.LEFT)
        menus = alchemy.session.query(MenuClass).all()
        entries = [e for e in alchemy.session.query(MenuEntry) if e.itemID == itemID]
        def toggle(menuID, button:Button):
            entries = [e for e in alchemy.session.query(MenuEntry) if e.itemID == itemID]
            entry = [e for e in entries if e.menuID==menuID][0]
            entry.state = "enabled" if entry.state=="disabled" else "disabled"
            alchemy.session.commit()
            button['bg'] = "green" if entry.state=="enabled" else "red"
        for i in range(len(menus)):
            if menus[i].menuID not in [e.menuID for e in entries]:
                e = MenuEntry(menus[i].menuID, itemID, state="disabled")
                entries.append(e)
                alchemy.session.add(e)
                alchemy.session.commit()
            b = Button(menuButtons, text=menus[i].menuName, font=h2)
            b['command'] =  partial(toggle, menus[i].menuID, b)
            b['bg'] = "green" if [e.state for e in entries if e.menuID==menus[i].menuID][0]=="enabled" else "red"
            b.pack(side=tk.LEFT)
        menuButtons.pack()
    def save():
        item.name = name.get()
        item.price = price.get()
        item.menuDescription = menuDescription.get()
        item.image = image.get()
        item.category = category.get()
        if itemID == -1:
            alchemy.session.add(item)
        alchemy.session.commit()
        window.destroy()
    Button(popup, text="Save", font=h2, command=save).pack()

main()
