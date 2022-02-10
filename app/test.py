from flask import Blueprint
from app.constants import TEST_PREFIX

test = Blueprint('test', __name__, url_prefix=TEST_PREFIX)

@test.route('/', methods=['GET'])
def test1() :
    return "test successed!!!"