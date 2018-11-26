from odoo import models, fields, api

class OutputFormat(models.Model):
    _name = 'output.format'

    name = fields.Char()
    order_outputFormat_ids = fields.One2many('virtual.artwork', 'outputformat_id')