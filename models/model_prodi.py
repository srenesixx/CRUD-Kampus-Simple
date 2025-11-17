from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.database import Base
from models.model_fakultas import Fakultas

class Prodi(Base):
    __tablename__ = "prodi"

    id_prodi = Column(Integer, primary_key=True, index=True)
    kode_prodi = Column(String(10), unique=True, nullable=False)
    nama_prodi = Column(String(100), nullable=False)
    id_fakultas = Column(Integer, ForeignKey("fakultas.id_fakultas"), nullable=False)

    fakultas = relationship("Fakultas", back_populates="prodi")
    mahasiswa = relationship("Mahasiswa", back_populates="prodi", cascade="all, delete")
