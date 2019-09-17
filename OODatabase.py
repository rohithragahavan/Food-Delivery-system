import mysql.connector

class Customers:
    def __init__(self):
        self.__name = ''
        self.__address = ''
        self.__mydb = None
        self.__mycursor = None
    
    def setName(self, name):
        if(len(name) < 5):
            return False
        else:
            self.__name = name
            return True
    
    def setAddress(self, address):
        self.__address = address
        
    def openConnection(self):
        print('Inside Open Connection Function')
        self.__mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          passwd="",
          database="mydatabase"
        )        
        self.__mycursor = self.__mydb.cursor()
         
    def getData(self):
        if(self.__mycursor == None):
            self.openConnection()
        sql = "SELECT * FROM customers"
        self.__mycursor.execute(sql)
        myresult = self.__mycursor.fetchall()
        for x in myresult:
          for val in x:
              print(val, end = ',')
          print()
        
    def insertData(self, name, address):
        ret = self.setName(name)
        if(ret == False):
            return False
        
        self.setAddress(address)
        
        if(self.__mycursor == None):
            self.openConnection()
            
        sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
        val = (self.__name, self.__address)
        self.__mycursor.execute(sql, val)
        self.__mydb.commit()
        
        
if __name__ == '__main__':
    c1 = Customers()
    name = input('Enter Name : ')
    #c1.setName(name)
    address = input('Enter Address : ')
    #c1.setAddress(address)
    print('Calling Insert Data')
    ret = c1.insertData(name, address)
    if(ret == False):
        print('Invalid Name')
    print('Calling Get Data')
    c1.getData()