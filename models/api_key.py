from odoo import models, fields, api
import secrets

class ApiKey(models.Model):
    _name = 'api.key'
    _description = 'API Key'

    name = fields.Char(string='Name', required=True)
    key = fields.Char(string='Key', required=True, copy=False, index=True, default=lambda self: secrets.token_urlsafe(16))
    user_id = fields.Many2one('res.users', string='User', required=True)
    active = fields.Boolean(string='Active', default=True)

    _sql_constraints = [
        ('unique_key', 'UNIQUE(key)', 'The API key must be unique.')
    ]

    @api.model
    def create(self, vals):
        if 'key' not in vals or not vals['key']:
            vals['key'] = self.generate_key()
        return super(ApiKey, self).create(vals)

    def generate_key(self):
        return secrets.token_urlsafe(16)