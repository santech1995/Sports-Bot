import mysql.connector

def DataInsertion(city,temp):
    mydatabase = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "root@123",
        database = "rasa_database"
        # auth_plugin='root@123'
    )

    mycursor = mydatabase.cursor()
    # sql = "CREATE TABLE weather_data (city VARCHAR(255),temperature VARCHAR(255))"
    # sql = "insert into weather_data VALUES({city},0);".format(city,0)
    sql = "insert into `weather_data` VALUES (%s,%s);"
    mycursor.execute(sql, (city, temp))

    mydatabase.commit()

    print(mycursor.rowcount," records inserted") 

