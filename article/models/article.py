from odoo import models, fields, api

class Article(models.Model):
    _inherit = 'article'
    is_available = fields.Boolean(string='Is Available')
    isbn = fields.Char(help="Use a valid ISBN-13 or ISBN-10")
    publisher_id = fields.Many2one('res.partner', string='Publisher', index=True)

    def _check_isbn(self):
        self.ensure_one()
        if not self.isbn.isdigit() or len(self.isbn) == 10:
            return True
        else:
            return super()._check_isbn()