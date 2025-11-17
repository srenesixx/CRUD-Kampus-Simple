from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from models.database import Base
from models.model_prodi import Prodi

class Mahasiswa(Base):
    __tablename__ = "mahasiswa"

    nim = Column(String(20), primary_key=True, index=True)
    nama = Column(String(100), nullable=False)
    tahun_masuk = Column(Integer, nullable=False)
    alamat = Column(String)
    tanggal_lahir = Column(Date)
    id_prodi = Column(Integer, ForeignKey("prodi.id_prodi"))

    prodi = relationship("Prodi", back_populates="mahasiswa")
