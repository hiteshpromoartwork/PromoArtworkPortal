# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class Promoartwork(http.Controller):
    @http.route('/order/apparel', auth='user',website=True)
    def request_form(self, **kw):
        # import pdb;pdb.set_trace()
        service_type = request.env['job.types'].search([('name','ilike','Vector Art')])
        colors = request.env['imprint.colors'].search([])
        imprint_process = request.env['imprint.process'].search([])
        output_format = request.env['output.format'].search([])
        turnaround_time = request.env['turnaround.time'].search([])
        return request.render('promoartwork.apparel', {
            'service_type': service_type,
            'colors': colors,
            'imprint_process': imprint_process,
            'output_format': output_format,
            'turnaround_time': turnaround_time,
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