# -*- coding: utf-8 -*-
{
    'name': "Demo Module",

    'summary': """
        Demo Module""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base','sale'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}