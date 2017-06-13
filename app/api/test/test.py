from flask import Blueprint, jsonify

# 导入模块数据
from app.api.test.test_data.test_data import test_modal

test = Blueprint('test', __name__, url_prefix='/test')

@test.route('/', methods=['GET'])
def test_show():
	return jsonify({'tasks': test_modal})