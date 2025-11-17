from models.database import SessionLocal

def get_db_session():
    """
    Mengembalikan session SQLAlchemy.
    Gunakan ini di repos atau handler.
    Contoh:
        with get_db_session() as session:
            session.query(Mahasiswa).all()
    """
    return SessionLocal()
