from sqlalchemy.orm import Session, joinedload
from models.model_prodi import Prodi
from repos.koneksi import get_db_session  # returns SQLAlchemy session


class RepoProdi:

    @staticmethod
    def getAll():
        session: Session = get_db_session()
        try:
            rows = session.query(Prodi).order_by(Prodi.nama_prodi.asc()).all()
            result = []
            for r in rows:
                result.append({
                    "id_prodi": r.id_prodi,
                    "kode_prodi": r.kode_prodi,
                    "nama_prodi": r.nama_prodi,
                    "id_fakultas": r.id_fakultas,
                    "nama_fakultas": r.fakultas.nama_fakultas if r.fakultas else None,
                    "mahasiswa": [
                        {
                            "nim": m.nim,
                            "nama": m.nama,
                            "tahun_masuk": m.tahun_masuk,
                            "alamat": m.alamat,
                            "tanggal_lahir": m.tanggal_lahir.strftime("%Y-%m-%d") if m.tanggal_lahir else None
                        } for m in r.mahasiswa
                    ]
                })
            return result
        finally:
            session.close()

    @staticmethod
    def getSingle(id_prodi):
        session: Session = get_db_session()
        try:
            p = session.query(Prodi).options(joinedload(Prodi.mahasiswa))\
                .filter(Prodi.id_prodi == id_prodi).first()
            if not p:
                return None
            return {
                "id_prodi": p.id_prodi,
                "kode_prodi": p.kode_prodi,
                "nama_prodi": p.nama_prodi,
                "id_fakultas": p.id_fakultas,
                "nama_fakultas": p.fakultas.nama_fakultas if p.fakultas else None,
                "mahasiswa": [
                    {
                        "nim": m.nim,
                        "nama": m.nama,
                        "tahun_masuk": m.tahun_masuk,
                        "alamat": m.alamat,
                        "tanggal_lahir": m.tanggal_lahir.strftime("%Y-%m-%d") if m.tanggal_lahir else None
                    } for m in p.mahasiswa
                ]
            }
        finally:
            session.close()

    @staticmethod
    def insert(data):
        session: Session = get_db_session()
        try:
            new_prodi = Prodi(
                kode_prodi=data['kode_prodi'],
                nama_prodi=data['nama_prodi'],
                id_fakultas=data['id_fakultas']
            )
            session.add(new_prodi)
            session.commit()
            session.refresh(new_prodi)
            return new_prodi.id_prodi
        finally:
            session.close()

    @staticmethod
    def update(data):
        session: Session = get_db_session()
        try:
            p = session.query(Prodi).filter(Prodi.id_prodi == data['id_prodi']).first()
            if not p:
                return False
            p.kode_prodi = data['kode_prodi']
            p.nama_prodi = data['nama_prodi']
            p.id_fakultas = data['id_fakultas']
            session.commit()
            return True
        finally:
            session.close()

    @staticmethod
    def delete(id_prodi):
        session: Session = get_db_session()
        try:
            p = session.query(Prodi).filter(Prodi.id_prodi == id_prodi).first()
            if not p:
                return False
            session.delete(p)
            session.commit()
            return True
        finally:
            session.close()
