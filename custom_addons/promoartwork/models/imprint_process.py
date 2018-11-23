from odoo import models, fields, api

class ImprintProcess(models.Model):
    _name = 'imprint.process'

    name = fields.Char()