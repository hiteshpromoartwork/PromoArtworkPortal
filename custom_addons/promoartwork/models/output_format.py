from odoo import models, fields, api

class OutputFormat(models.Model):
    _name = 'output.format'

    name = fields.Char()