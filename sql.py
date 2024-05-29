import sqlite3
connection = sqlite3.connect("Students")

cursor = connection.cursor()


def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS  students(ad TXT, soyad TXT, kurs INT, ortalama_bal INT)")
    connection.commit()

# def add_data():
#     cursor.execute("INSERT INTO students VALUES('Sevinc', 'Esedova', 2, 92)")
#     connection.commit()        


ad = input("telebenin adı:")
soyad = input("telebenin soyadı:")
kurs = int(input("kurs:"))
ortalama_bal = int(input("ortalama bal:"))


def dynamic_add_data(ad, soyad, kurs, ortalama_bal):
    cursor.execute("INSERT INTO students VALUES(?, ?, ?, ?)", (ad, soyad, kurs, ortalama_bal))
    connection.commit()  
    
dynamic_add_data(ad, soyad, kurs, ortalama_bal)

def delete_data(ad, soyad):
    with sqlite3.connect("Students") as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM students WHERE ad=? AND soyad=?", (ad, soyad))
        connection.commit()
        print("silindi")

def show_data():
    with sqlite3.connect("Students") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

# add_data()
# show_data()
# delete_data()
# create_table()
connection.close()


        