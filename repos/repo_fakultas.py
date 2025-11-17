from sqlalchemy.orm import Session
from models.model_fakultas import Fakultas
from repos.koneksi import get_db_session  # returns a SQLAlchemy session


class RepoFakultas:

    @staticmethod
    def getAll():
        session: Session = get_db_session()
        try:
            rows = session.query(Fakultas).order_by(Fakultas.nama_fakultas.asc()).all()
            return [
                {"id_fakultas": r.id_fakultas, "kode_fakultas": r.kode_fakultas, "nama_fakultas": r.nama_fakultas}
                for r in rows
            ]
        finally:
            session.close()

    @staticmethod
    def getSingle(id_fakultas):
        session: Session = get_db_session()
        try:
            f = session.query(Fakultas).filter(Fakultas.id_fakultas == id_fakultas).first()
            if not f:
                return None
            return {"id_fakultas": f.id_fakultas, "kode_fakultas": f.kode_fakultas, "nama_fakultas": f.nama_fakultas}
        finally:
            session.close()

    @staticmethod
    def insert(data):
        session: Session = get_db_session()
        try:
            new_fakultas = Fakultas(
                kode_fakultas=data['kode_fakultas'],
                nama_fakultas=data['nama_fakultas']
            )
            session.add(new_fakultas)
            session.commit()
            session.refresh(new_fakultas)  # get the generated id
            return new_fakultas.id_fakultas
        finally:
            session.close()

    @staticmethod
    def update(data):
        session: Session = get_db_session()
        try:
            f = session.query(Fakultas).filter(Fakultas.id_fakultas == data['id_fakultas']).first()
            if not f:
                return False
            f.kode_fakultas = data['kode_fakultas']
            f.nama_fakultas = data['nama_fakultas']
            session.commit()
            return True
        finally:
            session.close()

    @staticmethod
    def delete(id_fakultas):
        session: Session = get_db_session()
        try:
            f = session.query(Fakultas).filter(Fakultas.id_fakultas == id_fakultas).first()
            if not f:
                return False
            session.delete(f)
            session.commit()
            return True
        finally:
            session.close()
