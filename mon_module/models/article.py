from odoo import fields, models

class Article(models.Model):
    _name = 'article'
    _description = 'Article'
    name = fields.Char(string='Name', required=True)
    price = fields.Float(string='Price', required=True)
    suppliers_ids = fields.Many2many('res.partner', string='Suppliers', required=True)
    