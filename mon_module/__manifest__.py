{
    'name': "Mon Module",
    'version': '18.0.3.1',
    'depends': ['base'],
    'author': "Adrienfdupont",
    'category': 'General',
    'description': "Un module de gestion d'articles",
    'installable': True,
    'data': [
        'views/article_menu.xml',
        'views/article_view.xml',
        'views/category_menu.xml',
        'views/category_view.xml',
        'security/ir.model.access.csv',
        'security/library.security.xml',
    ],
    "license": "LGPL-3",
}