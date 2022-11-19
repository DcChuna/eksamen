from tkinter import *
import sqlite3

window = Tk()
window.title('Catalog')
window.geometry('1000x400')
window.config(bg='#3b3b3b')
inputAction = ''
connection = sqlite3.connect('products.sl3', 5)
cur = connection.cursor()
#cur.execute('CREATE TABLE productss (name TEXT, price TEXT, number TEXT)')
#connection.commit()
res = cur.fetchall()
