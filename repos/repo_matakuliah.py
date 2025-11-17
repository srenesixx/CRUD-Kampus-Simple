from sqlalchemy.orm import Session
from models.model_matakuliah import Matakuliah
from repos.koneksi import get_db_session

class RepoMatakuliah:

    # ---------------- CRUD Matakuliah ----------------
    @staticmethod
    def getAll():
        session: Session = get_db_session()
        try:
            rows = session.query(Matakuliah).order_by(Matakuliah.nama.asc()).all()
            result = []
            for m in rows:
                # jumlah mahasiswa yang mengambil matakuliah
                count = session.query(Matakuliah).filter(
                    Matakuliah.kode_matakuliah == m.kode_matakuliah
                ).count()
                result.append({
                    "kode_matakuliah": m.kode_matakuliah,
                    "nama": m.nama,
                    "sks": m.sks,
                    "semester": m.semester,
                    "jumlah_mahasiswa": count
                })
            return result
        finally:
            session.close()

    @staticmethod
    def getSingle(kode_matakuliah):
        session: Session = get_db_session()
        try:
            m = session.query(Matakuliah).filter(Matakuliah.kode_matakuliah == kode_matakuliah).first()
            if not m:
                return None

            mahasiswa_list = session.query(Matakuliah).filter(
                Matakuliah.kode_matakuliah == kode_matakuliah
            ).all()
            mahasiswa_nim = [mm.nim for mm in mahasiswa_list]

            return {
                "kode_matakuliah": m.kode_matakuliah,
                "nama": m.nama,
                "sks": m.sks,
                "semester": m.semester,
                "mahasiswa": mahasiswa_nim
            }
        finally:
            session.close()

    @staticmethod
    def insert(data):
        session: Session = get_db_session()
        try:
            new_m = Matakuliah(
                kode_matakuliah=data['kode_matakuliah'],
                nama=data['nama'],
                sks=data.get('sks', 0),
                semester=data.get('semester', 1)
            )
            session.add(new_m)
            session.commit()
            return new_m.kode_matakuliah
        finally:
            session.close()

    @staticmethod
    def update(data):
        session: Session = get_db_session()
        try:
            m = session.query(Matakuliah).filter(Matakuliah.kode_matakuliah == data['kode_matakuliah']).first()
            if not m:
                return False
            m.nama = data['nama']
            m.sks = data.get('sks', m.sks)
            m.semester = data.get('semester', m.semester)
            session.commit()
            return True
        finally:
            session.close()

    @staticmethod
    def delete(kode_matakuliah):
        session: Session = get_db_session()
        try:
            # Hapus relasi mahasiswa ↔ matakuliah
            session.query(Matakuliah).filter(
                Matakuliah.kode_matakuliah == kode_matakuliah
            ).delete()

            # Hapus matakuliah
            m = session.query(Matakuliah).filter(Matakuliah.kode_matakuliah == kode_matakuliah).first()
            if not m:
                return False
            session.delete(m)
            session.commit()
            return True
        finally:
            session.close()

    # ---------------- Relasi Mahasiswa ↔ Matakuliah ----------------
    @staticmethod
    def assignMahasiswa(nim, kode_matakuliah):
        session: Session = get_db_session()
        try:
            exists = session.query(Matakuliah).filter(
                Matakuliah.nim == nim,
                Matakuliah.kode_matakuliah == kode_matakuliah
            ).first()
            if exists:
                return False

            mm = Matakuliah(nim=nim, kode_matakuliah=kode_matakuliah)
            session.add(mm)
            session.commit()
            return True
        finally:
            session.close()

    @staticmethod
    def removeMahasiswa(nim, kode_matakuliah):
        session: Session = get_db_session()
        try:
            mm = session.query(Matakuliah).filter(
                Matakuliah.nim == nim,
                Matakuliah.kode_matakuliah == kode_matakuliah
            ).first()
            if not mm:
                return False
            session.delete(mm)
            session.commit()
            return True
        finally:
            session.close()

    @staticmethod
    def getMahasiswaByMatakuliah(kode_matakuliah):
        session: Session = get_db_session()
        try:
            rows = session.query(Matakuliah).filter(
                Matakuliah.kode_matakuliah == kode_matakuliah
            ).all()
            return [r.nim for r in rows]
        finally:
            session.close()

    @staticmethod
    def countMahasiswa(kode_matakuliah):
        session: Session = get_db_session()
        try:
            return session.query(Matakuliah).filter(
                Matakuliah.kode_matakuliah == kode_matakuliah
            ).count()
        finally:
            session.close()
