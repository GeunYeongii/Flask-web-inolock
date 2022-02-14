from flask import Blueprint, render_template
from app.constants import CASE_PREFIX

case = Blueprint('case', __name__, url_prefix=CASE_PREFIX)

@case.route('/', methods=['GET'])
@case.route('/no_person', methods=['GET'])
def product_main() :
    return render_template('product/case/no_person.html', url_parts='case')

@case.route('/plastic', methods=['GET'])
def plastic() :
    return render_template('product/case/plastic.html', url_parts='case')

@case.route('/iLock', methods=['GET'])
def iLock() :
    return render_template('product/case/iLock.html', url_parts='case')
    
@case.route('/leisure', methods=['GET'])
def leisure() :
    return render_template('product/case/leisure.html', url_parts='case')
    
@case.route('/electronic', methods=['GET'])
def electronic() :
    return render_template('product/case/electronic.html', url_parts='case')
    
@case.route('/digital', methods=['GET'])
def digital() :
    return render_template('product/case/digital.html', url_parts='case')
    
@case.route('/ect', methods=['GET'])
def ect() :
    return render_template('product/case/ect.html', url_parts='case')
    
@case.route('/lock_system', methods=['GET'])
def lock_system() :
    return render_template('product/case/lock_system.html', url_parts='case')
