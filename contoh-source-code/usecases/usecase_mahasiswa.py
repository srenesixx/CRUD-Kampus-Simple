from repos.repo_mahasiswa import RepoMahasiswa
from repos.repo_prodi import RepoProdi

class UsecaseMahasiswa:

    @staticmethod
    def getAll():
        return RepoMahasiswa.getAll()

    @staticmethod
    def getSingle(nim):
        m = RepoMahasiswa.getSingle(nim)
        if not m:
            return {"error": "Mahasiswa tidak ditemukan"}, 404
        return m

    @staticmethod
    def post(data):
        # Validasi prodi
        if 'id_prodi' in data and not RepoProdi.getSingle(data['id_prodi']):
            return {"error": "Prodi tidak ditemukan"}, 400

        # Cek duplicate NIM
        existing = RepoMahasiswa.getSingle(data['nim'])
        if existing:
            return {"error": "NIM sudah digunakan"}, 400

        RepoMahasiswa.insert(data)
        m = RepoMahasiswa.getSingle(data['nim'])
        return {"message": "Mahasiswa berhasil dibuat", "data": m}

    @staticmethod
    def update(data):
        existing = RepoMahasiswa.getSingle(data['nim'])
        if not existing:
            return {"error": "Mahasiswa tidak ditemukan"}, 404

        # Validasi prodi jika diubah
        if 'id_prodi' in data and not RepoProdi.getSingle(data['id_prodi']):
            return {"error": "Prodi tidak ditemukan"}, 400

        RepoMahasiswa.update(data)
        updated = RepoMahasiswa.getSingle(data['nim'])
        return {"message": "Mahasiswa berhasil diupdate", "data": updated}

    @staticmethod
    def delete(nim):
        existing = RepoMahasiswa.getSingle(nim)
        if not existing:
            return {"error": "Mahasiswa tidak ditemukan"}, 404

        RepoMahasiswa.delete(nim)
        return {"message": f"Mahasiswa {nim} berhasil dihapus"}
