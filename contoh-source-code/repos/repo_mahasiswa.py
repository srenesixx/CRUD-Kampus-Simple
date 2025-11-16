from sqlalchemy.orm import Session
from models.model_mahasiswa import Mahasiswa
from repos.koneksi import get_db_session

class RepoMahasiswa:

    @staticmethod
    def getAll():
        session: Session = get_db_session()
        try:
            rows = session.query(Mahasiswa).order_by(Mahasiswa.nama.asc()).all()
            result = []
            for m in rows:
                result.append({
                    "nim": m.nim,
                    "nama": m.nama,
                    "tahun_masuk": m.tahun_masuk,
                    "alamat": m.alamat,
                    "tanggal_lahir": m.tanggal_lahir.strftime("%Y-%m-%d") if m.tanggal_lahir else None,
                    "id_prodi": m.id_prodi,
                    "nama_prodi": m.prodi.nama_prodi if m.prodi else None  # ambil dari relationship
                })
            return result
        finally:
            session.close()

    @staticmethod
    def getSingle(nim):
        session: Session = get_db_session()
        try:
            m = session.query(Mahasiswa).filter(Mahasiswa.nim == nim).first()
            if not m:
                return None
            return {
                "nim": m.nim,
                "nama": m.nama,
                "tahun_masuk": m.tahun_masuk,
                "alamat": m.alamat,
                "tanggal_lahir": m.tanggal_lahir.strftime("%Y-%m-%d") if m.tanggal_lahir else None,
                "id_prodi": m.id_prodi,
                "nama_prodi": m.prodi.nama_prodi if m.prodi else None  # ambil dari relationship
            }
        finally:
            session.close()

    @staticmethod
    def insert(data):
        session: Session = get_db_session()
        try:
            new_m = Mahasiswa(
                nim=data['nim'],
                nama=data['nama'],
                tahun_masuk=data['tahun_masuk'],
                alamat=data.get('alamat'),
                tanggal_lahir=data.get('tanggal_lahir'),
                id_prodi=data.get('id_prodi')
            )
            session.add(new_m)
            session.commit()
            return new_m.nim
        finally:
            session.close()

    @staticmethod
    def update(data):
        session: Session = get_db_session()
        try:
            m = session.query(Mahasiswa).filter(Mahasiswa.nim == data['nim']).first()
            if not m:
                return False
            m.nama = data['nama']
            m.tahun_masuk = data['tahun_masuk']
            m.alamat = data.get('alamat')
            m.tanggal_lahir = data.get('tanggal_lahir')
            m.id_prodi = data.get('id_prodi')
            session.commit()
            return True
        finally:
            session.close()

    @staticmethod
    def delete(nim):
        session: Session = get_db_session()
        try:
            m = session.query(Mahasiswa).filter(Mahasiswa.nim == nim).first()
            if not m:
                return False
            session.delete(m)
            session.commit()
            return True
        finally:
            session.close()
