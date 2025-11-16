from flask import Blueprint, render_template, request, redirect, url_for
from models.database import SessionLocal
from models import Mahasiswa
import datetime

# Gunakan nama blueprint yang sama dengan main.py
mahasiswa_bp = Blueprint('mahasiswa_bp', __name__, template_folder='templates', static_folder='static')

# -------------------------------
# 🌸 ROUTES GUI MAHASISWA
# -------------------------------

@mahasiswa_bp.route('/mahasiswa')
def index():
    db = SessionLocal()
    mahasiswa_list = db.query(Mahasiswa).all()
    db.close()
    return render_template('index.html', mahasiswa_list=mahasiswa_list)


@mahasiswa_bp.route('/mahasiswa/form', methods=['GET', 'POST'])
def add_mahasiswa():
    if request.method == 'POST':
        db = SessionLocal()
        nim = request.form['nim']
        nama = request.form['nama']
        tahun_masuk = int(request.form['tahun_masuk'])
        alamat = request.form['alamat']
        tanggal_lahir = datetime.datetime.strptime(request.form['tanggal_lahir'], "%Y-%m-%d").date()

        new_mhs = Mahasiswa(
            nim=nim,
            nama=nama,
            tahun_masuk=tahun_masuk,
            alamat=alamat,
            tanggal_lahir=tanggal_lahir
        )
        db.add(new_mhs)
        db.commit()
        db.close()
        return redirect(url_for('mahasiswa_bp.index'))
    return render_template('form.html')


@mahasiswa_bp.route('/mahasiswa/detail/<string:nim>')
def detail_view(nim):
    db = SessionLocal()
    mahasiswa = db.query(Mahasiswa).filter(Mahasiswa.nim == nim).first()
    db.close()
    if not mahasiswa:
        return "Mahasiswa tidak ditemukan", 404
    return render_template('detail.html', mahasiswa=mahasiswa)


@mahasiswa_bp.route('/mahasiswa/delete/<string:nim>')
def delete_view(nim):
    db = SessionLocal()
    mahasiswa = db.query(Mahasiswa).filter(Mahasiswa.nim == nim).first()
    if mahasiswa:
        db.delete(mahasiswa)
        db.commit()
    db.close()
    return redirect(url_for('mahasiswa_bp.index'))
