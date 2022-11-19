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
def catalog(action):
   global inputAction
   global n0
   global n1
   global n2
   global n3
   global n4
   global n5
   global n6
   global nall
   global no
   if action == '1' or action == '2' or action == '3' or action == '4':
         inputAction = action
         if inputAction == '1':
               n0 = input('Enter name')
               n1 = int(input('Enter price'))
               n2 = int(input('Enter number'))
               cur.execute(f'INSERT INTO productss (name, price, number) VALUES ("{n0}" , "{n1}" , "{n2}")')
               connection.commit()
         if inputAction == '2':
               no = input('Enter row id')
               cur.execute(f'DELETE FROM productss WHERE rowid = {no}')
               connection.commit()
         if inputAction == '3':
               print(res)
         if inputAction == '4':
               n6 = int(input('Enter row id'))
               nall = input(
                     'If you want edit name enter: 1\nIf you want edit price enter: 2\nIf you want edit number enter: 3\n')
               if nall == '1':
                     n3 = input('Enter name')
                     cur.execute(f'UPDATE productss SET name = "{n3}" WHERE rowid = "{n6}"')
                     connection.commit()
               if nall == '2':
                     n4 = int(input('Enter price'))
                     cur.execute(f'UPDATE productss SET price = "{n4}" WHERE rowid = "{n6}"')
                     connection.commit()
               if nall == '3':
                     n5 = int(input('Enter number'))
                     cur.execute(f'UPDATE productss SET number = "{n5}" WHERE rowid = "{n6}"')
                     connection.commit()

