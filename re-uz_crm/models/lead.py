from odoo import models, fields, api

class Lead(models.Model):
    _inherit = 'crm.lead'
    _description = 'Lead Management'

    priority = fields.Selection(
        selection=[
            ('0', 'Low'),
            ('1', 'Normal'),
            ('2', 'High'),
            ('3', 'Urgent')
        ],
        string='Priority',
        default='1',
        help="Priority of the lead, from low to urgent."
    )

    @api.onchange('stage_id')
    def _onchange_stage_id(self):
        if self.stage_id == 2:
            self.priority = '2'
        elif self.stage_id == 3:
            self.priority = '3'