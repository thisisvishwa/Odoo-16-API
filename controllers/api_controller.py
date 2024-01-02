from odoo import http
from odoo.http import request
from odoo.exceptions import AccessError

class ApiController(http.Controller):

    @http.route('/api/create', type='json', auth='user', methods=['POST'])
    def create(self, model, values, **kwargs):
        try:
            ApiKey = request.env['api_key']
            if not ApiKey.validate_key(kwargs.get('api_key')):
                raise AccessError("Invalid API Key")
            record = request.env[model].sudo().create(values)
            return {'success': True, 'id': record.id, 'message': 'Record created successfully'}
        except Exception as e:
            return {'success': False, 'error': str(e)}

    @http.route('/api/read', type='json', auth='user', methods=['POST'])
    def read(self, model, domain, fields, **kwargs):
        try:
            ApiKey = request.env['api_key']
            if not ApiKey.validate_key(kwargs.get('api_key')):
                raise AccessError("Invalid API Key")
            records = request.env[model].sudo().search_read(domain, fields)
            return {'success': True, 'records': records}
        except Exception as e:
            return {'success': False, 'error': str(e)}

    @http.route('/api/update', type='json', auth='user', methods=['POST'])
    def update(self, model, id, values, **kwargs):
        try:
            ApiKey = request.env['api_key']
            if not ApiKey.validate_key(kwargs.get('api_key')):
                raise AccessError("Invalid API Key")
            record = request.env[model].sudo().browse(id)
            record.write(values)
            return {'success': True, 'message': 'Record updated successfully'}
        except Exception as e:
            return {'success': False, 'error': str(e)}

    @http.route('/api/delete', type='json', auth='user', methods=['POST'])
    def delete(self, model, id, **kwargs):
        try:
            ApiKey = request.env['api_key']
            if not ApiKey.validate_key(kwargs.get('api_key')):
                raise AccessError("Invalid API Key")
            record = request.env[model].sudo().browse(id)
            record.unlink()
            return {'success': True, 'message': 'Record deleted successfully'}
        except Exception as e:
            return {'success': False, 'error': str(e)}