from flask import Blueprint
from handlers.handler_kelas import HandlerKelas  # absolute import

kelas_bp = Blueprint('kelas_bp', __name__)

@kelas_bp.route('/kelas/get-all', methods=['GET'])
def getAll():
    return HandlerKelas.getAll()

@kelas_bp.route('/kelas/get-single', methods=['POST'])
def getSingle():
    return HandlerKelas.getSingle()

@kelas_bp.route('/kelas/post', methods=['POST'])
def post():
    return HandlerKelas.post()

@kelas_bp.route('/kelas/update', methods=['PUT'])
def update():
    return HandlerKelas.update()

@kelas_bp.route('/kelas/delete', methods=['DELETE'])
def delete():
    return HandlerKelas.delete()

# Endpoint untuk assign mahasiswa ke kelas
@kelas_bp.route('/kelas/assign-mahasiswa', methods=['POST'])
def assignMahasiswa():
    return HandlerKelas.assignMahasiswa()

# Endpoint untuk remove mahasiswa dari kelas
@kelas_bp.route('/kelas/remove-mahasiswa', methods=['POST'])
def removeMahasiswa():
    return HandlerKelas.removeMahasiswa()
