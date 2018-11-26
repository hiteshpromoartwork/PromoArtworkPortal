from odoo import models, fields, api

class Colors(models.Model):
    _name = 'imprint.colors'

    name = fields.Char()
    # order_color_ids = fields.One2many('virtual.artwork', 'color_id')