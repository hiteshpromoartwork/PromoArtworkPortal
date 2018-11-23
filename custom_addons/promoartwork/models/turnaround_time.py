from odoo import models, fields, api

class ImprintProcess(models.Model):
    _name = 'turnaround.time'

    name = fields.Char()