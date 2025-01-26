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

@app.route('/aerolineas/<int:id>', methods=['DELETE'])
def eliminar_aerolinea(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM aerolineas WHERE ID = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Aerolinea eliminada exitosamente"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
