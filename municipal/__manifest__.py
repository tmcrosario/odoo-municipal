{
    'name': 'TMC Municipal Taxes and Business Categories',
    'version': '13.0.1.0.0',
    'author': 'Tribunal Municipal de Cuentas - Municipalidad de Rosario',
    'license': 'AGPL-3',
    'depends': [
        'tmc'
    ],
    'data': [
        'views/municipal_menu.xml',
        'views/drei_views.xml',
        'views/drei_menus.xml',
        'views/business_category_views.xml',
        'views/business_category_menus.xml',
        'security/groups.xml',
        'security/ir.model.access.csv'
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': [],
}  # yapf: disable
