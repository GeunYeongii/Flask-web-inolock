from flask import Blueprint
from app.constants import TEST_PREFIX

mod = Blueprint('test', __name__, url_prefix=TEST_PREFIX)

@mod.route('/', methods=['GET'])
def test() :
    return "test successed!!!"