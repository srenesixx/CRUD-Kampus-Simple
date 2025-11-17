from sqlalchemy import Column, String, Integer, Table, ForeignKey
from sqlalchemy.orm import relationship
from models.database import Base
from models.model_mahasiswa import Mahasiswa

# Tabel asosiasi many-to-many mahasiswa ↔ matakuliah
class MahasiswaMatakuliah(Base):
    __tablename__ = "mahasiswa_matakuliah"

    nim = Column(String(20), ForeignKey("mahasiswa.nim"), primary_key=True)
    kode_matakuliah = Column(String(20), ForeignKey("matakuliah.kode_matakuliah"), primary_key=True)


class Matakuliah(Base):
    __tablename__ = "matakuliah"

    kode_matakuliah = Column(String(20), primary_key=True, index=True)
    nama = Column(String(100), nullable=False)
    sks = Column(Integer, default=0)
    semester = Column(Integer, default=1)

    # Relasi many-to-many ke Mahasiswa melalui MahasiswaMatakuliah
    mahasiswa = relationship(
        "Mahasiswa",
        secondary="mahasiswa_matakuliah",
        back_populates="matakuliah"
    )

# Tambahkan relasi back_populates di Mahasiswa agar dua arah
Mahasiswa.matakuliah = relationship(
    "Matakuliah",
    secondary="mahasiswa_matakuliah",
    back_populates="mahasiswa"
)
