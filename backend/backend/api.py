from flask import Blueprint, jsonify, request
from flask import render_template

import uuid

app_identifier = uuid.uuid4()

bp = Blueprint("api", __name__)

@bp.route("/hello", methods=['GET'])
def get_links():
    return jsonify({'my_id': app_identifier})
