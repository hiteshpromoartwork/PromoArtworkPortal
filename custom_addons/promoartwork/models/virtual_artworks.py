from odoo import models, fields, api

class promoartwork(models.Model):
    _name = 'virtual.artwork'

    artwork_file = fields.Binary()
    instructions = fields.Text()
    customer_name = fields.Many2one('res.partner')