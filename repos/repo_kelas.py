from sqlalchemy.orm import Session
from models.model_kelas import Kelas, mahasiswa_kelas
from models.model_mahasiswa import Mahasiswa
from models.model_matakuliah import Matakuliah
from repos.koneksi import get_db_session

class RepoKelas:

    # ---------------- CRUD Kelas ----------------
    @staticmethod
    def getAll():
        session: Session = get_db_session()
        try:
            rows = session.query(Kelas).order_by(Kelas.nama_kelas.asc()).all()
            result = []
            for k in rows:
                mahasiswa_list = [m.nim for m in k.mahasiswa]
                result.append({
                    "id_kelas": k.id_kelas,
                    "kode_matakuliah": k.kode_matakuliah,
                    "nama_kelas": k.nama_kelas,
                    "dosen": k.dosen,
                    "mahasiswa": mahasiswa_list
                })
            return result
        finally:
            session.close()

    @staticmethod
    def getSingle(id_kelas):
        session: Session = get_db_session()
        try:
            k = session.query(Kelas).filter(Kelas.id_kelas == id_kelas).first()
            if not k:
                return None
            mahasiswa_list = [m.nim for m in k.mahasiswa]
            return {
                "id_kelas": k.id_kelas,
                "kode_matakuliah": k.kode_matakuliah,
                "nama_kelas": k.nama_kelas,
                "dosen": k.dosen,
                "mahasiswa": mahasiswa_list
            }
        finally:
            session.close()

    @staticmethod
    def insert(data):
        session: Session = get_db_session()
        try:
            new_k = Kelas(
                kode_matakuliah=data['kode_matakuliah'],
                nama_kelas=data['nama_kelas'],
                dosen=data.get('dosen')
            )
            session.add(new_k)
            session.commit()
            return new_k.id_kelas
        finally:
            session.close()

    @staticmethod
    def update(data):
        session: Session = get_db_session()
        try:
            k = session.query(Kelas).filter(Kelas.id_kelas == data['id_kelas']).first()
            if not k:
                return False
            k.kode_matakuliah = data.get('kode_matakuliah', k.kode_matakuliah)
            k.nama_kelas = data.get('nama_kelas', k.nama_kelas)
            k.dosen = data.get('dosen', k.dosen)
            session.commit()
            return True
        finally:
            session.close()

    @staticmethod
    def delete(id_kelas):
        session: Session = get_db_session()
        try:
            k = session.query(Kelas).filter(Kelas.id_kelas == id_kelas).first()
            if not k:
                return False
            # Hapus relasi mahasiswa ↔ kelas
            k.mahasiswa.clear()
            session.delete(k)
            session.commit()
            return True
        finally:
            session.close()

    # ---------------- Relasi Mahasiswa ↔ Kelas ----------------
    @staticmethod
    def assignMahasiswa(nim, id_kelas):
        session: Session = get_db_session()
        try:
            k = session.query(Kelas).filter(Kelas.id_kelas == id_kelas).first()
            m = session.query(Mahasiswa).filter(Mahasiswa.nim == nim).first()
            if not k or not m:
                return False
            if m in k.mahasiswa:
                return False
            k.mahasiswa.append(m)
            session.commit()
            return True
        finally:
            session.close()

    @staticmethod
    def removeMahasiswa(nim, id_kelas):
        session: Session = get_db_session()
        try:
            k = session.query(Kelas).filter(Kelas.id_kelas == id_kelas).first()
            m = session.query(Mahasiswa).filter(Mahasiswa.nim == nim).first()
            if not k or not m:
                return False
            if m not in k.mahasiswa:
                return False
            k.mahasiswa.remove(m)
            session.commit()
            return True
        finally:
            session.close()

    @staticmethod
    def exists(nim, id_kelas):
        session: Session = get_db_session()
        try:
            k = session.query(Kelas).filter(Kelas.id_kelas == id_kelas).first()
            if not k:
                return False
            return any(m.nim == nim for m in k.mahasiswa)
        finally:
            session.close()
