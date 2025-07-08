from odoo import fields, models

class Category(models.Model):
    _name = 'article.category'
    _description = 'Article category'

    name = fields.Char(string='Name', required=True, translate=True)

    parent_id = fields.Many2one(
        comodel_name='article.category',
        string='Parent Category',
        ondelete='restrict',
    )

    child_ids = fields.One2many(
        comodel_name='article.category',
        inverse_name='parent_id',
        string='Child Categories',
    )
