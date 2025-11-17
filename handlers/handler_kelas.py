from flask import jsonify, request
from usecases.usecase_kelas import UsecaseKelas


class HandlerKelas:

    @staticmethod
    def getAll():
        return jsonify(UsecaseKelas.getAll())

    @staticmethod
    def getSingle():
        id_kelas = request.json.get("id_kelas")
        return jsonify(UsecaseKelas.getSingle(id_kelas))

    @staticmethod
    def post():
        data = request.json
        return jsonify(UsecaseKelas.post(data))

    @staticmethod
    def update():
        data = request.json
        return jsonify(UsecaseKelas.update(data))

    @staticmethod
    def delete():
        id_kelas = request.json.get("id_kelas")
        return jsonify(UsecaseKelas.delete(id_kelas))

    @staticmethod
    def assignMahasiswa():
        data = request.json
        kode_matakuliah = data.get("kode_matakuliah")
        nim = data.get("nim")
        return jsonify(UsecaseKelas.assignMahasiswa(kode_matakuliah, nim))

    @staticmethod
    def removeMahasiswa():
        data = request.json
        kode_matakuliah = data.get("kode_matakuliah")
        nim = data.get("nim")
        return jsonify(UsecaseKelas.removeMahasiswa(kode_matakuliah, nim))
