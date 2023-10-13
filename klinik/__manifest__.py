{
    'name': 'klinik',
    'version': '1.0',
    'author': 'all',
    'summary': 'module klinik',
    'description': """ ini adalah module custom di udoo mengenai klinik""",
    'application': True,
  #  'website': 'https://www.odooairplane.com',
    'depends': ['base'],
    'data' : [
      'views/klinik.xml',
      'security/ir.model.access.csv'
    ]
    # 'data': [
    #     'views/plane.xml',
    #     'views/template.xml',
    #     'views/dashboard.xml',
    #     'reports/report.xml',
    #     'reports/boarding_pass.xml',
    #     'data/data.xml',
    #     'security/ir.model.access.csv'
    # ],
    # 'qweb' : [
    #     'static/xml/*.xml',
    # ]
    
}

