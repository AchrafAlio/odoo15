# -*- coding: utf-8 -*-
{
    'name': 'Hospital Management',
    'version': '1.0',
    'sequence': -100,
    'description': """Hospital Management Software""",
    'category': 'Productivity/Discuss',
    'website': 'https://www.softifi.com',
    'license': 'LGPL-3',
    'depends': [ 'base'],
    'data': [
        'security/ir.model.access.csv',
        'views/patient.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}