import os

# DB_ENDPOINT = os.environ['db_endpoint']   # Uncomment while deploying into AWS through zappa
# DB_USER_NAME = os.environ['db_user_name'] # Uncomment while deploying into AWS through zappa
# DB_SECRET_KEY = os.environ['db_password'] # Uncomment while deploying into AWS through zappa
# DATABASE_NAME = os.environ['db_name']     # Uncomment while deploying into AWS through zappa

DB_ENDPOINT = 'localhost'   # Comment while deploying into AWS through zappa
DB_USER_NAME = 'gnyii'       # Comment while deploying into AWS through zappa
DB_SECRET_KEY = 'wnrmsdud12!'    # Comment while deploying into AWS through zappa
DATABASE_NAME = 'medium_db' # Comment while deploying into AWS through zappa

DB_CONNECTION_STR="mysql+pymysql://"+DB_USER_NAME+":"+DB_SECRET_KEY+"@"+DB_ENDPOINT+"/"+DATABASE_NAME

TEST_PREFIX = '/test'
PROD_PREFIX = '/product'
CASE_PREFIX = '/case'
COMPANY_PREFIX = '/company'