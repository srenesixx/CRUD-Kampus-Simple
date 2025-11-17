from repos.repo_matakuliah import RepoMatakuliah
from repos.repo_mahasiswa import RepoMahasiswa

class UsecaseMatakuliah:

    @staticmethod
    def getAll():
        data = RepoMatakuliah.getAll()
        # Bisa juga langsung tampilkan jumlah mahasiswa yang mengambil matakuliah
        for m in data:
            mahasiswa_count = RepoMahasiswa.countMahasiswa(m['kode_matakuliah'])
            m['jumlah_mahasiswa'] = mahasiswa_count
        return data

    @staticmethod
    def getSingle(kode_matakuliah):
        m = RepoMatakuliah.getSingle(kode_matakuliah)
        if not m:
            return {"error": "Matakuliah tidak ditemukan"}, 404
        
        # Tambahkan daftar mahasiswa yang mengambil matakuliah ini
        mahasiswa_list = RepoMahasiswa.getMahasiswaByMatakuliah(kode_matakuliah)
        m['mahasiswa'] = mahasiswa_list
        return m

    @staticmethod
    def post(data):
        # Cek duplicate kode_matakuliah
        existing = RepoMatakuliah.getSingle(data.get('kode_matakuliah'))
        if existing:
            return {"error": "Kode matakuliah sudah digunakan"}, 400

        RepoMatakuliah.insert(data)
        m = RepoMatakuliah.getSingle(data.get('kode_matakuliah'))
        return {"message": "Matakuliah berhasil dibuat", "data": m}

    @staticmethod
    def update(data):
        existing = RepoMatakuliah.getSingle(data.get('kode_matakuliah'))
        if not existing:
            return {"error": "Matakuliah tidak ditemukan"}, 404

        # Cek duplicate kode_matakuliah jika ingin diganti
        if 'kode_matakuliah_baru' in data:
            if RepoMatakuliah.getSingle(data['kode_matakuliah_baru']):
                return {"error": "Kode matakuliah baru sudah digunakan"}, 400
            data['kode_matakuliah'] = data.pop('kode_matakuliah_baru')

        RepoMatakuliah.update(data)
        updated = RepoMatakuliah.getSingle(data['kode_matakuliah'])
        return {"message": "Matakuliah berhasil diupdate", "data": updated}

    @staticmethod
    def delete(kode_matakuliah):
        existing = RepoMatakuliah.getSingle(kode_matakuliah)
        if not existing:
            return {"error": "Matakuliah tidak ditemukan"}, 404

        # Hapus relasi mahasiswa-matakuliah
        RepoMahasiswa.deleteByMatakuliah(kode_matakuliah)

        RepoMatakuliah.delete(kode_matakuliah)
        return {"message": f"Matakuliah {kode_matakuliah} berhasil dihapus"}

    @staticmethod
    def assignMahasiswa(kode_matakuliah, nim):
        # Pastikan matakuliah dan mahasiswa ada
        if not RepoMatakuliah.getSingle(kode_matakuliah):
            return {"error": "Matakuliah tidak ditemukan"}, 404
        if not RepoMahasiswa.getSingle(nim):
            return {"error": "Mahasiswa tidak ditemukan"}, 404

        # Cek apakah mahasiswa sudah terdaftar
        if RepoMahasiswa.exists(nim, kode_matakuliah):
            return {"error": "Mahasiswa sudah terdaftar di matakuliah ini"}, 400

        RepoMahasiswa.insert(nim, kode_matakuliah)
        return {"message": f"Mahasiswa {nim} berhasil ditambahkan ke matakuliah {kode_matakuliah}"}

    @staticmethod
    def removeMahasiswa(kode_matakuliah, nim):
        if not RepoMahasiswa.exists(nim, kode_matakuliah):
            return {"error": "Mahasiswa tidak terdaftar di matakuliah ini"}, 404

        RepoMahasiswa.delete(nim, kode_matakuliah)
        return {"message": f"Mahasiswa {nim} berhasil dihapus dari matakuliah {kode_matakuliah}"}
