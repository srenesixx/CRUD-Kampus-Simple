from flask import jsonify, request
from usecases.usecase_fakultas import UsecaseFakultas  # absolute import

class HandlerFakultas:

    @staticmethod
    def getAll():
        return jsonify(UsecaseFakultas.getAll())

    @staticmethod
    def getSingle():
        id_fakultas = request.json.get("id_fakultas")
        return jsonify(UsecaseFakultas.getSingle(id_fakultas))

    @staticmethod
    def post():
        data = request.json
        return jsonify(UsecaseFakultas.post(data))

    @staticmethod
    def update():
        data = request.json
        return jsonify(UsecaseFakultas.update(data))

    @staticmethod
    def delete():
        id_fakultas = request.json.get("id_fakultas")
        return jsonify(UsecaseFakultas.delete(id_fakultas))
