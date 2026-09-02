from flask import Flask
import os
import pymysql

app = Flask(__name__)


@app.route("/")
def home():
    try:
        connection = pymysql.connect(
            host=os.getenv("DB_HOST", "db"),
            user=os.getenv("DB_USER", "appuser"),
            password=os.getenv("DB_PASSWORD", "apppassword"),
            database=os.getenv("DB_NAME", "appdb"),
        )
        connection.close()
        return "API Flask funcionando y conectada a MySQL", 200
    except Exception as e:
        return f"Error de conexión a MySQL: {e}", 500


@app.route("/health")
def health():
    return "OK", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)