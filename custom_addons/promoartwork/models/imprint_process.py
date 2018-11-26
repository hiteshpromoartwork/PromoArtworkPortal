from odoo import models, fields, api

class ImprintProcess(models.Model):
    _name = 'imprint.process'

    name = fields.Char()
    order_process_ids = fields.One2many('virtual.artwork', 'process_id')