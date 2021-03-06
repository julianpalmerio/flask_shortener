from werkzeug.middleware.profiler import ProfilerMiddleware

from flask import Flask, jsonify
from flask_restful import Api
from flask_compress import Compress
from marshmallow import ValidationError
import os

from app.common.error_handling import ObjectNotFound, AppErrorBaseClass
from app.database import db
from app.urls.api_v1_0.resources import urls_v1_0_bp
from .ext import ma, migrate

def create_app(settings_module):
    app = Flask(__name__)
    app.config.from_object(settings_module)
    Compress(app)
    # Inicializa las extensiones
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    # Captura todos los errores 404
    Api(app, catch_all_404s=True)

    # Deshabilita el modo estricto de acabado de una URL con /
    app.url_map.strict_slashes = False

    # Registra los blueprints
    app.register_blueprint(urls_v1_0_bp)

    # Registra manejadores de errores personalizados
    register_error_handlers(app)

    return app

def register_error_handlers(app):
    @app.errorhandler(Exception)
    def handle_exception_error(e):
        return jsonify({'msg': 'Internal server error'}), 500

    @app.errorhandler(405)
    def handle_405_error(e):
        return jsonify({'msg': 'Method not allowed'}), 405

    @app.errorhandler(403)
    def handle_403_error(e):
        return jsonify({'msg': 'Forbidden error'}), 403

    @app.errorhandler(404)
    def handle_404_error(e):
        return jsonify({'msg': 'Not Found error'}), 404

    @app.errorhandler(AppErrorBaseClass)
    def handle_app_base_error(e):
        return jsonify({'msg': str(e)}), 500

    @app.errorhandler(ObjectNotFound)
    def handle_object_not_found_error(e):
        return jsonify({'msg': str(e)}), 404
    
    @app.errorhandler(ValidationError)
    def handle_validation_error(e):
        return jsonify({'msg': str(e.messages), 'valid_data': str(e.valid_data)}), 500