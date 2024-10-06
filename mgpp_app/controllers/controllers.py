# -*- coding: utf-8 -*-
# from odoo import http


# class MgppApp(http.Controller):
#     @http.route('/mgpp_app/mgpp_app', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mgpp_app/mgpp_app/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('mgpp_app.listing', {
#             'root': '/mgpp_app/mgpp_app',
#             'objects': http.request.env['mgpp_app.mgpp_app'].search([]),
#         })

#     @http.route('/mgpp_app/mgpp_app/objects/<model("mgpp_app.mgpp_app"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mgpp_app.object', {
#             'object': obj
#         })

