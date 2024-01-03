{
    'name': 'Odoo API Module',
    'version': '1.0',
    'summary': 'API Module for Odoo 16 CE',
    'sequence': 10,
    'license': 'LGPL-3',
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'category': 'Tools',
    'description': """
Odoo API Module
===============
This module provides an API interface for Odoo 16 CE, allowing for CRUD operations and secure data access.
    """,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'security/api_security.xml',
        'views/api_key_views.xml',
        'views/api_access_rule_views.xml',
        'views/api_endpoint_views.xml',
        'views/menu_items.xml',
        'controllers/api_controller.py',
        'data/api_data.xml',
    ],
    'demo': [],
    'qweb': [
        'static/src/xml/api_module_templates.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'assets': {
        'web.assets_backend': [
            'api_module/static/src/js/api_module.js',
            'api_module/static/src/css/api_module.css',
        ],
    },
}