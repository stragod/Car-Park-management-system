import sqlite3 as lite
import sys
import time
import datetime

class Database(object):
    
    def __init__(self):
        global cone
        global int pc = 375
        try:
            cone = lite.connect('main.db')
            with cone:
                cur = cone.cursor()
                sql = "CREATE TABLE IF NOT EXISTS main( index INTEGER AUTOINCREMENT,parsp INTEGER,type TEXT, number INTEGER PRIMARY KEY)"
                cur.execute(sql)
        except Exception:
            print("Unable To Create DB!")
        
    def insertdata(self, data):
        try:
            with cone:
                pc=pc-1
                cur = cone.cursor()
                sql = "INSERT INTO main(parsp,type, number) VALUES(?,?,?)"
                cur.execute(sql,data)
                return True
        except Exception:
            return False

    def fetchdata(self):
        try:
            with cone:
                cur = cone.cursor()
                sql = "SELECT * FROM main"
                cur.execute(sql)
                return cur.fetchall()
        except Exception:
            return False
    
    def deletedata(self, number):
        try:
            with cone:
                cur = cone.cursor()
                cur.execute("DELETE FROM main WHERE number = ?", [number])
                return True
        except Exception:
            return False
    def space(self,id):
        if id <= 


def main():

    print('#'*30)
    print("\n:: PARKING MANAGEMENT ::\n")
    print('#'*30)

    db = Database()

    print('\nPress 1. Check-In')
    print('\nPress 2. Show_parking space data')
    print('\nPress 3. Check-Out')

    print('\n')
    print('#'*30)

    choice = input("\n Enter a Choice: ")

    if choice == '1':
        typ=input("\n Type of Vehicle:car,truck or motorcycle:")
        if 'car' == typ:
                typeof = 'car'
        elif 'truck' == typ:
                 typeof = 'truck'
        elif 'motorcycle' == typ:
                   typeof = 'motorcycle'
        else:
                print("\n Wrong type of vehicle...cannot be parked here")
                sys.exit()

        number = input("\n Enter Vehicle Number: ")
        parsp = input(pc)

        if db.insertdata([typeof, number]):
            print("Entry inserted Sucess")
        else:
            print("Something went wrong")
    
    elif choice == '2':
        print("\n:: List :: \n")

        for iteam in db.fetchdata():
            print("\n ID : " + str(iteam[0]))
        
            print("\n Type of Vehicle : " + str(iteam[2]))
            print("\n Vehicle Number : " + str(iteam[3]))
        
            print("\n")
    
    elif choice == '3':
        record_id = input("Enter the ID No: ")

        if db.deletedata(record_id):
            print("Entry deleted Sucessfully ")
        else:
            print("Something went wrong")

    else:
        print("\n Enterd Number IS Out Of Range")

if __name__ == '__main__':
   while(1):
       main()
