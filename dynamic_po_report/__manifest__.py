# -*- coding: utf-8 -*-
{
    'name': "Dynamic PO Report",
    'summary': """
        Dynamic Purchase Order Report Template""",
    'description': """
        Dynamic PO report template
    """,
    'author': "SPS",
    'website': "http://www.shorepointsys.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['purchase'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner_view.xml',
        'views/po_report_template_view.xml',
        'views/purchase_view.xml',
        'views/purchase_order_report_templates.xml',
        'views/assets.xml',
    ],
}
