from flask import Blueprint, render_template
from app.constants import PROD_PREFIX

product = Blueprint('product', __name__, url_prefix=PROD_PREFIX)

@product.route('/', methods=['GET'])
@product.route('/no_person', methods=['GET'])
def product_main() :
    return render_template('product/introduction/no_person.html', url_parts="product")

@product.route('/plastic', methods=['GET'])
def plastic() :
    return render_template('product/introduction/plastic.html', url_parts="product")

@product.route('/iLock', methods=['GET'])
def iLock() :
    return render_template('product/introduction/iLock.html', url_parts="product")
    
@product.route('/leisure', methods=['GET'])
def leisure() :
    return render_template('product/introduction/leisure.html', url_parts="product")
    
@product.route('/electronic', methods=['GET'])
def electronic() :
    return render_template('product/introduction/electronic.html', url_parts="product")
    
@product.route('/digital', methods=['GET'])
def digital() :
    return render_template('product/introduction/digital.html', url_parts="product")
    
@product.route('/ect', methods=['GET'])
def ect() :
    return render_template('product/introduction/ect.html', url_parts="product")
    
@product.route('/lock_system', methods=['GET'])
def lock_system() :
    return render_template('product/introduction/lock_system.html', url_parts="product")


