# -*- coding: utf-8 -*-
{
    'name': "Gestión de Productos Perecederos",

    'summary': "Módulo para la gestión eficiente de productos perecederos en Cimex",

    'description': """
Este módulo está diseñado para ayudar a las empresas a gestionar sus productos perecederos de manera efectiva. 
Permite el seguimiento del inventario, la gestión de fechas de caducidad, y la optimización de la rotación de productos. 
Con herramientas para alertas de caducidad y reportes de stock, este módulo asegura que los productos frescos se manejen adecuadamente, minimizando pérdidas y mejorando la eficiencia operativa.
    """,

    'author': "Ing. Luis D. Gonzalez Sanches",
    'website': "https://www.cimex.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Inventory',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

