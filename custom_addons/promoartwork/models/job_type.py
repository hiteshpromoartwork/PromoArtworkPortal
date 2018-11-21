from odoo import models, fields, api

class JobType(models.Model):
    _name = 'job.types'

    name = fields.Char()