from odoo import models, fields, api

class ApiEndpoint(models.Model):
    _name = 'api.endpoint'
    _description = 'API Endpoint'

    name = fields.Char(string='Name', required=True)
    model_id = fields.Many2one('ir.model', string='Odoo Model', required=True, help='The model to which this endpoint will be linked.')
    api_key_id = fields.Many2one('api.key', string='API Key', required=True, help='The API Key that will be used for authentication.')
    active = fields.Boolean(string='Active', default=True)
    endpoint_url = fields.Char(string='Endpoint URL', compute='_compute_endpoint_url', store=True)
    access_rule_ids = fields.One2many('api.access.rule', 'endpoint_id', string='Access Rules')

    @api.depends('name', 'model_id')
    def _compute_endpoint_url(self):
        for record in self:
            base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
            record.endpoint_url = f"{base_url}/api/{record.model_id.model.replace('.', '/')}/{record.name}"

    @api.model
    def create(self, vals):
        # Custom logic before creating an endpoint
        endpoint = super(ApiEndpoint, self).create(vals)
        # Custom logic after creating an endpoint
        return endpoint

    def write(self, vals):
        # Custom logic before writing to an endpoint
        result = super(ApiEndpoint, self).write(vals)
        # Custom logic after writing to an endpoint
        return result

    def unlink(self):
        # Custom logic before deleting an endpoint
        result = super(ApiEndpoint, self).unlink()
        # Custom logic after deleting an endpoint
        return result

    # Additional methods for CRUD operations can be added here if necessary.