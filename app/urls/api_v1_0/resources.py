from flask import request, Blueprint, jsonify
from flask import current_app as app
from flask_restful import Api, Resource
from marshmallow import ValidationError
from werkzeug.utils import redirect
from hashids import Hashids

from .schemas import UrlSchema
from ..models import Url
from ...common.error_handling import ObjectNotFound

urls_v1_0_bp = Blueprint('urls_v1_0_bp', __name__)
url_schema = UrlSchema()

api = Api(urls_v1_0_bp)

class UrlResource(Resource):
    def __init__(self):
        # Creamos el generador de hashs
        self.hashids = Hashids(min_length=4, salt=app.config['SECRET_KEY'])

    def get(self):
        data = request.get_json()
        url_dict = url_schema.load(data)
        url = Url.simple_filter(original_url=url_dict["original_url"])
        if url is None:
            raise ObjectNotFound('La url no se encuentra cargada')
        hashid = self.hashids.encode(url.id)
        result = request.host_url + hashid
        return result

    def post(self):
        data = request.get_json()
        url_dict = url_schema.load(data)
        url = Url.simple_filter(original_url=url_dict["original_url"])
        if url is None:
            url = Url(original_url=url_dict["original_url"])
            url.save()
            status = 201
        else:
            status = 200
        hashid = self.hashids.encode(url.id)
        app.logger.debug(f'hasid: {hashid}')
        result = request.host_url + hashid
        return result, status
    
    def delete(self):
        data = request.get_json()
        url_dict = url_schema.load(data)
        url = Url.simple_filter(original_url=url_dict["original_url"])
        if url is None:
            raise ObjectNotFound('La url no se encuentra cargada')
        url.delete()
        return jsonify("Deleted")

class RedirectResource(Resource):
    def __init__(self):
        # Creamos el generador de hashs
        self.hashids = Hashids(min_length=4, salt=app.config['SECRET_KEY'])

    def get(self, id):
        original_id = self.hashids.decode(id)
        if original_id:
            original_id = original_id[0]
            url = Url.get_by_id(original_id)
            if url is None:
                raise ObjectNotFound('La url no se encuentra cargada')
            url.click()
            return redirect(url.original_url)
        else:
            raise ObjectNotFound('La url no se encuentra cargada')

api.add_resource(UrlResource, '/api/v1.0/url/', endpoint='url_resource')
api.add_resource(RedirectResource, '/<id>', endpoint='redirect_resource')