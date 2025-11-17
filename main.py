import sys
import os

# Tambahkan root folder ke sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from flask import Flask
from routes.mahasiswa_route import mahasiswa_bp
from routes.fakultas_route import fakultas_bp
from routes.prodi_route import prodi_bp
from routes.matakuliah_route import matakuliah_bp
from routes.kelas_route import kelas_bp  # Tambahkan blueprint Kelas
from models.database import Base, engine

# Import semua model supaya SQLAlchemy mengenal tabel
import models

app = Flask(__name__)

# Register semua blueprint
app.register_blueprint(mahasiswa_bp)
app.register_blueprint(fakultas_bp)
app.register_blueprint(prodi_bp)
app.register_blueprint(matakuliah_bp)
app.register_blueprint(kelas_bp)  # Register kelas

# Buat tabel otomatis jika belum ada
Base.metadata.create_all(bind=engine)
print("Tabel Mahasiswa, Prodi, Fakultas, Matakuliah, Kelas siap digunakan (otomatis dibuat jika belum ada).")

@app.route('/')
def index():
    return "API Mahasiswa, Prodi, Fakultas, Matakuliah, Kelas siap digunakan!"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8005, debug=True)
