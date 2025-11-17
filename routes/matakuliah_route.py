from flask import Blueprint
from handlers.handler_matakuliah import HandlerMatakuliah  # absolute import

matakuliah_bp = Blueprint('matakuliah_bp', __name__)

@matakuliah_bp.route('/matakuliah/get-all', methods=['GET'])
def getAll():
    return HandlerMatakuliah.getAll()

@matakuliah_bp.route('/matakuliah/get-single', methods=['POST'])
def getSingle():
    return HandlerMatakuliah.getSingle()

@matakuliah_bp.route('/matakuliah/post', methods=['POST'])
def post():
    return HandlerMatakuliah.post()

@matakuliah_bp.route('/matakuliah/update', methods=['PUT'])
def update():
    return HandlerMatakuliah.update()

@matakuliah_bp.route('/matakuliah/delete', methods=['DELETE'])
def delete():
    return HandlerMatakuliah.delete()
