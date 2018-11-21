from odoo import http
from odoo.http import request
import base64

class RequestForm(http.Controller):

    @http.route('/promoartwork/request_form/', auth='user',website=True)
    def request_form(self, **kw):
        return http.request.render('promoartwork.request_form', {})

    @http.route('/submit/request_form', auth='user',website=True,csrf=False)
    def form_submit(self, **kw):
        # import pdb;pdb.set_trace()base64.encodestring(field_value.read())
        if kw:
            request.env['virtual.artwork'].sudo().create({
                'artwork_file': base64.encodestring(kw.get('artwork_file').read()),
                'instructions':kw.get('instructions'),
                'customer_name':kw.get('customer')
            })
        return "HIIII"
