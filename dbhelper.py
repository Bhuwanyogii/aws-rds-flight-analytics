import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()


class DB:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host='bhuwan-mysql.cp8gaok8090x.ap-southeast-2.rds.amazonaws.com',
                user='admin',
                password=os.getenv("MYSQL_PASSWORD"),
                database='flights'
            )

            self.mycursor = self.conn.cursor()

            print("RDS connection successful!")
            print("Cursor created successfully!")

        except Exception as e:
            print("DATABASE CONNECTION ERROR:")
            print(e)
            raise

    def fetch_source_city(self):

        city = []
        self.mycursor.execute("""
            SELECT DISTINCT Source FROM flights
        """)

        data = self.mycursor.fetchall()

        for item in data:
            city.append(item[0])
        return city

    def fetch_destination_city(self, source):
        self.mycursor.execute("""
            SELECT DISTINCT Destination
            FROM flights
            WHERE Source = %s
        """, (source,))

        data = self.mycursor.fetchall()

        city = []

        for item in data:
            city.append(item[0])

        return city

    def fetch_all_flights(self, source, destination):
        self.mycursor.execute("""
        SELECT Airline, Route, Dep_time, Duration, Price FROM flights
        WHERE Source = '{}' AND Destination = '{}'
        """.format(source, destination))

        data = self.mycursor.fetchall()

        return data

    def fetch_airline_frequency(self):

        airline = []
        frequency = []

        self.mycursor.execute("""
        SELECT Airline, COUNT(*) FROM flights
        GROUP BY Airline
        """)

        data = self.mycursor.fetchall()

        for item in data:
            airline.append(item[0])
            frequency.append(item[1])

        return airline, frequency

    def busy_airport(self):
        self.mycursor.execute("""
        SELECT Source, COUNT(*) FROM (SELECT Source FROM flights
								UNION ALL
								SELECT Destination FROM flights) t
        GROUP BY t.Source
        ORDER BY COUNT(*) DESC
        """)

        city = []
        frequency = []

        data = self.mycursor.fetchall()

        for item in data:
            city.append(item[0])
            frequency.append(item[1])

        return city, frequency

    def daily_frequency(self):

        self.mycursor.execute("""
        SELECT Date_of_journey, COUNT(*) FROM flights
        GROUP BY Date_of_journey
        """)

        date = []
        frequency = []

        data = self.mycursor.fetchall()

        for item in data:
            date.append(item[0])
            frequency.append(item[1])

        return date, frequency

