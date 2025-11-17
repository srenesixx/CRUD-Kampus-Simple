from sqlalchemy import Column, String, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.database import Base
from models.model_mahasiswa import Mahasiswa
from models.model_matakuliah import Matakuliah

# Tabel asosiasi many-to-many antara Mahasiswa dan Kelas
mahasiswa_kelas = Table(
    "mahasiswa_kelas",
    Base.metadata,
    Column("nim", String(20), ForeignKey("mahasiswa.nim"), primary_key=True),
    Column("id_kelas", Integer, ForeignKey("kelas.id_kelas"), primary_key=True)
)

class Kelas(Base):
    __tablename__ = "kelas"

    id_kelas = Column(Integer, primary_key=True, autoincrement=True)
    kode_matakuliah = Column(String(20), ForeignKey("matakuliah.kode_matakuliah"), nullable=False)
    nama_kelas = Column(String(50), nullable=False)  # misal: A, B, C
    dosen = Column(String(100))  # opsional

    matakuliah = relationship("Matakuliah", back_populates="kelas")
    mahasiswa = relationship(
        "Mahasiswa",
        secondary=mahasiswa_kelas,
        back_populates="kelas"
    )

# Tambahkan back_populates ke model Mahasiswa dan Matakuliah
Mahasiswa.kelas = relationship(
    "Kelas",
    secondary=mahasiswa_kelas,
    back_populates="mahasiswa"
)

Matakuliah.kelas = relationship(
    "Kelas",
    back_populates="matakuliah"
)
