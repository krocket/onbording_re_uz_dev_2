from odoo import models, fields

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