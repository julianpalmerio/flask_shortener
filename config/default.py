PROPAGATE_EXCEPTIONS = True
# configuracion de DB
USER_DB = 'postgres'
PASS_DB = 'admin'
URL_DB = 'localhost'
NAME_DB = 'flask_shortener'
FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'
SQLALCHEMY_DATABASE_URI = 'postgresql://eqolrxigpauzfk:33ffbb04bba1e39c106f9cf7ccea92489b1900f054308c102460a095bb47830b@ec2-18-214-140-149.compute-1.amazonaws.com:5432/dcvpq1t87lu2uq'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SHOW_SQLALCHEMY_LOG_MESSAGES = False
ERROR_404_HELP = False