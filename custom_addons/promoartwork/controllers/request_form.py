from odoo import http
from odoo.http import request
import base64

class RequestForm(http.Controller):

    @http.route('/promoartwork/request_form/', auth='user',website=True)
    def request_form(self, **kw):
        return http.request.render('promoartwork.request_form', {})

    @http.route('/order/apparel', auth='user',website=True)
    def order_apparel(self, **kw):
        # import pdb;pdb.set_trace()
        service_type = request.env['job.types'].search([('name','ilike','Vector Art')])
        colors = request.env['imprint.colors'].search([])
        imprint_process = request.env['imprint.process'].search([])
        output_format = request.env['output.format'].search([])
        turnaround_time = request.env['turnaround.time'].search([])
        sizes = request.env['size.properties'].search([])
        return request.render('promoartwork.apparel', {
            'service_type': service_type,
            'colors': colors,
            'imprint_process': imprint_process,
            'output_format': output_format,
            'turnaround_time': turnaround_time,
            'sizes' : sizes,
        })
    
    @http.route('/order/service/<service_name>', auth='user',website=True)
    def order_artwork(self, service_name, **kw):
        # import pdb;pdb.set_trace()
        service_type = request.env['job.types'].search([('name','ilike','Vector Art')])
        colors = request.env['imprint.colors'].search([])
        imprint_process = request.env['imprint.process'].search([])
        output_format = request.env['output.format'].search([])
        turnaround_time = request.env['turnaround.time'].search([])
        sizes = request.env['size.properties'].search([])
        return request.render('promoartwork.order_artwork', {
            'service_type': service_type,
            'colors': colors,
            'imprint_process': imprint_process,
            'output_format': output_format,
            'turnaround_time': turnaround_time,
            'sizes' : sizes,
            'service_name': service_name,
        })

    @http.route('/send_art/form_submit', auth='user', website=True, csrf=False)
    def send_art(self, **kw):
        import pdb;pdb.set_trace()
        if kw:
            status = request.env['virtual.artwork'].sudo().create({
                'name' : kw.get('po'),
                'customer_name' : request.env.user.partner_id.id,
                'artwork_file' : base64.encodestring(kw.get('requested_file').read()),
                'instructions' : kw.get('instructions'),
                'process_id' : int(kw.get('imprint_process')),
                'outputformat_id' : int(kw.get('output_format')),
                'turnaround_id' : int(kw.get('turnaround_time')),
                'required_size' : str(kw.get('size_1')+'X'+kw.get('size_2')+" "+ request.env['size.properties'].search([('id','=',int(kw.get('size_property')))]).name)
            })
        print("sdfsdf")
        if status:
            return "Doine"

    @http.route('/request_quote/form_submit', auth='user', website=True, csrf=False)
    def request_quote(self, **kw):
        import pdb;pdb.set_trace()
        if kw:
            status = request.env['request.quote'].sudo().create({
                'name' : kw.get('po'),
                'customer_name' : request.env.user.partner_id.id,
                'artwork_file' : base64.encodestring(kw.get('requested_file').read()),
                'instructions' : kw.get('instructions'),
                'process_id' : int(kw.get('imprint_process')),
                'outputformat_id' : int(kw.get('output_format')),
                'turnaround_id' : int(kw.get('turnaround_time')),
                'expected_charges' : kw.get('expected_charges'),
                'required_size' : str(kw.get('size_1')+'X'+kw.get('size_2')+" "+ request.env['size.properties'].search([('id','=',int(kw.get('size_property')))]).name)
            })
        print("sdfsdf")
        if status:
            return "Doine"
    