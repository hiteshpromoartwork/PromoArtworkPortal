# -*- coding: utf-8 -*-
from odoo import http

# class Promoartwork(http.Controller):
#     @http.route('/promoartwork/promoartwork/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/promoartwork/promoartwork/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('promoartwork.listing', {
#             'root': '/promoartwork/promoartwork',
#             'objects': http.request.env['promoartwork.promoartwork'].search([]),
#         })

#     @http.route('/promoartwork/promoartwork/objects/<model("promoartwork.promoartwork"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('promoartwork.object', {
#             'object': obj
#         })