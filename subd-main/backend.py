from sqlite3 import *
from tkinter.messagebox import *


with connect('database.db') as db:
    cursor = db.cursor()
    query = """ CREATE TABLE IF NOT EXISTS """"(id INTEGER PRIMARY KEY, name TEXT,  expenses TEXT )"""
    cursor.execute(query)


def information():
    cursor.execute("SELECT * FROM table1")
    return  cursor.fetchall()


def show_info():
    msg = 'Кнопка "Добавить" работает следующим образом: указать имя, платеж, индекс, после нажатия создает и добавляет в файл\n\n' \
          'Кнопка "Изменить" работает следующим образом: Сначала надо указать индекс, где изменять столбец name, после указать новый name\n\n' \
          'Кнопка "Удалить" работает следущющим образом: Сначала надо указать индекс, где удалить строку, после нажать кнопку'
    showinfo("Информация", msg)