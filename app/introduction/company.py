from flask import Blueprint, render_template
from app.constants import COMPANY_PREFIX

company = Blueprint('company', __name__, url_prefix=COMPANY_PREFIX)

@company.route('/', methods=['GET'])
@company.route('/introduction', methods=['GET'])
def product_main() :
    return render_template('company/introduction.html', url_parts="company")

@company.route('/map', methods=['GET'])
def plastic() :
    return render_template('company/map.html', url_parts="company")
