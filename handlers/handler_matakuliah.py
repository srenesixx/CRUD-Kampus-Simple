from flask import jsonify, request
from usecases.usecase_matakuliah import UsecaseMatakuliah


class HandlerMatakuliah:

    @staticmethod
    def getAll():
        return jsonify(UsecaseMatakuliah.getAll())

    @staticmethod
    def getSingle():
        kode_matakuliah = request.json.get("kode_matakuliah")
        return jsonify(UsecaseMatakuliah.getSingle(kode_matakuliah))

    @staticmethod
    def post():
        data = request.json
        return jsonify(UsecaseMatakuliah.post(data))

    @staticmethod
    def update():
        data = request.json
        return jsonify(UsecaseMatakuliah.update(data))

    @staticmethod
    def delete():
        kode_matakuliah = request.json.get("kode_matakuliah")
        return jsonify(UsecaseMatakuliah.delete(kode_matakuliah))
