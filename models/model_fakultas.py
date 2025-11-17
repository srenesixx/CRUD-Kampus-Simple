from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.database import Base

class Fakultas(Base):
    __tablename__ = "fakultas"

    id_fakultas = Column(Integer, primary_key=True, index=True)
    kode_fakultas = Column(String(10), unique=True, nullable=False)
    nama_fakultas = Column(String(100), nullable=False)

    prodi = relationship("Prodi", back_populates="fakultas", cascade="all, delete")
