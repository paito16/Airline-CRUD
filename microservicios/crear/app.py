from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host='db',
        user='root',
        password='root',
        database='db_aerolinea'
    )

@app.route('/aerolineas', methods=['POST'])
def crear_aerolinea():
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO aerolineas (nombre, numero_aviones) VALUES (%s, %s)",
                   (data['nombre'], data['numero_aviones']))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Aerolinea creada exitosamente"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
