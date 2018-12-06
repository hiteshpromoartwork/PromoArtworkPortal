from odoo import models, fields, api

class VirtualOrders(models.Model):
    _name = 'virtual.artwork'

    name = fields.Char('PO#')
    artwork_file = fields.Binary(attachment=True)
    instructions = fields.Text()
    customer_name = fields.Many2one('res.partner')
    required_size = fields.Char('Size Required')

    # color_id = fields.Many2one('imprint.colors',string="Color")
    process_id = fields.Many2one('imprint.process',string="Process")
    jobType_id = fields.Many2one('job.types',string="Job Type")
    outputformat_id = fields.Many2one('output.format',string="Output Format")
    turnaround_id = fields.Many2one('turnaround.time',string="Turnaround Time")
    service_type = fields.Char()
    employee = fields.Many2one('hr.employee', string="Assigned to")
    # size_id = fields.Many2one('size.properties',string="Size")


