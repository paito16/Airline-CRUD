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

@app.route('/aerolineas/<int:id>', methods=['PUT'])
def actualizar_aerolinea(id):
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE aerolineas SET nombre = %s, numero_aviones = %s WHERE ID = %s",
                   (data['nombre'], data['numero_aviones'], id))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Aerolinea actualizada exitosamente"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)

