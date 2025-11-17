from repos.repo_kelas import RepoKelas
from repos.repo_matakuliah import RepoMatakuliah
from repos.repo_mahasiswa import RepoMahasiswa

class UsecaseKelas:

    @staticmethod
    def getAll():
        return RepoKelas.getAll()

    @staticmethod
    def getSingle(id_kelas):
        k = RepoKelas.getSingle(id_kelas)
        if not k:
            return {"error": "Kelas tidak ditemukan"}, 404
        return k

    @staticmethod
    def post(data):
        # Validasi matakuliah
        if 'kode_matakuliah' in data and not RepoMatakuliah.getSingle(data['kode_matakuliah']):
            return {"error": "Matakuliah tidak ditemukan"}, 400

        # Cek duplicate kelas (kode_matakuliah + nama_kelas)
        existing_classes = RepoKelas.getAll()
        if any(c['kode_matakuliah'] == data['kode_matakuliah'] and c['nama_kelas'] == data['nama_kelas'] for c in existing_classes):
            return {"error": "Kelas sudah ada"}, 400

        RepoKelas.insert(data)
        k = RepoKelas.getSingle(data['id_kelas'])
        return {"message": "Kelas berhasil dibuat", "data": k}

    @staticmethod
    def update(data):
        existing = RepoKelas.getSingle(data.get('id_kelas'))
        if not existing:
            return {"error": "Kelas tidak ditemukan"}, 404

        # Validasi matakuliah jika diubah
        if 'kode_matakuliah' in data and not RepoMatakuliah.getSingle(data['kode_matakuliah']):
            return {"error": "Matakuliah tidak ditemukan"}, 400

        RepoKelas.update(data)
        updated = RepoKelas.getSingle(data['id_kelas'])
        return {"message": "Kelas berhasil diupdate", "data": updated}

    @staticmethod
    def delete(id_kelas):
        existing = RepoKelas.getSingle(id_kelas)
        if not existing:
            return {"error": "Kelas tidak ditemukan"}, 404

        RepoKelas.delete(id_kelas)
        return {"message": f"Kelas {id_kelas} berhasil dihapus"}

    @staticmethod
    def assignMahasiswa(kode_matakuliah, nim):
        # Pastikan matakuliah dan mahasiswa ada
        if not RepoMatakuliah.getSingle(kode_matakuliah):
            return {"error": "Matakuliah tidak ditemukan"}, 404
        if not RepoMahasiswa.getSingle(nim):
            return {"error": "Mahasiswa tidak ditemukan"}, 404

        # Cek apakah mahasiswa sudah terdaftar di kelas
        if RepoKelas.exists(nim, kode_matakuliah):
            return {"error": "Mahasiswa sudah terdaftar di kelas ini"}, 400

        RepoKelas.assignMahasiswa(nim, kode_matakuliah)
        return {"message": f"Mahasiswa {nim} berhasil ditambahkan ke kelas {kode_matakuliah}"}

    @staticmethod
    def removeMahasiswa(kode_matakuliah, nim):
        if not RepoKelas.exists(nim, kode_matakuliah):
            return {"error": "Mahasiswa tidak terdaftar di kelas ini"}, 404

        RepoKelas.removeMahasiswa(nim, kode_matakuliah)
        return {"message": f"Mahasiswa {nim} berhasil dihapus dari kelas {kode_matakuliah}"}
