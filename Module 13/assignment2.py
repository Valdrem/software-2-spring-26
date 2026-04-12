from flask import Flask, request
import mysql.connector
conn = mysql.connector.connect(host='127.0.0.1',port=3306,database='flight_game',user='root',password='',autocommit=True)

app = Flask(__name__)
@app.route('/kentta/<icao>')

def airport(icao):

    sql = "SELECT ident, name, municipality FROM airport WHERE ident = %s"
    cur = conn.cursor()
    cur.execute(sql, (icao.upper(),))
    airport_data = cur.fetchall()

    for a_data in airport_data:
        airport_dict = {
            "ICAO": a_data[0],
            "Name": a_data[1],
            "Municipality": a_data[2]
        }

    return airport_dict

app.run(use_reloader=True, host='127.0.0.1', port=3000)

