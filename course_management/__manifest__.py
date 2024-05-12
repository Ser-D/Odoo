# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Course management',
    'category': 'Sales/CRM',
    'sequence': 150,
    'summary': 'Centralize your address book',
    'description': """
This module gives you a quick view of your contacts directory, accessible from your home page.
You can track your vendors, customers and other contacts.
""",
    'depends': ['contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/course_views.xml',
        'views/participant_views.xml',
        'views/lesson_view.xml',
    ],
    'application': True,
    'license': 'LGPL-3',
}
