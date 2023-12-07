import pymysql
import json
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/crime_weekday_data')
def crime_weekday_data():
    # Database connection details
    host = '127.0.0.1'
    user = 'fslllllki'
    password = 'wl90304zY!'
    db = 'crime_statistics'

    # Connect to the database
    connection = pymysql.connect(host=host, user=user, password=password, db=db)

    try:
        with connection.cursor() as cursor:
            sql = "SELECT Week_Day, Week_Day_Count, Week_Day_Count_SE, Week_Day_Count_NY FROM week_day_data"
            cursor.execute(sql)
            result = cursor.fetchall()
    finally:
        connection.close()

    # Convert data to a suitable format (e.g., a list of dictionaries)
    data = [{"Week_Day": row[0], "Week_Day_Count": row[1], "Week_Day_Count_SE": row[2], "Week_Day_Count_NY": row[3]} for row in result]

    # Convert the data to JSON
    json_data = json.dumps(data)

    # Return the JSON data
    return jsonify(data)

@app.route('/get_hourly_crime_stat')
def get_hourly_crime_stat():
    # Database connection details
    host = '127.0.0.1'
    user = 'fslllllki'
    password = 'wl90304zY!'
    db = 'crime_statistics'

    # Connect to the database
    connection = pymysql.connect(host=host, user=user, password=password, db=db)


    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM hourly_crime_stats"
            cursor.execute(sql)
            result = cursor.fetchall()
            data = [{"Hour": row[0], "Hour_Count": row[1], "Hour_Count_SE": row[2], "Hour_Count_NY": row[3]} for row in result]
    finally:
        connection.close()

    return jsonify(data)

@app.route('/get_monthly_crime_stat')
def get_monthly_crime_stat():
    # Database connection details
    host = '127.0.0.1'
    user = 'fslllllki'
    password = 'wl90304zY!'
    db = 'crime_statistics'

    # Connect to the database
    connection = pymysql.connect(host=host, user=user, password=password, db=db)

    try:
        with connection.cursor() as cursor:
            # Assuming your table is named 'monthly_crime_stats'
            sql = "SELECT * FROM monthly_stats"
            cursor.execute(sql)
            result = cursor.fetchall()
            # Adjust the row indices based on your table structure
            data = [{"Month": row[0], "Month_Count": row[1], "Month_Count_SE": row[2], "Month_Count_NY": row[3]} for row in result]
    finally:
        connection.close()

    return jsonify(data)


@app.route('/get_crime_type_stat')
def get_crime_type_stat():
    # Database connection details
    host = '127.0.0.1'
    user = 'fslllllki'
    password = 'wl90304zY!'
    db = 'crime_statistics'

    # Connect to the database
    connection = pymysql.connect(host=host, user=user, password=password, db=db)

    try:
        with connection.cursor() as cursor:
            # This SQL will count the number of occurrences of each Crime_Type
            # and join with the offense descriptions from the other table
            sql = """
            SELECT 
                t.Crime_Type_ID,
                t.Offense_Description,
                COUNT(d.Crime_Type) AS Crime_Count
            FROM 
                nyc_crime_data_instance d
            JOIN 
                nyc_crime_types t ON d.Crime_Type = t.Crime_Type_ID
            GROUP BY 
                t.Crime_Type_ID,
                t.Offense_Description;
            """
            cursor.execute(sql)
            result = cursor.fetchall()
            # Format the result into a list of dictionaries
            data = [{
                "Crime_Type_ID": row[0],
                "Offense_Description": row[1],
                "Crime_Count": row[2]
            } for row in result]
    finally:
        connection.close()

    return jsonify(data)    

@app.route('/get_crime_type_stat_seattle')
def get_crime_type_stat_seattle():
    # Database connection details
    host = '127.0.0.1'
    user = 'fslllllki'
    password = 'wl90304zY!'
    db = 'crime_statistics'

    # Connect to the database
    connection = pymysql.connect(host=host, user=user, password=password, db=db)

    try:
        with connection.cursor() as cursor:
            # This SQL will count the number of occurrences of each Crime_Type
            # and join with the offense descriptions from the other table
            sql = """
            SELECT 
                t.Crime_Type_ID,
                t.Offense_Description,
                COUNT(d.Crime_Type) AS Crime_Count
            FROM 
                seattle_crime_data_instance d
            JOIN 
                seattle_crime_types t ON d.Crime_Type = t.Crime_Type_ID
            GROUP BY 
                t.Crime_Type_ID,
                t.Offense_Description;
            """
            cursor.execute(sql)
            result = cursor.fetchall()
            # Format the result into a list of dictionaries
            data = [{
                "Crime_Type_ID": row[0],
                "Offense_Description": row[1],
                "Crime_Count": row[2]
            } for row in result]
    finally:
        connection.close()

    return jsonify(data)    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

