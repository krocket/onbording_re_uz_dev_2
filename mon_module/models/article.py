from odoo import fields, models
from odoo.exceptions import UserError

class Article(models.Model):
    _name = 'article'
    _description = 'Article'
    name = fields.Char(string='Name', required=True)
    price = fields.Float(string='Price', required=True)
    suppliers_ids = fields.Many2many('res.partner', string='Suppliers', required=True)
    description = fields.Text(string='Description')
    active = fields.Boolean(string='Active', default=True)
    category_ids = fields.Many2many(comodel_name='article.category', string='Categories')
    isbn = fields.Char(string='ISBN', help='International Standard Book Number')

    def _check_isbn(self):
        self.ensure_one()
        if len(self.isbn) != 13 or not self.isbn.isdigit():
            return False
        return True

    def button_check_isbn(self):
        for article in self:
            if article.isbn and not article._check_isbn():
                raise UserError(f"Article has an invalid ISBN: {article.isbn}")
                