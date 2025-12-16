import mysql.connector 
import PandasLearning

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@Bdull@h1023@$",
    database = "climate_db"

)
mycursor = conn.cursor()

Initalinput = input("Hi!, press 1 to sign in or 2 create a new account: ")

if Initalinput == "1":
    print("111")
    username = input("Write your username:")
    password = input("Write your password:")
    sql = "Select 1 FROM users Where username = %s and password = %s  Limit 1"
    mycursor.execute(
        sql,(username,password)
    )
    exists = mycursor.fetchone() is not None
    if exists:
        print("congrats this exists ")
        PandasLearning.climate_datamodel()
    else:
        print("Password or user is incorrect or does not exist")
        

    # check if it exists then go to climate model 
elif Initalinput == "2":
    newusername = input("Create a username:")
    newpassword = input("Write a password:")
    sql = "INSERT INTO users (username,password) VALUES (%s,%s)"
    mycursor.execute(
        sql,(newusername, newpassword)
        )
    conn.commit()
    print("user created")
else:

    print("write a proper number ya cunt")

# Create user and password interface that updates database 

