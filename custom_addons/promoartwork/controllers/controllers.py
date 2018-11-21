# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class Promoartwork(http.Controller):
    @http.route('/order/apparel', auth='user',website=True)
    def request_form(self, **kw):
        # import pdb;pdb.set_trace()
        service_type = request.env['job.types'].search([('name','ilike','Vector Art')])
        return request.render('promoartwork.apparel', {
            'service_type': service_type,
        })

    @http.route('/send_art/<service>', auth='public',website=True, csrf=False)
    def send_art_common(self, service, **kw):
        # import pdb;pdb.set_trace()
        print("sdfsdf")

#     @http.route('/promoartwork/promoartwork/objects/<model("promoartwork.promoartwork"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('promoartwork.object', {
#             'object': obj
#         })