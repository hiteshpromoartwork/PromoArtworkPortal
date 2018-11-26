# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Szes(models.Model):
    _name = 'size.properties'

    name = fields.Char()
    # order_size_ids = fields.One2many('virtual.artwork', 'size_id')