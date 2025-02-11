# База данных и управление 
import sqlite3
from ast import literal_eval

db = sqlite3.connect('data.db', check_same_thread=False)
cursor = db.cursor()

def auth(user_id):
    try:
        cursor.execute(f"INSERT INTO users (user_id) VALUES ({user_id})")
        db.commit()
    except Exception as error:
        print(error)

def add_to_cart(user_id, position):
    cart = cursor.execute(f'SELECT cart FROM users WHERE user_id = {user_id}').fetchall()[0][0]
    if str(cart) == '0':
        mylist = []
        mylist.append(position)
        position = f'{mylist}'
        cursor.execute(f"UPDATE users SET cart = '{position}' WHERE user_id = {user_id}")
        db.commit()
    else:
        mylist = literal_eval(cart)
        mylist.append(position)
        position = f'{mylist}'
        cursor.execute(f"UPDATE users SET cart = '{position}' WHERE user_id = {user_id}")
        db.commit()
        print('second')

def return_cart(user_id):
    result = cursor.execute(f'SELECT cart FROM users WHERE user_id = {user_id}').fetchall()[0][0]
    return result

def return_position_name(position):
    result = cursor.execute(f'SELECT name FROM market WHERE id = {position}').fetchall()[0][0]
    return result

def clear_cart(user_id):
    cursor.execute(f"UPDATE users SET cart = 0 WHERE user_id = {user_id}")
    db.commit()
    print(f'Success: {user_id}')

def set_waiting_status(user_id, column):
    if column == 1: # fio
        cursor.execute(f"UPDATE users SET fio = 1 WHERE user_id = {user_id}")
    if column == 2: # aphone number
        cursor.execute(f"UPDATE users SET number = 1 WHERE user_id = {user_id}")
    if column == 3: # address
        cursor.execute(f"UPDATE users SET address = 1 WHERE user_id = {user_id}")
    db.commit()

def return_status(user_id, column):
    if column == 1:
        result = cursor.execute(f'SELECT fio FROM users WHERE user_id = {user_id}').fetchall()[0][0]
        return result
    if column == 2:
        result = cursor.execute(f'SELECT number FROM users WHERE user_id = {user_id}').fetchall()[0][0]
        return result
    if column == 3:
        result = cursor.execute(f'SELECT address FROM users WHERE user_id = {user_id}').fetchall()[0][0]
        return result

def set_status(user_id, column, value):
    if column == 1: # fio
        cursor.execute(f"UPDATE users SET fio = '{value}' WHERE user_id = {user_id}")
    if column == 2: # aphone number
        cursor.execute(f"UPDATE users SET number = '{value}' WHERE user_id = {user_id}")
    if column == 3: # address
        cursor.execute(f"UPDATE users SET address = '{value}' WHERE user_id = {user_id}")
    db.commit()