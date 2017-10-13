import os

c = get_config()

# Database configuration
db_user = os.getenv('DB_USER')
db_pass = os.getenv('DB_PW')
db_host = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')

c.JupyterHub.debug_db = True
c.JupyterHub.db_kwargs = dict(echo_pool=True)
c.JupyterHub.db_url = 'mysql+mysqlconnector://{}:{}@{}/{}'.format(db_user, db_pass, db_host, db_name)
