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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

