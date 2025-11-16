from flask import Blueprint
from handlers.handler_prodi import HandlerProdi

prodi_bp = Blueprint('prodi_bp', __name__)

@prodi_bp.route('/prodi/get-all', methods=['GET'])
def getAllProdi():
    return HandlerProdi.getAll()

@prodi_bp.route('/prodi/get-single', methods=['POST'])
def getSingleProdi():
    return HandlerProdi.getSingle()

@prodi_bp.route('/prodi/post', methods=['POST'])
def postProdi():
    return HandlerProdi.post()

@prodi_bp.route('/prodi/update', methods=['PUT'])
def updateProdi():
    return HandlerProdi.update()

@prodi_bp.route('/prodi/delete', methods=['DELETE'])
def deleteProdi():
    return HandlerProdi.delete()
