from sqlalchemy.ext.automap import automap_base
from app import db

Base = automap_base()
Base.prepare(db.engine, reflect =True)

# Database Objects
customers_object = Base.classes.customers
accounts_object = Base.classes.accounts