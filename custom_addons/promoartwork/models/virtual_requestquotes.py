from odoo import models, fields, api

class VirtualOrders(models.Model):
    _name = 'request.quote'

    name = fields.Char('PO#')
    artwork_file = fields.Binary()
    instructions = fields.Text()
    customer_name = fields.Many2one('res.partner')
    required_size = fields.Char('Size Required')
    expected_charges = fields.Char('Expected Charges')

    # color_id = fields.Many2one('imprint.colors',string="Color")
    process_id = fields.Many2one('imprint.process',string="Process")
    jobType_id = fields.Many2one('job.types',string="Job Type")
    outputformat_id = fields.Many2one('output.format',string="Output Format")
    turnaround_id = fields.Many2one('turnaround.time',string="Turnaround Time")
    # size_id = fields.Many2one('size.properties',string="Size")


