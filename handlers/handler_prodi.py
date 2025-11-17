from flask import jsonify, request
from usecases.usecase_prodi import UsecaseProdi  # absolute import

class HandlerProdi:

    @staticmethod
    def getAll():
        return jsonify(UsecaseProdi.getAll())

    @staticmethod
    def getSingle():
        id_prodi = request.json.get("id_prodi")
        return jsonify(UsecaseProdi.getSingle(id_prodi))

    @staticmethod
    def post():
        data = request.json
        return jsonify(UsecaseProdi.post(data))

    @staticmethod
    def update():
        data = request.json
        return jsonify(UsecaseProdi.update(data))

    @staticmethod
    def delete():
        id_prodi = request.json.get("id_prodi")
        return jsonify(UsecaseProdi.delete(id_prodi))
