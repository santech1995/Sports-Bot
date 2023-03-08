import mysql.connector

def DataInsertion(city,temp):
    mydatabase = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "root@123",
        database = "rasa_database"
    )

    mycursor = mydatabase.cursor()
    # sql = "CREATE TABLE weather_data (city VARCHAR(255),temperature VARCHAR(255))"
    sql = "INSERT INTO weather_data (city_name,temperature) VALUES ('?','?');".format(city,temp)
    mycursor.execute(sql)

    mydatabase.commit()

    print(mycursor.rowcount," records inserted") 

    return[]
