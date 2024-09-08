# -*- coding: utf-8 -*-
# from odoo import http


# class Perecedero(http.Controller):
#     @http.route('/perecedero/perecedero', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/perecedero/perecedero/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('perecedero.listing', {
#             'root': '/perecedero/perecedero',
#             'objects': http.request.env['perecedero.perecedero'].search([]),
#         })

#     @http.route('/perecedero/perecedero/objects/<model("perecedero.perecedero"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('perecedero.object', {
#             'object': obj
#         })

