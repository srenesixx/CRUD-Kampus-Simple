from flask import jsonify, request
from usecases.usecase_mahasiswa import UsecaseMahasiswa


class HandlerMahasiswa:

    @staticmethod
    def getAll():
        return jsonify(UsecaseMahasiswa.getAll())

    @staticmethod
    def getSingle():
        nim = request.json.get("nim")
        return jsonify(UsecaseMahasiswa.getSingle(nim))

    @staticmethod
    def post():
        data = request.json
        return jsonify(UsecaseMahasiswa.post(data))

    @staticmethod
    def update():
        data = request.json
        return jsonify(UsecaseMahasiswa.update(data))

    @staticmethod
    def delete():
        nim = request.json.get("nim")
        return jsonify(UsecaseMahasiswa.delete(nim))
