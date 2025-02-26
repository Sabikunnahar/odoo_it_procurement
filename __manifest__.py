{
    'name': "IT Procurement Application",
    'version': '1.0',
    'depends': ['base', 'purchase'],
    'author': "Sabikun Nahar Bristy",
    'category': 'Purchasing',
    'description': "Custom IT Procurement Application with Approval Flow",
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/purchase_order_views.xml',
        'report/report.xml',
        'report/report_purchase_order.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
}
