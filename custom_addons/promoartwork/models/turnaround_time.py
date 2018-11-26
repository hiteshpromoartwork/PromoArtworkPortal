from odoo import models, fields, api

class ImprintProcess(models.Model):
    _name = 'turnaround.time'

    name = fields.Char()
    order_turnaround_ids = fields.One2many('virtual.artwork', 'turnaround_id')