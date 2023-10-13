# -*- coding: utf-8 -*-
# from odoo import http


# class Coba(http.Controller):
#     @http.route('/coba/coba/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/coba/coba/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('coba.listing', {
#             'root': '/coba/coba',
#             'objects': http.request.env['coba.coba'].search([]),
#         })

#     @http.route('/coba/coba/objects/<model("coba.coba"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('coba.object', {
#             'object': obj
#         })
