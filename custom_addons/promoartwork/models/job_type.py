from odoo import models, fields, api

class JobType(models.Model):
    _name = 'job.types'

    name = fields.Char()
    order_jobType_ids = fields.One2many('virtual.artwork', 'jobType_id')