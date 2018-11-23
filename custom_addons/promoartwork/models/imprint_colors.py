from odoo import models, fields, api

class Colors(models.Model):
    _name = 'imprint.colors'

    name = fields.Char()