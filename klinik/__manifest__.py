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
      'reports/report.xml',
      'reports/surat_klinik.xml',
      'security/ir.model.access.csv'
    ]
    # 'qweb' : [
    #     'static/xml/*.xml',
    # ]
    
}

