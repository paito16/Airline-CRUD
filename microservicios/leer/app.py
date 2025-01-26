from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host='db',
        user='root',
        password='root',
        database='db_aerolinea'
    )

@app.route('/aerolineas', methods=['GET'])
def leer_aerolineas():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM aerolineas")
    aerolineas = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(aerolineas)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
