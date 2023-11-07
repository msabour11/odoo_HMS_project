
# -*- coding: utf-8 -*-
{
    'name': "HMS App",
    'summary': "A brief summary of your module",
    'description': "A more detailed description of your module",
    'author': "Mohamed Sabour",
    'category': 'Productivity',
    'version': '16.0.1.0',
    'depends': ['base','mail','crm'],
    'application': True,
    'installable': True,
    'data': [
        'data/data.xml',
        'security/security_groups.xml',
        'security/ir.model.access.csv',
        'security/record_rules.xml',
        'views/base_menus.xml',
        'views/patient_view.xml',
        'views/department_view.xml',
        'views/doctor_view.xml',
        'views/res_partner_view.xml',
        'reports/patient_report.xml'

    ],
}
