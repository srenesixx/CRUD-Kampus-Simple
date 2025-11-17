from repos.repo_prodi import RepoProdi
from repos.repo_fakultas import RepoFakultas

class UsecaseProdi:

    @staticmethod
    def getAll():
        data = RepoProdi.getAll()
        return data  # langsung return list dict

    @staticmethod
    def getSingle(id_prodi):
        p = RepoProdi.getSingle(id_prodi)
        if not p:
            return {"error": "Prodi tidak ditemukan"}
        return p

    @staticmethod
    def post(data):
        # Validasi fakultas
        f = RepoFakultas.getSingle(data.get('id_fakultas'))
        if not f:
            return {"error": "Fakultas tidak ditemukan"}, 400

        # Cek duplicate kode_prodi
        existing = RepoProdi.getAll()
        if any(p['kode_prodi'] == data.get('kode_prodi') for p in existing):
            return {"error": "Kode prodi sudah ada"}, 400

        inserted_id = RepoProdi.insert(data)
        p = RepoProdi.getSingle(inserted_id)
        return {"message": "Prodi berhasil dibuat", "data": p}

    @staticmethod
    def update(data):
        existing = RepoProdi.getSingle(data.get('id_prodi'))
        if not existing:
            return {"error": "Prodi tidak ditemukan"}, 404

        # Validasi fakultas jika diubah
        if 'id_fakultas' in data:
            f = RepoFakultas.getSingle(data['id_fakultas'])
            if not f:
                return {"error": "Fakultas tidak ditemukan"}, 400

        # Cek duplicate kode_prodi (kecuali untuk dirinya sendiri)
        all_data = RepoProdi.getAll()
        for p in all_data:
            if p['kode_prodi'] == data.get('kode_prodi') and p['id_prodi'] != data.get('id_prodi'):
                return {"error": "Kode prodi sudah digunakan"}, 400

        RepoProdi.update(data)
        updated = RepoProdi.getSingle(data.get('id_prodi'))
        return {"message": "Prodi berhasil diupdate", "data": updated}

    @staticmethod
    def delete(id_prodi):
        existing = RepoProdi.getSingle(id_prodi)
        if not existing:
            return {"error": "Prodi tidak ditemukan"}, 404
        RepoProdi.delete(id_prodi)
        return {"message": f"Prodi {id_prodi} berhasil dihapus"}
