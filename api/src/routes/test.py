from flask import Blueprint, jsonify
from http import HTTPStatus

test_bp = Blueprint("test_bp", __name__)

@test_bp.route('/', methods=['GET'])
def test_route():
    return jsonify({'test': 'hello world!!'}), HTTPStatus.OK


@test_bp.route('/movies', methods=['GET'])
def test_get_movies():
    return "", HTTPStatus.OK