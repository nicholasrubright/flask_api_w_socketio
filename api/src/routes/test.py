from flask import Blueprint, jsonify
from http import HTTPStatus

test_bp = Blueprint("test_bp", __name__)

@test_bp.route('/', methods=['GET'])
def test_route():
    return jsonify({'test': 'hello world!!'}), HTTPStatus.OK
