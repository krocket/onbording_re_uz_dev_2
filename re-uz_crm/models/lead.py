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
        stage2 = self.env.ref('crm.crm_stage_lead_2')
        stage3 = self.env.ref('crm.crm_stage_lead_3')
        
        if self.stage_id.id == stage2.id:
            self.priority = '2'
        elif self.stage_id.id == stage3.id:
            self.priority = '3'