# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Sale Order Automation',
    'version' : '1.0',
    'depends' : ['sale_stock'],
    'author':'AsesoraIT',
    'summary': """Enable auto sale workflow with sale order confirmation.""",
    'description': """

        You can directly create invoice and set done to delivery order by single click

    """,
    "price": 0,    
    "currency": "USD",
    'category': 'Sales',
    'website': '',
    'license': 'LGPL-3',
    "website" : "",
    'data': [
        'views/stock_warehouse.xml',
    ],
    
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': ['static/description/main_screen.png'],

}
