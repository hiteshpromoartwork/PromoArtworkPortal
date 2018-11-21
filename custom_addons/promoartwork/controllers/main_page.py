from odoo import http
from odoo.http import request
from odoo.addons.website.controllers.main import Website

class Website(Website):
    @http.route(auth='user')
    def index(self,**kw):
        super(Website, self).index(**kw)
        return http.request.render('promoartwork.index_page', {})