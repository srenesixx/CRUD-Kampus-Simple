from flask import Blueprint
from handlers.handler_fakultas import HandlerFakultas

fakultas_bp = Blueprint('fakultas_bp', __name__)

@fakultas_bp.route('/fakultas/get-all', methods=['GET'])
def getAllFakultas():
    return HandlerFakultas.getAll()

@fakultas_bp.route('/fakultas/get-single', methods=['POST'])
def getSingleFakultas():
    return HandlerFakultas.getSingle()

@fakultas_bp.route('/fakultas/post', methods=['POST'])
def postFakultas():
    return HandlerFakultas.post()

@fakultas_bp.route('/fakultas/update', methods=['PUT'])
def updateFakultas():
    return HandlerFakultas.update()

@fakultas_bp.route('/fakultas/delete', methods=['DELETE'])
def deleteFakultas():
    return HandlerFakultas.delete()
