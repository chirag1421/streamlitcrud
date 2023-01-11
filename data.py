import sqlite3


conn = sqlite3.connect('da.db', check_same_thread=False)
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE  IF NOT EXISTS STUDENT(StudentID VARCHAR UNIQUE NOT NULL ,firstname TEXT NOT NULL, lastname TEXT NOY NULL, city TEXT NOT NULL, PRIMARY KEY(StudentID))')


def add_data(StudentID, firstname, lastname, city):
    c.execute('INSERT INTO STUDENT(StudentID,firstname, lastname, city) VALUES(?,?,?,?)',(StudentID,firstname,lastname,city))
    conn.commit()

def view_data():
    c.execute('SELECT * FROM STUDENT')
    data = c.fetchall()
    return data

def view_StudentID():
    c.execute('SELECT DISTINCT StudentID FROM STUDENT')
    data = c.fetchall()
    return data
def get_StudentID(StudentID):
    c.execute('SELECT * FROM STUDENT WHERE StudentID="{}"'.format(StudentID))
    data = c.fetchall()
    return data
def edit(new_firstname,new_lastname,new_city,firstname,lastname,city):
    c.execute('UPDATE STUDENT SET firstname=?,lastname=?,city=? WHERE image=? and firstname=? and lastname=? and city=?',(new_firstname,new_lastname, new_city,firstname,lastname,city))
    conn.commit()
    data = c.fetchall()
    return data
def delete(StudentID):
    c.execute('DELETE FROM STUDENT WHERE StudentID="{}"'.format(StudentID))
    conn.commit()