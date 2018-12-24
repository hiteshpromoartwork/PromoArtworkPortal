from odoo import models, fields, api

class VirtualOrders(models.Model):
    _name = 'virtual.artwork'
    _inherit = ['mail.thread',]

    name = fields.Char('PO#', track_visibility='always')
    artwork_file = fields.Binary(string='Artwork', track_visibility='always')
    artwork_file_name = fields.Char( track_visibility='always')
    
    # attachment_ids_n = fields.Many2many('ir.attachment','submitted_file_virtual_rel',string="Submitted File")
    instructions = fields.Text(track_visibility='always')
    customer_name = fields.Many2one('res.partner', track_visibility='always')
    required_size = fields.Char('Size Required', track_visibility='always')

    # color_id = fields.Many2one('imprint.colors',string="Color")
    process_id = fields.Many2one('imprint.process',string="Process", track_visibility='always')
    jobType_id = fields.Many2one('job.types',string="Job Type", track_visibility='always')
    outputformat_id = fields.Many2one('output.format',string="Output Format", track_visibility='always')
    turnaround_id = fields.Many2one('turnaround.time',string="Turnaround Time", track_visibility='always')
    service_type = fields.Char(track_visibility='always')
    employee = fields.Many2one('hr.employee', string="Assigned to", track_visibility='always')
    # size_id = fields.Many2one('size.properties',string="Size")&filename=product_stock.xls
    state = fields.Selection([('draft', 'Draft'), ('in_progress', 'In Progress'), ('completed', 'Completed'), ('sent', 'Sent'), ], string='Status', readonly=True,default='draft')

    @api.multi
    def action_download_file(self):
        # import pdb;pdb.set_trace()
        # print("sadddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd")
        # /web/binary/saveas?model=website_downloads.files&amp;field=file&amp;filename_field=name&amp;id={{ f.id }}"
        return {
             'type' : 'ir.actions.act_url',
             'url': '/download_artwork/%s'%(self.id),
             'target': 'self',
        }
        # return {
        #      'type' : 'ir.actions.act_url',
        #      'url': "/web/binary/saveas?model=virtual.artwork&amp;field=artwork_file&amp;filename_field=artwork_file_name&amp;id=%s"%(self.id),
        #      'target': 'self',
        # }



