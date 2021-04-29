from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

ma = Marshmallow()
# configurar flask-migrate
migrate = Migrate()
# migrate.init_app(app, db)