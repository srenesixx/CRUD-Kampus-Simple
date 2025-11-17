from flask import Blueprint
from handlers.handler_mahasiswa import HandlerMahasiswa  # absolute import

mahasiswa_bp = Blueprint('mahasiswa_bp', __name__)

@mahasiswa_bp.route('/mahasiswa/get-all', methods=['GET'])
def getAll():
    return HandlerMahasiswa.getAll()

@mahasiswa_bp.route('/mahasiswa/get-single', methods=['POST'])
def getSingle():
    return HandlerMahasiswa.getSingle()

@mahasiswa_bp.route('/mahasiswa/post', methods=['POST'])
def post():
    return HandlerMahasiswa.post()

@mahasiswa_bp.route('/mahasiswa/update', methods=['PUT'])
def update():
    return HandlerMahasiswa.update()

@mahasiswa_bp.route('/mahasiswa/delete', methods=['DELETE'])
def delete():
    return HandlerMahasiswa.delete()
