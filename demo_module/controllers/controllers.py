# -*- coding: utf-8 -*-
from odoo import http

# class PratiseModule(http.Controller):
#     @http.route('/pratise_module/pratise_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pratise_module/pratise_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pratise_module.listing', {
#             'root': '/pratise_module/pratise_module',
#             'objects': http.request.env['pratise_module.pratise_module'].search([]),
#         })

#     @http.route('/pratise_module/pratise_module/objects/<model("pratise_module.pratise_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pratise_module.object', {
#             'object': obj
#         })