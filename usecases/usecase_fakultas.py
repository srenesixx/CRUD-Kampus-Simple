from repos.repo_fakultas import RepoFakultas
from models.model_fakultas import Fakultas

class UsecaseFakultas:

    @staticmethod
    def getAll():
        data = RepoFakultas.getAll()
        # Convert ke dict langsung
        return data

    @staticmethod
    def getSingle(id_fakultas):
        f = RepoFakultas.getSingle(id_fakultas)
        if not f:
            return {"error": "Fakultas tidak ditemukan"}
        return f

    @staticmethod
    def post(data):
        # Cek jika kode_fakultas sudah ada
        existing = RepoFakultas.getAll()
        if any(f["kode_fakultas"] == data.get("kode_fakultas") for f in existing):
            return {"error": "Kode fakultas sudah ada"}, 400

        inserted_id = RepoFakultas.insert(data)
        f = RepoFakultas.getSingle(inserted_id)
        return {"message": "Fakultas berhasil dibuat", "data": f}

    @staticmethod
    def update(data):
        existing = RepoFakultas.getSingle(data.get("id_fakultas"))
        if not existing:
            return {"error": "Fakultas tidak ditemukan"}

        # Cek duplicate kode_fakultas (kecuali untuk dirinya sendiri)
        all_data = RepoFakultas.getAll()
        for f in all_data:
            if f["kode_fakultas"] == data.get("kode_fakultas") and f["id_fakultas"] != data.get("id_fakultas"):
                return {"error": "Kode fakultas sudah digunakan"}, 400

        RepoFakultas.update(data)
        updated = RepoFakultas.getSingle(data.get("id_fakultas"))
        return {"message": "Fakultas berhasil diupdate", "data": updated}

    @staticmethod
    def delete(id_fakultas):
        existing = RepoFakultas.getSingle(id_fakultas)
        if not existing:
            return {"error": "Fakultas tidak ditemukan"}
        RepoFakultas.delete(id_fakultas)
        return {"message": f"Fakultas {id_fakultas} berhasil dihapus"}
